try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Collin McLean',
    'url': 'http://github.com/wingedillidan/PROJECT',
    'download_url': 'Where to download it.',
    'author_email': 'wingedillidan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
