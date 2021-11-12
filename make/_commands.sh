set -o errexit   # -e: Exit when a command fails
set -o nounset   # -u: Treat unset variables as an error
set -o pipefail  # The return value of a pipeline is the value of the last command that failed

# Debug options
# set -o noexec   # -n: Read and parse but do not execute commands
# set -o verbose  # -v: Print shell input lines as they are read
set -o xtrace     # -x: Print commands before execution


clean() {
    rm -rf .cache
    rm -rf __pycache__
    rm -rf src/__pycache__
    rm -rf src/humblebundle_to_sqlite/__pycache__
    rm -rf test/__pycache__
}


venv() {
    pyenv virtualenv 3.9.5 humblebundle-to-sqlite
    pyenv local humblebundle-to-sqlite
}


update_dependencies() {
    # python -m pip install --upgrade pip setuptools wheel pip-tools
    python -m pip install --no-deps --upgrade pip setuptools wheel pip-tools
    python -m piptools compile --upgrade --allow-unsafe --build-isolation --generate-hashes requirements.in
    python -m piptools compile --upgrade --allow-unsafe --build-isolation --generate-hashes requirements-dev.in
    pre-commit autoupdate --freeze
}


compile_dependencies() {
    python -m pip install --upgrade pip setuptools wheel pip-tools
    python -m piptools compile --allow-unsafe --build-isolation --generate-hashes requirements.in
    python -m piptools compile --allow-unsafe --build-isolation --generate-hashes requirements-dev.in
}


test_all() {
    pytest
}


test_acceptance() {
    pytest -m "acceptance"
}


test_unit() {
    pytest -m "not acceptance"
}


lint() {
    nitpick --offline check
    mypy .
    flake8 .
    black . --check --diff --color --experimental-string-processing
    # isort . --check-only --diff
}


report() {
    pytest --cov-report html:.cache/coverage-report
    firefox .cache/coverage-report/index.html
}


install_production() {
    python -m pip install --no-deps --upgrade pip setuptools wheel
    python -m pip install --no-deps .
    python -m pip install --require-hashes --no-deps --upgrade --requirement requirements.txt
}


install_development() {
    python -m pip install --no-deps --upgrade pip setuptools wheel pip-tools
    # python -m pip install --require-hashes --no-deps --upgrade --requirement requirements.txt  --requirement requirements-dev.txt
    python -m piptools sync --pip-args '--require-hashes --no-deps' requirements.txt requirements-dev.txt
    python -m pip install --no-deps --editable .
}


install_git_hooks() {
    pre-commit install --install-hooks --hook-type pre-commit
    pre-commit install --install-hooks --hook-type pre-push
}


generate_config_files() {
    nitpick --offline fix
}


format_code() {
    black . --experimental-string-processing --color
}
