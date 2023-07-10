#!/bin/bash

# Obtém a lista de namespaces
namespaces=$(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}')

# Loop pelos namespaces
for namespace in $namespaces; do
  echo "Procurando por pods evicted no namespace: $namespace"
  
  # Obtém a lista de pods evicted no namespace atual
  evicted_pods=$(kubectl get pods -n $namespace --field-selector=status.phase=Failed -o jsonpath='{range .items[*]}{.metadata.name} {.status.phase}{"\n"}{end}' | grep Evicted)
  
  # Se houver pods evicted, exclua-os
  if [ ! -z "$evicted_pods" ]; then
    echo "Os seguintes pods foram encontrados com status evicted no namespace $namespace:"
    echo "$evicted_pods"
    
    # Exclua cada pod encontrado
    while read -r pod _; do
      kubectl delete pod $pod -n $namespace
    done <<< "$evicted_pods"
    
    echo "Os pods evicted foram excluídos com sucesso."
  else
    echo "Nenhum pod com status evicted foi encontrado no namespace $namespace."
  fi
  
  echo ""
done