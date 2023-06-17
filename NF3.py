

#repositorio
https://github.com/EnzoFx2/-NF3-BIG-DATA-ENZO-SOUZA-FELIX.git

import pandas as pd
#1
data=pd.read_csv('https://raw.githubusercontent.com/EnzoFx2/-NF3-BIG-DATA-ENZO-SOUZA-FELIX/main/world_alcohol.csv', encoding='latin-1',sep=',')
#1-a
data.groupby('Beverage Types')
data['Beverage Types'].value_counts()

#1-b
data.groupby('Beverage Types').sum()
data.groupby(['WHO region','Year']).sum()

#1-c
data['Year'].value_counts()
data['WHO region'].value_counts()
data['Country'].value_counts()
data['Display Value'].sum()

#1-d

data.groupby('Beverage Types').mean()
data.groupby('Beverage Types').median()
data.groupby('Beverage Types').mode()
data.groupby('Beverage Types').describe()
result=data.groupby('Beverage Types')
result.plot.bar(x='Beverage Types')

#1-e-i
data.loc[data['Year'] =='1985']

#1-e-ii
data.loc[data['WHO region'] >'4']

#2
data=pd.read_csv('https://raw.githubusercontent.com/EnzoFx2/-NF3-BIG-DATA-ENZO-SOUZA-FELIX/main/cursos-prouni.csv.csv', encoding='latin-1',sep=',')

#2-a
data.fillna(0.0, inplace=True)

#2-b
data.groupby('grau')

#2-c
result1 = data.loc[data['curso_busca'] == 'Medicina']
result2 = data.loc[data['curso_busca'] == 'Matemática']
result3 = data.loc[data['curso_busca'] == 'Pedagogia']

#2-d
result4 = data.groupby('cidade_busca')['nota_integral_ampla'].mean()

#2-e
result5 = data.loc[data['grau'] == 'TecnolÃ³gico']
result5

#2-f
data.drop('cidade_filtro', axis='columns')

#2-g

result6 = data.loc[data['curso_busca'] == 'Medicina', 'mensalidade'].mean()
result6

#2-h
result7 = data.loc[data['turno'] == 'Integral', 'nota_integral_ampla'].mean()
result7

#2-i

result8 = data.loc[data['grau'] == 'Bacharelado', 'nota_integral_ampla'].describe()
result8

#2-j








