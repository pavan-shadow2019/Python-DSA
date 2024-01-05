"""
Question

Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

Video approach to solve this question: here

Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.

Output:
Print the required array.


Constraints:
1<T≤20
1 ≤N<105
0 ≤K<106
0≤ A[i] ≤ 106


Explanation

Here Tis 1, which means one test case.
N = 5 denoting the number of elements in the array and K = 2, denoting the number of steps of
rotations.
The initial array is: 1, 2, 3, 4, 5
In first rotation, 5 will come in the first position and all other elements will move to one position ahead from
their current position. Now, the resultant array will be 5, 1, 2, 3, 4
In second rotation, 4 will come in the first position and all other elements will move to one position ahead
from their current position. Now, the resultant array will be 4, 5, 1, 2, 3   """



#Solution

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle the case when k is greater than n
    return arr[n-k:] + arr[:n-k]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = rotate_array(A, K)
    print(*result)
"""
the time complexity of this solution is O(n) where n is the size of the array. This is because we’re using slicing to rotate the array, which takes linear time. 
The space complexity is also O(n) because we’re creating a new array to store the result.


The function rotate_array takes two arguments: arr (the array to be rotated) and k (the number of rotations). 
The length of the array is stored in n. The line k = k % n is used to handle the case when k is greater than n, as rotating the array n times doesn’t change the array. 
The function then returns the rotated array, which is obtained by slicing the array at n-k and appending the first n-k elements to the end.

The part of the code handles the input and output. It first reads the number of test cases T. For each test case, it reads the array size N and the number of rotations K, and the array A. 
It then calls the function rotate_array to perform the rotations and prints the result.

The * in print(*result) is used to print the list elements separated by a space. Without the *, the list would be printed with brackets and commas.
"""
