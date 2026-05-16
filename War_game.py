import random

deck = list(range(2,15))*4
random.shuffle(deck)

class War:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    @classmethod
    def create_player_cards(cls):
        return cls(deck[:26],deck[26:])
        
    @staticmethod
    def check_card(card1, card2):
        if card1 > card2:
            return 'player1'
           
        elif card1 < card2:
            return 'player2'
            
        else:
            return 'war'
            
    def play(self):
        round_number = 0
        while self.player1 and self.player2:
            round_number += 1
            print(f'========== round {round_number} ==========')
            card1 = self.player1.pop(0)
            card2 = self.player2.pop(0)
            
            table = [card1,card2]
            
            result = self.check_card(card1,card2)
            
            while result == 'war':
                print('War!')
                
                if len(self.player1) < 4:
                    print('player2 wins as player1 cant continue')
                    return 
                
                if len(self.player2) < 4:
                    print('player1 wins as player 2 cant continue')
                    return
                
                for _ in range(3):
                    table.append(self.player1.pop(0))
                    table.append(self.player2.pop(0))
                
                card1 = self.player1.pop(0)
                card2 = self.player2.pop(0)
            
                table.extend([card1,card2])
            
                print(f'player1 war card: {card1}')
                print(f'player2 war card: {card2}')
            
                result = self.check_card(card1,card2)
            
            if result == 'player1':
                print(f'player1 card: {card1}')
                print(f'player2 card: {card2}')
                print('\nplayer1 won this round')
                
                self.player1.extend(table)
                
                print(f'\nplayer1 card left: {len(self.player1)}')
                print(f'player2 card left: {len(self.player2)}')
                
            else:
                print(f'player1 card: {card1}')
                print(f'player2 card: {card2}')
                print('\nplayer2 won this round')
                
                self.player2.extend(table)
                
                print(f'\nplayer1 card left: {len(self.player1)}')
                print(f'player2 card left: {len(self.player2)}')
                
        if self.player1:
            print('player1 won the game')
            
        else:
            print('player2 won the game')
                
                
if __name__ == "__main__":
    war = War.create_player_cards()
    war.play()
            
            
                    
        
        
