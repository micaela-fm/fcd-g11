#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
A3_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PROPERTIES_FILE="$A3_DIR/config/local.properties"

if [ ! -f "$PROPERTIES_FILE" ]; then
    echo "Ficheiro local.properties não encontrado."
    echo "Cria-o a partir do template:"
    echo "cp A3/config/local.properties.example A3/config/local.properties"
    exit 1
fi

repo_root="$(grep '^repo_root=' "$PROPERTIES_FILE" | cut -d '=' -f 2-)"
venv_path="$(grep '^venv_path=' "$PROPERTIES_FILE" | cut -d '=' -f 2-)"

if [ -z "$repo_root" ]; then
    echo "Falta definir repo_root em $PROPERTIES_FILE."
    exit 1
fi

if [ -z "$venv_path" ]; then
    echo "Falta definir venv_path em $PROPERTIES_FILE."
    exit 1
fi

if [ ! -d "$repo_root" ]; then
    echo "A pasta repo_root não existe: $repo_root"
    exit 1
fi

if [ ! -f "$venv_path/bin/activate" ]; then
    echo "O virtualenv não existe ou não tem bin/activate: $venv_path"
    exit 1
fi

cd "$repo_root"
source "$venv_path/bin/activate"
python -m A3.src.menu
