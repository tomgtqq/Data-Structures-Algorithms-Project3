# Data_Structures_Algorithms-Project3

1. Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root. For example, if the given number is 16, then the answer would be 4.If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5. The expected time complexity is O(log(n)).

2. Search in a Rotated Sorted Array
You are given a sorted array that is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

3. Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answer, return anyone.

4. Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

5. Autocomplete with Tries

6. Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

7. HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.
There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.
The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
