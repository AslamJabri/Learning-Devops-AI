name1 = input("name1: ").lower()
name2 = input("name2: ").lower()

def calculate_lovescore(name1,name2):
    name = name1+name2
    true = 0
    love = 0
    for n in name:
        if "t" == n or "r" == n or "u" == n or "e" == n:
            true += 1
    for l in name: 
        if "l" == l or "o" == l or "v" == l or "e" == l:
            love+=1
            
    print(f"This love score is  {true}{love}")
 
calculate_lovescore(name1,name2)       