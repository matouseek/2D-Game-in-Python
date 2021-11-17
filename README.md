# 2D Game in Python

## Introduction
Hey, my name is Matouš and I'm a Czech High School student. 
This file serves as help for constructing my documentation for my long-term graduation work, it will also help me keep track of my progress.
At least for the time being. My goal for this project is to create a 2D videogame in Python using OOP and the Pygame module.

## Expectations
The game will consist of two parts. The first one will be an interactive menu that you can navigate through.
The second part will be the game itself. It will be an arcade medieval styled game, where your main goal is to defeat your opponent using your special attacks.
The game will be played by two players on the same computer. It will feature two unique heroes. Both of them will also have their own animations in idle, running and attacking positions.
The first hero is inspired by my favourite manga Berserk, specifically by its main hero Guts. The second hero is inspired by one of the main characters of Terry Pratchetts Discworld books about the Wizards, Rincewind (even though he can't actually cast any spells in the books :D).
This is also the first time I'm using GitHub on a real project, so I'll have this as sort of a learning experience as well.

This file is going to be updated regularly until I finish my work and submit it.

## Game logic
Just a side note but none of the code bellow will work on its own, its used here only to showcase how certain
mechanics work without having to take huge chunks of code from the actual game
* **Movement**

To move our character we'll be working with the following variables and functions:

(example shown on the Guts class)
```python
class Guts:
    def __init__(self, x):
        self.x = x
        self.velx = 10
        
    def move_guts(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width:
            self.x += self.velx
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
```
**self.x** - position of the character on the x-axis

**self.velx** - x-axis velocity of the character

**userInput** - input from the user, we'll be getting that in the game loop,
in this case it will be either Right key or Left key

**win_width** - predefined window width, used here to track whether
the character is still inside our window

We are moving the character on **x-axis** *only* so we won't be needing any **y-axis** variables for now

**def move_guts(self, userInput)** - If the player presses the Right key and our characters x-axis value is less than **win_width**,
the value of our characters x-axis will increase by 10 for every frame until we let go of the Right key
or the x-axis value reaches win_width value

If the player presses the Left key and our characters x-axis value is more than **0**,
the value of our character will decrease by 10 for every frame until we let go of that key
or the x-axis value reaches 0

  * **Attacking**
      * **Mrakoplas**\
    To be able to attack as Mrakoplas we'll need the following variables and functions:
    ```python
    class Mrakoplas:
        def __init__(self):
            self.fireball_x = 0
            self.fireball_y = 0
            self.fireball_velx = 5

            self.att_right = True
            self.att_left = False
            self.att_check = False
            self.fireball_check = False
    
        def attack(self, userInput):
            if userInput[pygame.K_SPACE] and self.fireball_check == False:
                self.att_check = True
  
        def move_mrakoplas(self, userInput):
            if self.att_check:
                pass
            else:
                #Mrakoplas movement
 
        def draw(self, win):
            if self.att_check:
                if #att animation - done:
                    self.att_check = False
                    self.fireball_check = True
                if self.att_right:
                    win.blit(#att animation - right)
                elif self.att_left:
                    win.blit(#att animation - left)

        def fireball(self, win):
            if 0<self.fireball_x<win_width:
                if self.att_right and self.fireball_check:
                    win.blit(#fireball animation - right)
                    self.fireball_x += self.fireball_velx
                elif self.att_left and self.fireball_check:
                    win.blit(#fireball animation - left)
                    self.fireball_x -= self.fireball_velx
            else:
                self.fireball_check = False
    ```
    **self.fireball_x** - position of the fireball on the x-axis\
\
    **self.fireball_y** - position of the fireball on the y-axis (fireball can be combined with jump so we need y-axis value as well)\
\
    **self.fireball_velx** - x-axis velocity of the fireball\
\
    **self.att_right** - variable for checking whether to shoot right - This is set True while running right\
\
    **self.att_left** - variable for checking whether to shoot left - This is set True while running left\
\
    **self.att_check** - variable for checking if and when to print attack animation and stop movement\
\
    **self.fireball_check** - variable for checking if and when to print the fireball\
\
    **userInput** - input from the user, we'll be getting that in the game loop,
    in this case it will be the space bar\
\
    **def attack(self, userInput)** - checks if the user pressed the attack key, in this case the space bar\
\
    **def move_mrakoplas(self, userInput)** - this is the move function from above but with added feature to halt any
    movement if the character is attacking\
\
    **def draw(self, win)** - prints the attack animation, if the attack animation is over, sets self.fireball_check on True\
\
    **def fireball(self, win)** - prints the fireball and stops the user from firing another fireball
    until the first one disappears behind the edges of the window
  
    * **Guts**\
    To be able to attack as Guts we'll need the following variables and functions:
    ```python
    class Guts:
        def __init__(self):
            self.att_right = True
            self.att_left = False
            self.att_check = False

        def attack(self, userInput):
            if userInput[pygame.K_RCTRL] and self.att_check = False:
                self.att_check = True
        
        def move_guts(self, userInput):
            if self.att_check:
                pass
            else:
                #Guts movement
    
        def draw(self, win):
            if self.att_check:
                if #att animation - done:
                    self.att_check = False
            if self.att_right:
                win.blit(#att animation - right)
                win.blit(#sword animation - right)
            elif self.att_left:
                win.blit(#att animation - left)
                win.blit(#sword animation - left)
    ```
    **self.att_right** - variable for checking whether to attack right - This is set True while running right\
\
    **self.att_left** - variable for checking whether to attack left - This is set True while running left\
\
    **self.att_check** - variable for checking if and when to print attack animation and stop movement\
\
    **userInput** - input from the user, we'll be getting that in the game loop,
    in this case it will be the right CTRL key\
\
    **def attack(self, userInput)** - checks if the user pressed the attack key, in this case the right CTRL key\
\
    **def move_guts(self, userInput)** - this is the move function from above but with added feature to halt any
    movement if the character is attacking\
\
    **def draw(self, win)** - prints the attack animation

  * **Animations**\
In order to print animations we'll need these variables and functions:\
(example shown on the Mrakoplas class, specifically on his move animation)
```python
mrakoplas_right = [file1.png, file2.png, file3.png, file4.png]
mrakoplas_left = [file1.png, file2.png, file3.png, file4.png]
mrakoplas_idle = [file1.png, file2.png, file3.png, file4.png]

class Mrakoplas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.face_right = False
        self.face_left = False
        self.idle = True
    
        self.stepIndex = 0
        self.stepIndex_Idle = 0
    
    def draw(self, win):
        if self.stepIndex >= 16:
            self.stepIndex = 0
        if self.stepIndex_Idle >= 16:
            self.stepIndex_Idle = 0
        if self.face_right:
            win.blit(mrakoplas_right[self.stepIndex//4], (self.x, self.y))
            self.stepIndex += 1
        if self.face_left:
            win.blit(mrakoplas_left[self.stepIndex//4], (self.x, self.y))
            self.stepIndex += 1
        elif self.idle:
            win.blit(mrakoplas_idle[self.stepIndex_Idle//4], (self.x, self.y))
            self.stepIndex_Idle += 1
```
**self.x** - position of the character on the x-axis\
\
**self.y** - position of the character on the y-axis\
\
**self.face_right** - variable that helps us see if the character is running right\
\
**self.face_left** - variable that helps us see if the character is running left\
\
**self.idle** - variable that helps us see if the character is in idle position (not running left or right)\
\
**self.stepIndex** - index to help us track which frame of the right/left animation to print\
\
**self.stepIndex_Idle** - index to help us track which frame of the idle animation to print\
\
**win** - is the surface on which our character will be printed\
\
**def draw(self, win)** - \
-in this function the right/left or idle animation will be printed based on which variables are True and which are False\
-the images are taken from our previously defined lists (i.e. mrakoplas_idle)\
-the index of each frame is divided by 4 and the indexes reset if the value is 16, that is because we want the animations to last longer without changing the FPS, 
we can achieve that by printing one frame more than once (in this case 4 times) before moving onto another one

  * **Jumping**\
If we want our character to jump we need the following variables and functions:\
(example shown on the Guts class)

```python
import pygame


class Guts:
    def __init__(self, y):
        self.y = y
        self.vely = 10

        self.jump_check = False

    def jump(self, userInput):
        if userInput[pygame.K_UP] and self.jump_check = False:
            self.jump_check = True
        if self.jump_check:
            self.y -= self.vely*2
            self.vely -= 1
        if self.vely < -10:
            self.vely = 10
            self.jump_check = False
```
**self.y** - position of the character on the y-axis\
\
**self.vely** - y-axis velocity of the character\
\
**self.jump_check** - variable for checking when to jump\
\
**userInput** - input from the user, we'll be getting that in the game loop,
in this case it will be the UP key\
\
**def jump(self, userInput)** -\
-if the user presses the UP key, self.jump_check will be set to True\
-self.vely will be subtracted from self.y for every frame that self.jump_check is True(the *2 is there only so the character jumps faster)\
-1 will be subtracted from self.vely for every frame that self.jump_check is True\
-this will result in self.vely eventually turning negative and moving the character back into its original position\
-because of the decaying (and after self.vely < 0, raising) velocity it also simulates gravity pretty well
