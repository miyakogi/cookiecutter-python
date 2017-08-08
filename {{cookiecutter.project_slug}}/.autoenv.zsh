autostash PYVENV_NAME={{ cookiecutter.project_slug }}
autostash PROJECT_ROOT=${HOME}/Projects/{{ cookiecutter.project_slug }}
if type workon >/dev/null 2>&1; then
  workon ${PYVENV_NAME} && echo "Activate Venv (${PYVENV_NAME})"
else
  [[ -e ${PYVENV_DIR:-$HOME/.pyvenv}/${PYVENV_NAME}/bin/activate ]] && \
    echo "Activate Venv (${PYVENV_NAME})" && \
    source ${PYVENV_DIR:-$HOME/.pyvenv}/${PYVENV_NAME}/bin/activate
fi
autostash PYTHONPATH=$PROJECT_ROOT${PYTHONPATH:+:}$PYTHONPATH
autostash MYPYPATH=$PROJECT_ROOT
