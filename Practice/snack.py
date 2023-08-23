import pygame
import sys
import random
# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()
# 颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# 蛇和食物的大小
block_size = 20
# 蛇的初始位置
snake_position = [[100, 100], [120, 100], [140, 100]]
# 食物的初始位置
food_position = [random.randrange(1, (800//block_size)) * block_size, random.randrange(1, (600//block_size)) * block_size]
food_spawn = True
# 蛇的初始速度
snake_speed = [block_size, 0]
# 计分
score = 0
# 游戏循环
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       keys = pygame.key.get_pressed()
       for key in keys:
           if keys[pygame.K_UP]:
               snake_speed = [0, -block_size]
           if keys[pygame.K_DOWN]:
               snake_speed = [0, block_size]
           if keys[pygame.K_LEFT]:
               snake_speed = [-block_size, 0]
           if keys[pygame.K_RIGHT]:
               snake_speed = [block_size, 0]
   # 更新蛇的位置
   snake_position[0][0] += snake_speed[0]
   snake_position[0][1] += snake_speed[1]
   # 判断是否吃到食物
   if snake_position[0] == food_position:
       score += 10
       food_spawn = False
   else:
       snake_position.pop()
   # 生成新的食物
   if not food_spawn:
       food_position = [random.randrange(1, (800//block_size)) * block_size, random.randrange(1, (600//block_size)) * block_size]
   food_spawn = True
   # 检查蛇是否撞到墙或自己
   if (snake_position[0][0] < 0 or snake_position[0][0] >= 800 or
       snake_position[0][1] < 0 or snake_position[0][1] >= 600 or
       snake_position[0] in snake_position[1:]):
       pygame.quit()
       sys.exit()
   # 绘制游戏元素
   screen.fill(WHITE)
   for position in snake_position:
       pygame.draw.rect(screen, GREEN, pygame.Rect(position[0], position[1], block_size, block_size))
   pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], block_size, block_size))
   # 显示得分
   font = pygame.font.Font(None, 36)
   text = font.render("得分：" + str(score), True, (0, 0, 0))
   screen.blit(text, (10, 10))
   # 更新屏幕
   pygame.display.flip()
   clock.tick(10000)