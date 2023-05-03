#!/bin/bash

# Define o diretório base
DIR='/home/raff'
echo "$DIR"
# Percorre todos os diretórios filhos do diretório atual
for d in */; do
echo "$d"
    # Entra no diretório se for um repositório Git
    if [[ -d "$DIR/$d/.git" ]]; then
    echo "$DIR/$d"
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
