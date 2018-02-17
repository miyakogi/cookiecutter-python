#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""

import unittest

import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        print({{ cookiecutter.project_slug }}.__version__)
