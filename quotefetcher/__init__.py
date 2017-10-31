from pyramid.config import Configurator
from pyramid.renderers import JSON
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from quotefetcher import quotes_wrapper
from .models import Base


def database(request):
    """Return a session using the SQLAlchemy session factory stored in the application registry"""
    dbmaker = request.registry.dbmaker
    session = dbmaker()

    def cleanup(request):
        """Rollback changes to database if needed; otherwise, commit"""
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()

    request.add_finished_callback(cleanup)
    return session


def main(global_config, **settings):
    """Configure application settings"""
    config = Configurator(settings=settings)

    #  Store SQLAlchemy session factory in application registry
    engine = engine_from_config(settings, prefix='sqlalchemy.', echo=True)
    Base.metadata.create_all(engine)
    config.registry.dbmaker = sessionmaker(bind=engine)

    #  Initialize session factory
    my_session_factory = SignedCookieSessionFactory('secret')
    config.set_session_factory(my_session_factory)

    config.add_request_method(database, reify=True)
    config.add_renderer('pretty_json', JSON(indent=4))
    config.include('.routes')  # initialize routes found in routes.py
    config.scan()  # scan all packages for View classes and @view_config decorates

    return config.make_wsgi_app()
