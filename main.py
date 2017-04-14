import csv
import random
from collections import defaultdict



def load_data(filename):
    quotes = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter= ';')
        for line in reader:
            parsedQuote = line[0].split(' ')
            author = line[1]
            quotes.append([parsedQuote, author])

    return quotes

class Game:
    def __init__(self):

        self.player_1 = None
        self.player_1_score = 0
        self.player_2 = None
        self.player_2_score = 0

        self.current_player = None
    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def add_point(self):
        if self.current_player == self.player_1:
            self.player_1_score += 1
        else:
            self.player_2_score += 1



    def play_game(self, quotes):

        # get player information
        self.player_1 = raw_input("Enter player 1's name: ")

        self.player_2 = raw_input("Enter player 2's name: ")
        self.current_player = self.player_1



        # game loop
        while quotes:
            # get the quote
            quote_group = quotes.pop()
            quote = quote_group[0]
            author = quote_group[1]

            # choose a random index
            random_index = random.randint(0, (len(quote)-1))
            missing_word = quote[random_index]
            quote[random_index] = "_____"

            # guess the word
            print "it's your turn, {0}".format(self.current_player)
            print "This quote is by {0}: \n {1}".format(author, ' '.join(quote))
            guess = raw_input('Guess the missing word: ')
            if guess == missing_word:
                print "correct! You get a point! You guessed {0}, and the missing word was {1}".format(guess, missing_word)

                self.add_point()
            elif guess in missing_word:
                print "close, but you still get a point! You guessed {0}, and the missing word was {1}".format(guess, missing_word)
            else:
                print "Wrong guess The missing word was: {0}".format(missing_word)

            self.switch_player()

        print "All out of quotes!"
        print "The final score is: {0}:{1}, {2}:{3}".format(self.player_1, self.player_1_score, self.player_2, self.player_2_score)


def main():
    quotes = []
    quotes = load_data('test.csv')
    print "Welcome to Guess the word in the quote!"
    game = Game()
    game.play_game(quotes)



if __name__ == "__main__":
    main()
