import requests
import json


def get_quotes():
    resp = requests.get('https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes')
    quotes_list = json.loads(resp.text)['quotes']
    return quotes_list


def get_quote(quote_number):
    resp = requests.get('https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/{}'.format(quote_number))
    quote = json.loads(resp.text)['quote']
    return quote

