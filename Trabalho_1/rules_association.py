from apyori import apriori
import matplotlib.pyplot as plt

transactions = []

# Load the data
for line in open('retail.dat', 'r'):
    
    # Remove spaces
    items = line.strip()
    
    # Split and add the items to the transaction
    transactions.append(items.split(' '))


# Initialize the apriori generator
results_generator = apriori(transactions, min_support=0.005, min_confidence=0.9)

for i in results_generator:
    
    items_base = list(i.ordered_statistics[0].items_base)
    items_add = list(i.ordered_statistics[0].items_add)
    
    print(', '.join(items_base) + ' => ' + ','.join(items_add))


supports = []
confidences = []
lifts = []
for item in results_generator:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    supports.append(item[1])
    print("Support: " + str(item[1]))

    confidences.append(item[2][0][2])
    lift = item[2][0][3]
    lifts.append(lift)

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

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

