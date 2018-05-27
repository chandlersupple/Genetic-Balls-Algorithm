import pygame
import random
from pygame.locals import *

master = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (86, 66, 244)

camera_plus = 0
camera_move = 0
border_list_left = [(0, 0 + camera_move), (350, 550 + camera_move)]
border_list_right = [(1000, 0 + camera_move), (650, 550 + camera_move)]
previous_y = 550
previous_x = 400
all_points_left = []
all_points_right = []
scores = []
terminated = 0
population = 200
border_once = 0
add_left = 300
speed_mate = []
turn_range_mate = []
size_mate = []
cars_dict = {}
size_max = 25
size_min = 3
speed_max = 60
speed_min = 1
turn_range_max = 250
turn_range_min = 1
vieux = 0

class Car:
    def __init__(self):
        self.x = 500
        self.y = 200
        self.size = random.randint(size_min, size_max)
        self.speed = random.randint(speed_min, speed_max)
        self.turn_range = random.randint(turn_range_min, turn_range_max)
        self.terminate = 0
        self.once = 0
        self.body = pygame.draw.circle(master, blue, (self.x, self.y), self.size, 0)
        self.score = 0
        
    def move(self):
        global all_points_left, all_points_right, scores, terminated, size_mate, speed_mate, turn_range_mate
                                
        for point in range (0, len(all_points_left)):
            if (abs(self.y - int(round(all_points_left[point][1], 0))) <= self.size):
                if (self.x - self.size <= int(round(all_points_left[point][0], 0))):
                    self.terminate = 1
            if (abs((self.y + self.size)- int(round(all_points_left[point][1], 0))) <= self.size):
                if (self.x <= int(round(all_points_left[point][0], 0))):
                    self.terminate = 1
        for point in range (0, len(all_points_right)):
            if (abs(self.y - int(round(all_points_right[point][1], 0))) <= self.size):
                if (self.x + self.size >= int(round(all_points_right[point][0], 0))):
                    self.terminate = 1
            if (abs((self.y + self.size) - int(round(all_points_right[point][1], 0))) <= self.size):
                if (self.x >= int(round(all_points_right[point][0], 0))):
                    self.terminate = 1
                    
        for point in range (0, len(all_points_left)):
            if (self.y == int(round(all_points_left[point][1], 0))):
                if (abs((self.x - self.size) - all_points_left[point][0]) <= self.turn_range):
                    self.x = self.x + self.speed
        for point in range (0, len(all_points_right)):
            if (self.y == int(round(all_points_right[point][1], 0))):
                if (abs((self.x + self.size) - all_points_right[point][0]) <= self.turn_range):
                    self.x = self.x - self.speed
                    
        if (self.terminate == 0):
            self.body = pygame.draw.circle(master, blue, (self.x, self.y), self.size, 0)
            self.score = self.score + 1
        if (self.terminate == 1 and self.once == 0):
            scores.append(self.score)
            terminated = terminated + 1
            self.once = 1
            if (population - terminated <= 20):
                size_mate.append(self.size)
                speed_mate.append(self.speed)
                turn_range_mate.append(self.turn_range)
                    
