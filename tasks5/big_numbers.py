digits = {}

num0 = """
 ###
#   #
#   #
#   #
 ###
"""

digits[0] = num0

num1 = """
  #
 ##
  #
  #
 ###
"""

digits[1] = num1

num2 = """
 ###
#   #
  ##
 #
#####
"""

digits[2] = num2

num3 = """
####
    #
 ###
    #
####
"""

digits[3] = num3

num4 = """
 #
#
#####
  #
  #
"""

digits[4] = num4

num5 = """
#####
#
####
    #
####
"""

digits[5] = num5

num6 = """
 ###
#
####
#   #
 ###
"""

digits[6] = num6

num7 = """
#####
   #
 ###
 #
#
"""

digits[7] = num7

num8 = """
 ###
#   #
 ###
#   #
 ###
"""

digits[8] = num8

num9 = """
 ###
#   #
 ####
    #
 ###
"""

digits[9] = num9


question_mark = """
 ###
#   #
  ##

  #
"""


def fix(s):
    L = s.split("\n")
    for i in range(len(L)):
        if len(L[i]) < 5:
            L[i] += (5 - len(L[i])) * " "
        else:
            L[i] = L[i][:5]
    return L[1:-1]


def give_number(n):
    if n not in range(10):
        return fix(question_mark)
    return fix(digits[n])
