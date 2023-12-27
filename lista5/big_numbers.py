digits = {}

digits[
    0
] = """
 ###
#   #
#   #
#   #
 ###
"""

digits[
    1
] = """
  #
 ##
  #
  #
 ###
"""

digits[
    4
] = """
 #
#
#####
  #
  #
"""


digits[
    2
] = """
 ###
#   #
  ##
 #
#####
"""

digits[
    5
] = """
#####
#
####
    #
####
"""

digits[
    8
] = """
 ###
#   #
 ###
#   #
 ###
"""

digits[
    6
] = """
 ###
#
####
#   #
 ###
"""

digits[
    9
] = """
 ###
#   #
 ####
    #
 ###
"""

digits[
    3
] = """
####
    #
 ###
    #
####
"""

digits[
    7
] = """
#####
   #
 ###
 #
#
"""

question_mark = """
 ###
#   #
  ##

  #
"""


def fix(s):
    L = s.split('\n')
    for i in range(len(L)):
        if len(L[i]) < 5:
            L[i] += (5 - len(L[i])) * ' '
        else:
            L[i] = L[i][:5]
    return L[1:-1]


def give_number(n):
    if n not in range(10):
        return fix(question_mark)
    return fix(digits[n])
