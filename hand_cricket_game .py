import numpy as np

class Cricket:

    def __init__(self):
        pass

    def check_number(self,user_input):
        if user_input>=0 and user_input<=6:
            return user_input
        else:
            print("You can only enter 1 to 6")
            return self.player_turn()
        
    def player_turn(self):
        user_input = int(input("Enter your number (1,6) "))
        user_input = self.check_number(user_input)
        return user_input

    def computer_turn(self):
        return np.random.randint(1,7)

    def update_match(self,user_input,computer_input):
        if user_input%2 ==0 and computer_input%2==0 or user_input%2==1 and computer_input%2==1:
            self.out = True
        else:
            self.score += user_input

    def game_play(self):
        self.out = False
        self.score = 0
        while self.out == False:
            user_input = self.player_turn()
            print("Player Number:",user_input)
            computer_input = self.computer_turn()
            print("Computer Number:", computer_input)
            self.update_match(user_input,computer_input)
        return self.score
    
    def play(self):
        player_name=input("enter your name")
        print(f' {player_name} turn')
        player_score = self.game_play()
        print(f' {player_name} score is {player_score}')
        print(f'{player_name} is out with {player_score} Score')
        print('Now Computer')
        computer_score = self.game_play()
        print(f'Computer score is {computer_score}')
        print(f"Computer out with {computer_score} Score")
        if computer_score>player_score:
            print(f"Computer Wins with {computer_score} and the player only have {player_score}")
        elif player_score>computer_score:
            print(f"{player_name} wins with {player_score},and computer got {computer_score}")
        else: 
            return print("TIED")





game = Cricket()
game.play()
