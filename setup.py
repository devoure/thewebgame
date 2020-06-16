#This will allow to test a line of code for errors
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config ={
    'description':'My Web Game',
    'author': 'Athman',
    'url':'url to get it at',
    'download_url':'Where to download it',
    'author_email':'My email.',
    'version':'0.1',
    'install_requires':['nose'],
    'packages': ['thegame'],
    'scripts':[],
    'name':'thewebgame'
}
setup(**config)
