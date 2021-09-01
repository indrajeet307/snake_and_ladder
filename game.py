import random


class SnakeNotFoundError(KeyError):
    pass


class LadderNotFoundError(KeyError):
    pass


class Board:
    def __init__(self):
        self.snakes = {
            17: 7,
            54: 34,
            62: 19,
            64: 60,
            93: 73,
            95: 75,
            99: 78,
        }

        self.ladders = {
            4: 14,
            9: 31,
            20: 38,
            28: 84,
            40: 59,
            51: 67,
            63: 81,
            71: 91,
        }

    def has_snake(self, pos):
        return pos in self.snakes

    def has_ladder(self, pos):
        return pos in self.ladders

    def get_snake_tail(self, pos):
        if self.has_snake(pos):
            return self.snakes[pos]
        else:
            raise SnakeNotFoundError(f"Snake not found at pos, {pos}")

    def get_ladder_end(self, pos):
        if self.has_ladder(pos):
            return self.ladders[pos]
        else:
            raise LadderNotFoundError(f"Ladder not found at pos, {pos}")


class Player:
    def __init__(self, name):
        self.name = name
        self.pos = 0

    @property
    def position(self):
        return self.pos

    @position.setter
    def position(self, pos):
        self.pos = pos

    def __str__(self):
        return self.name

    def show_position(self):
        return f"{self.name} is at position, {self.position}."


class Dice:
    def __init__(self, is_crooked=False):
        self.crooked = is_crooked

    def __str__(self):
        return f"This is {'' if self.crooked else 'not '}a crooked dice"

    def throw(self):
        if self.crooked:
            return random.choice([2, 4, 6])
        else:
            return random.choice([1, 2, 3, 4, 5, 6])


if __name__ == "__main__":

    board = Board()
    players = [Player("Bob"), Player("Alice")]
    is_crooked = random.choice([True, False])
    dice = Dice(is_crooked)
    game_winner = None

    print("Starting game with:")
    for player in players:
        print(player.show_position())
    print(dice)

    input("Press enter to start the game and CTRL-C to exit...")

    for turn in range(1, 11):

        for player in players:

            dice_value = dice.throw()
            print(f"{player} dice has {dice_value}.")

            player.position += dice_value

            if player.position == 100:
                game_winner = player
                break
            if player.position >= 100:
                print(f"{player} losses run, next move beyond board")
                player.position -= dice_value
                continue

            if board.has_snake(player.position):
                print(f"{player} found a snake at {player.position}.")
                player.position = board.get_snake_tail(player.position)
            elif board.has_ladder(player.position):
                print(f"{player} found a ladder at {player.position}.")
                player.position = board.get_ladder_end(player.position)

        print(f"After turn {turn}, player positions are:")
        for player in players:
            print(player.show_position())

        if game_winner:
            print(f"Player {game_winner} wins, Game-Over")
            break

        input(f"Press enter to play next turn.")
