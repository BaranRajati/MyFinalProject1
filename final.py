import os

zoo=['elefnt', 'monke', 'wolf', 'tiger']

msg = """
Choose from options:
1. show
2. add
3. remove
4. exit
"""


while True :
    print(msg)

    us=int(input())

    if us == 1:
        # print animal list
        print(zoo)
    elif us == 2:
        # add
        newAnimal = input('Type animal to ADD: ')
        zoo.append(newAnimal)

    elif us ==3:    
        #remove animal
        removeAnimal=input('Type animal to REMOVE: ')
        zoo.remove(removeAnimal)
        
    elif us ==4:
        #exit
        break

    os.system('cls')
    print(zoo)












