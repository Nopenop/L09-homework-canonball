from math import sin, cos
import random
from matplotlib import pyplot as plt

##Represents the printing interface to be used within the cannball class

class Print_interface:
    """Creates an interface component to be used within the cannonball class.

    Uses the matplotlib and math libraries to plot the location of the ball
    """
    def plot_shot(x, y, rand = -1):
        """Prints the cordinates and plots the location of the cannonball

        Args:
            x (float)): Input self.getX()
            y (float): Input self.getY()
        """
        print("The ball is at (%.1f, %.1f)"% (x, y))
        plt.scatter(x,y)
        plt.pause(.01)
        #checks to see if a random number was also included in the shoot method
        if rand != -1:
            print(f"Random number is {rand}")
    pass

## Represent a cannonball, tracking its position and velocity.
#
class Cannonball:
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0

    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y

    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)
        while self.getY() > 1e-14:
            Print_interface.plot_shot(self.getX(),self.getY())
            self.move(0.1, user_grav)


##Represents a crazyball whose position is randomized in the plotting of the ball
class Crazyball(Cannonball):
    """Child class of cannonball, whose position

    Args:
        Cannonball (_type_): _description_
    """
    def __init__(self, x):
        """Creates a crazy ball object with an additional rand_q object

        Args:
            x (int): Location of the ball, where it starts
        """
        self.rand_q = 0
        super().__init__(x)
    def move(self, sec, grav=9.81):
        """Moves the ball in the x and y directions

        Args:
            sec (float): Time intervals to count
            grav (float, optional): The gravity of the object. Defaults to 9.81.
        """
        self.rand_q = random.randrange(0,10)
        #If the ball is less that 400 meters in the x direction, the ball is crazy
        if self.getX() < 15:
            dx = (self._vx) * sec
            dy = (self._vy) * sec
            #rand_q acts as the gravity 
            self._vy = self._vy - self.rand_q * sec

            self._x = self._x + dx
            self._y = self._y + dy
        #Otherwise, the ball acts normally
        else:
            super().move(sec, grav)

    def shoot(self, angle, velocity, user_grav):
        """Shoots the crazy ball. Only difference is to print out the random number

        Args:
            angle (Float): Angle to launch the ball at
            velocity (Float): Speed to launch the ball at
            user_grav (Float): Gravity the ball is under
        """
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)
        while self.getY() > 1e-14:
            #Onlly difference between parent class shoot() and child class.
            Print_interface.plot_shot(self.getX(),self.getY(),self.rand_q)
            self.move(0.1, user_grav)



def menu():
    """menu to be used for the main function

    Returns:
        the integer of to be input(1 earth gravity, 2 moon gravity, crazy, quit).
    """
    text = "Gravity: (1)Earth Gravity, (2)Moon gravity, (3)Crazy Trajectory, (4)Quit"
    usinput = int(input(text))
    return usinput
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Demonstrate the cannonball class.
    
    from cannonball import Cannonball
    """

    print("Welcome to the cannonball tester!")
    menu_list = 0
    while menu_list != 4:
        angle = float(input("Enter starting angle:"))
        v = float(input("Enter initial velocity:"))
        menu_list = menu()
        if menu_list == 1:
            c = Cannonball(0)
            c.shoot(angle, v, 9.81)
        elif menu_list == 2:
            c = Cannonball(0)
            c.shoot(angle, v, 1.62)
        elif menu_list == 3:
            c = Crazyball(0)
            c.shoot(angle, v, 9.81)
        elif menu_list!=4:
            print("Unrecognized input. Please try again.")
    print("Thank you for testing.")

    # angle = float(input("Enter starting angle:"))
    # v = float(input("Enter initial velocity:"))
    # c = Cannonball(0)
    # c.shoot(angle, v, 9.81)