class Car_Babies:
    def __init__(self, size, speed, turn_range):
        self.x = 500
        self.y = 200
        self.size = size
        self.speed = speed
        self.turn_range = turn_range
        self.terminate = 0
        self.once = 0
        self.body = pygame.draw.circle(master, blue, (self.x, self.y), self.size, 0)
        self.score = 0
        
    def move(self):
        global all_points_left, all_points_right, scores, terminated, size_mate, speed_mate, turn_range_mate
                                
        for point in range (0, len(all_points_left)):
            if (abs(self.y - int(round(all_points_left[point][1], 0))) <= self.size):
                if (self.x - self.size <= int(round(all_points_left[point][0], 0))):
                    self.terminate = 1
            if (abs((self.y + self.size)- int(round(all_points_left[point][1], 0))) <= self.size):
                if (self.x <= int(round(all_points_left[point][0], 0))):
                    self.terminate = 1
        for point in range (0, len(all_points_right)):
            if (abs(self.y - int(round(all_points_right[point][1], 0))) <= self.size):
                if (self.x + self.size >= int(round(all_points_right[point][0], 0))):
                    self.terminate = 1
            if (abs((self.y + self.size) - int(round(all_points_right[point][1], 0))) <= self.size):
                if (self.x >= int(round(all_points_right[point][0], 0))):
                    self.terminate = 1
                    
        for point in range (0, len(all_points_left)):
            if (self.y == int(round(all_points_left[point][1], 0))):
                if (abs((self.x - self.size) - all_points_left[point][0]) <= self.turn_range):
                    self.x = self.x + self.speed
        for point in range (0, len(all_points_right)):
            if (self.y == int(round(all_points_right[point][1], 0))):
                if (abs((self.x + self.size) - all_points_right[point][0]) <= self.turn_range):
                    self.x = self.x - self.speed
                    
        if (self.terminate == 0):
            self.body = pygame.draw.circle(master, blue, (self.x, self.y), self.size, 0)
            self.score = self.score + 1
        if (self.terminate == 1 and self.once == 0):
            scores.append(self.score)
            terminated = terminated + 1
            self.once = 1
            if (population - terminated <= 50):
                size_mate.append(self.size)
                speed_mate.append(self.speed)
                turn_range_mate.append(self.turn_range)
                    
def build_map():
    global border_list_left, border_list_right, previous_y, previous_x, camera_move, all_points_left, all_points_right, border_once, add_left
    
    move_y = 1
    previous_y = previous_y + move_y
    up = previous_y + move_y
    left = previous_x + random.randint(-25, 25)
    if (left + 150 >= 1000):
        left = 850
    if (left <= 0):
        left = 0
    previous_x = left
    
    border_list_left.append((left, up))
    if (border_once <= 35):
        border_list_right.append((left + add_left, up))
        border_once = border_once + 1
        add_left = add_left - 3
    border_list_right.append((left + 150, up))
    border_list_left_change = []
    border_list_right_change = []
        
    for update_cord in range(0, (len(border_list_left))):
        border_list_left_change.append((border_list_left[update_cord][0], border_list_left[update_cord][1] + camera_move))
        border_list_right_change.append((border_list_right[update_cord][0], border_list_right[update_cord][1] + camera_move))
    border_list_left = []
    border_list_right = []
    border_list_left = border_list_left_change
    border_list_right = border_list_right_change
    all_points_left = border_list_left
    all_points_right = border_list_right

    pygame.draw.lines(master, white, False, border_list_left, 5)
    pygame.draw.lines(master, white, False, border_list_right, 5)
    
for car in range (0, population):
    cars_dict[('car%s') %(car)] = Car()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                
    if (camera_plus >= 2):
        camera_move = camera_move - 0.1
        master.fill(black)
        build_map()    
        if (vieux == 0):
            for car in range (0, population):
                (cars_dict[('car%s') %(car)]).move()
        if (vieux == 1):
            for car in range (0, population):
                cars_dict_babies[('car%s') %(car)].move()
        camera_plus = 0
    if (camera_plus < 4):
        camera_plus = camera_plus + 1
        
    if (terminated == population):
        print(scores)
        camera_plus = 0
        camera_move = 0
        border_list_left = [(0, 0 + camera_move), (350, 550 + camera_move)]
        border_list_right = [(1000, 0 + camera_move), (650, 550 + camera_move)]
        previous_y = 550
        previous_x = 400
        all_points_left = []
        all_points_right = []
        scores = []
        terminated = 0
        population = 200
        border_once = 0
        add_left = 300
        cars_dict = {}
        cars_dict_babies = {}
        vieux = 1
        for car in range (0, population):
            cars_dict_babies[('car%s') %(car)] = Car_Babies(size_mate[random.randint(0, len(size_mate) - 1)], speed_mate[random.randint(0, len(speed_mate) - 1)], turn_range_mate[random.randint(0, len(turn_range_mate) - 1)])
        car_dict_babies[('car%s') %(population + 1)]
        size_mate = []
        speed_mate = []
        turn_range_mate = []
        
    pygame.display.flip()
    clock.tick(20)
