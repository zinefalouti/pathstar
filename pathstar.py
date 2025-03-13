import numpy as np
import heapq

# Global variables for submatrix positioning
RowStart, ColStart = 0, 0

def main():
    global RowStart, ColStart
    
    M = generate_matrix(10, 10)
    print(M)

    obstacles = [4, 7, 2, 9]

    print_pathstar(pathstar(M,(9,7),(2,3),obstacles))

    viz_pathstar(M, pathstar(M,(9,7),(2,3), obstacles))


def generate_matrix(rows, cols):
    return np.random.randint(0, 10, (rows, cols))


def scan(M, Spos, Dpos):
    global RowStart, ColStart
    
    Sx, Sy = Spos
    Dx, Dy = Dpos

    RowStart, RowEdge = min(Sy, Dy), max(Sy, Dy)
    ColStart, ColEdge = min(Sx, Dx), max(Sx, Dx)

    SubM = M[RowStart:RowEdge + 1, ColStart:ColEdge + 1]
    return SubM


def record_positions(SubM, obstacles):
    global RowStart, ColStart
    
    found_obstacles = []

    for r, row in enumerate(SubM):
        for c, col in enumerate(row):
            abs_pos = (RowStart + r, ColStart + c)
            
            if col in obstacles:
                found_obstacles.append(abs_pos)
    
    return found_obstacles


# Using A* Algorithm to Find the Path from Start Pos to Dest Pos
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(M, start, destination, obstacles):
    rows, cols = M.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, destination)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == destination:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] 
        
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in obstacles:
                temp_g_score = g_score[current] + 1
                
                if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + heuristic(neighbor, destination)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    came_from[neighbor] = current
    
    return []  # No path found


#Composite Function to Call From Other Files
def pathstar(M, Spos, Dpos, obstacles):
    SubM = scan(M, Spos, Dpos)
    obs = record_positions(SubM, obstacles)
    path = a_star_search(M, Spos, Dpos, obs)
    
    return path

#Print The A Star Most Optimal Path Between Start Pos and Dest Pos
def print_pathstar(path):
    print("-"*30)
    print("Path Star Most Optimal Positions To Walk Through are: ")
    for i, p in enumerate(path):
        print(f"Position {i+1}: {p}")


#Visualize the Path
def viz_pathstar(M, path):
    matrix_copy = np.array(M, dtype=str)
    
    for r in range(matrix_copy.shape[0]):
        for c in range(matrix_copy.shape[1]):
            matrix_copy[r, c] = str(M[r, c])
    
    for pos in path:
        r, c = pos
        matrix_copy[r, c] = '*'
    
    for row in matrix_copy:
        print(" ".join(row))

if __name__ == "__main__":
    main()