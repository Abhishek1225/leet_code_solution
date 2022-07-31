"""Given an array, rotate the array to the right by k steps, where k is non-negative."""

 



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = nums 
    
    # k might be more than length of the array , we need to mod against length of the array 
        k %= len(n)
    
        self.reverseArray(n, 0, len(nums)-1)
        self.reverseArray(n, 0, k-1)
        self.reverseArray(n,k,len(nums)-1)
    
        return nums
    def reverseArray(self, n, s, e):
              while s<e:
                n[s], n[e] = n[e], n[s]
                s +=1 
                e -=1
    
    
