# Time Complexity O(nlogn)  -- Space Complexity O(n) 
groupe_1 = []
groupe_2 = []
sum_distances = 0
with open("Day_1/input_day_1.txt","r") as file:
    for line in file :
        if line.strip():
            left ,right = map(int,line.split())
            groupe_1.append(left)        
            groupe_2.append(right)

groupe_1.sort()    
groupe_2.sort()
for i in range(len(groupe_1)):
    sum_distances += abs(groupe_1[i] - groupe_2[i])

print(sum_distances)





