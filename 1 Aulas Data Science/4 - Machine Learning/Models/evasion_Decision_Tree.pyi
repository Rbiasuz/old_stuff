import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

print('''------------------ Bibliotecas ----------------
OK''')

submission = pd.DataFrame()
test = pd.read_csv('Evasao_30.csv', sep=';')
# test = pd.read_csv('Evasao/Evasao_30.csv', sep=';')
train = pd.read_csv('Evasao_70.csv', sep=';')
# train = pd.read_csv('Evasao/Evasao_70.csv', sep=';')

print('''------------------ Dataset foi lido ----------------
OK''')

submission['REAL'] = test['EVADIDO']

train.drop(['CADASTRO', 'CURRICULO', 'FORMADO'], axis=1, inplace = True)
test.drop(['CADASTRO', 'CURRICULO', 'FORMADO', 'EVADIDO'], axis=1, inplace = True)

data_train = pd.get_dummies(train)
data_test = pd.get_dummies(test)

# modelando a arvore de decisão
x = data_train.drop('EVADIDO', axis=1)
y = data_train['EVADIDO']

print('''------------------ Modelo criado ----------------
OK''')

tree = DecisionTreeClassifier(max_depth=1, random_state=0)

print('''------------------ Iniciando Cálculos ----------------
OK''')

tree.fit(x,y)
print('First Try:')
print(tree.score(x, y))
print('----------------------------------------------')

DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2,
                       min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None,
                       random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0,
                       min_impurity_split=None, class_weight=None, presort=False)

tree = DecisionTreeClassifier(max_depth=3, random_state=0)
tree.fit(x,y)
print('2nd Try:')
print(tree.score(x, y))
print('----------------------------------------------')

tree = DecisionTreeClassifier(max_depth=3, random_state=1)
tree.fit(x,y)
print('3th Try:')
print(tree.score(x, y))
print('----------------------------------------------')

tree = DecisionTreeClassifier(max_depth=4, random_state=2)
tree.fit(x,y)
print('4nd Try:')
print(tree.score(x, y))
print('----------------------------------------------')

tree = DecisionTreeClassifier(max_depth=5, random_state=0)
tree.fit(x,y)
print('Last attempt:')
print(tree.score(x, y))


# criando a submissão

submission['EVADIDO'] = tree.predict(data_test)
submission['Acertou?'] = np.where(submission['EVADIDO'] == submission['REAL'], 'yes', 'no')
submission.to_csv('submission.csv', index=False)

print('----------------------------------------------')
print('''------------------ Submissão criada ----------------
OK''')