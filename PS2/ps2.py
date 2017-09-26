# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:42:07 2017

@author: Shruthi
"""

# Enter your code for RectangularRoom in this box
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        #self.tiles_x = {}
        #self.tiles_y = {}
        self.tiles = {}
        #for i in range(self.width):
         #   self.tiles_x[i] = 0
        #for j in range(self.height):
         #   self.tiles_y[j] = 0
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[i*10 + j] = 0
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #self.tiles_x[int(pos.getX())] = 1
        #self.tiles_y[int(pos.getY())] = 1
        self.tiles[(int(pos.getX()))*10 + int(pos.getY())] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #if (self.tiles_x[m] and self.tiles_y[n]):
        if (self.tiles[m*10 + n]):
            return True
        else:
            return False
                
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return (self.width*self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                #if (self.tiles_x[i] and self.tiles_y[j]):
                if (self.tiles[i*10 + j]):
                    count += 1
        return (count)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x_range = []
        y_range = []
        for i in range(self.width):
            x_range.append(i)
        for y in range(self.height):
            y_range.append(y)
        x_r = random.choice(x_range)
        y_r = random.choice(y_range)
        p = Position(x_r,y_r)
        return (p)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if ((pos.getX() < self.width and pos.getX() >= 0.00) and (pos.getY() < self.height and pos.getY() >= 0.00)):
            return True
        else:
            return False


# Enter your code for RectangularRoom (from the previous problem)
#  and Robot in this box
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        #self.tiles_x = {}
        #self.tiles_y = {}
        self.tiles = {}
        #for i in range(self.width):
         #   self.tiles_x[i] = 0
        #for j in range(self.height):
         #   self.tiles_y[j] = 0
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[i*10 + j] = 0
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #self.tiles_x[int(pos.getX())] = 1
        #self.tiles_y[int(pos.getY())] = 1
        self.tiles[(int(pos.getX()))*10 + int(pos.getY())] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #if (self.tiles_x[m] and self.tiles_y[n]):
        if (self.tiles[m*10 + n]):
            return True
        else:
            return False
                
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return (self.width*self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                #if (self.tiles_x[i] and self.tiles_y[j]):
                if (self.tiles[i*10 + j]):
                    count += 1
        return (count)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x_range = []
        y_range = []
        for i in range(self.width):
            x_range.append(i)
        for y in range(self.height):
            y_range.append(y)
        x_r = random.choice(x_range)
        y_r = random.choice(y_range)
        p = Position(x_r,y_r)
        return (p)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if ((pos.getX() < self.width and pos.getX() >= 0.00) and (pos.getY() < self.height and pos.getY() >= 0.00)):
            return True
        else:
            return False


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        self.pos = self.room.getRandomPosition()
        m_direc = []
        for i in range(360):
            m_direc.append(i)
        self.direction = random.choice(m_direc)
        

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
        
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
        
# Enter your code for Robot (from the previous problem)
#  and StandardRobot in this box
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        self.pos = self.room.getRandomPosition()
        m_direc = []
        for i in range(360):
            m_direc.append(i)
        self.direction = random.choice(m_direc)
        self.room.cleanTileAtPosition(self.pos)
        

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
        
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_pos = self.pos.getNewPosition( self.direction, self.speed)
        while(not self.room.isPositionInRoom(new_pos)):
            m_direc = []
            for i in range(360):
                m_direc.append(i)
            self.direction = random.choice(m_direc)
            new_pos = self.pos.getNewPosition(self.direction, self.speed)
        self.pos = new_pos
        self.room.cleanTileAtPosition(new_pos)
        
# Enter your code for Robot and RandomWalkRobot in this box
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        self.pos = self.room.getRandomPosition()
        m_direc = []
        for i in range(360):
            m_direc.append(i)
        self.direction = random.choice(m_direc)
        self.room.cleanTileAtPosition(self.pos)
        

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
        
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        m_direc = []
        for i in range(360):
            m_direc.append(i)
        self.direction = random.choice(m_direc)
        new_pos = self.pos.getNewPosition( self.direction, self.speed)
        while(not self.room.isPositionInRoom(new_pos)):
            self.direction = random.choice(m_direc)
            new_pos = self.pos.getNewPosition(self.direction, self.speed)
        self.pos = new_pos
        self.room.cleanTileAtPosition(new_pos)  