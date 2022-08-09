# Projeto Big Data com Spark

Projeto desenvolvido para o curso Big Data Engineer Semantix Academy. O projeto consiste em desenvolver executar tarefas para responder a 09 questões. Os dados usados no projeto são da fonte https://covid.saude.gov.br/. 
</br>

## 🛠️ Questões e Soluções

### 1. Enviar os dados para o hdfs:

* Envio dos arquivos para o HDFS:
</br>
#### 📌 Visualização
![](img/img-hdfs/envio-csv-hdfs.JPG)
![](img/img-hdfs/arquivos-no-hdfs.JPG)
</br>
</br>

### 2. Otimizar todos os dados do hdfs para uma tabela Hive particionada por município.

#### 📌 Visualizações
</br>

* Criando a tabela tb_covide19 no Hive:
![](img/img-hive/criando_tab_hive.JPG)
</br>

* Visualizando a descrição da tabela tb_covide19:
![](img/img-hive/desc_tabela_hive.JPG)

* Select na tabela tb_covide19 vazia:
![](img/img-hive/select_tb_vazia.JPG)

* Load dos dados na tabela:
![](img/img-hive/load-tab-hive.JPG)

* Select na tabela tb_covide19:
![](img/img-hive/select_tb_com_dados.JPG)
</br>

* Contando os registros da tabela:
![](img/img-hive/select_qtd_reg_tb.JPG)
</br>

* Visualizando os dados distintos da coluna região:
![](img/img-hive/select_regiao.JPG)
</br>
</br>

### 3. Criar as 3 vizualizações pelo Spark com os dados enviados para o HDFS:

![](img/img-div/carta.JPG)

#### 🛠️ Soluções:
</br>

* Cartão 01: Casos Recuperados e Em acompanhamento:
![](img/img-spark/cartao-01.JPG)
</br>

* Cartão 02: Casos confirmados:
![](img/img-spark/cartao-02.JPG)
</br>

* Cartão 3: Óbitos Confirmados:
![](img/img-spark/cartao-03.JPG)
</br>
</br>

### 4. Salvar a primeira visualização como tabela Hive.

#### 🛠️ Solução:

* Salvando a visualização do cartão 01 em como tabela hive:
![](img/img-spark/cartao-01-pHive.JPG)
</br>
</br>

## 5. Salvar a segunda visualização com formato parquet e compressão snappy:


#### 🛠️ Solução:

* Salvando a visualização do cartão 02 em formato parquet e compressão snappy:
![](img/img-spark/cartao-02-pParquetSnap.JPG)
</br>
</br>

### 6. Salvar a terceira visualização em um tópico no Kafka:

#### 🛠️ Solução:

* Criando o tópico no Kafka:
![](img/img-kafka/topic_criado.JPG)
</br>
* Salvando a visualização do cartão 03 no tópico no Kafka:
![](img/img-spark/cartao-03-kafka.JPG)
</br>
![](img/img-spark/cartao-03-kafka2.JPG)
</br>
</br>

### 7. Criar a visualização pelo Spark com os dados enviados para o HDFS:

#### 🛠️ Solução:

![](img/img-spark/cartao-full.JPG)
</br>
</br>

### 8. Salvar a visualização do exercício 6 em um tópico no Elastic.

#### 🛠️ Solução:
* Em desenvolvimento
![](img/)
</br>
</br>

### 9. Criar um dashboard no Elastic para visualização dos novos dados enviados.

#### 🛠️ Solução:
* Em desenvolvimento