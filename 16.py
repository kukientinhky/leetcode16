def main():
    nums = [0,0,0]
    target = 1
    nums.sort()
    ans = 20000
    ss = 20000
    for i in range(0, len(nums)):
        low, high = i + 1, len(nums) - 1
        while low < high:
            kq = []
            s = nums[i] + nums[low] + nums[high]
            if (ss > abs(s - target)):
                ans = s
                ss = abs(s - target)
            if (s > target): 
                high -= 1
            elif (s < target):
                low += 1
            else:
                lastLowOccurrence, lastHighOccurrence = nums[low], nums[high]
                while low < high and nums[low] == lastLowOccurrence:
                    low += 1  
                while low < high and nums[high] == lastHighOccurrence:
                    high -= 1
    print(ans)
if __name__ == "__main__":
    main()