---Google IT Automation with Python Professional Certificate

---Python basic scripts:

>>>>Syntax of Code<<<<


friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

=Result:  Hi Taylor
          Hi Alex
          Hi Pat
          Hi Eli


Here's how printing "Hello, World" 10 times looks in Bash and Powershell:


Now try out the Python example yourself:

  for i in range(10):
  print("Hello, World!")


  git link to useful Python stuff

  https://github.com/jeremymaya/google-it-automation-with-python/blob/master/crash-course-on-python/week-one/course-one-week-one.py

  https://technorj.com/crash-course-in-python-coursera-quiz-assessment/


---Week_Two   quizes

  https://quizlet.com/511707998/week-2-python-crash-course-flash-cards/

  https://technorj.com/crash-course-in-python-coursera-quiz-assessment/#:~:text=2%20%2B%202%20%3D%204-,Question%205,produce%20a%20result%20when%20evaluated%3F&text=An%20expression%20is%20a%20combination,operators%2C%20and%20calls%20to%20functions.

  https://gist.github.com/AnisahTiaraPratiwi/378137dd55e477284b502e4a52d78df6


Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to the amount of seconds in 45 minutes and 15 seconds.
Then print the result.

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same.
Confirm your results by making a function call with the correct parameters for both months listed.

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")




---Down below is replaced code:


def month_days(month,days):
    print(month + " has " + str(days) + " days.")
month_days("June", "30")
month_days("July", "31")



This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6?
Tip: a function that calculates the area of a rectangle should probably be called rectangle_area, and if it's receiving base and height, that's what the parameters should be called.


def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))



  ---Refactored CODE


  def rectangle_area(base, height):
z = base*height  # the area is base*height
print("The area is " + str(z))
rectangle_area(5,6)


---Correct Refactored CODE:


  def rectangle_area(base, height):
    area = base*height
    print(" The area is " + str(area))

rectangle_area(5,6)



Functions:


Question 2
This function compares two numbers and returns them in increasing order.

Fill in the blanks, so the print statement displays the result of the function call in order.

Hint: if a function returns multiple values, don't forget to store these values in multiple variables


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
if number2 > number1:
return number1, number2
else:
return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


Question 4
Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed.
Fill in the blanks to complete the code to make it work.


def lucky_number(name):
  number = len(name) * 9
  greet = "Hello " + name + ". Your lucky number is " + str(number)
  return greet

print(lucky_number("Kay"))
print(lucky_number("Cameron"))



Question
The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?


def is_positive(number):
  if  number > 0:
    return True


    Question
The is_positive function should return True if the number received is positive and False if it isn't. Can you fill in the gaps to make that happen?


def is_positive(number):
  if number > 0:
    return True
  else:
    return False



    Question
The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?



def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


Question 5
If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage.
A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return full_blocks*4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192



Question 1
Complete the function by filling in the missing parts.
The color_translator function receives the name of a color, then prints its hexadecimal value.
Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

def color_translator(color):
if color == "red":
hex_color = "#ff0000"
elif color == "green":
hex_color = "#00ff00"
elif color == "blue":
hex_color = "#0000ff"
else:
hex_color = "unknown"
return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


Question 4
Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score".
Fill in this function so that it returns the proper grade.


def exam_grade(score):
  if score:
 grade = "Top Score"
 elif score >= 60:
 grade = "Pass"
 else:
  grade = "Fail"
 return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


Question 7
The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length).
Fill in the blank to make this happen.


def longest_word(word1, word2, word3):
 if len(word1) >= len(word2) and len(word1) >= len(word3):
  word = word1
 elif len(word2) >= len(word3):
  word = word2
 else:
  word = word3
 return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

Module2 Graded Assessment Quizery link:

  https://www.quizerry.com/2021/01/module-2-graded-assessment/



  Fill in the blanks to make the print_prime_factors function print all the prime factors of a number.
  A prime factor is a number that is prime and divides another without a remainder.


def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT



Question 5
The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
An additional requirement is that the result is not to exceed 25, which is done with the break statement.
Fill in the blanks to complete the function to satisfy these conditions.


