class Compass:
    def __init__(self, heading) -> None:
        if 0 <= heading <= 359:
            self.heading = heading
        else:
            raise TypeError('A compass must have a heading between 0 and 359')

    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = round(self.heading / 45) * 45

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
            case 360:
                return 'N'

    def turn(self, degrees, direction) -> None:
        if direction == 'right':
            self.heading = self.__add__(degrees)
        elif direction == 'left':
            self.heading = self.__sub__(degrees)

        if self.heading < 0:
            self.heading += 360
        elif self.heading > 359:
            self.heading -= 360

        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        return (self.heading + degrees) % 360

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another'''
        return (self.heading - degrees) % 360

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        return self.heading == other.heading

    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        ...
