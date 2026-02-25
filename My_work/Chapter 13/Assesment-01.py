"""Assessment 1: 
99 Bottles of water

Goal: Create an application that sings the "99 bottles of water" song.
You must write a Python program that prints out all the verses of the song, exactly as the following lyrics show:
99 bottles of water on the wall! 99 bottles of water! Take one down And pass it around 98 bottles of water on the wall!
(...)
2 bottles of water on the wall! 2 bottles of water! Take one down And pass it around 1 bottle of water on the wall! 1 bottle of water! Take one down And pass it around No more bottles of water on the wall!
Tips provided: When developing your solution, consider the following tips:
• The same verse is repeated, each time with fewer bottles, until the bottle counter reaches zero.
• Note how the last two verses read 1 bottle and not 1 bottles, and No more bottles instead of 0 bottles."""


for n in range(99,-1,-1):
    if n == 1:
        print(f"{n:<3}bottle of water on the wall!")
        print(f"{n:<3}bottle of water!\nTake one down\nAnd pass it around")
    elif n == 0:
        print("No more bottles of water on the wall!")
    else:
        print(f"{n:<3}bottles of water on the wall!")
        print(f"{n:<3}bottles of water!\nTake one down\nAnd pass it around")