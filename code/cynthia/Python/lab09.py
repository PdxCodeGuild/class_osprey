#lab09

class Compass:
    def __init__(self, heading) -> None:
        self.heading = heading
        

    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = round(self.heading/360)*45

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
        ...
        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        ...

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another'''
        ...

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        ...

    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        ...