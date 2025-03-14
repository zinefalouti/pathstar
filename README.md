# Pathfinding with A* Algorithm Within a Large Matrix

The Pathstar library implements a pathfinding algorithm using the A* search technique to find the optimal path between a start position and a destination within a large matrix. It avoids looping through the entire matrix by using a scan function that extracts a smaller submatrix based on the start and destination positions.

## Features
- **Matrix Generation**: Generates a random matrix with values between 0 and 9.
- **A* Pathfinding**: Implements the A* search algorithm to find the shortest path avoiding obstacles.
- **Visualization**: Prints the resulting path on the matrix using ASCII characters for easy visualization.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pathstar.git
    cd pathstar
    ```

2. Install dependencies (e.g., NumPy):
    ```bash
    pip install numpy
    ```

3. Import and call the `pathstar` function from your code:
    ```python
    from pathstar import pathstar, print_pathstar, viz_pathstar, generate_matrix

    # Example usage:
    M = generate_matrix(10, 10)
    obstacles = [4, 7, 2, 9]
    start_pos = (9, 7)
    dest_pos = (2, 3)

    path = pathstar(M, start_pos, dest_pos, obstacles)

    # Optionally print the path or visualize it
    print_pathstar(path)
    viz_pathstar(M, path)
    ```

    - `pathstar(M, Spos, Dpos, obstacles)` computes the optimal path.
    - `print_pathstar(path)` prints the path step by step.
    - `viz_pathstar(M, path)` visualizes the path on the matrix using ASCII characters.


