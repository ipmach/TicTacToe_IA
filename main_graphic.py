import sys
from graphicInterface import gameInterface

def main():
    try:
        size = int(sys.argv[1])
        train_steps = int(sys.argv[2])
        height = int(sys.argv[3])
        width = int(sys.argv[4])
    except:
        raise RuntimeError("Error: must be 'python main size train_steps height width' with ints ")
    print("Welcome, choose game type:")
    print("1) Player vs Player")
    print("2) Player vs IA")
    print("3) IA vs Player")
    while(True): #Initial menu
        try:
            choose = input("Select number: ")
            assert choose in ["1","2","3"], "Must be one of the options"
            break
        except:
            print("You must choose one of the options")
    gameInterface(height,width,size,train_steps,int(choose)-1)

if __name__ == "__main__":
    main()