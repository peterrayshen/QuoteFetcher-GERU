def includeme(config):
    """Add routes and static views to application configuration"""
    # Add static route for static assets
    config.add_static_view(name='static', path='quotefetcher:static')

    # Add routes for normal views
    config.add_route('home', '/')
    config.add_route('quotes_all', '/quotes')
    config.add_route('quotes_single', '/quotes/{quote_id}')

    # Add routes for RESTful endpoints
    config.add_route('sessions_all', '/api/sessions')
    config.add_route('sessions_by_id', '/api/sessions/id/{session_id}')
    config.add_route('requests_all', '/api/requests')
    config.add_route('requests_by_uid', '/api/requests/{request_uid}')
    config.add_route('requests_by_date', '/api/requests/date/{date}')
    config.add_route('requests_by_session', '/api/requests/session/{session_id}')
