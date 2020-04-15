import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        answer = input("""Choose your move - Rock, Paper or """
                       """Scissors? To exit press x\n""")
        answer = answer.lower()
        while answer not in moves and answer != 'x':
            answer = input("Enter a valid move!")
        if answer == 'x':
            exit()
        return answer

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return (random.choice(moves))
        else:
            return self.their_move


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def move(self):
        move = None
        if self.last_move is None:
            move = Player.move(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move

    def learn(self, my_move, their_move):
        pass


class Game:

    def __init__(self, RandomPlayer, HumanPlayer):
        self.RandomPlayer = RandomPlayer
        self.HumanPlayer = HumanPlayer
        self.count_wins = 0
        self.count_losses = 0
        self.count_ties = 0

    def play_round(self):
        move1 = self.RandomPlayer.move()
        move2 = self.HumanPlayer.move()
        print(f"Player 1 Move: {move1}  Player 2 Move: {move2}")

        if beats(move1, move2):
            self.count_wins += 1
            print(f"wins:{self.count_wins}")
        elif move1 == move2:
            self.count_ties += 1
            print(f"ties:{self.count_ties}")
        elif beats(move2, move1):
            self.count_losses += 1
            print(f"losses:{self.count_losses}")
        else:
            print("tada mistake")

        self.score1 = self.count_wins
        self.score2 = self.count_wins
        print(f"""Player One Score: {self.count_wins} """
              f"""Player Two Score: {self.count_losses}\n""")

        self.RandomPlayer.learn(move1, move2)
        self.HumanPlayer.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for i in range(10):
            currentRound = i  # this sets the currentRound pointer to the
            # current i or index
            print(f"Round {currentRound}:")
            self.play_round()
        print("\nThanks for playing")
        print(f"""Final Tallies\nPlayer One Points: {self.count_wins} """
              f""" Player Two Points: {self.count_losses}""")
        if self.count_wins > self.count_losses:
            print("Player One is Victorious\n")
        elif self.count_wins < self.count_losses:
            print("Player Two is Victorious\n")
        else:
            print("Nobody is the Victor - Tie Game\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()