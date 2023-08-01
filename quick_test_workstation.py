import pathlib as Path
import math, random, sys

# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """

# fruits = ['apple', 'banana', 'cherry']

# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)

# print(fruits)
# m = 3
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]

# nums1 = nums1[:m]

# nums1.extend(nums2)

# print(nums1)


def smallASCII (s1, s2):
    sizeofs1, sizeofs2 = len(s1), len(s2)
    s1, s2 = list(s1), list(s2)
    toRemove = []
    removedCount = 0
    totalCount = 0

    if sizeofs1 < sizeofs2:
        small, big = s1, s2
    else: 
        small, big = s2, s1

    for i in range(len(small)):
        if small[i] in big:
            toRemove.append(small[i])

    
    for j in range(len(toRemove)):
        small.pop(small.index(toRemove[j]))
        big.pop(big.index(toRemove[j]))


        
        
        # small.pop(toRemove[j] - removedCount)
        # big.pop(toRemove[j] - removedCount)
        # removedCount += 1
   

    for x in range(len(small)):
        totalCount += ord(small[x])

    for y in range (len(big)):
        totalCount += ord(big[y])

    print(toRemove)
    print(f"S1: {small} ----------  S2: {big}")
    print(f"Total Counts: {totalCount}")
            

string1 = "aes"
string2 = "aet"
 
smallASCII(string1, string2)

cat = "AAAMMMAAA"
cat = list(cat)

print(cat.index("M"))

