"""
Consider the subset-sum problem: given an array A[1..n] of n > 0 distinct positive integers and
a positive integer M , find one subset S of the elements in A such that the elements in S sum to M.
For example, if A = [3, 6, 2, 1, 9, 10, 8, 7, 5, 4] and M = 12, then any one of the following sets could be
returned as an answer:
{3, 2, 7}, {3, 1, 8}, {3, 9}, {3, 5, 4}, {2, 1, 9}, {2, 10}, {1, 7, 4}, {8, 4}, {7, 5}.
Write a recursive algorithm for the subset-sum problem. Your algorithm should return one subset that
satisfies the subset sum requirement; it should return “NIL” if no such subset can be found. What is
the complexity of your algorithm? Justify your answer.


"""


def subsetSum(A, n, M):#n is number of elements in array
    if M == 0:#it means we have found the required subset
        return set()
    if n == 0 and M != 0:
        return None# it means fail to find the required subset
    if A[n-1] > M: #to check whether the last element in array is greater than M, if yes, then we cannot include it (because it is impossible to say A[n-1] can form part of M)
        return subsetSum(A, n-1, M)
    else:
        #logic: "one jump, one not jump :)"
        subset1 = subsetSum(A, n-1, M)#exclude the last element in subset, then we continue
        subset2 = subsetSum(A, n-1, M - A[n-1])#include the last element in subset, so we minus
        if subset2 is not None:#we found that a sums up to M - A[n-1], then we add back A[n-1]
            subset2.add(A[n-1])
            return subset2
        else:
            return subset1

# Example usage
A = [3, 6, 2, 1, 9, 10, 8, 7, 5, 4]
M = 12
result = subsetSum(A, len(A), M)
if result is None:
    print("NIL")
else:
    print(result)

#O(2^n)
