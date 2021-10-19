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

# Convert the generator into a list
results = list(results_generator)

# Show the rules with support, confidence and lift
print(' Rule \t\t\t Support,  Confidence,  Lift')
for i in results:    
    items_base = list(i.ordered_statistics[0].items_base)
    items_add = list(i.ordered_statistics[0].items_add)
    
    print(', '.join(items_base) + ' => ' + ','.join(items_add) + '\t\t' + str( round(i[1], 3)) + ', ' + str( round(i[2][0][2], 3) )   + ', ' + str(round(i[2][0][3], 3) ) )


# Plot the confidence, support and lift
supports = []
confidences = []
lifts = []
for item in results:

    supports.append(item[1])
    confidences.append(item[2][0][2])
    lifts.append(item[2][0][3])

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

