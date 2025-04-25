# # Create a variable called my_var and assign it the value 42.
# my_var = 42
#
# # Calculate the sum of two numbers, 5 and 7.
# not_my_var = 5 + 7
# print(my_var)
# print(not_my_var)
# print(my_var + not_my_var)
#
# # Define a variable my_string with the value "Hello, World!" and print it.
# my_string = "Hello World!"
# print(my_string)
#
# # Calculate the product of 3 and 4 using the * operator.
# product = 3 * 4
# print(product)
#
# # Convert the string "123" to an integer.
# my_string = "123"
# print(int(my_string))
#
# # Write a program that takes user input for their name and prints a greeting using that name.
# user_input = input("What is your name: ")
# print("Hello " + user_input)
#
# # Create a list of three fruit names: "apple," "banana," and "cherry."
# my_list = ["apple", "banana", "cherry"]
#
# # Access and print the second item in the list of fruits.
# print(my_list[1])
#
# # Perform integer division to divide 7 by 3.
# print(451 // 52)
#
# # Use the if statement to check if a my_var is greater than 10 and print "x is greater than 10"
# # if it is.
# if my_var <= 10:
#     print(my_var)
# else:
#     print("My_var is greater than 10")
#
# # Write a program that reads a file called "sample.txt" and prints its contents.
# # my_file = open("sample.txt", "r")
# # print(my_file)
# #file read all lines a function you would call on file
#
# # Create a string variable my_string and check if it contains the substring "Python.
# my_pie = "How does python work?"
# if "python" in my_pie:
#     print(my_pie)
# else:
#     print("No shot")
#
# # Implement a function that adds two numbers and returns the result
# def add_both(numer_one, second_number):
#     return numer_one + second_number
#
#
# numer_one = 1556221562
# second_number = 124854785484
#
# print(add_both(numer_one, second_number))
#
# # Use a for loop to print numbers from 1 to 5.
# for x in range(1,6):
#     print(x)
#
#
# # Write a program that checks if a number is even or odd and prints the result.
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))
#
# # Create a dictionary called student with keys "name" and "age" and values "Alice" and 20, respectively.
# my_dictionary = {"name": "Alice", "age": 20}
# print(my_dictionary["name"])
#
#
# # Read a file named "data.txt" line by line and print each line.
# # my_file = open("datA.txt", "r")
# # the_lines = fileHandler.readlines()
# # for line in the_lines:
#     # print(line.strip())
#
# # Check if a given string is equal to "Python" using the == operator.
# string1 = "Hello"
# string2 = "Python"
#
# if string1 == "Python":
#     print("Both strings are equal")
# else:
#     print("Both strings are not equal")
#
#
# # Create a list of numbers and use a while loop to print each number until you reach 10.
# my_list_of_numbers = [441, 21, 34, 32, 25, 159, 10, 456, 457, 156]
# index = 0
#
# while index < len(my_list_of_numbers):
#     print(my_list_of_numbers[index])
#     index += 1
#
# print("my_list_of_numbers[index]")
#
# index = 0
# while index < len(my_list_of_numbers):
#     print(my_list_of_numbers[index])
#     if my_list_of_numbers[index] == 10:
#         break
#     index += 1

# Use an elif statement to check the value of a variable score and print a grade (A, B, C, D, or F) based on the score.
your_grade = int(input("What was your score?: "))
if your_grade >= 101:
    print("You can't do that")
elif your_grade >= 90:
    print("A")
elif your_grade >= 80:
    print("B")
elif your_grade >= 70:
    print("C")
elif your_grade >= 60:
    print("D")
elif your_grade <= 60:
    print("F")

