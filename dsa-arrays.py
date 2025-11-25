# Q1: Find max in array
arr = [5, 2, 9, 1]
print(max(arr))

# Q2: Find min in array
arr = [5, 2, 9, 1]
print(min(arr))

# Q3: Reverse array
arr = [1,2,3,4]
print(arr[::-1])

# Q4: Move zeroes to end
arr = [0,1,0,3,12]
result = [x for x in arr if x != 0] + [0]*arr.count(0)
print(result)

# Q5: Second largest
arr = [10,5,8,20,3]
arr = list(set(arr))
arr.sort()
print(arr[-2])
