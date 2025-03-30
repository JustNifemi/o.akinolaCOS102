from tabulate import tabulate

# The student's data
girls = [
    ("Evelyn", 17, 5.5, 80), ("Jessica", 16, 5.0, 85), ("Somto", 17, 5.4, 70), 
    ("Edith", 18, 5.9, 60), ("Liza", 16, 5.5, 76), ("Madonna", 17, 6.1, 87), 
    ("Waje", 20, 6.0, 95), ("Tola", 19, 5.7, 50), ("Aisha", 19, 5.5, 49), ("Latifa", 17, 5.5, 95)
]

boys = [
    ("Chinedu", 19, 5.7, 74), ("Liam", 16, 5.9, 87), ("Wale", 18, 5.8, 75), 
    ("Gbenga", 17, 6.1, 68), ("Abiola", 20, 5.9, 66), ("Kola", 19, 5.5, 78), 
    ("Kunle", 16, 6.1, 87), ("George", 18, 5.4, 98), ("Thomas", 17, 5.8, 54), ("Wesley", 19, 5.7, 60)
]

# to merge the student's data
students = girls + boys

# Creating the table
headers = ["Name", "Age", "Height", "Score"]
print(tabulate(students, headers=headers, tablefmt="grid"))
