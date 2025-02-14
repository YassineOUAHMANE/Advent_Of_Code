data = []
with open("Day_2/input_day_2.txt", "r") as file:
    for line in file:
        if line.strip():
            data.append(list(map(int, line.split())))

def is_safe(report):
    # Check if the levels are either all increasing or all decreasing
    increasing = decreasing = True
    
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        
        # If the difference is outside the range of 1 to 3, it's unsafe
        if diff < 1 or diff > 3:
            return False
        
        # Determine if the sequence is increasing or decreasing
        if report[i] < report[i + 1]:
            decreasing = False
        elif report[i] > report[i + 1]:
            increasing = False
    
    # If it's neither entirely increasing nor entirely decreasing, it's unsafe
    return increasing or decreasing


def safe_with_one_removal(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]  # Remove one level
        if is_safe(new_report):
            return True
    return False


def analyze_reports(data):
    safe_data = 0
    
    for report in data:
        # Check if the report is safe without removing any level
        if is_safe(report):
            safe_data += 1
        # Check if the report is unsafe, but becomes safe with one removal
        elif safe_with_one_removal(report):
            safe_data += 1
    
    return safe_data

print(analyze_reports(data))

