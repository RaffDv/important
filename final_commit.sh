#!/bin/zsh

# Define o diretório base como a home do usuário
DIR="$HOME"

# Percorre todos os diretórios e subdiretórios do diretório base
for d in "$DIR"/**/.git/; do
echo"$d"
    # Entra no diretório se for um repositório Git
    if [[ -d "$d" ]]; then
        cd "$d/.."
        
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
