import random

class rock_paper_scissors:
    player_one_move = 0
    player_two_move = 0
    dictionary_of_moves = { 0: 'ROCK', 1: 'PAPER', 2: 'SCISSORS' }
    dictionary_of_messages = { 
        'player_one_victory': 'You win! This time...',
        'player_two_victory': 'You lose',
        'draw': 'its a draw. Go again!'
    }

    def __init__(self, player_one_move):
        self.player_one_move = self.dictionary_of_moves[int(player_one_move)]

    def choose_player_two_move(self):
        self.player_two_move = random.choice(self.dictionary_of_moves)
    
    def check_and_return_winner(self):
        if (self.player_one_move == self.dictionary_of_moves[0] and self.player_two_move == self.dictionary_of_moves[1]):
            return self.dictionary_of_messages['player_two_victory']
        elif(self.player_one_move == self.dictionary_of_moves[2] and self.player_two_move == self.dictionary_of_moves[0]):
            return self.dictionary_of_messages['player_one_victory']
        elif(self.player_one_move == self.dictionary_of_moves[0] and self.player_two_move == self.dictionary_of_moves[2]):
            return self.dictionary_of_messages['player_two_victory']
        elif(self.player_one_move == self.dictionary_of_moves[1] and self.player_two_move == self.dictionary_of_moves[2]):
            return self.dictionary_of_messages['player_two_victory']
        elif(self.player_one_move == self.dictionary_of_moves[2] and self.player_two_move == self.dictionary_of_moves[1]):
            return self.dictionary_of_messages['player_one_victory']
        elif(self.player_one_move == self.dictionary_of_moves[1] and self.player_two_move == self.dictionary_of_moves[0]):
            return self.dictionary_of_messages['player_one_victory']
        elif(self.player_one_move == self.player_two_move):
            return self.dictionary_of_messages['draw']
        else:
            return self.dictionary_of_messages['error']