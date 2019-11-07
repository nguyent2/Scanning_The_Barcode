# A08: UPC Barcodes

Name 1: Thy H. Nguyen

Name 2: No needed

Name 3 (if needed): No needed

Repository Link: https://github.com/2019-fall-csc-226/a08-upc-barcodes-nguyent2-a08.git

Google Document Link: https://docs.google.com/document/d/1wShSJoalKz5PZ6jC4kLEOsmpCPQluki8AyW8hutePUg/edit?usp=sharing

## Milestone Reports

Throughout this assignment, I will request (in class) that you give me an update on progress on this assignment. 
Use this space to provide those reports.

Thursday, October 24, 2019:
* Initial commit in the new own branch.

Sunday, October 27, 2019:
* Completed initial design plan and implementations

Monday, October 28, 2019:
* Completed the project

Tuesday, October 29, 2019:
* Added test_suite and check the project again

Wednesday, October 29, 2019:
* Comment out the codes so that other programmers can understand it better.
 
#### USING THE FORMAT OF README IN PROJECT A05 TO WRITE THE REFLECTION AND SUMMARY FOR PROJECT A08

## INITIAL DESIGN PLAN:

Summarize a plan which meets the computational requirements to solve the problem. 
Your plan does not need to be syntactically correct. It needs to capture the flow of logic in a human readable format.

1. Function check_integer() uses to check if the input is an integer
2. Function is_valid_input() uses to check if the input is a valid input for barcode or not
3. Function sum_odd() calculates the digits at the odd position.
4. Function sum_even() calculates the digits at the even position (not including the last digit) 
5. Function find_digit() finds the the check digit of the calculation needed to determine whether it is a barcode or 
not.
6. Function is_valid_modulo() checks to see if the_check_digit matches the last digit of the input 
7. Function left_translation() translate the five number on the left, counting from the second position
8. Function right_translation() translate the five number on the right, counting from the 6th position
9. Function left_longer_translate() translate the number on the first position
10. Function right_longer_translate() translate the number on the last position
11. Function color_black_white() makes the turtle draw the barcode
12. Function draw_barcode() actually draws the barcode on the screen
13. Function draw_number() draws the number below the barcode
14. Function main() Calls all of the functions

## IMPLEMENTATIONS:

A list in bullet form of each function you created, and what is each function’s purpose.
* Function check_integer()
* Function is_valid_input() 
* Function sum_odd() 
* Function sum_even()  
* Function find_digit() 
* Function is_valid_modulo()  
* Function left_translation()
* Function right_translation()
* Function left_longer_translate()
* Function right_longer_translate()
* Function color_black_white()
* Function draw_barcode() 
* Function draw_number() 
* Function main() 


## TESTING:

* Test each function separately in the Scratch work file 
* Print out the result before return something for a function

## ERRORS:

A list in bullet form of all known errors and deficiencies in your implementation.
* Compare an integer with a string (Solving by print(type) of the variable and fix it.)

## SUMMARY:

A brief summary description of the design and implementation, including how much your initial design plan evolved, 
the final result you achieved, and the amount of time you spent as a programmer in accomplishing these results. 
This should be no more than two paragraphs. Consider this like a report of what you did.

I love this project. I could practice with all of dictionary, list, turtle, and everything else. However, I think that
I need to refactor this code more and more in order to make the lines of codes densed but it still does what it should
do.

## COMMENTS:

A paragraph or so of your own comments on and reactions to this assignment. Consider this like a reflection.

This project is absolutely the best project for the final project. In order to make this project become
the final project, I think that I just need to put class in this code, and make it more interactive for users.
