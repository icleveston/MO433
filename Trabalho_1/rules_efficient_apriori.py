from efficient_apriori import apriori
import matplotlib.pyplot as plt

transactions = []

# Load the data
for line in open('retail.dat', 'r'):
    
    # Remove spaces
    items = line.strip()
    
    # Split and add the items to the transaction
    transactions.append(items.split(' '))


# Initialize the apriori generator
itemsets, rules = apriori(transactions, min_support=0.005, min_confidence=0.9)

# Print rules
for rule in reversed(sorted(rules, key=lambda rule: rule.lift)):
  print(rule)
  
# Plot the confidence, support and lift
supports = []
confidences = []
lifts = []
for item in rules:

    supports.append(item.support)
    confidences.append(item.confidence)
    lifts.append(item.lift)

# Plots
plt.title("Confidence vs Support")
plt.scatter(supports, confidences,   alpha=0.5, marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()

plt.title("Support vs Lift")
plt.scatter(supports, lifts,   alpha=0.5, marker="*")
plt.xlabel('support')
plt.ylabel('lift') 
plt.show()

plt.title("Lift vs Support")
plt.scatter(confidences, lifts,   alpha=0.5, marker="*")
plt.xlabel('confidences')
plt.ylabel('lift') 
plt.show()
