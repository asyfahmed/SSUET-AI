### 5-3. Alien Colors #1:5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color
### and assign it a value of 'green', 'yellow', or 'red'.

###  Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

alien_color = "green"

if alien_color =="green":
    print("Yay! you just earned 5 points..!")

### Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color = "red"

if alien_color =="green":
    print("Yay! you just earned 5 points..!")

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and Write an if-else chain.

alien_color = "green"

if alien_color =="green":
    print("\nYay! you just earned 5 points for shooting the alien..!")
else:
    print("You just earned 10 points.")

# Write one version of this program that runs the if block and another that runs the else block.

alien_color = "red"

if alien_color =="green":
    print("\nYay! you just earned 5 points for shooting the alien..!")
else:
    print("You just earned 10 points.")


""""5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien."""

alien_color = "green"

if alien_color =="green":
    print("\nYou just earned 5 points")
elif alien_color == "yellow":
    print("\nYou just earned 10 points")
elif alien_color == "red":
    print("\nYou just earned 15 points")


alien_color = "yellow"

if alien_color =="green":
    print("\nYou just earned 5 points")
elif alien_color == "yellow":
    print("\nYou just earned 10 points")
elif alien_color == "red":
    print("\nYou just earned 15 points")

alien_color = "red"

if alien_color =="green":
    print("\nYou just earned 5 points")
elif alien_color == "yellow":
    print("\nYou just earned 10 points")
elif alien_color == "red":
    print("\nYou just earned 15 points")

'''5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:'''

'''
If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
'''
print("\n\n")

age=72
if age < 2:
    print("Person is a baby")
elif age >= 2 and age < 4:
    print("Person is a toddler")
elif age >= 4 and age < 13:
    print("Person is a kid")
elif age >= 13 and age < 20:
    print("Person is a teenager")
elif age >= 20 and age < 65:
    print("Person is an adult")
else:
    print("Person is an elder")

