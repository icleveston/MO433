from apyori import apriori

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
