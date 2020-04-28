class NumArray:

	def __init__(self, nums: List[int]):
		self.nums = [0] + nums[::]
		n = len(self.nums)
		self.BIT = [0] * (n)
		for i in range(1, n):
			for j in range(i - self.lowbit(i) + 1, i+1):
				self.BIT[i] += self.nums[j]
	   

	def lowbit(self, x):
		return x & (~x + 1)

	def update(self, i: int, val: int) -> None:
		idx = i+1
		diff = val - self.nums[idx]
		self.nums[idx] = val
		while idx < len(self.nums):
			self.BIT[idx] += diff
			idx += self.lowbit(idx)

	def presum(self, i):
		res = 0
		while i >= 1:
			res += self.BIT[i]
			i -= self.lowbit(i)
		return res

	def sumRange(self, i: int, j: int) -> int:
		res = self.presum(j+1) - self.presum(i)
		return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)