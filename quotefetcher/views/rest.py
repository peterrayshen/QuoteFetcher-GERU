from pyramid.view import view_config
from ..models import Request, Session
from datetime import datetime as dt


class RESTViews:
    """View class containing all views for RESTful API endpoints"""

    def __init__(self, request):
        self.request = request

    def _request_info(self, request):
        """Helper method to return a dictionary containing all attributes of a request object"""
        return {'session_id': request.session_id,
                'page_route': request.page,
                'date': str(request.date),  # convert DateTime.Date object to string
                'time': str(request.time)}  # convert DateTime.Time object to string

    @view_config(route_name='requests_all', renderer='pretty_json')
    def requests_all(self):
        """Return every request and corresponding info as JSON"""
        return {"requests": [self._request_info(request) for request in
                             self.request.database.query(Request).order_by(Request.date)]}

    @view_config(route_name='requests_by_uid', renderer='pretty_json')
    def requests_by_uid(self):
        """Return single request and corresponding info as JSON"""
        request = self.request.database.query(Request).filter(
            Request.uid == self.request.matchdict['request_uid']).first()
        if request is not None:
            return {"request": self._request_info(request)}
        else:
            return {"error": "Not Found"}

    @view_config(route_name='requests_by_date', renderer='pretty_json')
    def requests_by_date(self):
        """Return all requests and corresponding info within a day (YYYY-MM-DD) as JSON"""
        try:
            requests = self.request.database.query(Request).filter(
                Request.date == dt.strptime(self.request.matchdict['date'], '%Y-%m-%d').date()).all()
            if len(requests) == 0:
                return {"error": "Not Found"}
            else:
                return {"requests": [self._request_info(request) for request in requests]}
        except ValueError:
            return {"error": "Not Found"}

    @view_config(route_name='requests_by_session', renderer='pretty_json')
    def requests_by_session(self):
        """Return all requests within a given session_id as JSON"""
        requests = self.request.database.query(Request).filter(
            Request.session_id == self.request.matchdict['session_id']).all()
        if len(requests) == 0:
            return {"error": "Not Found"}
        else:
            return {"requests": [self._request_info(request) for request in requests]}

    @view_config(route_name='sessions_all', renderer='pretty_json')
    def sessions_all(self):
        """Return all sessions and corresponding info as JSON"""
        context = []
        for session in self.request.database.query(Session):
            session_info = {'session_id': session.session_id,
                            'requests': [self._request_info(request) for request in session.requests]}
            context.append(session_info)
        return {"sessions": context}

    @view_config(route_name='sessions_by_id', renderer='pretty_json')
    def sessions_by_id(self):
        """Returns a session given a session_id as JSON"""
        session = self.request.database.query(Session).filter(
            Session.session_id == self.request.matchdict['session_id']).first()
        if session is not None:
            return {"session_id": session.session_id,
                    'requests': [self._request_info(request) for request in session.requests]}
        else:
            return {'error': 'Not Found'}
