# web: https://pythonprogramminglanguage.com/machine-learning-classifier/
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

#{height, weights, shoe size}
X = [[190,70,44],[166,65,45],[190,90,47],[175,64,39],[171,75,40],[177,80,42],[160,60,38],[144,54,37]]
Y = ['male','male','male','male','female','female','female','female']

#Predict for this vector (height, wieghts, shoe size)
P = [[190,80,46]]

#{Decision Tree Model}
clf = DecisionTreeClassifier()
clf = clf.fit(X,Y)
print "\n1) Using Decision Tree Prediction is " + str(clf.predict(P))

#{K Neighbors Classifier}
knn = KNeighborsClassifier()
knn.fit(X,Y)
print "2) Using K Neighbors Classifier Prediction is " + str(knn.predict(P))

#{using MLPClassifier}
mlpc = MLPClassifier()
mlpc.fit(X,Y)
print "3) Using MLPC Classifier Prediction is " + str(mlpc.predict(P))

#{using MLPClassifier}
rfor = RandomForestClassifier()
rfor.fit(X,Y)
print "4) Using RandomForestClassifier Prediction is " + str(rfor.predict(P)) +"\n"