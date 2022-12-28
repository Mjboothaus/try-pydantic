pipx install --force pip-tools
pip-compile requirements-dev.in
python -m venv .venv_try-pydantic
source .venv_try-pydantic/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
ipython kernel install --name ".venv_try-pydantic" --user