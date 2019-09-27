import pandas as pd
from sklearn.tree import DecisionTreeClassifier


test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')

train.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace = True)
test.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace = True)

data_train = pd.get_dummies(train)
data_test = pd.get_dummies(test)

# data_train.isnull().sum().sort_values(ascending=False).head(10)
# Achamos alguns em AGE

# data_test.isnull().sum().sort_values(ascending=False).head(10)
# Achamos alguns em Fare

# new_data_train indica que nós utilizaremos o DataFrame
# .isnull() é uma função que retorna todos os valores nulos encontrados
# .sum() irá somar todas as ocorrências e agrupá-las;
# .sort_values(ascending=False) ordenará os dados.
# Ao passar o argumento ascending=False eu indico querer ordenar do maior para o menor.

data_train['Age'].fillna(data_train['Age'].mean(), inplace = True)
data_test['Age'].fillna(data_test['Age'].mean(), inplace = True)

# .filnna preenche valores nulos

data_test['Fare'].fillna(data_test['Fare'].mean(), inplace = True)

# modelando a arvore de decisão
x = data_train.drop('Survived', axis=1)
y = data_train['Survived']

tree = DecisionTreeClassifier(max_depth=5, random_state=0)
tree.fit(x,y)

print(tree.score(x, y))

# criando a submissão

submission = pd.DataFrame()
submission['PassengerId'] = data_test['PassengerId']
submission['Survived'] = tree.predict(data_test)

submission.to_csv('submission.csv', index=False)