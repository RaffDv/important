#!/bin/zsh

# Define o diretório base como a home do usuário
DIR="$HOME"

# Percorre todos os diretórios e subdiretórios do diretório base
find "$DIR" -type d -name ".git" -prune | while read d; do
    # Obtém o caminho do diretório pai
    parent_dir="$(dirname "$d")"

    # Entra no diretório se for um repositório Git
    if [[ -d "$parent_dir" ]]; then
        cd "$parent_dir" || continue
        
        # Obtém o nome do repositório Git
        REPO_NAME=$(basename "$(git rev-parse --show-toplevel)")
        
        # Faz commit nas mudanças
        git add -A
        git commit -m "[automatic] automatic commit"
        
        # Faz push para o repositório remoto
        git push
        
        echo "Commit realizado em $REPO_NAME"
    fi
done

echo "Finalizado."
