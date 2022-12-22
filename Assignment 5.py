# Driver: Christian Taylor          U-Number: U75799592       Participation percentage: 50%
# Navigator: Anshul Raghuvanshi     U-Number: U69656337       Participation percentage: 50%
# This program was designed to simulate the tortoise vs hare race.

import random

time_t = 0
time_h = 0

# movement of tortoise
def move_T(current_pos):
    # random int from 1 to 10
    num = random.randint(1, 10)
    global time_t
    # fast plod - 50%
    if 1 <= num <= 5:
        newPos = current_pos + 3
        time_t += 1
    # slip - 20%
    elif 6 <= num <= 7:
        newPos = current_pos - 5
        time_t += 1
    # slow plod - 30%
    else:
        newPos = current_pos + 1
        time_t += 1

    # move to position 1 if slips at the start position
    if newPos < 1:
        return 1
    elif newPos > 50:
        return 50
    else:
        return newPos


#  movement of hare
def move_H(currentPos):

    num = random.randint(1, 10)
    global time_h
    # sleep -20%
    if num in (1, 2):
        newPos = currentPos
        time_h += 1
    # big hop - 20%
    elif num in (3, 4):
        newPos = currentPos + 7
        time_h += 1
    # big slip - 10%
    elif num == 5:
        newPos = currentPos - 10
        time_h += 1
    # small hop - 30%
    elif num in (6, 7, 8):
        newPos = currentPos + 1
        time_h += 1
    # small slip - 20%
    else:
        newPos = currentPos - 2
        time_h += 1

    if newPos < 1:
        return 1
    elif newPos > 50:
        return 50
    else:
        return newPos

#  progress
def progress(Tpos, Hpos):
    track = ""
    for i in range(1, 51):

        if i == Tpos and i == Hpos:
            track += "OW!!"
            break
        # show T at tortoise position
        elif i == Tpos:
            track += "T"
        # show H at hare position
        elif i == Hpos:
            track += "H"

        else:
            track += " "
    # print the track
    print(track)

# initialize
T_position = 1
H_position = 1

print("ON YOUR MARK... GET SET...")
print("GO!!!!!!")
print("AND THEY'RE OFF!\n")

# run loop until one of them reaches pos 50
while 50 not in (T_position, H_position):
    # get the new position of Tortoise and Hare
    T_position = move_T(T_position)
    H_position = move_H(H_position)

    #progress
    progress(T_position, H_position)

if T_position >= H_position:
    print("Tortoise wins!! Yay!")
else:
    print("Hare wins!! Yay!")

if time_h < time_t:
    print(f"Time of race:", time_h, "seconds.")
else:
    print(f"Time of race:", time_t, "seconds.")