#!/bin/bash

# Obtém a lista de todos os namespaces
echo "[1/3] Obtendo lista dos namespaces existentes."
echo ""
sleep 2
echo "[2/3] Lista obtida. Iniciando varredura."
echo ""
namespaces=$(kubectl.exe get namespaces -o=jsonpath='{.items[*].metadata.name}')

# Loop pelos namespaces
echo "[3/3] Varrendo namespaces a procura de pods com o status Evicted"
for namespace in $namespaces; do
  echo "Namespace: $namespace"

  # Obtém a lista de pods evicted no namespace atual
  evicted_pods=$(kubectl.exe get pods -n $namespace --field-selector=status.phase=Failed -o=jsonpath='{range .items[?(@.status.reason=="Evicted")]}{.metadata.name}{"\n"}{end}')

  # Loop pelos pods evicted
  for pod in $evicted_pods; do
    echo "Deleting pod: $pod"
    kubectl.exe delete pod $pod -n $namespace
  done

  echo ""
done
echo "Script concluído."