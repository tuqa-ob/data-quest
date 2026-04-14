import math
print("=== Game Coordinate System ===\n")


def get_player_pos():
    while True:
        user_input = input(
                "Enter new coordinates as "
                "floats in format ’x,y,z’: ")
        parts = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(parts[0].strip())
        except Exception as e:
            print(f"Error on parameter '{parts[0]}': {e}")
            continue
        try:
            y = float(parts[1].strip())
        except Exception as e:
            print(f"Error on parameter '{parts[1]}': {e}")
            continue
        try:
            z = float(parts[2].strip())
        except Exception as e:
            print(f"Error on parameter '{parts[2]}': {e}")
            continue

        return (x, y, z)


print("Get a first set of coordinates")
pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

dist1 = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
print(f"Distance to center: {round(dist1, 4)}")

print("\nGet a second set of coordinates")
pos2 = get_player_pos()

dist2 = math.sqrt(
    (pos2[0] - pos1[0])**2 +
    (pos2[1] - pos1[1])**2 +
    (pos2[2] - pos1[2])**2
)

print(f"Distance between the 2 sets of coordinates: {round(dist2, 4)}")
