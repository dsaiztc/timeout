from setuptools import setup
from warnings import warn
import sys

if sys.version_info[0] < 3:
    warn('This package requires the concurrent.futures package only available for Python 3.x\n'
         'Python 2.x users need to install the backport https://github.com/agronholm/pythonfutures')

setup(
    name='timeout',
    version='0.1',
    description='Set a maximum execution time for your functions with a simple decorator',
    url='http://github.com/dsaiztc/timeout',
    author='Daniel Saiz Llarena',
    author_email='dsaiztc@gmail.com',
    license='MIT',
    packages=['timeout'],
    install_requires=['futures'],
    dependency_links=['https://github.com/agronholm/pythonfutures/tarball/master#egg=futures-3.0.5'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False
)
