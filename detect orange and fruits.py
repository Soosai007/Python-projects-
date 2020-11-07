from sklearn import tree

# Gathering training data

# features = [[155, “Bumpy”], [180, “Bumpy”], [135, “Bumpy”], [110, “smooth”]]  # Input to classifier

features = [[150, 0], [180, 0], [135, 1], [110, 1]]  # scikit-learn requires real-valued features

# labels = [“orange”, “orange”, “apple”, “apple”]  # output values

labels = [1, 1, 0, 0]

# Training classifier

classifier = tree.DecisionTreeClassifier()  # using decision tree classifier

classifier = classifier.fit(features, labels)  # Find patterns in data

# Making predictions

print (classifier.predict([[150, 0]]))

# Output is 0 for apple
