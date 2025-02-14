data = []
with open("Day_2/input_day_2.txt", "r") as file:
    for line in file:
        if line.strip():
            data.append(list(map(int, line.split())))

safe_data = 0

# Iterate over each report in data
for line in data:
    increasing = decreasing = True  # Assume both increasing and decreasing by default
    
    # Compare each consecutive pair of numbers in the current report
    for a, b in zip(line, line[1:]):
        diff = abs(a - b)

        # If the difference is outside the range of 1 to 3, it's unsafe
        if diff < 1 or diff > 3:
            increasing = decreasing = False
            break  # No need to check further, this report is unsafe
        
        # Check if the sequence is increasing or decreasing
        if a < b:
            decreasing = False  # It can't be decreasing if we have an increase
        elif a > b:
            increasing = False  # It can't be increasing if we have a decrease

    # If it's either fully increasing or fully decreasing, it's safe
    if increasing or decreasing:
        safe_data += 1

print(safe_data)



                


        

