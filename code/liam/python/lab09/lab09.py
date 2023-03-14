class Compass:
    def __init__(self, heading) -> None:
        self.heading = int(heading)

    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = int(45 * round(self.heading / 45 ))

        if direction == 360:
            direction = 0

        match direction:
            case 0:
                return 'N'
            case 45:
                return 'NE'
            case 90:
                return 'E'
            case 135:
                return 'SE'
            case 180:
                return 'S'
            case 225:
                return 'SW'
            case 270:
                return 'W'
            case 315:
                return 'NW'

    def turn(self, degrees, direction) -> None:
        self.degrees = int(degrees)

        if direction == 'R' or direction == 'Right':
            direction = 'to the right'
            self.__add__(degrees)
        if direction == 'L' or direction == 'Left':
            direction = 'to the left'
            self.__sub__(degrees)

        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        self.degrees = int(degrees)
        self.heading = int(heading)
        self.heading = int(self.heading) + self.degrees
        if self.heading >= 360:
            self.heading = (self.heading % 360)
        return self.heading

    def __sub__(self, degrees: int) -> int:
        self.degrees = int(degrees)
        self.heading = int(heading)
        self.heading = int(self.heading) - self.degrees
        if self.heading < 0:
            self.heading = 360 - abs(self.heading)
        return self.heading

    def __eq__(self, other) -> bool:
        if self.heading == other.heading:
            return True
        return 'The compasses are not the same.'

    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str: 
        return '''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠻⣿⣿⣿⣿⠟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠛⢿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⠿⠛⠉⢠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⠄⠁⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⡀⠀⠀⠀⢀⠄⢠⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠋⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⠋⠀⠀⢀⣴⠃⠀⠙⣿⣿⣿⣿⣿
⣿⡟⠻⠿⠃⠀⠀⢀⣾⣿⣿⣿⠿⠛⠁⠀⠀⠀⢀⣴⡿⠃⡀⠀⠀⠘⠿⠟⢻⣿
⣿⣿⣿⣦⠀⠀⠀⣾⣿⣿⣿⠃⣤⡀⠀⠀⢀⣴⣿⡿⢁⣼⣷⠀⠀⠀⣴⣿⣿⣿
⣿⣿⣿⣿⠀⠀⠀⣿⣿⡿⠁⣼⣿⣿⡦⢴⣿⣿⡟⢀⣾⣿⣿⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⠟⠀⠀⠀⢿⡿⢁⣾⣿⡿⠋⠀⠀⠙⠟⢠⣾⣿⣿⡿⠀⠀⠀⠻⣿⣿⣿
⣿⣧⣴⣶⡄⠀⠀⠈⢀⣾⡿⠋⠀⠀⠀⢀⣠⣴⣿⣿⣿⡿⠁⠀⠀⢠⣶⣦⣼⣿
⣿⣿⣿⣿⣿⡄⠀⢠⡿⠋⠀⠀⣀⣴⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⡠⠋⠀⠀⠀⠈⠙⠛⠛⠛⠛⠋⠉⠀⠀⠀⢀⠐⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⣀⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣷⣤⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣴⣿⣶⣶⣿⣦⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        '''


if __name__ == '__main__':
    #compass functionality tests
    heading = input('How many degrees reads on the heading? ')
    compass = Compass(heading) #init instance of a compass
    print(compass)
    direction = compass.get_direction()
    print(f'You are facing {direction}')

    while True:
        turn = input('How many degrees have you turned? ')
        turn_facing = input('To the right or left? ').title()
        valid_input = ['Left', 'L', 'Right', 'R',]
        if turn_facing not in valid_input:
            print('This is not a way you can turn.')
            continue
        compass.turn(turn, turn_facing)
        break

    second = Compass('270')
    print('The second compass is pointed at 270 degrees. Is this the same as the first currently:')
    print(compass.__eq__(second))