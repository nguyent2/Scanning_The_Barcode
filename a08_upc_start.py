######################################################################
# Author: Thy H. Nguyen      TODO: Change this to your names
# Username: nguyent2         TODO: Change this to your usernames
#
# Assignment: A08: UPC Barcodes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle
#import the turtle module
def check_integer(barcode):
    """
    check_integer() uses to check if the input is an integer
    :param barcode: the input (of the barcode needed to draw)
    :return: True if the input only contains digits from 0 to 9
    False if the input does not only contain digits from 0 to 9
    """
    try:
        int(barcode)
        #Try to convert the input into an integer.
        return True
        #If the input is an integer, return True
    except ValueError:
        #If an input is not an integer, it will cause a runtime error called ValueError
        #In this case, return False
        return False

def is_valid_input(barcode):
    """
    is_valid_input() uses to check if the input is a valid input for barcode or not
    in other words, if the input has 12 digits and all of the digits are from 0 to 9
    :param barcode: the input of the user (the barcode needed to draw)
    :return: True if the input is a valid barcode, False if the input is not a valid barcode
    """
    if len(barcode) == 12 and check_integer(barcode) == True:
        #This line checks the length of the input, and check to see if it only contains 0 to 9
        return True
        # return True if the input is a valid barcode
        # return False if the input is not a valid barcode
    return False

def sum_odd(barcode):
    """
    sum_odd() calculates the digits at the odd position.
    :param barcode: the user's input to draw a barcode
    :return: sum_odd: the sum of all of the digits at the odd position
    """
    sum_odd =0
    #The sum of the odd positions starts at 0
    for i in [0,2,4,6,8,10]:
        #This means to take the integer at the 1st, 3rd, 5th, 7th, 9th position
        sum_odd = int(sum_odd)+int(barcode[i])
        #Only add the value of the integer at the odd position to the sum
    print("\nThe sum of digits at the position 1,3,5,7,9, 11 is ",sum_odd)
    #Print out the sum of the digits at the odd positions
    return sum_odd

def sum_even(barcode):
    """
    sum_even() calculates the digits at the even position (not including the last digit)
    :param barcode: the user's input to draw a barcode
    :return: sum_even: the sum of all of the digits at the even positions (not including the last digit)
    """
    sum_even = 0
    # The sum of the even positions starts at 0
    for i in (1,3,5,7,9):
        # This means to take the integer at the 2nd, 4th, 6th, 8th, 10th position
        sum_even = int(sum_even)+int(barcode[i])
        # Only add the value of the integer at the even position to the sum
    print("\nThe sum of digits at the position 2,4,6,8,10 is ",sum_even)
    return sum_even

def find_digit(barcode):
    """
    find_digit() finds the the check digit of the calculation needed to determine whether it is a barcode or not.
    :param barcode: the input of the user (the barcode needed to draw)
    :return: the_check_digit: of the calculation needed to determine whether it is a barcode or not
    """
    result = (int(sum_odd(barcode)) * 3 + int(sum_even(barcode))) % 10
    # The result of the sum of odd positions, times three, and the sum of even positions.
    # Then divide that sum for 10 and get the remainder
    print("\nThe remainder of the calculation is ", result)
    if result != 0:
        # If the result is not 0
        the_check_digit = 10 - int(result)
        # The the_check_digit will be 10 - the result
    else:
        the_check_digit = 0
        # Otherwise, the check_digit is 0
    print("\nThe digit to compare is ", the_check_digit)
    return the_check_digit

def is_valid_modulo(barcode):
    """
    is_valid_modulo() checks to see if the_check_digit matches the last digit of the input
    :param barcode: the input of the user (the barcode needed to draw)
    :return: True if the_check_digit matches the last digit of the input
    False if the_check_digit does not match the last digit of the input
    """
    print("\nThe last digit is ", barcode[11])
        #print the last digit
    if int(find_digit(barcode)) == int(barcode[11]):
        print("\nThe last digit matches the check digit.")
        return True
    print("\nThe last digit does not match the check digit.")
    return False


def left_translation (barcode):
    """
    left_translation() translate the five number on the left, counting from the second position
    :param barcode: the input of the user (the barcode needed to draw)
    :return: the_one_to_draw_on_the_left: the string of numbers needed to draw on the left
    """
    dictionary = { 0: "0001101",
                    1 : "0011001",
                   2 : "0010011",
                   3 : "0111101",
                   4: "0100011",
                   5 : "0110001",
                   6 : "0101111",
                   7: "0111011",
                   8 : "0110111",
                   9: "0001011" }
    the_one_to_draw_on_the_left = ""
    #Create a dictionary for the binary code of the digit
    for i in range(1,6):
        #This means take the digit from the 1st to the 5th position
        j = 0
        # j starts at 0 in the dictionary
        while j < 10:
            # loop through the whole dictionary
            if int(barcode[i]) == j:
                #If the digit equals anything in the dictionary, concatenate the binary
                the_one_to_draw_on_the_left = str(the_one_to_draw_on_the_left) + dictionary[j]
            j+=1 #Next j
    print("\nThe binary code of digit from 2 to 6 is ",the_one_to_draw_on_the_left)
    return the_one_to_draw_on_the_left

