def badge_maker(name):
    message = (f"Hello, my name is {name}.")
    return message

def batch_badge_creator(names):
    badges = []
    for name in names:
        message = f"Hello, my name is {name}."
        badges.append(message)
    return badges

batch_badge_creator(["Arel", "Carol"])

def assign_rooms(names):
    rooms = range(1, 9)
    room_assignments = []

    for i, speaker in enumerate(names):
        room_number = rooms[i]
        assignment = f"Hello, {speaker}! You'll be assigned to room {room_number}!"
        room_assignments.append(assignment)

    return room_assignments

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for message in badge_messages:
        print(message)

    for assignment in room_assignments:
        print(assignment)