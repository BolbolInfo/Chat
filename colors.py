from random import randint


class style:
    def AutoReset(inp:bool):
        Autoreset=True

    Autoreset=False
    NORMAL="\033[0m"
    BRIGHT="\033[1m"
    DIM="\033[2m"
    ITALIC="\033[3m"
    UNDERLINED="\033[4m"
    BLINCKING="\033[5m"
    INVERTED="\033[7m"
    HIDDEN="\033[8m"
    RESET="\033[0m"

class text :
    RED="\033[38;2;255;0;0m"
    GREEN="\033[38;2;0;255;0m"
    BLUE="\033[38;2;0;0;255m"
    YELLOW="\033[38;2;255;255;0m"
    PURPLE="\033[38;2;128;0;128m"
    ORANGE="\033[38;2;255;165;m"
    PINK="\033[38;2;255;192;203m"
    BROWN="\033[38;2;139;69;19m"
    BLACK="\033[38;2;0;0;0m"
    WHITE="\033[38;2;255;255;255m"
    def custom(r:int,g:int,b:int):
        col="\033[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"
        return col
    def random():
        col="\033[38;2;"+str(randint(10,255))+";"+str(randint(10,255))+";"+str(randint(10,255))+"m"
        return col
class back:
    pass

