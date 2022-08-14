# -*- coding: utf-8 -*-
"""
@author: Devasena

Define a class which takes in 3 methods (climate, play, condition) and print the following based on user input:
If the climate is windy, condition is light, play = yes
If the climate is windy, condition is hard, play = no
If the climate is sunny, condition is light, play = yes
If the climate is sunny, condition is hard, play = no (Eg - i/p = windy, hard , o/p = no)

"""


class weather:
    def __init__(self, climate, condition):
        self.climate = climate
        self.condition = condition
        
    def question(self):
        if self.climate == "windy" or self.climate == "sunny":
            if self.condition == "light":
                print("yes")
            elif self.condition == "hard":
                print("no")
            else: print("invalid")
        else: print("invalid")
                    
climate = str(input("how is the climate? \n"))
condition = str(input("how is the condition? \n"))

answer = weather(climate, condition)
answer.question()
