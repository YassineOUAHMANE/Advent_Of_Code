# Time complexity O(n)  space_complexity O(n)
groupe_1 = []
groupe_2 = []
Score_similarity = 0
with open("Day_1/input_day_1.txt","r") as file:
    for line in file :
        if line.strip():
            left ,right = map(int,line.split())
            groupe_1.append(left)        
            groupe_2.append(right)
occurences_groupe_2 = {}
for num1 in groupe_2:
    if num1 in occurences_groupe_2:
        occurences_groupe_2[num1]+=1
    else:
        occurences_groupe_2[num1] = 1
for num2 in groupe_1:
    if num2 in occurences_groupe_2: # O(1)
        Score_similarity += occurences_groupe_2[num2]*num2
    
print(Score_similarity)