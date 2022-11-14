from moviepy.editor import *
import pygame

#while True:
#    path = input()
#    break

pygame.init()
pygame.display.set_mode((0,0),0,32)
clip = VideoFileClip('test.mp4').resize((1920,1080))
clip.preview()
pygame.quit()