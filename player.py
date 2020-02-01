class typePlayer:
    IA_PLAYER = 1
    GRAPHIC_PLAYER = 2
    IA_PLAYER_2 = 3
    NUMER_PLAYERS = 3

typePlayer.IA_PLAYER

class players:

    type_player = {}

    def insertPlayer_1(self,type_player,name):
        self.type_player[True] = type_player
        self.PLAYER1 = name
        assert 0 < type_player <= typePlayer.NUMER_PLAYERS, "Error, player unknow."

    def insertPlayer_2(self,type_player,name):
        self.type_player[False] = type_player
        self.PLAYER2 = name
        assert 0 < type_player <= typePlayer.NUMER_PLAYERS, "Error, player unknow."

    def reset(self):
        self.turn = True
        self.ROUND = 0

    def playerTurn(self):
        return self.type_player[self.turn]

    def newTurn(self):
        self.turn = not self.turn
        self.ROUND += self.ROUND

    def __init__(self):
        self.reset()
