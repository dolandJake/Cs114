

print("Ask any question. about the future.")
life = input()
import random
def getanswer(answernumber):
    if answernumber == 1:
        return "What do you think?"
    elif answernumber == 2:
        return "It might be."
    elif answernumber == 3:
        return "totes mcgoats"
    elif answernumber == 4:
        return "I have no idea bro"
    elif answernumber == 5:
        return "Leave me alone, I don't work for you"
    elif answernumber == 6:
        return "ask the question better"
    elif answernumber == 7:
        return "oh snap, lookin bad"
    elif answernumber == 8:
        return "nope. no. no way. not at all. never."
    elif answernumber == 9:
        return "yeah probably not"


random_int = random.randint(1,9)
fortune = getanswer(random_int)
print(fortune)
