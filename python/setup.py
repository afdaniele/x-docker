import sys
from distutils.core import setup


def get_version(filename):
    import ast
    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in %r.' % filename)
    if version is None:
        raise ValueError(filename)
    return version


if sys.version_info < (3, 6):
    msg = 'xdocker works with Python 3.6 and later.\nDetected %s.' % str(sys.version)
    sys.exit(msg)


lib_version = get_version(filename='include/xdocker/__init__.py')

setup(
    name='x-docker',
    packages=[
        'xdocker'
    ],
    package_dir={
        'xdocker': 'include/xdocker'
    },
    package_data={},
    version=lib_version,
    license='MIT',
    description='Utility tool that makes it easy to configure a Docker container for use with '
                'GUI applications.',
    author='Andrea F. Daniele',
    author_email='afdaniele@ttic.edu',
    url='https://github.com/afdaniele/x-docker',
    download_url='https://github.com/afdaniele/x-docker/tarball/{}'.format(lib_version),
    zip_safe=False,
    include_package_data=True,
    keywords=['docker', 'gui', 'graphical', 'x-server'],
    install_requires=[
        'docker'
    ],
    scripts=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
