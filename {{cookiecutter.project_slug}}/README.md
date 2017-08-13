{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![PyPI version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }})
[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh{{ cookiecutter.github_username }}//{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

* Free software: {{ cookiecutter.license }}
* Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}

## Features

* TODO

## Installation

### Requirements

## Usage

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
