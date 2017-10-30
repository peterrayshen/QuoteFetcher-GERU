from pyramid.response import Response
from pyramid.view import view_config
from datetime import datetime as dt
from webapp import quotes_wrapper
from .models import Request, Session
import random
import uuid
import logging


log = logging.getLogger(__name__)


class Views:
    def __init__(self, request):
        self.request = request;

        for session in request.database.query(Session):
            print(session.requests)
        session = request.session
        if 'id' not in session:
            session_id = str(uuid.uuid4())
            session['id'] = session_id
            request.database.add(Session(session_id=session['id']))

        route_url = request.current_route_url()
        date = str(dt.utcnow().date())
        time = str(dt.utcnow().time())

        req_entry = Request(session_id=session['id'], date=date, time=time, page=route_url)
        request.database.add(req_entry)

    @view_config(route_name='all_quotes',  renderer='templates/all_quotes.jinja2')
    def quotes(self):
        log.debug("Incoming request for all quotes")
        context = {'quotes': quotes_wrapper.get_quotes()}
        return context

    @view_config(route_name='one_quote')
    def random(self):
        print(self.request.matchdict)
        quote_id = self.request.matchdict['quote_id']
        if quote_id == 'random':
            random_num = random.randrange(0, len(quotes_wrapper.get_quotes()))
            log.debug("Incoming request for random quote: {} @ time: {}".format(random_num, dt.utcnow()))
            return Response('<body><h1>{}</h1></body>'.format(quotes_wrapper.get_quote(random_num)))
        else:
            quote_num = int(quote_id) - 1
            log.debug("Incoming request for quote: {} @ time: {}".format(quote_num, dt.utcnow()))
            return Response('<body><h1>{}</h1></body>'.format(quotes_wrapper.get_quote(quote_num)))

    @view_config(route_name='home', renderer='json')
    def home(self):
        log.debug("Incoming request for home page")
        return {'first_name': 'Peter',
                'last_name': 'Shen',
                'address': '123 wallabeeeee'}

    @view_config(route_name='requests_all_json', renderer='prettyjson')
    def requests_all_json(self):
        requests_list = []
        for request in self.request.database.query(Request).order_by(Request.date):
            requests_dict = {}
            requests_dict['session_id'] = request.session_id
            requests_dict['page_url'] = request.page
            requests_dict['date'] = request.date
            requests_dict['time'] = request.time
            requests_list.append(requests_dict)
        return {"requests": requests_list}

    @view_config(route_name='requests_single_json', renderer='prettyjson')
    def requests_single_json(self):
        uid = self.request.matchdict['request_uid']
        request = self.request.database.query(Request).filter(Request.uid == uid).first()
        if request is None:
            return {"error": "Not Found"}
        else:
            requests_info = {}
            requests_info['session_id'] = request.session_id
            requests_info['page_url'] = request.page
            requests_info['date'] = request.date
            requests_info['time'] = request.time

            return {"request": requests_info}

    @view_config(route_name='sessions_all_json', renderer='prettyjson')
    def sessions_all_json(self):
        sessions_list = []
        for session in self.request.database.query(Session):
            session_dict = {}
            session_dict['string_id'] = session.session_id
            requests = session.requests
            requests_list = []

            for request in requests:
                requests_dict = {}
                requests_dict['page_url'] = request.page
                requests_dict['date'] = request.date
                requests_dict['time'] = request.time
                requests_list.append(requests_dict)

            session_dict['requests'] = requests_list
            sessions_list.append(session_dict)

        return {"sessions": sessions_list}
