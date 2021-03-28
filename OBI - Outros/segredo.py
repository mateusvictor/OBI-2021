def read_nums():
	return [int(n) for n in input().split()]

def solution(nums, pos):
	ans = [0] * 10
	length = len(nums)
	prefix = [nums[0]] * length

	for i in range(1, length):
		prefix[i] = prefix[i-1] + nums[i]

	for i in range(0, len(pos)-1):
		start = pos[i]-1
		end = pos[i+1]

		if i != 0:
			div = nums[start+1:end] if end >= start else nums[end-1:start]
		else:
			div = nums[start:end] if end >= start else nums[end-1:start]			
		
		for n in div:
			ans[n] += 1

	return ans


N, M = read_nums()
nums = read_nums()
pos =  read_nums()

print(*solution(nums, pos))
