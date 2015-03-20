from setuptools import setup, find_packages
import os

version = '1.1'
long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')
    
setup(name='iol.gisweb.base',
      version=version,
      description="Templates, scripts and assets to support gisweb iol Plomino application",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Gis & Web Srl',
      author_email='info@gisweb.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iol', 'iol.gisweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'gisweb.utils',
          'Products.CMFPlomino',
          'collective.wtf',
          'Products.CMFPlacefulWorkflow',
          'collective.wkpdfview', 
          'zope.app.component',
          'dict2xml',
          #'suds'     
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