def multiplication_table(number):
# Initialize the starting point of the multiplication table
 multiplier = 1
# Only want to loop through 5
 while multiplier <= 5:
  result = multiplier * number
  # What is the additional condition to exit out of the loop?
  if result > 25:
   break
  print(str(number) + "x" + str(multiplier) + "=" + str(result))
  # Increment the variable for the loop
  multiplier += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24


Question
Want to try this out? Let's give it a go!

Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).


def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285


Question
In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24.
Fill in the blanks to make the factorial function return the right number.


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


Question
The validate_users function is used by the system to check if a list of users is valid or invalid.
 A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users("purplecat")

Question 2
Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120.
Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1, n):
        result *= x
    return result

for n in range(0, 10):
    print(n, factorial(n+ 1))


    Question 3
Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.


for x in range(1, 11):
  print(x**3)


  Question 4
Write a script that prints the multiples of 7 between 0 and 100.
Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
Remember that 0 is also a multiple of 7.

for i in range(0,100):
    if i%7==0:
        print(i)


  Question 5
The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.
Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.



def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else :
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)


Question
The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1.
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
 Fill in the gaps to make this work:

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


Question 5
Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1.
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.


def sum_positive_numbers(n):
  if n <= 1:
    return n
  return n + sum_positive_numbers(n-1)
  return 0


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15



Question 3
Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number.
Tip: for functions that return a boolean value, you can return the result of a comparison.


def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number//base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number.
Tip: for functions that return a boolean value, you can return the result of a comparison.


def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number//base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


Question 5
Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1.
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.


def sum_positive_numbers(n):
  if n <= 1:
    return n
  return n + sum_positive_numbers(n-1)
  return 0


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


Question 1
Fill in the blanks of this code to print out the numbers 1 through 7.

number = 1
while number <= 7:
	print(number, end=" ")
	 number+=1

   The show_letters function should print out each letter of a word on a separate line.
   Fill in the blanks to make that happen.

   def show_letters(word):
 for letter in word:
  print(letter)

show_letters("Hello")
# Should print one line per letter


Question 3
Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits.
Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

import math
def digits(n):
	count = 0
 if n == 0:
    return 1
 while (n>0):
  count += 1
  n = math.floor(n/10)
 return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

Question 4
This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

1 2 3

2 4 6

3 6 9


def multiplication_table(start, stop):
 for x in range(start, stop+1):
  for y in range(start, stop+1):
   print(str(x*y), end=" ")
  print()

multiplication_table(1, 3)
# Should print the multiplication table shown above


Question 5
The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.
Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
 if start > stop:
  return_string = "Counting down: "
  while x >= stop:
    return_string += str(x)
   if  x != stop:
    return_string += ","
    x -= 1
 else:
  return_string = "Counting up: "
  while x <= stop:
   return_string += str(x)
   if x != stop:
    return_string += ","
   x += 1
 return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function.
For example, even_numbers(6) returns “2 4 6”.
Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
 for x in range(2, maximum +1, 2):
  return_string += str(x) + " "
 return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


Question 7
The following code raises an error when executed. What's the reason for the error?

1234
def decade_counter():
 while year < 50:
  year += 10
 return year

1 / 1 point

Incrementing by 10 instead of 1



Failure to initialize variables



Nothing is happening inside the while loop



Wrong comparison operator


Correct
Well done! The variable year needs to be initialized prior to being used in the while loop.


What is the value of x at the end of the following code?

for x in range(1, 10, 3):
    print(x)


---Answer: Value is 7


What is the value of y at the end of the following code?

for x in range(10):
    for y in range(x):
        print(y)


  Question 10
How does this function need to be called to print yes, no, and maybe as possible options to vote for?


def votes(params):
 for vote in params:
     print("Possible option:" + vote)


votes(['yes', 'no', 'maybe'])


Correct
Excellent! This function is looking for one argument, and the list of strings is just one argument.




Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word.
For example, double_word("hello") should return hellohello10.


def double_word(word):
    return word + word + str(len(word) * 2)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0



Question
Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1].
Be careful how you handle the empty string, which should return True since nothing is equal to nothing.



