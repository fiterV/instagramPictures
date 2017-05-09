from setuptools import setup

setup(
	name='instagramPictures',
	packages = ['instagramPictures'],
	version='1.01',
	description = 'Script for downloading pictures from instagram.com',
	author = 'Vadym Prokopets',
	author_email = 'vadym_prokopec@mail.ru',
	url = 'https://github.com/fiterV/instagramPictures', # use the URL to the github repo
	keywords = ['instagram', 'pictures', 'download'], # arbitrary keywords
	classifiers = [],
	entry_points={
          'console_scripts': ['instagramPictures = instagramPictures.main']
      },
)