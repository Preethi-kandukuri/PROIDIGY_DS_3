import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt


# Load the data from the extracted CSV file
data = pd.read_csv('/content/bank.csv')

# Display the first few rows of the dataset
print("Dataset preview:\n", data.head())

# Preprocessing the data
# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Define features and target variable
# If it's something else, replace 'y' with the actual column name
X = data.drop(columns=['y' if 'y' in data.columns else 'Y' if 'Y' in data.columns else data.columns[-1]])  
y = data['y' if 'y' in data.columns else 'Y' if 'Y' in data.columns else data.columns[-1]]  

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the Decision Tree
plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=label_encoders['y' if 'y' in label_encoders else 'Y' if 'Y' in label_encoders else data.columns[-1]].classes_) # Update for class_names
plt.title("Decision Tree")
plt.show()
