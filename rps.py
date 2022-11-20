#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        # initialization of player attributes
        self.my_move = moves
        # random choise from Random Player
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        # Plays move randomly
        return random.choice(moves)


class AllRockPlayer(Player):
    def move(self):
        # Plays only rock at every move
        return "rock"


class HumanPlayer(Player):
    def move(self):
        # iterate the input until user gives a choise that match the options
        # Either Payer, Rock or Scissors
        return Game.valid_input("Rock, paper, scissors? > ", moves)


class ReflectPlayer(Player):
    def move(self):
        # reflects the choice of the previous round
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        # plays a different move from what it played the last round
        if self.my_move == moves[2]:
            return moves[0]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[1]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # records player 1 Score
        self.score_p1 = 0
        # records player 2 score
        self.score_p2 = 0

    def valid_input(prompt, options):
        while True:
            option = input(prompt).lower()
            if option in options:
                return option
            elif option == 'exit':
                exit(0)
            else:
                print("Invalid input!!! Please type in a correct input!")

    def play_round(self):
        my_move = self.p1.move()
        their_move = self.p2.move()
        print(f"Player 1: {my_move}  Player 2: {their_move}")
        if self.beats(my_move, their_move):
            self.score_p1 += 1
            winner = '**** PLAYER ONE WINS THIS ROUND ****'
        elif my_move == their_move:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = '**** THIS ROUND IS A TIE ****'
        else:
            self.score_p2 += 1
            winner = '**** PLAYER TWO WINS THIS ROUND ****'
        # output the game result to console
        print(
            f"> You played : {my_move}"
            f"\n> Opponent played : {their_move}"
            f"\n{winner}"
        )
        self.p1.learn(my_move, their_move)
        self.p2.learn(my_move, their_move)

    def play_game(self):
        play_again = True
        while play_again is True:
            print("Game start!")
            for round in range(3):
                print(f"Round {round+1}:")
                self.play_round()
                print("#=====================#\n"
                      f"#= Current round: {round+1}  =#\n"
                      "#=====================#\n"
                      f"#= Player 1 score: {self.score_p1} =#\n"
                      f"#= Player 2 score: {self.score_p2} =#\n"
                      "#=====================#\n"
                      )
                if (round+1) == 3:
                    print("#=====================#\n"
                          f"#=   General Score:  =#\n"
                          "#=====================#\n"
                          f"#= Player 1 score: {self.score_p1} =#\n"
                          f"#= Player 2 score: {self.score_p2} =#\n"
                          "#=====================#\n"
                          )
                    if self.score_p1 > self.score_p2:
                        print("Player 1 won!")
                    elif self.score_p1 < self.score_p2:
                        print("Player 2 won!")
                    else:
                        print("The game ended in a draw!")

            print("The Game is over!")
            play_again_input = input("Do you want to play again? (Y/N) > ")
            if play_again_input.lower() == "y":
                play_again = True
                self.score_p1 = 0
                self.score_p2 = 0
            else:
                play_again = False

    @staticmethod
    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), CyclePlayer(), ReflectPlayer(), AllRockPlayer()]
        ))
    game.play_game()
