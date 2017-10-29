from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import engine_from_config
from webapp import quotes_wrapper
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
    config.add_request_method(database, reify=True)

    my_session_factory = SignedCookieSessionFactory('factory')
    config.set_session_factory(my_session_factory)
    config.add_route('home', '/')
    config.add_route('all_quotes', '/quotes')
    config.add_route('one_quote', '/quotes/{quote_id}')
    config.add_route('cookie', '/cookie')
    config.scan('.views')
    config.add_static_view(name='static', path='webapp:static')

    return config.make_wsgi_app()


