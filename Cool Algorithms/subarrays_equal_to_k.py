def solution(K, nums):
	N = len(nums)

	mydict = {0:1}
	count  = 0
	s = 0

	for num in nums:
		s += num

		if s-K in mydict:
			count += mydict[s-K]

		if s in mydict:
			mydict[s] += 1
			
		else:
			mydict[s] = 1

	c = {x:nums.count(x) for x in sorted(list(set(nums)))}
	print(mydict, '\n', c)
	return count

def solution_2(K, nums):
    N = len(nums)
    ans = 0
    for i in range(N):
        summ = 0
        for j in range(i, N):
            summ += arr[j]
            if summ == K:
                ans += 1
    return ans

K = 4
arr = [2, 0, 1, 1, 0, 0, 8, 4, 1, 3]

print(solution_2(K, arr))