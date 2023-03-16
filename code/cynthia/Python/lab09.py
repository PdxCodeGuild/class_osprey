#lab09

class Compass:
    def __init__(self, heading) -> None:
        self.heading = heading
        self.degrees = degrees
        
    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = self.degrees

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
        
        if direction == 'left':
            self.heading = degrees - self.heading      
            if self.heading < 0:
                self.degrees = (round(self.heading / 45) * 45) % 360 
                self.degrees = self.get_direction()
                    #  print(subtracted_heading)
            else:
                self.degrees = (round(self.heading /45) * 45)
                self.degrees = self.get_direction()
                # print(f'line 43 {self.degrees}')
        elif direction == 'right':
            self.heading = degrees + self.heading

            if self.heading > 335:
                self.degrees = (round(self.heading /45) * 45) %360
                self.degrees = self.get_direction()
                print(f'line 50 {self.degrees}')
            else:
                self.degrees = (round(self.heading /45) * 45)
                self.degrees = self.get_direction()
                # print(f'line 53 {self.degrees}')


        print(f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')
        return self.heading, degrees, self.degrees

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        combined_heading = add_heading + self.heading
        if combined_heading > 335:
            self.degrees = (round(combined_heading /45) * 45) %360
        else:
            self.degrees = (round(combined_heading /45) * 45)
        self.degrees = self.get_direction()
        print(f'New heading {combined_heading}')
        return self.degrees

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another''' 
        subtracted_heading = add_heading - sub_heading           
        if subtracted_heading < 0:
            self.degrees = (round(subtracted_heading / 45) * 45) % 360 
        else:
            self.degrees = (round(subtracted_heading /45) * 45)

        self.degrees = self.get_direction()
        print(f'New heading {self.degrees}')
        return self.degrees 

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        if self.heading == other:
            print(True)
        else:
            print(False)


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
    degrees = round(heading /45) * 45
    compass = Compass(heading)
    if heading > 335:
        degrees = round(heading / 45)* 45%45 
    degrees = compass.get_direction()
    print(f'Your direction is {degrees}')

    #turn
    degrees = int(input('how many degrees do you want to turn? '))
    direction = input('which direction do you want to turn? ').lower() #enter left or right 
    compass.turn(degrees, direction)

    #add
    add_heading = int(input('Add to heading: '))
    print(f'New direction is {compass.__add__(add_heading)} ')

    #subtract
    sub_heading = int(input('Subtract from original heading: '))
    compass.__sub__(degrees)
    # print(degrees)

    #compare two headings
    other = int(input("what is the heading you want to compare: "))
    if other == heading:
        print(compass.__eq__(other))
    elif other < heading:
        print(compass.__lt__(other))
    elif other > heading:
        compass.__gt__(other)

