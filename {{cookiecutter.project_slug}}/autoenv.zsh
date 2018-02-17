autostash PYVENV_NAME={{ cookiecutter.project_slug }}
autostash PROJECT_ROOT=${HOME}/Projects/{{ cookiecutter.project_slug }}
workon $PYVENV_NAME
autostash MYPYPATH=$PROJECT_ROOT
autostash VIM_PYTHON_TEST="green"
