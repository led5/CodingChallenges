def divisible_string(S):
    """
       :param S: digits
       :type S: string
       :return: count of digits divisible by 3 in changed S 
       :rtype: int 

    """
    sum_of_s = sum(map(int, S))
    count = int(sum_of_s % 3 == 0) 
    for i in map(int,S): # check each digit
        for j in range(10): # check if multiple of 3
            if (i != j) and (sum_of_s - i + j) % 3 ==0:  
                count += 1 
    return count




    