🎯 Análise Exploratória do Desempenho Estudantil 🎯

Este projeto tem como objetivo analisar as pontuações dos alunos em três disciplinas — Matemática, Leitura e Escrita — a partir de variáveis sociais como gênero, escolaridade dos pais e participação em curso preparatório.

Realizei todo o processo de ETL utilizando Python e a biblioteca pandas, desde a leitura e transformação dos dados até a análise e visualização com seaborn e matplotlib. Renomeei as colunas para o português e verifiquei a integridade do dataset (ausência de nulos e duplicados).

As visualizações mostram claramente a variação das notas por grupo. Destaco alguns insights:

Curso de Preparação: Alunos que fizeram o curso obtiveram médias mais altas nas três disciplinas.

Gênero: Meninas apresentaram desempenho superior em leitura e escrita; meninos tiveram mais variabilidade em matemática.

Escolaridade dos Pais: Quanto maior o nível educacional dos pais, melhores as notas dos filhos.

Optei por não usar o Power BI neste projeto justamente para reforçar que um bom analista de dados não deve se limitar a uma única ferramenta. O domínio de múltiplas soluções técnicas, como Python, permite análises mais profundas e flexíveis.

![image](https://github.com/user-attachments/assets/0190c1aa-35bc-4635-b951-0d583b73e7a1)

Mapa heatmap gerado através do seaborn, nos mostra que o dataframe não contém valores nulos para ser tratado e possamos seguir sem comprometer o restante das nossas analises.

![image](https://github.com/user-attachments/assets/7ab6571e-9ec1-4355-b1ad-1843d30b52d0)

🎯 Interpretação dos Boxplots
Cada boxplot compara duas categorias de alunos:

completed → fez o curso preparatório.

none → não fez o curso preparatório.

🔍 Observações importantes:
Média e mediana:

Em todos os casos, alunos que fizeram o curso preparatório (completed) tiveram notas mais altas, com uma mediana mais elevada em Matemática, Leitura e Escrita.

Dispersão dos dados:

A faixa interquartil (IQR, o “corpo” do boxplot) é ligeiramente mais concentrada entre os que fizeram o curso, principalmente em Leitura e Escrita.

Isso sugere menor variabilidade entre esses alunos.

Outliers:

Alunos que não fizeram o curso têm mais outliers de notas muito baixas, especialmente em Matemática e Escrita.

Conclusão sugerida (para usar no seu portfólio):
Ao comparar os grupos com e sem curso preparatório, fica evidente que os alunos que participaram do curso apresentaram desempenho superior em todas as áreas avaliadas (Matemática, Leitura e Escrita), com menos outliers negativos. Isso reforça a hipótese de que a preparação formal contribui positivamente para os resultados nos testes.


![image](https://github.com/user-attachments/assets/a7ffa83d-4b94-4988-bb14-e5884fc9281d)

🎯 Análise de Desempenho Escolar por Gênero
Nesta visualização, utilizei boxplots para comparar a distribuição das pontuações em três disciplinas — Matemática, Leitura e Escrita — de acordo com o gênero dos estudantes.

🔍 Principais Insights:
Matemática: Observa-se que os estudantes do gênero masculino apresentaram uma mediana de desempenho ligeiramente superior à do gênero feminino. Além disso, a dispersão dos dados masculinos foi um pouco maior, indicando uma variedade maior de resultados. Já no grupo feminino, houve mais presença de outliers negativos, representando estudantes com desempenho bem abaixo da média.

Leitura e Escrita: O cenário se inverte. As estudantes do gênero feminino apresentaram medianas mais elevadas e distribuições mais concentradas nessas disciplinas, evidenciando não só um desempenho melhor como também maior consistência nas notas. Os estudantes do gênero masculino, por outro lado, mostraram maior variabilidade e uma mediana inferior.

💡 Conclusão:
A análise evidencia um padrão comportamental de desempenho: homens tendem a se destacar levemente em Matemática, enquanto mulheres demonstram vantagem em áreas de Leitura e Escrita. Essas diferenças podem ser exploradas para entender fatores socioeducacionais que influenciam o rendimento acadêmico, como hábitos de estudo, estilo de aprendizagem ou expectativas sociais relacionadas ao gênero.


![image](https://github.com/user-attachments/assets/03661263-1e86-4415-9398-71ad8d0526cc)

🎓 Impacto da Escolaridade dos Pais no Desempenho dos Alunos
Essa visualização em boxplots explora como o nível educacional dos pais se relaciona com as notas dos alunos em três disciplinas: Matemática, Leitura e Escrita.

🔍 Principais Observações:
Tendência de Crescimento Positivo: Em todas as disciplinas, há uma tendência clara de aumento na mediana das pontuações conforme o nível de escolaridade dos pais avança. Alunos cujos pais possuem ensino superior (bachelor’s ou master’s degree) tendem a ter desempenho acima da média em comparação aos filhos de pais com ensino médio incompleto ou completo.

Matemática: A variação é perceptível. Filhos de pais com nível superior apresentaram melhores desempenhos, enquanto os de pais com some high school ou high school apresentaram menor mediana e mais outliers negativos.

Leitura e Escrita: A influência da escolaridade dos pais é ainda mais evidente. As distribuições são mais homogêneas e elevadas nos níveis de escolaridade mais altos, com menos dispersão e menos presença de valores extremos.

💡 Conclusão:
A análise sugere que o nível de instrução dos pais exerce um papel importante no rendimento escolar dos filhos. Isso pode estar relacionado ao suporte educacional oferecido em casa, à valorização do estudo no ambiente familiar e à maior probabilidade de acesso a recursos pedagógicos. Compreender essa relação pode ajudar a direcionar políticas públicas mais inclusivas e ações de reforço escolar para estudantes em contextos familiares menos favorecidos.


