#lab09

class Compass:
    def __init__(self, heading) -> None:
        self.heading = heading
        
    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = degrees

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
        return direction

    def turn(self, degrees, direction) -> None:
        ...

        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        degrees = ((new_heading + self.heading)/45)*45
        if degrees >= 359:
            degrees = round(heading / 45)* 45%45 
        return degrees

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another''' #keeps mimicking the first headings degree output
        degrees = ((new_heading - self.heading)/45)*45
        if degrees <= 0:
            degrees = ((new_heading - self.heading)/45)* 45% 45
        return degrees 

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        if self.heading == other:
            print(f'{self.heading} is the same as {other}') #needs to be refined 
        


    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        ...


if __name__ in '__main__':

    heading = int(input('heading: '))
    degrees = round(heading / 45)* 45
    compass = Compass(heading)
    if heading >= 359:
        degrees = round(heading / 45)* 45%45  #trying to make the compass cyclical
    degrees = compass.get_direction()
    print(degrees)


    new_heading = int(input('New heading: '))
    compass.__add__(degrees)
    print(degrees)

    other = int(input("what is the other heading: "))
    compass.__eq__(other)
