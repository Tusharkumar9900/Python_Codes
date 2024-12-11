# basics Questions of Python Asked in Interview for fresher

#Factorial of a given Number
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))



# Largest among three Numbers entered by user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)
print("Largest number:", largest)



# check given string is a Palindrome
def is_palindrome(s):
  return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
  print("Palindrome")
else:
  print("Not a palindrome")



# count the vowels in a given string
def count_vowels(s):
  vowels = "aeiouAEIOU"
  return sum(1 for char in s if char in vowels)

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))



#Check if given number is prime
def is_prime(num):
  if num <= 1:
    return False

  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

num = int(input("Enter a number: "))
if is_prime(num):
  print("Prime")
else:
  print("Not prime")


# Array Programs

### QUestion -1
#Examples:
# Input : arr[] = {1, 2, 3}
# Output : 6
# Explanation: 1 + 2 + 3 = 6

def _sum(arr):
 
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0
 
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
 
    return(sum)
 
 
# main function
if __name__ == "__main__":
    # input values to list
    arr = [12, 3, 4, 15]
 
    # calculating length of array
    n = len(arr)
    # calling function ans store the sum in ans
    ans = _sum(arr)
    # display sum
    print('Sum of the array is ', ans)



# Python Program to Find Largest Element in an Array

# Input : arr[] = {10, 20, 4}
# Output : 20
# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100

def largest(arr, n):
 
    # Initialize maximum element
    max = arr[0]
 
    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
 
 
# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)