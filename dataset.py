# Provided dataset
data = """
Lucas
Benjamin
Amelia
Olivia
Liam
James
Amelia
James
William
Emma
Ava
Amelia
Harper
Benjamin
Elijah
Benjamin
Amelia
Harper
Olivia
William
Harper
Lucas
James
Elijah
Liam
Isabella
Sophia
Charlotte
Mason
Mia
Amelia
Elijah
Benjamin
Mason
James
Mia
James
Olivia
Olivia
Lucas
Olivia
Ava
Noah
James
Lucas
Benjamin
Sophia
Harper
Ava
Mia
"""
# Splitting the data into lines and removing any empty lines
lines = data.strip().split('\n')

# Converting the list of lines into a set to get unique values
unique_variables = set(lines)

# Printing the unique variables
print(unique_variables)
