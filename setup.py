# -*- coding: utf-8 -*-
"""Simple Telegram logging with zero dependencies.
https://github.com/lbltavares/telegram-logging
"""

from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='telegram_logging',
      version='1.0.1',
      description='Simple Telegram logging with zero dependencies.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/lbltavares/telegram-logging',
      author='lbltavares',
      license='MIT',
      packages=['telegram_logging'],
      setup_requires=['wheel'],
      zip_safe=False)
