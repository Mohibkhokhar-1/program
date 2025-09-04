import matplotlib.pyplot as plt

models = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM']
accuracy = [82, 78, 90, 85]

plt.bar(models, accuracy, color=['orange', 'green', 'blue', 'purple'])
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy (%)")
plt.ylim(70, 100)
plt.xticks(rotation=15)
plt.show()

