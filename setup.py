from setuptools import setup

requires = ['pyramid',
            'waitress',
            'requests',
            'pyramid_jinja2',
            'sqlalchemy',
            'pyramid_debugtoolbar',
            ]

setup(name='quotefetcher',
      install_requires=requires,
      entry_points={
        'paste.app_factory': [
            'main = quotefetcher:main',
        ]},
      author='Peter Ray Shen',
      author_email='prshen@edu.uwaterloo.ca',
      description='''Simple web application that fetches quotes from an API, displays to user and stores requests/sessions 
      in a SQL database''',

)
