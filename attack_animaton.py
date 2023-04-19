from enum import Enum

class AttackType(Enum):

   ROCK = 0
   PAPER = 1
   SCISSORS = 2

class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0

self.rock = AttackAnimation(AttackType.ROCK)
self.paper = AttackAnimation(AttackType.PAPER)
self.scissors = AttackAnimation(AttackType.SCISSORS)

def __init__(self, attack_type):
   super().__init__()

   self.attack_type = attack_type
   if self.attack_type == AttackType.ROCK:
       self.textures = [
           arcade.load_texture("assets/srock.png"),
           arcade.load_texture("assets/srock-attack.png"),
       ]
   elif self.attack_type == AttackType.PAPER:
       self.textures = [
           arcade.load_texture("assets/spaper.png"),
           arcade.load_texture("assets/spaper-attack.png"),
       ]
   else:
       self.textures = [
           arcade.load_texture("assets/scissors.png"),
           arcade.load_texture("assets/scissors-close.png"),
       ]

   self.scale = self.ATTACK_SCALE
   self.current_texture = 0
   self.set_texture(self.current_texture)

#attack code

