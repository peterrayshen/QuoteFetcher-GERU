from setuptools import setup

requires = ['pyramid',
            'waitress',
            'requests',
            'pyramid_jinja2',
            'sqlalchemy',
            'pyramid_debugtoolbar',
            ]

setup(name='quotefetcher',
      description='''Simple web application that fetches quotes from an API, displays to user and stores requests/sessions 
      in a SQL database''',
      install_requires=requires,
      version='0.1',
      url='https://github.com/peterrayshen/QuoteFetcher',
      entry_points={
          'paste.app_factory': [
              'main = quotefetcher:main',
          ]},
      author='Peter Ray Shen',
      author_email='prshen@edu.uwaterloo.ca',

      )
