def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # step 1: count number of zeros
        counter = 0 # keeping track of zeros
        for i in nums:
            if i == 0:
                counter += 1
               
        # step 3: append all zeros to the end of the list
        for x in range(counter):
            nums.remove(0)
            nums.append(0)

if __name__ == '__main__':
    # testing my code
    nums = [0, 0, 1]
    print('func:', moveZeroes([0, 0, 1]))