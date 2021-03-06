#!/usr/bin/env python

"""Hypatia package installer.

$ setup.py sdist bdist_wheel
$ twine upload dist/hypatia_engine-0.2.3.tar.gz dist/hypatia_engine-0.2.3*.whl
$ rm -rf dist

You'll need the wheel, twine package for bdist_wheel. Don't forget
to clear your dist when finished.

"""

from setuptools import setup


exec(open('hypatia/version.py').read())
setup(name='hypatia_engine',
      version=__version__,
      description='2D action adventure game engine',
      author='Lillian Lemmer',
      author_email='lillian.lynn.lemmer@gmail.com',
      url='http://lillian-lemmer.github.io/hypatia',
      license='MIT',
      packages=['hypatia'],
      install_requires=['pillow', 'pyganim'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Operating System :: Microsoft :: Windows :: Windows 7',
                   'Operating System :: Microsoft :: Windows :: Windows Vista',
                   'Operating System :: Microsoft :: Windows :: Windows XP',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: BSD :: FreeBSD',
                   'Operating System :: POSIX :: Linux',
                   'Topic :: Games/Entertainment :: Role-Playing',
                   'Topic :: Software Development :: Libraries :: pygame',
                  ],
      keywords=('games gaming development sprites adventure game tilemap '
                'tilesheet zelda gamedev 2d')
    )

