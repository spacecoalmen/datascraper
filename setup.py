from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

version = "0.0.1"

INSTALL_REQUIREMENTS = [
      'pymongo==3.0.2',
      'numpy'
]

setup(name='datascraper',
      version=version,
      description="",
      long_description=README,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Unknown',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=INSTALL_REQUIREMENTS,
      entry_points={
            'console_scripts': [
                  'scrape_data = datascraper.__main__:main',
            ]
      }
      )
