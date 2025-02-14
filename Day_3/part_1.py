import re 
somme_mul = 0
with open("Day_3/input_day_3.txt", "r") as file:
    for line in file:
        if line.strip():
            # how to find this structure in a line"mul(number,number)" using regular expression multply them and add them to somme  
            for num1,num2 in re.findall(r"mul\((\d+),(\d+)\)",line):
                somme_mul += int(num1)*int(num2) 

    print(somme_mul)            
