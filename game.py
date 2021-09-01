import random

SNAKES = {
        17:7,
        54:34,
        62:19,
        64:60,
        93:73,
        95:75,
        99:78,
        }

LADDERS = {
        4:14,
        9:31,
        20:38,
        28:84,
        40:59,
        51:67,
        63:81,
        71:91,
        }

def throw_dice(is_crooked):
    if is_crooked:
        return random.choice([2, 4, 6])
    else:
        return random.randint(1, 6)


if __name__ == "__main__":
    
    player_pos = 0

    is_crooked = random.randint(0, 1)
    print(f"Using a crooked dice {is_crooked}")

    print(f"Player is at {player_pos}")
    for x in range(1, 11):
        input(f"turn {x}")
        dice_value = throw_dice(is_crooked)
        print(f"Player dice has {dice_value}")

        player_pos += dice_value
        if player_pos > 100:
            printf(f"Player losses the turn, next move outside the board")
            player_pos -= dice_value
            continue

        if player_pos in SNAKES:
            print(f"Player found a snake at {player_pos}")
            player_pos = SNAKES[player_pos]

        elif player_pos in LADDERS:
            print(f"Player found a ladder at {player_pos}")
            player_pos = LADDERS[player_pos]

        print(f"Player is at {player_pos}")
        if player_pos == 100:
            print(f"Player wins!!!")
            break
