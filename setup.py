from setuptools import setup

setup(name='rerldo',
      version='0.1',
      description='¯\\_(ツ)_/¯',
      url='https://github.com/mark-solo/python_packaging_practice',
      author='me',
      author_email='ali.abdulzhalilov@gmail.com',
      license='MIT',
      packages=['rerldo'],
	  install_requires=[
		'markdown',
	  ],
	  test_suite='nose.collector',
	  tests_require=['nose'],
	  entry_points = {
		'console_scripts': ['rerldo-yup=rerldo.command_line:main']
	  },
	  include_package_data=True,
      zip_safe=False)