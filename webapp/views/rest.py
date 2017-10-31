from pyramid.view import view_config
from ..models import Request, Session
from datetime import datetime as dt


def get_request_info(request):
    return {'session_id': request.session_id,
            'page url': request.page,
            'date': str(request.date),
            'time': str(request.time)}


class RESTViews:

    def __init__(self, request):
        self.request = request;

    @view_config(route_name='requests_all_json', renderer='pretty_json')
    def requests_all_json(self):
        context = []
        for request in self.request.database.query(Request).order_by(Request.date):
            context.append(get_request_info(request))
        return {"requests": context}

    @view_config(route_name='requests_single_json', renderer='pretty_json')
    def requests_single_json(self):
        uid = self.request.matchdict['request_uid']
        request = self.request.database.query(Request).filter(Request.uid == uid).first()
        if request is not None:
            return {"request": get_request_info(request)}
        else:
            return {"error": "Not Found"}

    @view_config(route_name='requests_date_json', renderer='pretty_json')
    def requests_date_json(self):
        date = self.request.matchdict['date']
        try:
            requests = self.request.database.query(Request).filter(Request.date == dt.strptime(date, '%Y-%m-%d').date()).all()
            context = []
            if len(requests) == 0:
                return {"error": "Not Found"}
            else:
                for request in requests:
                    context.append(get_request_info(request))
                return {"requests": context}
        except ValueError:
            return {"error": "Not Found"}

    @view_config(route_name='requests_session_json', renderer='pretty_json')
    def requests_session_json(self):
        session_id = self.request.matchdict['session_id']
        requests = self.request.database.query(Request).filter(
            Request.session_id == session_id).all()
        context = []
        if len(requests) == 0:
            return {"error": "Not Found"}
        else:
            for request in requests:
                context.append(get_request_info(request))
            return {"requests": context}

    @view_config(route_name='sessions_all_json', renderer='pretty_json')
    def sessions_all_json(self):
        context = []
        for session in self.request.database.query(Session):
            requests = []
            for request in session.requests:
                requests.append(get_request_info(request))
                session_info = {'session_id': session.session_id, 'requests': requests}
            context.append(session_info)
        return {"sessions": context}

    @view_config(route_name='sessions_id_json', renderer='pretty_json')
    def sessions_id_json(self):
        session_id = self.request.matchdict['session_id']
        session = self.request.database.query(Session).filter(Session.session_id == session_id).first()

        if session is not None:
            requests = []
            for request in session.requests:
                requests.append(get_request_info(request))
            return {"session_id": session.session_id, 'requests': requests}
        else:
            return {'error': 'Not Found'}