def right_translation(barcode):
    """
    right_translation() translate the five number on the right, counting from the 6th position
    :param barcode: the input of the user (the barcode needed to draw)
    :return: the_one_to_draw_on_the_right: the string of numbers needed to draw on the left
    """
    dictionary = {0: "1110010",
                  1: "1100110",
                  2: "1101100",
                  3: "1000010",
                  4: "1011100",
                  5: "1001110",
                  6: "1010000",
                  7: "1000100",
                  8: "1001000",
                  9: "1110100"}
    the_one_to_draw_on_the_right = ""
    # Create a dictionary for the binary code of the digit
    for i in range(6, 11):
        j = 0
        while j < 10:
            if int(barcode[i]) == j:
                the_one_to_draw_on_the_right = str(the_one_to_draw_on_the_right) + dictionary[j]
            j += 1
    print("\nThe binary code of digit from position 7 to 11 is ", the_one_to_draw_on_the_right)
    return the_one_to_draw_on_the_right

def left_longer_translate(barcode):
    """
    left_longer_translate() translate the number on the first position
    :param barcode: the input of the user (the barcode needed to draw)
    :return: the_left_longer_translation, which is the binary of the first position in the barcode
    """
    dictionary = {0: "0001101",
                  1: "0011001",
                  2: "0010011",
                  3: "0111101",
                  4: "0100011",
                  5: "0110001",
                  6: "0101111",
                  7: "0111011",
                  8: "0110111",
                  9: "0001011"}
    #Create a dictionary for the binary code
    j = 0
    while j<10:
        if int(barcode[0]) ==j:
            #Just take the first digit
            the_left_longer_translation = "101"+dictionary[j]
        j+=1
    print("\nBinary of longer lines on the left is ",the_left_longer_translation)
    return the_left_longer_translation


def right_longer_translate(barcode):
    """
    right_longer_translate() translate the number on the last position
    :param barcode: the input of the user (the barcode needed to draw)
    :return: the_right_longer_translation, which is the binary of the first position in the barcode
    """

    dictionary = {0: "1110010",
                  1: "1100110",
                  2: "1101100",
                  3: "1000010",
                  4: "1011100",
                  5: "1001110",
                  6: "1010000",
                  7: "1000100",
                  8: "1001000",
                  9: "1110100"}
    j = 0
    while j < 10:
        if int(barcode[11]) == j:
            #Take only the last digit
            the_right_longer_translation = dictionary[j]+"101"
        j += 1
    print("\nBinary of longer lines on the right is ", the_right_longer_translation)
    return the_right_longer_translation


def color_black_white(option, turtle, height):
    """
    color_black_white() makes the turtle draw the barcode
    :param option: the binary code
    :param turtle: the turtle to draw with
    :param height: the height of the line
    :return: None
    """
    turtle.shape("circle")
    turtle.shapesize(0.0001,0.0001)
    turtle.speed(0)
    turtle.pensize(2)
    for i in range(len(option)):
        #Draw 1 or 0 for each digit
        if int(option[i]) == 1:
            turtle.right(90)
            turtle.forward(height)
            turtle.forward(-height)
            turtle.penup()
            turtle.left(90)
            turtle.forward(2)
            turtle.pendown()

        else:
            #Draw 0
            # 0 and 1 is the same, but 0 is penup all the time, and 1 is pendown and penup
            turtle.penup()
            turtle.right(90)
            turtle.forward(height)
            turtle.forward(-height)
            turtle.left(90)
            turtle.forward(2)
            turtle.pendown()

def draw_barcode(barcode, turtle):
    """
    draw_barcode() actually draws the barcode on the screen
    :param barcode: the user's input
    :param turtle: the turtle to draw with
    :return: None
    """
    color_black_white((left_longer_translate(barcode)),turtle,110)
    color_black_white((left_translation(barcode)),turtle,100)
    color_black_white("01010",turtle,110)
    color_black_white((right_translation(barcode)),turtle,100)
    color_black_white((right_longer_translate(barcode)),turtle,110)
    #Draw barcode with different height

def draw_number(turtle,barcode):
    """
    draw_number() draws the number below the barcode
    :param turtle: the turtle to draw with
    :param barcode: the user's input
    :return: None
    """
    #Draw the line of number of barcodes below
    turtle.shape("circle")
    turtle.shapesize(0.0001, 0.0001)
    turtle.speed(0)
    turtle.penup()
    turtle.right(90)
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(-10)
    turtle.pendown()
    turtle.write((barcode[0]),move=False,align="center",font=("TimesNewRoman",14,"bold"))
    turtle.penup()
    turtle.forward(70)
    five_first_num = barcode[1]+barcode[2]+barcode[3]+barcode[4]+barcode[5]
    turtle.pendown()
    turtle.write(five_first_num,move=False,align="center",font=("TimesNewRoman",14,"bold"))
    turtle.penup()
    turtle.forward(70)
    five_last_num = barcode[6]+barcode[7]+barcode[8]+barcode[9]+barcode[10]
    turtle.pendown()
    turtle.write(five_last_num,move=False,align="center",font=("TimesNewRoman",14,"bold"))
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
    turtle.write(barcode[11],move=False,align="center",font=("TimesNewRoman",14,"bold"))
    # Take all of the number of the barcode

def main():
    """
    Call all of the functions
    :return: The barcode on the screen
    """

    input_code = input("\nEnter a 12 digit code [0-9]: ")
    while is_valid_input(input_code) == False:
        print("\nThis input is invalid!")
        input_code = input("\nEnter a 12 digit code [0-9]: ")
        is_valid_input(input_code)
    print("\nThis input has 12 digits and it is ready for next step! The input is ", input_code)
    wns = turtle.Screen()
    thy = turtle.Turtle()
    jessie = turtle.Turtle()

    if is_valid_modulo(input_code):
        draw_barcode(input_code,thy)
        draw_number(jessie,input_code)
    else:
        thy.write("Input is not a valid barcode!",move=False,align="center",font=("TimesNewRoman",14,"bold"))

    wns.exitonclick()


if __name__ == "__main__":
    main()
