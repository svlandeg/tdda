import os
from setuptools import setup, find_packages

from tdda.version import version as __version__

def read(fname):
    # read contents of file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def data(path, pathitems):
    # build list of additional files to package up from a subdirectory
    names = []
    for relpath in pathitems:
        subpath = path + [relpath]
        dirname = os.path.join(*subpath)
        for name in os.listdir(dirname):
            pathname = os.path.join(relpath, name)
            fullpathname = os.path.join(dirname, name)
            if os.path.isdir(fullpathname):
                names.extend(data(path, [pathname]))
            else:
                names.append(pathname)
    return names

setup(
    name='tdda',
    version=__version__,
    description='Test Driven Data Analysis',
    long_description=read('README.md'),
    author='Stochastic Solutions Limited',
    author_email='info@StochasticSolutions.com',
    license='MIT',
    url='http://www.stochasticsolutions.com',
    download_url='https://github.com/tdda/tdda',
    keywords='tdda constraint referencetest rexpy',
    packages=find_packages(),
    package_data={
        'tdda.referencetest': data(['tdda', 'referencetest'], ['examples']),
        'tdda.referencetest.tests': data(['tdda', 'referencetest', 'tests'],
                                         ['testdata']),
        'tdda.constraints': data(['tdda', 'constraints'],
                                  ['testdata', 'examples']),
        'tdda.rexpy': data(['tdda', 'rexpy'], ['examples']),
        'tdda': ['README.md', 'LICENSE.txt'],
    },
    include_package_data=True,
)

