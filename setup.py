from distutils.core import setup
setup(
  name = 'PySOSA',         # How you named your package folder (MyLib)
  packages = ['PySOSA'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='Apache 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python module for building SOSA based RDF graphs',   # Give a short description about your library
  author = 'Badisa Mosesane',                   # Type in your name
  author_email = 'landrs@nd.edu',      # Type in your E-Mail
  url = 'https://github.com/landrs-toolkit/PySOSA',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/landrs-toolkit/PySOSA',    # I explain this later on
  keywords = ['building SOSA based graphs', 'RDF graphs', 'Python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'isodate==0.6.0',
          'pyld==1.0.5',
          'pyobs==0.1',
          'pyparsing==2.4.5',
          'pytz==2019.3',
          'rdflib==4.2.2',
          'six==1.13.0',
          'websocket-client==0.56.0'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache 2.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
