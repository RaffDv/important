#!/bin/zsh

# Define o diretório base
DIR="/home/$USER"
git config --global user.email "rafael.vargas.emp@gmail.com";
git config --global user.name "Rafael Vargas"  ;

# Percorre todos os diretórios filhos do diretório atual
for d in */**/*; do
    # Entra no diretório se for um repositório Git
    if [[ -d "$DIR/$d/.git" ]]; then
        cd "$DIR/$d"
        echo "$(pwd)"
        # Obtém o nome do repositório Git
        REPO_NAME=$(basename `git rev-parse --show-toplevel`)
        # Faz commit nas mudanças
        git add -A
        git commit -m "[final turn] automatic commit"
        # Faz push para o repositório remoto
        git push
        echo "Commit realizado em $REPO_NAME"
    fi
done

echo "Finalizado."
