#Импорты
from thefuzz import fuzz
from thefuzz import process

import time
import os


#основные (статичные) переменные
list = []


#На выходе должен выдовать стринговую переменную, для дальнейшего использования
def Input ():
    Text = str(input())
    Text = Text.lower()
    return Text

#Главная логика (распределение задач по функциям)
def Processing ():
    pass

def Comm (Text):
    pass