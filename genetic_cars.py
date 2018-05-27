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

border_list_left = [(0, 0 + camera_move), (370, 550 + camera_move)]
border_list_right = [(1000, 0 + camera_move), (580, 550 + camera_move)]
previous_y = 550
previous_x = 450

all_points_left = []
all_points_right = []

class Car:
    def __init__(self):
        self.x = 500
        self.y = 200
        self.size = random.randint(5, 30)
        self.speed = random.randint(1, 20)
        self.turn_range = random.randint(1, 100)
        self.terminate = 0
        self.body = pygame.draw.circle(master, blue, (self.x, self.y), self.size, 0)
        self.score = 0
        
    def move(self):
        global all_points_left, all_points_right
                                
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
                    
def build_map():
    global border_list_left, border_list_right, previous_y, previous_x, camera_move, all_points_left, all_points_right
    
    move_y = 1
    previous_y = previous_y + move_y
    up = previous_y + move_y
    left = previous_x + random.randint(-15, 15)
    if (left + 150 >= 1000):
        left = 850
    if (left <= 0):
        left = 0
    previous_x = left
    
    border_list_left.append((left, up))
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
    
car = Car()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                
    if (camera_plus >= 2):
        camera_move = camera_move - 0.1
        master.fill(black)
        build_map()    
        car.move()
        camera_plus = 0
    if (camera_plus < 4):
        camera_plus = camera_plus + 1
        
    pygame.display.flip()
    clock.tick(20)