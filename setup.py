VERSION = '0.0.1'

from setuptools import setup, find_packages

setup(
      name='nagare-vdom',
      version=VERSION,
      author='',
      author_email='',
      description='',
      license='',
      keywords='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      package_data={'': ['*.cfg']},
      zip_safe=False,
      install_requires=('nagare',),
      message_extractors={'nagare_vdom': [('**.py', 'python', None)]},
      entry_points="""
      [nagare.applications]
      nagare_vdom = nagare_vdom.app:app
      """
     )

