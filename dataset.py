# Provided dataset
data = """


# Splitting the data into lines and removing any empty lines
lines = data.strip().split('\n')

# Converting the list of lines into a set to get unique values
unique_variables = set(lines)

# Printing the unique variables
print(unique_variables)
