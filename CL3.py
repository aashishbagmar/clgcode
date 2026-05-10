import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate dummy data (replace with real structural damage data)
def generate_dummy_data(samples=100, features=10):
    data = np.random.rand(samples, features)
    labels = np.random.randint(0, 2, size=samples)  # Binary classification (0/1)
    return data, labels


# AIRS Algorithm (Improved)
class AIRS:
    def __init__(self, num_detectors=10, hypermutation_rate=0.1):
        self.num_detectors = num_detectors
        self.hypermutation_rate = hypermutation_rate

    def train(self, X, y):
        # Select random detectors and store corresponding labels
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = X[indices]
        self.detector_labels = y[indices]

    def predict(self, X):
        predictions = []
        for sample in X:
            # Compute Euclidean distance
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            
            # Find closest detector
            closest_index = np.argmin(distances)
            
            # Assign label of closest detector
            prediction = self.detector_labels[closest_index]
            predictions.append(prediction)

        return np.array(predictions)


# Step 1: Generate Data
data, labels = generate_dummy_data(samples=100, features=10)

# Step 2: Train-Test Split
train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, test_size=0.2, random_state=42
)

# Step 3: Initialize AIRS
airs = AIRS(num_detectors=10, hypermutation_rate=0.1)

# Step 4: Train Model
airs.train(train_data, train_labels)

# Step 5: Predict
predictions = airs.predict(test_data)

# Step 6: Evaluate
accuracy = accuracy_score(test_labels, predictions)

print("Predictions:", predictions)
print("Actual Labels:", test_labels)
print(f"Accuracy: {accuracy:.2f}")
