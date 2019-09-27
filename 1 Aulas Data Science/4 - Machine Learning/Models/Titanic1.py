import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix


test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')

train.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace = True)
test.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace = True)

data_train = pd.get_dummies(train)
data_test = pd.get_dummies(test)

# data_train.isnull().sum().sort_values(ascending=False).head(10)
# Achamos alguns em AGE, dessa forma vamos usar "fillna" posteriormente para preencher esses campos vazios

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

# modelando a rede neural
x = data_train.drop('Survived', axis=1)
y = data_train['Survived']

#mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

mlp = MLPClassifier(activation='relu', alpha=1e-50, hidden_layer_sizes=(5, 5), learning_rate='constant',
       learning_rate_init=0.000000000000000000000000000000000000000000000000000001, max_iter=3000, momentum=0.99,
       nesterovs_momentum=True, power_t=0.5, random_state=2, shuffle=True,
       solver='lbfgs', tol=0.0000000000000000000001, validation_fraction=0.3, verbose=False,
       warm_start=True)

mlp.fit(x,y)

#MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
#       beta_1=0.9, beta_2=0.999, early_stopping=False,
#       epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',
#       learning_rate_init=0.001, max_iter=1500, momentum=0.9,
#       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
#       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
#       warm_start=False)

#MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
#       beta_2=0.999, early_stopping=False, epsilon=1e-08,
#       hidden_layer_sizes=(30, 30, 30), learning_rate='constant',
#       learning_rate_init=0.001, max_iter=300, momentum=0.9,
#       nesterovs_momentum=True, power_t=0.5, random_state=None,
#       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
#       verbose=False, warm_start=False)

predictions = mlp.predict(x)

print(confusion_matrix(y,predictions))
print(classification_report(y,predictions))


# criando a submissão

submission = pd.DataFrame()
submission['PassengerId'] = data_test['PassengerId']
submission['Survived'] = mlp.predict(data_test)

submission.to_csv('submission.csv', index=False)