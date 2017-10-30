from setuptools import setup

requires = ['pyramid',
            'waitress',
            'pyramid_jinja2',
            'sqlalchemy',
            'pyramid_tm',
            'zope.sqlalchemy']

setup(name='webapp', install_requires=requires,  entry_points={
        'paste.app_factory': [
            'main = webapp:main',
        ], 'console_scripts': [
        'initialize_db = webapp.initialize_db:main',
        ]}
   )