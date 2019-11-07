from a08_upc_start import *
import sys

def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def a08_test_suite():
    print("\n Test check_integer()")
    testit(check_integer("abc")==False)
    testit(check_integer("HiThePersonWhoIsReadingThisCode")==False)
    testit(check_integer("Bye")==False)

    print("\n Test is_valid_input()")
    testit(is_valid_input("abc")==False)
    testit(is_valid_input("036000291452")==True)
    testit(is_valid_input("036000291455")==True)

    print("\n Test sum_odd()")
    print("")
    testit(sum_odd("036000291452")==14)
    print("")
    testit(sum_odd("012000002304")==4)

    print("\n Test sum_even()")
    print("")
    testit(sum_even("036000291452")==16)
    print("")
    testit(sum_even("012000002304") == 4)

    print("\n Test find_digit()")
    print("")
    testit(find_digit("036000291452")==2)
    print("")
    testit(find_digit("012000002304") == 4)

    print("\n Test  is_valid_modulo()")
    print("")
    testit(find_digit("036000291452")==2)
    print("")
    testit(find_digit("012000002304") == 4)

    print("\n Test left_translation()")
    print("")
    testit(left_translation("036000291452") == "01111010101111000110100011010001101")
    print("")
    testit(left_translation("012000002304") == "00110010010011000110100011010001101")

    print("\n Test right_translation()")
    print("")
    testit(right_translation("036000291452") == "11011001110100110011010111001001110")
    print("")
    testit(right_translation("012000002304") == "11100101110010110110010000101110010")

    print("\n Test left_longer_translate()")
    print("")
    testit(left_longer_translate("036000291452") == "1010001101")
    print("")
    testit(left_longer_translate("012000002304") == "1010001101")

    print("\n Test right_longer_translate()")
    print("")
    testit(right_longer_translate("036000291452") == "1101100101")
    print("")
    testit(right_longer_translate("012000002304") == "1011100101")


if __name__ == "__main__":
    a08_test_suite()
