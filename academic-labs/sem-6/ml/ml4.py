import csv

def find_s(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    # Extract attributes and target
    attributes = [row[:-1] for row in data[1:]]
    target = [row[-1] for row in data[1:]]
    
    # Initialize with the first positive example
    for i, val in enumerate(target):
        if val.strip().lower() == 'yes':
            hypothesis = attributes[i].copy()
            break
            
    # Update hypothesis based on remaining positive examples
    for i, val in enumerate(attributes):
        if target[i].strip().lower() == 'yes':
            for j in range(len(hypothesis)):
                if val[j] != hypothesis[j]:
                    hypothesis[j] = '?'
                    
    return hypothesis

# To run: ensure your .csv file matches the table in the image
# result = find_s('training_data.csv')
# print("The most specific hypothesis is:", result)
