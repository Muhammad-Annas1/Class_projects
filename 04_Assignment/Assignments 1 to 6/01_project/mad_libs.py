from . import code, hp, hungergames
from sample_madlibs import zombie
import random

if __name__ == '__main__':
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()






adj = input("Adjective:")
verb1 = input("Verb:")
verb2 = input("Verb:")
famous_person = input("Famous person:")

madlib = f"Computer programming is so {adj}! It makes me excited all the time because " \
    f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

