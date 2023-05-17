def is_idempotent_matrix(matrix):
    n = len(matrix)
    
    # Multiply the matrix with itself
    product = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                product[i][j] += matrix[i][k] * matrix[k][j]
    
    # Check if the product is equal to the original matrix
    for i in range(n):
        for j in range(n):
            if product[i][j] != matrix[i][j]:
                return False
    
    return True

# Read the input
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Check if the matrix is idempotent
result = is_idempotent_matrix(matrix)

# Print the result
print(result)
