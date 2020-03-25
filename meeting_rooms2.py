# file: meeting_rooms.py
# author: Cedric Wille cwille97@bu.edu
# description: Leet Code problem 253 Meeting rooms 2
# date: 3/25/20

def solution(input):
    '''Solution to the meeting rooms 2 problem'''

    rooms = [] # a container list of meeting rooms
    room1 = [] # create first room and append to room container
    rooms.append(room1)
    # print(rooms) 

    for item in input:
        if not check_if_new_room_needed(item, rooms): # if this is false we need a new room
            new_room = [item] # new room with just the one meeting in it
            rooms.append(new_room)
        # else a new room wasn't needed and everything has been taken care of
    
    return len(rooms)


def check_if_new_room_needed(item, rooms): 
    '''Checks if we can use an existing room or if we must create a new room'''
    for room in rooms:
        if meeting_valid_in_room(item, room): # if the meeting is valid
            room.append(item) # meeting is valid here so let's add it to this room
            return True # return so we don't bother checking other rooms
    return False # all rooms checked and nothing is compatible, we need a new room
 
def meeting_valid_in_room(item, room): 
    '''check if this new meeting, named item, is valid in this room'''
    for meeting in room:
        if item[0] > meeting[0] and item[0] < meeting[1]: # conflict
            return False
        elif item[1] > meeting[0] and item[1] < meeting[1]: # conflict
            return False


    return True # we only do this if we've checked each meeting in this room and they're all compatible

    



# tests for our function
test_input = [[0, 30], [5, 10], [15, 20]]
print("solution(test_input): " + str(solution(test_input))) # unable to veryify solution because it was locked behind a paywall :(