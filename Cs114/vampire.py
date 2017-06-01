"""if vampire ask age"""



print("Are you a vampire?")
vamp = str(input())
if vamp == "no":
    print("Are you a werewolf?")
    wolf = str(input())
    if wolf == "yes":
        print("The feeding continues during the next full moon.")
    if wolf == "no":
        print("Then you are free of curses!")
if vamp == "yes":
    print("How old are you?")
    num = int(input())
    if num < 100:
        print("There is still time to break the curse.")
    if num > 100:
            print("It is too late for you, your soul has been tainted.")
    if num == 100:
        print("You have passed the Threshold, your soul is doomed.")
