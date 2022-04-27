import random
import pandas as pd

student = pd.read_excel('people.xlsx',sheet_name='Sheet1') 
students = student['name'].tolist()

def make_random_groups(students, number_of_groups):
    
    #Shuffle list of students
    random.shuffle(students)
    
    #Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = students[index::number_of_groups]
        all_groups.append(group)
    
    #Format and display groups
    home = ['Gryffindor','Ravenclaw','Hufflepuff','Slytherin']
    
    for index, group in enumerate(all_groups):
        print(f"{home[index]}: {', '.join(group)}")
        print(f"number of people :{len(group)}")
        print('----------------')
    
    print(len(students))

make_random_groups(students, 4)