"""Repeating a beat in a loop."""

__author__ = "730323188"

counter: int = 0
beat_name: str = input("What beat do you want to repeat? ")
beat_name_concat: str = " " + beat_name 
desired_repititions: int = int(input("How many times do you want to repeat it? "))

while counter < desired_repititions - 1:
    beat_name = beat_name + beat_name_concat
    counter = counter + 1

if desired_repititions <= 0:
    print("No beat...")
else: 
    print(beat_name)    