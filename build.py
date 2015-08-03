from distutils.core import setup

#files = files = ["enums/*"]

setup(name='agescx',
      version='0.7',
      description='Age of Empires 2 .scx reading module',
      author='Daniel Derevjanik',
      author_email='daniel.derevjanik@gmail.com',
      url='http://www.st.fmph.uniba.sk/~derevjanik7/rp1/',
      packages=['agescx',
                'agescx.models',
                'agescx.utilities',
                'agescx.controller',
                'agescx.enums',
                'agescx.groups'])
