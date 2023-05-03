#!/bin/bash

# Define o diretório base
DIR=$(pwd)

# Percorre todos os diretórios filhos do diretório atual
for d in */; do
    # Entra no diretório se for um repositório Git
    if [[ -d "$DIR/$d/.git" ]]; then
        cd "$DIR/$d"
        # Obtém o nome do repositório Git
        REPO_NAME=$(basename `git rev-parse --show-toplevel`)
        # Faz commit nas mudanças
        git add .
        git commit -m "[final turn] automatic commit"
        # Faz push para o repositório remoto
        git push
        echo "Commit realizado em $REPO_NAME"
    fi
done

echo "Finalizado."
