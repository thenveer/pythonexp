def display(grid):

    row = len(grid)
    col = len(grid[0])
    neighbour_count = []
    for i in range(row):
        l = []
        for j in range(col):
            l.append(0)
        neighbour_count.append(l)
    return(neighbour_count)            
  
