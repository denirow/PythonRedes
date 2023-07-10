#!/bin/bash

# Variáveis de configuração
DB_HOST="pg.smartsuite.imd.ufrn.br"
DB_PORT="5432"
DB_USER="denys.alexandre"
BACKUP_DIR="/data/backup_bd_aws/"
DB_LIST_FILE="/data/backup_bd_aws/lista_de_bancos.txt"

# Lê a lista de bancos de dados do arquivo
while read -r DB_NAME; do
  # Nome do arquivo de backup
  BACKUP_FILE="$DB_NAME-$(date +%Y%m%d%H%M%S).sql"

  # Comando para fazer o backup
  PG_DUMP_CMD="pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER -w -F p -b -v -f $BACKUP_DIR/$BACKUP_FILE $DB_NAME"

  # Executa o comando de backup
  eval $PG_DUMP_CMD

  # Verifica se o backup foi criado com sucesso
  if [ $? -eq 0 ]; then
    echo ""
    echo "Backup do banco de dados $DB_NAME foi criado com sucesso: $BACKUP_FILE"
    echo ""
  else
    echo ""
    echo "Erro ao criar o backup do banco de dados $DB_NAME"
    echo ""
  fi
done < "$DB_LIST_FILE"