def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    else:
        return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))



 Try using the index method yourself now!


Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
print(word.index("x"))



Want to try some string methods yourself? Give it a go!


Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case.
For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


Question
Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam".
For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".


def student_grade(name, grade):
#return ""

  return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


#Question 1
#The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
#Fill in the blanks in this function to return True if the passed string is a palindrome, False if not. 


def is_palindrome(input_string):
	# We'll create two strings, to compare them
 new_string = ""
 reverse_string = ""
	# Traverse through each letter of the input string
 for letter in input_string:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
    if letter != " ":
   new_string += letter.lower()
 reverse_string = letter.lower() + reverse_string
 # Compare the strings
 if new_string == reverse_string:
  return True
 return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


#Question 2
#Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place.
#For example, convert_distance(12) should return "12 miles equals 19.2 km".


def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km



Question 4
Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period.
For example, nametag("Jane", "Smith") should return "Jane S."


def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

Question 5
The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).


def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
 if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the
		# end with the new string
  i = sentence.rfind(old)
  new_sentence = sentence[:i]+new
  return new_sentence

	# Return the original sentence if there is no match
 return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


Question
The skip_elements function returns a list containing every other element from an input list, starting with the first element. 
Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in range(len(elements)):
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(elements[i])
	

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []



Question
Let's use tuples to store information about a file: its name, its type and its size in bytes. 
Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 

def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



Question
Try out the enumerate function for yourself in this quick exercise. 
Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position


def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


#Question
#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
#Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.


def odd_numbers(n):
	return [x for x in range(0, n+1) if x%2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


.
Question 2
Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    text = word[1:] + word[0] + "ay" + " "
    say += text
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



#Question 3
#The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
 #For example: 
 #640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
 #755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
 #Fill in the blanks to make the code convert a permission in octal format into a string format.
 
 
 
 def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result +='-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------



#The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … 
#For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.



def group_list(group, users):
  members = group + ": " + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"




#Question 6
#The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. 
#Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 



def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code

Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer


Question
Now, it's your turn! Have a go at iterating over a dictionary!
 


#Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, feature in cool_beasts.items():
    print("{} have {}".format(beast, feature))

#Question
#The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	1) Add an entry for Epilogue on page 39. 	2) Change the page number for Chapter 3 to 24. 	3) Display the new dictionary contents. 	4) Display True if there is Chapter 5, 
#False if there isn't.



toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"]=39
toc["Chapter 3"]=24
print(toc)
print("Chapter 5" in toc)




#Question
#In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
#Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
	for color in wardrobe[cloth]:
		print("{} {}".format(color, cloth))
        

#The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
#Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).


def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+'@'+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))



#The groups_per_user function receives a dictionary, which contains group names with the list of users. 
#Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 



def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
        
        
        
#The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.     




def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". 
The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. 
For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
house_number = ()
street_name = ()

address_string.split()
for house_number, street_name in enumerate(address_string):
  if address_string[0].isnumeric():
    house_number = address_string
    elif address_string[1:].isalpha():
      street_name = address_string    

  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_no,street_no)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


#Above code isn't working


#Question 2
#The highlight_word function changes the given word in a sentence to its upper-case version. 
#For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?


def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


#Question 4
#Use a list comprehension to create a list of squared numbers (n*n). 
#The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.
#For example, squares(2, 3) should return [4, 9].


def squares(start, end):
	return [ (x*x) for x in range(start,end+1)] 

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



#Question 5
#Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.



def car_listing(car_prices):
  result = ""
  for cars in car_prices:
    result += "{} costs {} dollars".format(cars, car_prices[cars]) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))



#Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. 
#Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
#Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. 
#Then print the resulting dictionary.



def combine_guests(guests1, guests2):

    guests2.update (guests1)
    return guests2



Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))



#Question 7
#Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. 
#For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.




def count_letters(text):
  result = {}
  text = text.lower()
  
  for letter in text:
    if letter.isalpha() and letter not in result:
      result[letter] = text.lower().count(letter)
  
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}





#Question
#Want to give this a go? Fill in the blanks in the code to make it print a poem.


class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color="blue"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 


#Question 2
#Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. 
#The values of these attributes can be easily changed at the object level.  The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. 
#Fill in the blanks to make the code satisfy the behavior described in the quote. 



# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    temp=you.apples
    you.apples=me.apples
    me.apples=temp
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
   you.ideas =me.ideas+you.ideas
   me.ideas =you.ideas
   return you.ideas, me.ideas
   
exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))




#The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). 
#Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. 
#For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria". 

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	highest_elevation=0
	return_city =""

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (city1.population>min_population):
		if(highest_elevation<city1.elevation):
			highest_elevation=city1.elevation
			return_city = ("{}, {}".format(city1.name,city1.country))
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (city2.population>min_population):
		if(highest_elevation<city2.elevation):
			highest_elevation=city2.elevation
		return_city = ("{}, {}".format(city2.name,city2.country))
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if(city3.population>min_population):
		if(highest_elevation<city3.elevation):
			highest_elevation=city3.elevation
		return_city = ("{}, {}".format(city3.name,city3.country))

	#Format the return string
	if return_city!="":
		return return_city
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""



#Question 5
#We have two pieces of furniture: a brown wood table and a red leather couch. 
#Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"


class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"
couch = Furniture()
couch.color = "red"
couch.material = "leather"





def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"


 #In this code, there's a Person class that has an attribute name, which gets set when constructing the object. 
 #Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.
 
 
 class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "Hi, my name is {}".format(self.name)  

# Create a new instance with a name of your choice
some_person = Person("Now")  
# Call the greeting method
print(some_person.greeting())


#Let’s create a new class together and inherit from it. Below we have a base class called Clothing. 
#Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. 
#Fill in the blanks to make it work properly.



class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()


#Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: 
#Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. 
#When you’re finished, the script should add up to 10 cotton Polo shirts


class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


#Can you identify which code snippet will correctly open a file and print lines one by one without whitespace?

with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())
        


#Some more functions of the os.path module include getsize() and isfile() which get information on the file size and determine if a file exists, respectively. 
#In the following code snippet, what do you think will print if the file does not exist?



import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")



#The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. 
#Fill in the gaps to create a script called "program.py".



import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'a+') as f:
    f.write(comments)
    print(f.read())
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))



#The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. 
#Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 


import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.exists(directory):
    os.mkdir(directory)
    name=os.path.join(directory, filename)
    file=open(name, 'w')
    file.close()
    return os.listdir(directory)



print(new_directory("PythonPrograms", "script.py"))




#Question 4
#The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. 
#Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.



import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename, 'w') as file:
    pass
  timestamp = os.path.getmtime(filename)
  c=datetime.datetime.fromtimestamp(timestamp)
  # Convert the timestamp into a readable format, then into a string
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(c.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


#The parent_directory function returns the name of the directory that's located just above the current working directory. 
#Remember that '..' is a relative path alias that means "go up to the parent directory". 
#Fill in the gaps to complete this function.



import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())


#Fill in the code to check if the text passed contains the vowels a, e and i, 
#with exactly one occurrence of any other character in between.


import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True




#Fill in the code to check if the text passed contains punctuation symbols: 
#commas, periods, colons, semicolons, question marks, and exclamation points.


import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


#The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. 
#For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. 
#Fill in the code to make this work.


 import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


#Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, 
#and underscores) separated by one or more whitespace characters.



import re
def check_character_groups(text):
  result = re.search(r"[0-9]\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


#Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, 
#followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.



 import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z| ]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


#Question 1
#The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. 
#Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.



import re
def check_web_address(text):
  pattern = r'^[\W\._-]*\.[A-Za-z]*$'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True




#The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. 
#Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?



import re
def check_time(text):
  pattern = r'^(1[0-2]|1?[1-9]):([0-5][0-9])( ?([AaPp][Mm]))'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False



#The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." 
#Fill in the regular expression in this function:


 import re
def contains_acronym(text):
  pattern = r'\(+[A-Z0-9][a-zA-Z]*\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True



#Question 6
#Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. 
#The zip code needs to be preceded by at least one space, and cannot be at the start of the text.



