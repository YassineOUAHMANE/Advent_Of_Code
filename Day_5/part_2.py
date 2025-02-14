# Count occurences
slash_elements = set()
updates = []
sum_mid_elements = 0
with open("Day_5/input_day_5.txt", "r") as file:
    for line in file:
        if line.strip() and line[2] == "|":
            first_part = line[0:2]
            second_part = line[3:5]
            slash_elements.add((int(first_part), int(second_part)))
        else:
            updates.append(line)
    updates = updates[1:]  
    updates = [update.replace("\n","") for update in updates]
    updates = [list(map(int,update.split(","))) for update in updates]
    for update in updates:
        valid = True
        for i in range(len(update)-1):
            for j in range(i+1,len(update)):
                if (update[j],update[i])  in slash_elements:
                    update[j],update[i] = update[i],update[j]
                    valid = False
                    
                 
        if not valid:
            sum_mid_elements += update[len(update)//2]
    print(sum_mid_elements)