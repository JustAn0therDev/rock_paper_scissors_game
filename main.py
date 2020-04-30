import rock_paper_scissors_game

def main():
  try:
    print("Rock, paper, scissors!")
    player_one_move = input("Choose your move: (ROCK = 0 | PAPER = 1 | SCISSORS = 2) ")
    rock_paper_scissors_instance = rock_paper_scissors_game.rock_paper_scissors(player_one_move)
    rock_paper_scissors_instance.choose_player_two_move()
    match_result = rock_paper_scissors_instance.check_and_return_winner()
    print(match_result)
  except Exception:
    print('Choose a valid move!')
  except KeyboardInterrupt:
    print('\nbye!')
    exit()
    pass

while (True):
  main()