import random
import uuid

from pyramid.view import view_config

from webapp import quotes_wrapper
from ..models import Request, Session


class QuoteViews:

    def __init__(self, request):
        self.request = request;
        session = request.session
        if 'id' not in session:
            session_id = str(uuid.uuid4())
            session['id'] = session_id
            request.database.add(Session(session_id=session['id']))

        route_path = request.current_route_path()
        req_entry = Request(session_id=session['id'], page=route_path)
        request.database.add(req_entry)

    @view_config(route_name='all_quotes', renderer='./templates/all_quotes.jinja2')
    def quotes(self):
        return {'quotes': quotes_wrapper.get_quotes()}

    @view_config(route_name='one_quote', renderer='./templates/single_quote.jinja2')
    def single_quote(self):
        quote_id = self.request.matchdict['quote_id']
        if quote_id == 'random':
            random_num = random.randrange(0, len(quotes_wrapper.get_quotes()))
            return {'quote': quotes_wrapper.get_quote(random_num), 'quote_num': random_num + 1}
        else:
            quote_num = int(quote_id) - 1
            return {'quote': quotes_wrapper.get_quote(quote_num), 'quote_num': quote_num + 1}

    @view_config(route_name='home', renderer='./templates/home.jinja2')
    def home(self):
        return {'message': "Web Challenge 1.0", 'author': 'Peter Ray Shen'}




