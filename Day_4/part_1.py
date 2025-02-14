import re 
somme_XMAS = 0
with open("Day_4/input_day_4.txt", "r") as file:
    lines = file.readlines()
    lines = [line.replace("\n","") for line in lines]
    for i_line in range(len(lines)):
        for j in range(len(lines[i_line])):
            if lines[i_line][j] == "X":
                # Horizontal forward
                if j+1 < len(lines[i_line]) and lines[i_line][j+1] == "M" and j+2 < len(lines[i_line]) and lines[i_line][j+2] == "A" and j+3 < len(lines[i_line]) and lines[i_line][j+3] == "S":
                  somme_XMAS += 1
                # Horizontal backward
                if j-1 >= 0 and lines[i_line][j-1] == "M" and j-2 >= 0 and lines[i_line][j-2] == "A" and j-3 >= 0 and lines[i_line][j-3] == "S":
                  somme_XMAS += 1
                # vertical forward
                if i_line+1 < len(lines) and lines[i_line+1][j] == "M" and i_line+2 < len(lines) and lines[i_line+2][j] == "A" and i_line+3 < len(lines) and lines[i_line+3][j] == "S":
                  somme_XMAS += 1
                # vertical backward
                if i_line-1 >= 0 and lines[i_line-1][j] == "M" and i_line-2 >= 0 and lines[i_line-2][j] == "A" and i_line-3 >= 0 and lines[i_line-3][j] == "S":
                  somme_XMAS += 1
                # diagonal forward
                if i_line+1 < len(lines) and j+1 < len(lines[i_line]) and lines[i_line+1][j+1] == "M" and i_line+2 < len(lines) and j+2 < len(lines[i_line]) and lines[i_line+2][j+2] == "A" and i_line+3 < len(lines) and j+3 < len(lines[i_line]) and lines[i_line+3][j+3] == "S":
                  somme_XMAS += 1  
                if i_line-1 >= 0 and j+1 < len(lines[i_line]) and lines[i_line-1][j+1] == "M" and i_line-2 >= 0 and j+2 < len(lines[i_line]) and lines[i_line-2][j+2] == "A" and i_line-3 >= 0 and j+3 < len(lines[i_line]) and lines[i_line-3][j+3] == "S":
                  somme_XMAS += 1  
                # diagonal backward
                if i_line+1 < len(lines) and j-1 >= 0 and lines[i_line+1][j-1] == "M" and i_line+2 < len(lines) and j-2 >= 0 and lines[i_line+2][j-2] == "A" and i_line+3 < len(lines) and j-3 >= 0 and lines[i_line+3][j-3] == "S":
                  somme_XMAS += 1  
                if i_line-1 >= 0 and j-1 >= 0 and lines[i_line-1][j-1] == "M" and i_line-2 >= 0 and j-2 >= 0 and lines[i_line-2][j-2] == "A" and i_line-3 >= 0 and j-3 >= 0 and lines[i_line-3][j-3] == "S":
                  somme_XMAS += 1
    print(somme_XMAS)              

                    
                    
    
        

