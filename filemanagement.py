import os

class Points():

    def __init__(self,game):
        self.game=game

    def read(self):
        while True:
            try:
                with open("record.txt") as file:
                    record=int(file.read())
                    break
            except FileNotFoundError:
                with open("record.txt","w") as file:
                    file.write("0")
        return record

    def write(self):
        with open("record.txt","w")as file:
            file.write(str(self.game.record))