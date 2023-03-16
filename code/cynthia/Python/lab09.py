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
        if direction == 'left':
            subtracted_heading = heading - desired_degrees       
            if desired_degrees < 0:
                degrees = (round(subtracted_heading / 45) * 45) % 360 
                print(degrees)
            else:
                degrees = (round(subtracted_heading /45) * 45)
                print(degrees)
        elif direction == 'right':
            combined_heading = desired_degrees + heading
            if combined_heading > 335:
                degrees = (round(combined_heading /45) * 45) %360
            else:
                degrees = (round(combined_heading /45) * 45)
                print(degrees)

        print(f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        combined_heading = add_heading + heading
        if combined_heading > 335:
            degrees = (round(combined_heading /45) * 45) %360
        else:
            degrees = (round(combined_heading /45) * 45)
            print(degrees)
        return degrees

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another''' 
        subtracted_heading = heading - sub_heading           
        if subtracted_heading < 0:
            degrees = (round(subtracted_heading / 45) * 45) % 360 
            print(degrees)
        else:
            degrees = (round(subtracted_heading /45) * 45)
            print(degrees)
        return degrees 

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        if heading == other:
            print(True)
        else:
            print(False)


    def __gt__(self, other):

        raise TypeError('Cardinal directions cannot be greater or less than')
        

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        ...


if __name__ in '__main__':


        heading = int(input('heading: '))
        degrees = round(heading /45) * 45
        compass = Compass(heading)
        if heading > 335:
            degrees = round(heading / 45)* 45%45 
        degrees = compass.get_direction()
        print(degrees)

    #turn
        direction = input('which direstion do you want to turn? ').lower() #enter left or right 
        desired_degrees = int(input('how many degrees do you want to turn? '))
        compass.turn(direction, desired_degrees)
        print(degrees)





        # add_heading = int(input('Add heading: '))
        # compass.__add__(add_heading)
        # compass.get_direction(degrees)
        # print(degrees)

        # sub_heading = int(input('Subtract heading: '))
        # compass.__sub__(degrees)
        # print(degrees)

        # other = int(input("what is the other heading: "))
        # compass.__eq__(other)
        
