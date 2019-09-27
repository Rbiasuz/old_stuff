# web: https://pythonprogramminglanguage.com/training-and-test-data/
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load dataset.
iris = load_iris()
X, y = iris.data, iris.target

# split data into training and test data.
train_X, test_X, train_y, test_y = train_test_split(X, y, 
                                                    train_size=0.5,
                                                    test_size=0.5,
                                                    random_state=123)
print("Labels for training and testing data")
print(train_y)
print(test_y)