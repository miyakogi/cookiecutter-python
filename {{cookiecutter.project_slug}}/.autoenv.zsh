autostash PYVENV_NAME={{ cookiecutter.project_slug }}
autostash PROJECT_ROOT=${HOME}/Projects/{{ cookiecutter.project_slug }}
python -m venv "$vdir"
[[ -e ${HOME}/.pyvenv/{{ cookiecutter.project_slug }}/bin/activate ]] && \
  echo "Activate Venv (${PYVENV_NAME})" && \
  source ${HOME}/.pyvenv/{{ cookiecutter.project_slug }}/bin/activate
autostash PYTHONPATH=$PROJECT_ROOT${PYTHONPATH:+:}$PYTHONPATH
autostash MYPYPATH=$PROJECT_ROOT
autostash GREEN_CONFIG=${PROJECT_ROOT}/.green