import re
def check_zip_code (text):
  result = re.search(r' \d{5}| \d{5}-\d{4}', text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False



#The long_words function returns all words that are at least 7 characters. 
#Fill in the regular expression to complete this function.


import re
def long_words(text):
  pattern = r'\w{7,}'
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


#Add to the regular expression used in the extract_pid function, 
#to return the uppercase message in parenthesis, after the process id.


import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


#We're working with a CSV file, which contains employee information. 
#Each record has a name field, followed by a phone number field, and a role field. 
#The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the phone number. 
#Fill in the regular expression, using groups, to use the transform_record function to do that.


import re
def transform_record(record):
  new_record = re.sub(r",(\d{3})",r",+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


#The multi_vowel_words function returns 
#all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.


import re
def multi_vowel_words(text):
  pattern = r'\w+[aiueo]{3,}\w+'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


#Question 4
#The transform_comments function converts comments in a Python script into those usable by a C compiler. 
#This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. 
#We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 


import re
def transform_comments(line_of_code):
  result = re.sub(r'\#{1,}',r'//',line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"


#The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
#Fill in the regular expression to complete this function.


import re
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b",r"(\1) \2-\3",phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


#The following code snippet represents the result of a merge conflict. Edit the code to fix the conflict and keep the version represented by the current branch.#


print("Keep me!")



#The following script contains the result of a merge conflict. Edit the code to fix the conflict, so that both versions are included.



def main():
  print("Start of program>>>>>>>")
  print("End of program!")
main()


Question 5
#The datetime module supplies classes for manipulating dates and times, and contains many types, objects, and methods. You've seen some of them used in the dow function, which returns the day of the week for a specific date. 
#We'll use them again in the next_date function, which takes the date_string parameter in the format of "year-month-day", and uses the add_year function to calculate the next year that this date will occur (it's 4 years later for the 29th of February during Leap Year, and 1 year later for all other dates). 
#Then it returns the value in the same format as it receives the date: "year-month-day".   
#Can you find the error in the code? Is it in the next_date function or the add_year function? How can you determine if the add_year function returns what it's supposed to? 
#Add debug lines as necessary to find the problems, then fix the code to work as indicated above. 


import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails, 
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string, 
  # in the format of "yyyy-mm-dd"
  #next_date_string = next_date_obj.strftime("yyyy-mm-dd")
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29



#Question 2
#The find_item function uses binary search to recursively locate an item in the list, returning True if found, False otherwise.
#Something is missing from this function. Can you spot what it is and fix it? Add debug lines where appropriate, to help narrow down the problem.



def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list? 
  ##if item < list[middle]:
  if item in list[ :middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False




#The binary_search function returns the position of key in the list if found, or -1 if not found. We want to make sure that it's working correctly, 
#so we need to place debugging lines to let us know each time that the list is cut in half, whether we're on the left or the right. Nothing needs to be printed when the key has been located.   

#For example, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) first determines that the key, 3, is in the left half of the list, and prints "Checking the left side", 
#then determines that it's in the right half of the new list and prints "Checking the right side", before returning the value of 2, which is the position of the key in the list.  

#Add commands to the code, to print out "Checking the left side" or "Checking the right side", in the appropriate places.  






def binary_search(list, key):
    #Returns the position of key in the list if found, -1 otherwise.

    #List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            print("Checking the left side")
            right = middle - 1
        if list[middle] < key:
            print("Checking the right side")
            left = middle + 1
    return -1 

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
"""Should print 2 debug lines and the return value:
Checking the left side
Checking the left side
0
"""

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
"""Should print no debug lines, as it's located immediately:
4
"""

print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the left side
Checking the right side
6
"""

print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the right side
Checking the right side
9
"""

print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
"""Should print 4 debug lines and the "not found" value of -1:
Checking the right side
Checking the right side
Checking the right side
Checking the right side
-1
"""





#Question 5
#The best_search function compares linear_search and binary_search functions, to locate a key in the list, and returns how many steps each method took, and which one is the best for that situation. 
#The list does not need to be sorted, as the binary_search function sorts it before proceeding (and uses one step to do so). 
#Here, linear_search and binary_search functions both return the number of steps that it took to either locate the key, or determine that it's not in the list. 
#If the number of steps is the same for both methods (including the extra step for sorting in binary_search), then the result is a tie. Fill in the blanks to make this work. 





def linear_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #Initialize the counter of steps
    steps=0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps 

def binary_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #List must be sorted:
    list.sort()

    #The Sort was 1 step, so initialize the counter of steps to 1
    steps=1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        
        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps 

def best_search(list, key):
    steps_linear = linear_search(list, key)
    steps_binary = binary_search(list, key) 
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if (steps_linear < steps_binary):
        results += "Best Search is Linear."
    elif (steps_linear > steps_binary):
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results

print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.



#User exercise
#Now that you understand how multiprocessing works, let's fix CPU bound so that it doesn't take more than 20 hours to finish. Try applying multiprocessing, which takes advantage of the idle CPU cores for parallel processing.

#Open the dailysync.py Python script in the nano editor that needs to be modified. It's similar to multisync.py that utilizes idle CPU cores for the backup.



nano ~/scripts/dailysync.py




#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
import os


def backup(src):
    dest = os.getcwd() + "/data/prod_backup/"
    print("Backing up {} into {}".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
    src = os.getcwd() + "/data/prod/"
    list_of_files = os.listdir(src)
    all_files = []

    for value in list_of_files:
        full_path = os.path.join(src, value)
        all_files.append(full_path)

    with Pool(len(all_files)) as pool:
        pool.map(backup, all_files)
        
        
        
#Improving script
 
#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year =int(input('Enter a value for the year: '))
    month =int(input('Enter a value for the month: '))
    day =int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.


#Write a Python script
#This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:

#Iterate through each file in the folder
#For each file:
#Rotate the image 90° clockwise
#Resize the image from 192x192 to 128x128
#Save the image to a new folder in .jpeg format


#!/usr/bin/env python3
import os, sys
from PIL import Image

size = (128, 128)


for infile in os.listdir():
    outfile = os.path.splitext(infile) [0]
    try:
        with Image.open(infile).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save("/opt/icons/" + outfile, "JPEG")
    except OSError:
        pass


#Web server corpweb
#Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. A Web framework is a set of components that provide a standard way to develop websites quickly and easily.

1. sudo apt-get update

2. sudo apt install python-django-common

3. sudo systemctl start google-startup-scripts.service


*************** Refer to this Code below:


#! /usr/bin/env python3

import os
import requests

#Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file)as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://<IP Address>/feedback/",
    json=fb
print(response.request.body)
print(response.status_code)

#Next steps

#Use the Python requests module to post the dictionary to the company's website. 
#Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.
#In this case that's External IP Address of machine



#In my case  code below was efficient:


#! /usr/bin/env python3
import os
import requests
 
dir="/data/feedback/"
url= "http://1.1.1.1/feedback/"
#IMPORTANT: Replace 1.1.1.1 with your
#  Replace with external "corpweb" IP Address
 
for file in os.listdir(dir):
    tipos = ["title","name","date","feedback"]
    datos = {}
    lineas = []
    print(file)
    with open(dir+"/"+file,"r") as txtfile:
        x = 0
        for line in txtfile:
            datos[tipos[x]] = line.rstrip('\n')
            x += 1
    print(datos)
    response = requests.post(url,json=datos)



#Sample report
#In this section, you will be creating a PDF report named "A Complete Inventory of My Fruit". 
#The script to generate this report and send it by email is already pre-done. You can have a look at the script in the scripts/ directory.

#In the scripts/ directory, you will find reports.py and emails.py files. These files are used to generate PDF files and send emails respectively.
#Take a look at these files using cat command.


#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])


#Emails script



#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
  
  
#Example py script


#!/usr/bin/env python3

import emails
import os
import reports

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48]]
reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "sender@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
emails.send(message)


#Granting executable permission to the example.py script above.

sudo chmod o+wx ~/scripts/example.py



#!/usr/bin/env python3

import json
import locale
import sys

from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    new_data = json.load(json_file)
    data = sorted(new_data, key=lambda i: i['total_sales'])
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    # TODO: also handle most popular car_year

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data




  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  sales = {"total_sales": 0}
  best_car = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    if item["total_sales"] > sales["total_sales"]:
            sales = item
    if not item["car"]["car_year"] in best_car.keys():
            best_car[item["car"]["car_year"]] += item["total_sales"]
    else:
            best_car[item["car"]["car_year"]] += item["total_sales"]
        all_values = best_cart.values()
        max_value = max(all_values)
        max_key = max(best_car, key=best_car.get)
    # TODO: also handle max sales
    # TODO: also handle most popular car_year

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report

  # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
  main(sys.argv)




#Second CODE that's working is below:



#!/usr/bin/env python3

import collections
import json
import locale
import mimetypes
import os.path
import reports
import emails
import sys


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  #locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_sales = {"total_sales": 0}
  max_revenue = {"revenue": 0}
  car_year_sales = collections.defaultdict(int)
  for item in data:
    # We need to convert "$1234.56" into 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item
    car_year_sales[item["car"]["car_year"]] += item["total_sales"]
  max_car_sales_year = (0,0)
  for year, sales in car_year_sales.items():
    if sales > max_car_sales_year[1]:
      max_car_sales_year = (year,sales)
  summary = []
  summary.append("The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]))
  summary.append("The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]))
  summary.append("The most popular year was {} with {} sales.".format(
      max_car_sales_year[0], max_car_sales_year[1]))
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  data = load_data(os.path.expanduser('~') + "/car_sales.json")
  summary = process_data(data)

  # Generate a paragraph that contains the necessary summary
  paragraph = "<br/>".join(summary)
  # Generate a table that contains the list of cars
  table_data = cars_dict_to_table(data)
  # Generate the PDF report
  title = "Sales summary for last month"
  attachment = "/tmp/cars.pdf"
  reports.generate(attachment, title, paragraph, table_data)

  # Send the email
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "\n".join(summary)
  message = emails.generate(sender, receiver, title, body, attachment)
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)
  
  
  
#!/usr/bin/env python3

import os, sys
from PIL import Image

user = os.getenv('USER') # To get the username from environment variable
image_directory = '/home/supplier-data/iamges/'.format(user)
for image_name in os.listdir(image_directory):
   if not image_name.startswith('.') and 'tiff' in image_name:
       image_path = image_directory + image_name
       path = os.path.splitext(image_path)[0]
       im = image.open(image_path)
       new_path = '{}.jepg'.format(path)
       im.convert('RGB').resize((600, 400).save(new_path, "JPEG")



#Below is working script for "Working with supplier images
#In this section, you will write a Python script named changeImage.py to process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

#Size: Change image resolution from 3000x2000 to 600x400 pixel
#Format: Change image format from .TIFF to .JPEG


#!/usr/bin/env python3
from os import listdir, path
from PIL import Image

# set image dir:
img_dir = "supplier-data/images/"

# set reprocess vars:
rx_size = (600, 400)
rx_frmt = "JPEG"

# gather list of image files:
img_files = [f for f in listdir(img_dir) if f.endswith(".tiff")]

# reprocess images:
for file in img_files:
    src_img = Image.open(img_dir + file)
    new_img = src_img.resize(rx_size)
    # NOTE: we need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")
    file, ext = path.splitext(file)
    file += ".jpeg"
    new_img.save(img_dir + file, rx_frmt)
    
    
#Uploading images to web server
#You have modified the fruit images through changeImage.py script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the [linux-instance-IP-Address]/upload URL.

#Copy the external IP address of your instance from the Connection Details Panel on the left side and enter the IP address in a new web browser tab. This opens a web page displaying the text "Fruit Catalog".
#In the home directory, you'll have a script named example_upload.py to upload images to the running fruit catalog web server. To view the example_upload.py script use the cat command.

#Example script is below:

#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})



#Script for uploading images to webserver


#!/usr/bin/env python3
import requests
from os import listdir

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"


def upload(file, url):
    with open(file, "rb") as opened:
        requests.post(url, files={"file": opened})


# set image dir:
img_dir = "supplier-data/images/"

# gather list of image files:
img_files = [img_dir + f for f in listdir(img_dir) if f.endswith(".jpeg")]
for file in img_files:
    upload(file, url)
    
    
    
#Uploading the descriptions
#The Django server is already set up to show the fruit catalog for your company. 
#You can visit the main website by entering linux-instance-IP-Address in the URL bar or by removing /media/images from the existing URL opened earlier. The interface looks like this:

#!/usr/bin/env python3
from os import listdir, path
from unicodedata import normalize
import requests
import json

# set text dir:
txt_dir = "supplier-data/descriptions/"

# gather list of text files:
text_files = [txt_dir + f for f in listdir(txt_dir) if f.endswith(".txt")]

# read text entry:
def getEntry(file):
    # get entry id & set image file name:
    entry_id = path.splitext(path.basename(file))[0]
    img_name = entry_id + ".jpeg"

    # read lines in file, assign to vars:
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name, weight, description = lines

    # reformat weight to integer:
    weight = int(weight.replace(" lbs", ""))

    # set & return entry object:
    keys = ["name", "weight", "description", "image_name"]
    vals = [name, weight, description, img_name]
    entry = dict(zip(keys, vals))
    return entry


url = "http://localhost/fruits/"
for file in text_files:
    data = getEntry(file)
    response = requests.post(url, data=data)
    if response.ok:
        print("uploaded data")
    else:
        print(f"error: {response.status_code}")
        
        
#Generate a PDF report and send it through email
#Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. 
#To generate PDF reports, you can use the ReportLab library. The content of the report should look like this

#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info])
    
    
#Report_email.py

#!/usr/bin/env python3
import os
import datetime
import reports
import emails


# read text entry:
def getDesc(file):
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)


def main():
    # set text dir & gather files:
    txt_dir = "supplier-data/descriptions/"
    txt_files = [txt_dir + f for f in os.listdir(txt_dir) if f.endswith(".txt")]

    # set report file:
    report_file = "/tmp/processed.pdf"

    # generate report body:
    report_body = ""
    for file in txt_files:
        report_body += getDesc(file)

    # set report title:
    today = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(
        today.strftime("%B"), today.day, today.year
    )

    # generate report file:
    reports.generate_report(report_file, report_title, report_body)

    # generate & send email report:
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": report_file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)


if __name__ == "__main__":
    main()
    
    
#Health check py.script


#Health check
#This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

#Report an error if CPU usage is over 80%
#Report an error if available disk space is lower than 20%
#Report an error if available memory is less than 500MB
#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"



#!/usr/bin/env python3
import psutil
import socket
import emails

# set system thresholds:
max_cpu_usage_perc = 80
max_disk_avail_perc = 20
max_mem_avail_mb = 500
chk_local_host_ip = "127.0.0.1"


def chkCPU():
    """check if CPU usage % exceeds max threshold"""
    cpu_usage_perc = psutil.cpu_percent(interval=3)
    return cpu_usage_perc > max_cpu_usage_perc


def chkDisk():
    """check if Disk usage exceeds max threshold"""
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    return dsk_usage_perc > max_disk_usage_perc


def chkMem():
    """check if Memory usage % exceeds max threshold"""
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_mem_avail_mb
    mem_avail = psutil.virtual_memory().available
    return mem_avail < max_mem_avail


def chkNet():
    """check if local host name resolves to local IP"""
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != chk_local_host_ip


def sendAlert(alert):
    """output alert error and send email"""
    content = {
        "sender": "automation@example.com",
        "receiver": "student@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    try:
        message = emails.generate_email(**content)
        emails.send_email(message)
    except:
        print("unable to send alert email notification!")
    finally:
        print(alert)
        exit(1)


def main():
    # check system resources:
    print("checking system resources")
    alert = None
    if chkCPU():
        alert = f"Error - CPU usage is over {max_cpu_usage_perc}%"
    elif chkDisk():
        alert = f"Error - Available disk space is less than {max_disk_avail_perc}%"
    elif chkMem():
        alert = f"Error - Available memory is less than {max_mem_avail_mb}MB"
    elif chkNet():
        alert = f"Error - localhost cannot be resolved to {chk_local_host_ip}"

    # alert if error raised:
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()
    
