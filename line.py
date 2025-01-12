import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line():
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0)  # Starting point
    glVertex2f(0.5, 0)   # Ending point
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-1, 1, -1, 1)  # Set the orthographic projection

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_line()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
