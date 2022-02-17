import weaponClass as w
import csv


"""
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
"""

# create a file object to open the file in read mode

weapons = open("weapons.csv", "r")
weapons_text_file = csv.reader(weapons, delimiter=",")

# skip the header row

next(weapons_text_file)

# create an empty dictionary named 'weapons_dict'

weapons_dict = {}

# outfile = open("weapons_dict.csv", "w")

# use a for loop to iterate through every row of the csv file

for record in weapons_text_file:
    print(record)
    name = record[0]
    speed = record[1]
    wep_range = record[2]

    # use variables for name,speed and range (optional)

    # create an instance of the weapon object using the
    # specs from the csv file (name,speed and range)

    weapon = w.weaponClass(name, speed, wep_range)
    weapon.bullet_count()

    # append the name and bullet count to 'weapons_dict'

    weapons_dict["Name"] = name

    weapons_dict["Bullet count"] = [weapon.get_bullets()]

    print(weapons_dict)

    # print out the name of the weapon using the appropriate method of the object

    print("Weapon is a", name)

    # print out the speed of the weapon using the appropriate method of the object

    print("Weapon speed is", speed)

    # print out the range of the weapon using the appropriate method of the object

    print("Weapon range is", wep_range)

    # print out the number of bullets of the weapon using the appropriate method of the object

    print("Weapon has", weapon.get_bullets(), "bullets")

    # use an input statement to halt the program and wait for the user -

    input("Press any key to fire the weapon")

    # use an appropriate loop to keep firing the weapon until all bullets run out
    # call the appropriate method to fire a bullet
    # print out the bullet count every time the weapon is fired

    for count in range(weapon.get_bullets()):
        weapon.fire_bullet()
        print(weapon.get_bullets())


# using a loop print out the name and number of bullets from the dictionary
