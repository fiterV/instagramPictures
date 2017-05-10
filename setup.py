from setuptools import setup

setup(
	name='instagramPictures',
	packages = ['instagramPictures'],
	version='1.3.1',
	description = 'Script for downloading pictures from instagram.com',
	author = 'Vadym Prokopets',
	author_email = 'vadym_prokopec@mail.ru',
	url = 'https://github.com/fiterV/instagramPictures', # use the URL to the github repo
	keywords = ['instagram', 'pictures', 'download'], # arbitrary keywords
	classifiers = [
		'Intended Audience :: Customer Service',
		'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: System :: Software Distribution',
		'Topic :: Utilities',
	],

	install_requires=[
          'selenium',
      ],
    license='MIT',
	entry_points={
          'console_scripts': ['instagramPictures = instagramPictures.main:main']
      },

)