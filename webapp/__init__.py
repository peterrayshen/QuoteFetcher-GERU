from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config

from webapp import quotes_wrapper

def main(global_config, **setting):
    my_session_factory = SignedCookieSessionFactory('factory')

    config = Configurator(settings=setting)
    config.set_session_factory(my_session_factory)
    config.add_route('home', '/')
    config.add_route('all_quotes', '/quotes')
    config.add_route('one_quote', '/quotes/{quote_id}')
    config.add_route('cookie', '/cookie')
    config.scan('.views')
    config.add_static_view(name='static', path='webapp:static')

    return config.make_wsgi_app()


