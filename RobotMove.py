import DirectionEnum
import MovesEnum
Direction = DirectionEnum.Direction
Moves = MovesEnum.Moves

#Global Variable
X = 0
Y = 0
Face = Direction.NORTH.name

#Validate current position
def CheckValidMove(cordinate):
    if cordinate > 5  or cordinate < 0:
        print("I'm falling from table please save")
        return False;
    return True;

#Set current Position
def setPosition(input):
    if len(input.split(",")) == 3:
        inputArray = input.split(",")
        x_pos = int(inputArray[0])
        y_pos = int(inputArray[1])
        if CheckValidMove(x_pos) and CheckValidMove(y_pos):
            global X
            global Y
            global Face
            X = x_pos
            Y = y_pos
            Face = inputArray[2]

#Show current position
def showCurrentPosition():
    print("Output: {X}, {Y}, {Face}".format(X=X,Y=Y,Face=Face))

#Function defines next move based on position
def nextMove(leftMove,rightMove,move):
    global Face
    global X
    global Y
    if Face == Direction.NORTH.name:
        if leftMove:
            Face = Direction.WEST.name
        if rightMove:
            Face = Direction.EAST.name
        if move:
            if CheckValidMove(Y + 1):
                Y = Y + 1
    elif Face == Direction.SOUTH.name:
        if leftMove:
            Face = Direction.EAST.name
        if rightMove:
            Face = Direction.WEST.name
        if move:
            if CheckValidMove(Y - 1):
                Y = Y - 1
    elif Face == Direction.EAST.name:
        if leftMove:
            Face = Direction.NORTH.name
        if rightMove:
            Face = Direction.SOUTH.name
        if move:
            if CheckValidMove(X + 1):
                X = X + 1
    elif Face == Direction.WEST.name:
        if leftMove:
            Face = Direction.SOUTH.name
        if rightMove:
            Face = Direction.NORTH.name
        if move:
            if CheckValidMove(X - 1):
                X = X - 1
#Main function
def main():
    isValidInput = False    #True when PLACE command is initialized
    while 1:
        initialInput = input()
        if "PLACE" in initialInput:     #PLACE command is executed
            isValidInput = True
            setPosition(initialInput.split(" ")[1])
        elif "report" in initialInput.lower() and isValidInput: #REPORT command is executed
            showCurrentPosition()
        elif initialInput.lower() == Moves.MOVE.name.lower() and isValidInput: #MOVE command is executed
            nextMove(False, False, True)
        elif "left" in initialInput.lower():    #LEFT command is executed
            nextMove(True, False, False)
        elif "right" in initialInput.lower():   #RIGHT command is executed
            nextMove(False,True,False)
        elif isValidInput == False:
            print("Place Toy Robot in table top")
        else:
            print("Not a valid command")

if __name__ == '__main__':
    main()
