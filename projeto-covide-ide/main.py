from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("Projeto Covide19").getOrCreate()

# Armazenando o caminho dos diretórios em váriaveis
raw_path = 'hdfs://namenode:8020/user/elvis/projeto-covid/spark'
stage_path = 'hdfs://namenode:8020/user/elvis/projeto-covid/stage'

# Definindo SCHEMA
schema = 'regiao STRING, estado STRING, municipio STRING, coduf STRING, codmun STRING, codRegiaoSaude STRING, nomeRegiaoSaude STRING, data STRING, semanaEpi INT, populacaoTCU2019 BIGINT, casosAcumulado BIGINT, casosNovos BIGINT, obitosAcumulado BIGINT, obitosNovos BIGINT, Recuperadosnovos BIGINT, emAcompanhamentoNovos BIGINT, interior/metropolitana BIGINT'

# Definindo um diciário com parametros options
options_dic = {
    'sep': ';',
    'header': 'True',
    'schema': 'schema',
    'encoding': 'UTF-8'
}

# Lendo os arquivos do diretório /spark que estão no HDFS
df_covid = (
    spark.read
        .format('csv')
        .options(**options_dic)
        .load(raw_path)
)

print()
print("3. Criando as 3 vizualizações pelo Spark com os dados enviados para o HDFS:")
print()

# Criando visualização do Cartão 1: Casos Recuperados e Em acompanhamento
print("Cartão 1: Casos Recuperados e Em acompanhamento")

df_recuperados_emAcompanhamento = (
    df_covid
        .select(col('Recuperadosnovos').alias("Casos Recuperados"),
                col('emAcompanhamentoNovos').alias("Em acompanhamento"))
        .filter(col('regiao') == 'Brasil')
        .orderBy(col('data').desc())
        .limit(1)
)
df_recuperados_emAcompanhamento.show()
print()
print("------*****------*****------*****------*****------*****")
print()

# Criando visualização do Cartão 2: Casos confirmados
print("Cartão 2: Casos confirmados")

df_casos_confirmados = (
    df_covid
        .withColumn('Incidências*', format_number(col('casosAcumulado') / (col('populacaoTCU2019') / 100000), 1))
        .filter(col('regiao') == 'Brasil')
        .orderBy(col('data').desc())
        .select(col('casosAcumulado').alias("Acumulado"), col('casosNovos').alias("Casos Novos"), 'Incidências*')
        .limit(1)
)
df_casos_confirmados.show()

print()
print("------*****------*****------*****------*****------*****")
print()

# Criando visualização do Cartão 3: Óbitos Confirmados
print("Cartão 3: Óbitos Confirmados")

df_obitos_confirmados = (
    df_covid
        .withColumn('Letalidade*',
                    concat(format_number((col('obitosAcumulado') / (col('casosAcumulado')) * 100), 0), lit(" %")))
        .withColumn('Mortalidade*', format_number(col('obitosAcumulado') / (col('populacaoTCU2019') / 100000), 1))
        .filter(col('regiao') == 'Brasil')
        .orderBy(col('data').desc())
        .select(col('obitosAcumulado').alias("Obitos acumulados"), col('obitosNovos').alias("Casos Novos"),
                'Letalidade*', 'Mortalidade*')
        .limit(1)
)
df_obitos_confirmados.show()

print()
print("------*****------*****------*****------*****------*****")
print()

# Criando visualização pelo Spark com os dados enviados para o HDFS:
print("Criando a visualização pelo Spark com os dados enviados para o HDFS")

(
    df_covid
        .groupBy('regiao', 'data')
        .agg(
        format_number(sum(col('casosAcumulado')), 0).alias("Casos"),
        format_number(sum(col('obitosAcumulado')), 0).alias("Óbitos"),
        format_number(sum(col('casosAcumulado')) / (sum(col('populacaoTCU2019')) / 100000), 1).alias('incidencia'),
        format_number(sum(col('obitosAcumulado')) / (sum(col('populacaoTCU2019')) / 100000), 1).alias('mortalidade')
    )
        .orderBy(col('data').desc())
        .select('regiao', "Casos", "Óbitos", col('incidencia').alias("Incidência/100mil hab."),
                col('mortalidade').alias('Mortalidade/100mil hab'))
        .show(6)
)

spark.stop()
