from pyramid.response import Response
from pyramid.view import view_config
import random
import uuid
import logging
from datetime import datetime as dt
from webapp import quotes_wrapper

log = logging.getLogger(__name__)


class Views:
    def __init__(self, request):
        self.request = request;
        session = request.session
        if 'id' not in session:
            session_id = str(uuid.uuid4())
            session['id'] = session_id

    @view_config(route_name='all_quotes',  renderer='templates/all_quotes.jinja2')
    def quotes(self):
        log.debug("Incoming request for all quotes")
        context = {'quotes': quotes_wrapper.get_quotes()}
        return context

    @view_config(route_name='one_quote')
    def random(self):
        quote_id = self.request.matchdict['quote_id']
        if quote_id == 'random':
            random_num = random.randrange(0, len(quotes_wrapper.get_quotes()))
            log.debug("Incoming request for random quote: {} @ time: {}".format(random_num, dt.utcnow()))
            return Response('<body><h1>{}</h1></body>'.format(quotes_wrapper.get_quote(random_num)))
        else:
            quote_num = int(quote_id) - 1
            log.debug("Incoming request for quote: {} @ time: {}".format(quote_num, dt.utcnow()))
            return Response('<body><h1>{}</h1></body>'.format(quotes_wrapper.get_quote(quote_num)))

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        log.debug("Incoming request for home page")
        return {'first_name': 'Peter',
                'last_name': 'Shen',
                'address': '123 wallabeeeee'}

    @view_config(route_name='cookie')
    def cookie(self):
        log.debug("Incoming request for cookie page")
        response = Response()
        response.text = 'hello {}'.format(self.request.session['id'])
        print(self.request.current_route_url())
        return response