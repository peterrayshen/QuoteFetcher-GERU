import random
import uuid
from pyramid.view import view_config
from webapp import quotes_wrapper
from ..models import Request, Session


class QuoteViews:
    """View class containing all views for display of quotes to user"""

    def __init__(self, request):
        self.request = request;
        session = request.session

        # check if 'id' attribute is in session; if not, assign a unique string ID to the session
        if 'id' not in session:
            session_id = str(uuid.uuid4())
            session['id'] = session_id
            request.database.add(Session(session_id=session['id']))

        # store request in database
        route_path = request.current_route_path()
        req_entry = Request(session_id=session['id'], page=route_path)
        request.database.add(req_entry)

    @view_config(route_name='all_quotes', renderer='./templates/all_quotes.jinja2')
    def quotes(self):
        """Return a list of all quotes to the template for rendering"""
        return {'quotes': quotes_wrapper.all_quotes()}

    @view_config(route_name='one_quote', renderer='./templates/single_quote.jinja2')
    def single_quote(self):
        """Return a single quote to the template for rendering"""
        quote_id = self.request.matchdict['quote_id']
        if quote_id == 'random':
            random_num = random.randrange(0, len(quotes_wrapper.all_quotes()))
            return {'quote': quotes_wrapper.quote(random_num), 'quote_num': random_num + 1}
        else:
            quote_num = int(quote_id) - 1
            return {'quote': quotes_wrapper.quote(quote_num), 'quote_num': quote_num + 1}

    @view_config(route_name='home', renderer='./templates/home.jinja2')
    def home(self):
        """Return display message for home page template"""
        return {'message': "Web Challenge 1.0", 'author': 'Peter Ray Shen'}
