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
    "math score" : "Pontuação de Matemática",
    "reading score" : "Pontuação de Leitura",
    "writing score" : "Pontuação de Escrita"
},inplace=True)

#Extraindo informações sobre o conjunto de dados e verificando se precisa de alguma tranformação na tipagem dos dados
print(base_dados.info())

#Verificando se contém nulos e contabilizando os mesmo 
nulos = base_dados.isnull()

plt.figure(figsize=(10, 6))
plt.title("Mapa de Valores Nulos")
sns.heatmap(nulos, cbar=False, cmap="viridis", yticklabels=False)
plt.xticks(rotation=45, fontsize=10)
plt.show()


#Verifica os valores únicos por coluna 
print(base_dados.nunique())


#Total de registros duplicados no dataframe
print(base_dados.duplicated().sum())


# Tamanho geral da figura
plt.figure(figsize=(18, 6))

# Matemática
plt.subplot(1, 3, 1)
sns.boxplot(y="curso de preparacao para testes", x="Pontuação de Matemática", data=base_dados)
plt.title("Matemática")

# Leitura
plt.subplot(1, 3, 2)
sns.boxplot(y="curso de preparacao para testes", x="Pontuação de Leitura", data=base_dados)
plt.title("Leitura")

# Escrita
plt.subplot(1, 3, 3)
sns.boxplot(y="curso de preparacao para testes", x="Pontuação de Escrita", data=base_dados)
plt.title("Escrita")

# Título geral da figura
plt.suptitle("Distribuição e Variabilidade das Pontuações por Curso Preparatório", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()


# Criando 3 subplots lado a lado
plt.figure(figsize=(18, 6))

# Matemática
plt.subplot(1, 3, 1)
sns.boxplot(y="genero", x="Pontuação de Matemática", data=base_dados, palette={"male": "blue", "female": "pink"})
plt.title("Matemática")
plt.ylabel('')

# Leitura
plt.subplot(1, 3, 2)
sns.boxplot(y="genero", x="Pontuação de Leitura", data=base_dados, palette={"male": "blue", "female": "pink"})
plt.title("Leitura")
plt.ylabel('')

# Escrita
plt.subplot(1, 3, 3)
sns.boxplot(y="genero", x="Pontuação de Escrita", data=base_dados, palette={"male": "blue", "female": "pink"})
plt.title("Escrita")
plt.ylabel('')

# Título geral da figura
plt.suptitle("Distribuição de Pontuação por Disciplina e Gênero", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()


# Criando 3 subplots lado a lado
plt.figure(figsize=(18, 6))

# Matemática
plt.subplot(1, 3, 1)
sns.boxplot(y="nível de educacao dos pais", x="Pontuação de Matemática", data=base_dados)
plt.title("Matemática")
plt.ylabel('')

# Leitura
plt.subplot(1, 3, 2)
sns.boxplot(y="nível de educacao dos pais", x="Pontuação de Leitura", data=base_dados)
plt.title("Leitura")
plt.ylabel('')

# Escrita
plt.subplot(1, 3, 3)
sns.boxplot(y="nível de educacao dos pais", x="Pontuação de Escrita", data=base_dados)
plt.title("Escrita")
plt.ylabel('')

# Título geral da figura
plt.suptitle("Distribuição de Pontuação por Disciplina e Gênero", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
