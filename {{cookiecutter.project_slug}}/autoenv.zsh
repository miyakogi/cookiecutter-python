autostash PYVENV_NAME={{ cookiecutter.project_slug }}
autostash PROJECT_ROOT=${HOME}/Projects/{{ cookiecutter.project_slug }}
[[ -e ${PROJECT_ROOT}/bin/activate ]] && \
  echo "Activate Venv (${PYVENV_NAME})" && \
  source ${PROJECT_ROOT}/bin/activate
autostash PYTHONPATH=$PROJECT_ROOT${PYTHONPATH:+:}$PYTHONPATH
autostash MYPYPATH=$PROJECT_ROOT
