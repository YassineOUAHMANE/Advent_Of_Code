somme_MAS_shape_X = 0
with open("Day_4/input_day_4.txt", "r") as file:
    lines = file.readlines()
    lines = [line.replace("\n","").replace("X",".") for line in lines]
    print(lines)
    for i_line in range(len(lines)):
        for j in range(len(lines[i_line])):
            if lines[i_line][j] == "A":
                if i_line+1 < len(lines) and j+1 < len(lines[i_line]) and lines[i_line+1][j+1] == "S" and i_line-1 >= 0 and j+1 < len(lines[i_line]) and lines[i_line-1][j+1] == "S" and i_line+1 < len(lines) and j-1 >= 0 and lines[i_line+1][j-1] == "M" and i_line-1 >= 0 and j-1 >= 0 and lines[i_line-1][j-1] == "M":
                  somme_MAS_shape_X += 1
                if i_line+1 < len(lines) and j+1 < len(lines[i_line]) and lines[i_line+1][j+1] == "M" and i_line-1 >= 0 and j+1 < len(lines[i_line]) and lines[i_line-1][j+1] == "M" and i_line+1 < len(lines) and j-1 >= 0 and lines[i_line+1][j-1] == "S" and i_line-1 >= 0 and j-1 >= 0 and lines[i_line-1][j-1] == "S":
                  somme_MAS_shape_X += 1  
                if i_line+1 < len(lines) and j+1 < len(lines[i_line]) and lines[i_line+1][j+1] == "M" and i_line-1 >= 0 and j+1 < len(lines[i_line]) and lines[i_line-1][j+1] == "S" and i_line+1 < len(lines) and j-1 >= 0 and lines[i_line+1][j-1] == "M" and i_line-1 >= 0 and j-1 >= 0 and lines[i_line-1][j-1] == "S":
                  somme_MAS_shape_X += 1
                if i_line+1 < len(lines) and j+1 < len(lines[i_line]) and lines[i_line+1][j+1] == "S" and i_line-1 >= 0 and j+1 < len(lines[i_line]) and lines[i_line-1][j+1] == "M" and i_line+1 < len(lines) and j-1 >= 0 and lines[i_line+1][j-1] == "S" and i_line-1 >= 0 and j-1 >= 0 and lines[i_line-1][j-1] == "M":
                  somme_MAS_shape_X += 1    
                
    print(somme_MAS_shape_X)