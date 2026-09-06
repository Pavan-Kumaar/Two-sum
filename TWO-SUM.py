def twosum(nums,ans):
    seen={}
    for i,n in enumerate(nums):
        compli = ans-n
        if compli in seen:
            print([seen[compli],i])
        seen[n] = i
    return[]
nums = []
while True:
    a = int(input("ENTER LIST ELEMENT: "))
    nums.append(a)
    b = input("ENTER 'k' TO STOP: ")
    if b == 'k':
        break
print(nums)
ans = int(input("ENTER TARGET NUMBER: "))
twosum(nums,ans)
