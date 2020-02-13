class Solution:
    def bestRotation(self, A: List[int]) -> int:
        change = [1] * len(A)
        n = len(A)
        
        for i in range(len(A)): change[(i - A[i] + 1) % n] -= 1
        for i in range(1, len(change)): change[i] += change[i-1]
            
        return change.index(max(change))

# 这个高票答案可谓是非常的精简，优美，但是不是很容易理解
# 出发的思路是要把每个元素在移动N次的全过程中，只有一次+1 和减1.
# 而加一操作可以用数组每次rotate的默认+1来覆盖，不需要特殊对待。
# 每个元素的-1操作的移动次数记录下来即可
# 那么有了这个数据，就可以评估每个rotate值k所带来的影响的大小，从而选取最优的k值