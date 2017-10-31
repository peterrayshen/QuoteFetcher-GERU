from pyramid.config import Configurator
from pyramid.renderers import JSON
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from webapp.tools import quotes_wrapper
from .models import Base


def database(request):
    dbmaker = request.registry.dbmaker
    session = dbmaker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()
    request.add_finished_callback(cleanup)
    return session


def main(global_config, **settings):
    config = Configurator(settings=settings)

    engine = engine_from_config(settings, prefix='sqlalchemy.', echo=True)
    Base.metadata.create_all(engine)
    config.registry.dbmaker = sessionmaker(bind=engine)

    my_session_factory = SignedCookieSessionFactory('factory')
    config.set_session_factory(my_session_factory)

    config.add_request_method(database, reify=True)
    config.add_renderer('pretty_json', JSON(indent=4))
    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()


