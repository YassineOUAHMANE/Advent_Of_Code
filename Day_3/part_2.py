import re 
somme_mul = 0
do = True
with open("input_day_3.txt", "r") as file:
        instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", file.read())
        for instr in instructions:
            if instr == "do()":
                do = True
            elif instr == "don't()":
                do = False
            elif instr.startswith("mul") and do:
                # Extract the two numbers from the mul instruction
                match = re.match(r"mul\((\d+),(\d+)\)", instr)
                if match:
                    num1, num2 = map(int, match.groups())
                    somme_mul += num1 * num2

print(somme_mul)