#!/usr/bin/env python

from setuptools import setup

setup(
    name='myCMS',
    version='1.0',
    description='Django CMS OpenShift App',
    author='Danny Ho',
    author_email='dannyhch@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.5.5',
    				  'PIL==1.1.7',
    				  'django-cms==2.4.3',
    				  'django-mptt==0.5.2',
    				  'djangocms-admin-style==0.2.0',
    				  'djangocms-text-ckeditor==1.0.11',
    				  'django-reversion==1.7',
    				  'django-filer==0.9.5',
    				  'cmsplugin-filer==0.9.5'
    				  ],
)
