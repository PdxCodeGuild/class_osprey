#lab09

class Compass:
    def __init__(self, heading) -> None:
        self.heading = heading
        
    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''

        direction = int(round(self.heading /45) * 45)

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
        
        if direction == 'left':
            self.__sub__(degrees)

        elif direction == 'right':
            self.__add__(degrees)
           
        print(f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        self.heading= degrees + self.heading
        if self.heading> 336:
            self.heading = (round(self.heading/45) * 45) %336
        else:
            self.heading = (round(self.heading/45) * 45)
        return self.heading

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another''' 
        self.heading = degrees - self.heading           
        if self.heading < 0:
            self.heading = (round(self.heading / 45) * 45) % 336 
        else:
            self.heading = (round(self.heading /45) * 45)
        return self.heading

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        if self.heading == other:
            print(True)

    def __gt__(self, other):
        if other > self.heading:
            raise TypeError('Cardinal directions cannot be greater or less than')
    
    def __lt__(self, other):
        if other < self.heading:
            raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        return self.heading 


if __name__ == '__main__':

    heading = int(input('Enter a heading: '))
    compass = Compass(heading)
    degrees = compass.get_direction()
    print(f'Your direction is {degrees}')

    #turn
    degrees = int(input('how many degrees do you want to turn? '))
    direction = input('which direction do you want to turn? ').lower() #enter left or right 
    compass.turn(degrees, direction)

    #compare two headings
    other = int(input("what is the heading you want to compare: "))
    if other == heading:
        print(compass.__eq__(other))
    elif other < heading:
        print(compass.__lt__(other))
    elif other > heading:
        print(compass.__gt__(other))

