# airflow_aw_desafio

Este repositório contém uma solução para gerenciar e automatizar a execução das transformações e testes de modelos no dbt utilizando o Apache Airflow Standalone. A DAG configurada executa as tarefas de dbt run e dbt test em sequência, garantindo que os modelos sejam validados após a execução.

## Visão Geral

A DAG, chamada dbt_run_test_job, foi configurada para iniciar no dia 24 de janeiro de 2025, com execução diária às 9h da manhã (schedule_interval="0 9 * * *")

A DAG contém duas tarefas principais, implementadas com o BashOperator:
dbt_run: Executa os modelos dbt, aplicando as transformações definidas.
dbt_test: Valida os dados transformados executando os testes configurados no dbt.

## Pré-requisitos

Para utilizar este projeto, você precisará:

1. **Apache Airflow**
   Instale a versão standalone do Apache Airflow seguindo as [instruções oficiais](https://airflow.apache.org/docs/apache-airflow/stable/start.html).

2. **dbt**
   Certifique-se de que o dbt está instalado e configurado no ambiente virtual utilizado. Para mais informações, consulte a [documentação oficial do dbt](https://docs.getdbt.com/).

3. **Variáveis do Airflow**
   Defina as seguintes variáveis no Airflow para configurar corretamente o caminho do projeto dbt e o ambiente virtual:
   - `PATH_TO_DBT_PROJECT`: Caminho do diretório do projeto dbt.
   - `PATH_TO_DBT_VENV`: Caminho para o binário `activate` do ambiente virtual onde o dbt está instalado.

   Exemplo de configuração:
   ```bash
   airflow variables set PATH_TO_DBT_PROJECT /caminho/para/seu/projeto/dbt
   airflow variables set PATH_TO_DBT_VENV /caminho/para/seu/venv/bin/activate
