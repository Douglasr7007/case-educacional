import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Lendo o arquivo e armazenando o mesmo em uma variavél 
base_dados = pd.read_csv("C:/case-educacional/Dados/StudentsPerformance.csv")

#Faz uma breve visualização para verificar o contexto dos dados 
print(base_dados.head())

#Verificando a dimensão do dataframe
print(base_dados.shape)

#Renoamendo as colunas no local ( na mesma variável )
base_dados.rename(columns={
    "gender" : "genero",
    "race/ethnicity" : "raça/etnia",
    "parental level of education" : "nível de educacao dos pais",
    "lunch" : "almoco",
    "test preparation course" : "curso de preparacao para testes",
    "math score" : "pontuação de matemática",
    "reading score" : "pontuacao de leitura",
    "writing score" : "pontuação de escrita"
},inplace=True)

#Extraindo informações sobre o conjunto de dados e verificando se precisa de alguma tranformação na tipagem dos dados
print(base_dados.info())



