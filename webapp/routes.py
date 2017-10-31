def includeme(config):
    """Add routes and static views to application configuration"""
    config.add_static_view(name='static', path='webapp:static')

    config.add_route('home', '/')
    config.add_route('all_quotes', '/quotes')
    config.add_route('one_quote', '/quotes/{quote_id}')

    config.add_route('sessions_all_json', '/api/sessions')
    config.add_route('sessions_id_json', '/api/sessions/id/{session_id}')

    config.add_route('requests_all_json', '/api/requests')
    config.add_route('requests_single_json', '/api/requests/{request_uid}')
    config.add_route('requests_date_json', '/api/requests/date/{date}')
    config.add_route('requests_session_json', '/api/requests/session/{session_id}')

