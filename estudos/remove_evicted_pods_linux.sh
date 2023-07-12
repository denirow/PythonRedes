#!/bin/bash

# Obtém a lista de todos os namespaces
echo "Obtendo lista dos namespaces existentes"
echo ""
namespaces=$(kubectl get namespaces -o=jsonpath='{.items[*].metadata.name}')

# Loop pelos namespaces
echo "Varrendo namespaces a procura de pods com o status Evicted"
for namespace in $namespaces; do
  echo "Namespace: $namespace"

  # Obtém a lista de pods evicted no namespace atual
  evicted_pods=$(kubectl get pods -n $namespace --field-selector=status.phase=Failed -o=jsonpath='{range .items[?(@.status.reason=="Evicted")]}{.metadata.name}{"\n"}{end}')

  # Loop pelos pods evicted
  for pod in $evicted_pods; do
    echo "Deleting pod: $pod"
    kubectl delete pod $pod -n $namespace
  done

  echo ""
done