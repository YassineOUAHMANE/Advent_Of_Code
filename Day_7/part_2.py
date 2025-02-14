from itertools import product

# Read the input file
with open("Day_7/input_day_7.txt", "r") as file:
    lines = [line.strip() for line in file]

# Optimized function to validate the test
def is_test_valid(line: str) -> int:
    operators = ['*', '+','||']
    result, test_line = line.split(':')
    test_line = test_line.strip()
    numbers = test_line.split(' ')
    result = int(result)

    # Try all combinations of operators, pruning as early as possible
    for ops in product(operators, repeat=len(numbers) - 1):
        # Calculate the result of the current expression
        # Evaluate manually without using eval to avoid overhead
        calculated_result = int(numbers[0])  # Start with the first number
        for i in range(1, len(numbers)):
            if ops[i - 1] == '+':
                calculated_result += int(numbers[i])
            elif ops[i - 1] == '*':  # ops[i - 1] == '*'
                calculated_result *= int(numbers[i])
            else:
                calculated_result = int(str(calculated_result)+str(numbers[i]))

        # If the calculated result matches the target result, return it
        if calculated_result == result:
            return result

    return 0  # Return 0 if no valid expression matches

# Sum the valid test results
calibration_sum = 0
for line in lines:
    calibration_sum += is_test_valid(line)

print(calibration_sum)



def generate_expressions(numbers,idx = 0,current_expression = ' '):
     expressions = []
     if idx == len(numbers) -1:
          current_expression += str(numbers[idx])
          return [current_expression]
     
     operators = ['*','+']
     for op in operators:
               new_expression  = current_expression + str(numbers[idx]) + op
               expressions.extend(generate_expressions(numbers,idx+1,new_expression))
     return expressions



          













