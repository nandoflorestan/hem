import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = ''#open(os.path.join(here, 'README.md')).read()
CHANGES = ''#open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'zope.interface'
    , 'pyramid'
]

setup(name='hem'
      , version='0.1'
      , description='Generic utilities to help build frameworks on top of pyramid'
      , long_description=README + '\n\n' +  CHANGES
      , classifiers=[
            'Intended Audience :: Developers'
            , 'License :: OSI Approved :: BSD License'
            , 'Operating System :: OS Independent'
            , 'Programming Language :: Python'
            , 'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
            , 'Topic :: Software Development :: Libraries :: Python Modules'
      ]
      , author='John Anderson'
      , author_email='sontek@gmail.com'
      , url='https://github.com/eventray/hem'
      , keywords='pyramid'
      , license='BSD'
      , packages=find_packages()
      , include_package_data=True
      , zip_safe=False
      , install_requires=requires
      , tests_require=requires + ['pytest', 'mock', 'webtest', 'pytest-cov']
      , test_suite='hem'
)
