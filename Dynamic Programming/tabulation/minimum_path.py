
def print_matrix(matrix):
	print('[')
	for row in matrix:
		print(f'	{row},')
	print(']')


def min_path():
	dp = [[0 for _ in range(W)] for _ in range(H)]

	for row in range(H):
		for column in range(W):
			if row==0 and column==0:
				dp[row][column] = grid[row][column]
			else:
				dp[row][column] = grid[row][column] + min(
					(float('inf') if row==0 else dp[row-1][column]), # Up cell
					(float('inf') if column==0 else dp[row][column-1]), # Left cell
					# (float('inf') if column==0 or row==0 else dp[row-1][column-1]) # Check for diagonal
				) 

	return dp[H-1][W-1]

W = H = 3
grid = [
	[1, 3, 1],
	[1, 9, 1],
	[4, 6, 1],
]

print(min_path())