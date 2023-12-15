####################################
# Program:  zycie.py
####################################

from kwadrat import kwadrat
from turtle import update, clear
import random
import sys


txt = """
......................
......................
..............###.....
......................
......................
......................
......................
..###.................
....#.................
...#..................
......................
"""

tab = [] # TODO

MY = len(tab)
MX = len(tab[0])

def rysuj_plansze(tab):
    clear()
    #TODO
    update()        


rysuj_plansze(tab)

KIERUNKI = [ (1,0), (0,1), (-1, 0), (0, -1), (1,1), (-1,1), (1,-1), (-1,-1)]

def liczba_sasiadow(x, y):
    ls = 0  
    #TODO
    return ls
   
def pusta_plansza():
    return [...]
            
# reguły gry w życie:
# jeżeli komórka pełna ma 2 lub 3 sąsiadów przeżywa, wpp ginie
# jeżeli komórka pusta ma 3 sąsiadów, to rodzi się nowa
#
#
print ('Koniec')
input()

