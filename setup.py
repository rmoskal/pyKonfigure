from distutils.core import setup
setup(
  name = 'konfigure',
  tests_require=['nose', 'pinocchio'],
  packages = ['konfigure'], # this must be the same as the name above
  version = '0.1',
  description = 'Python config files good for PAAS',
  author = 'Robert Moskal',
  author_email = 'rmoskal@mostmedia.com',
  url = 'git remote add origin https://github.com/rmoskal/pyKonfigure.git', # use the URL to the github repo
  download_url = 'https://github.com/rmoskal/pyKonfigure/tarball/0.1', # I'll explain this in a second
  keywords = ['configuration', 'PAAS', 'Heroku', 'Flask'], # arbitrary keywords
  classifiers = [],
)
