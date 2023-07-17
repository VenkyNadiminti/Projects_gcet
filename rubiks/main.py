from cube.cube import Cube
from cube.gui import Gui
import pygame

def welcome_screen():
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        
        pygame.init()
        size = [700, 500]
        screen = pygame.display.set_mode(size)
        
        pygame.display.set_caption("CONTROLS SCREEN")
        done = False
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        display_instructions = True
        instruction_page = 1
        while not done and display_instructions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    instruction_page += 1
                    if instruction_page == 3:
                        display_instructions = False
        
            screen.fill(BLACK)
        
            if instruction_page == 1:
                text = font.render("CONTROLS", True, WHITE)
                screen.blit(text, [270, 230])
        
            if instruction_page == 2:
                # Draw instructions, page 2
                text = font.render("1.L-->Turn Left Face", True, WHITE)
                screen.blit(text, [10, 10])
        
                text = font.render("2.R-->Turn Right Face", True, WHITE)
                screen.blit(text, [10, 40])

                text = font.render("3.U-->Turn Upper Face", True, WHITE)
                screen.blit(text, [10, 70])

                text = font.render("4.D-->Turn Down Face", True, WHITE)
                screen.blit(text, [10, 100])

                text = font.render("5.B-->Turn Back Face", True, WHITE)
                screen.blit(text, [10, 130])

                text = font.render("6.F-->Turn Front Face", True, WHITE)
                screen.blit(text, [10, 160])

                text = font.render("7.S-->Scramble the CUBE", True, WHITE)
                screen.blit(text, [10, 190])

                text = font.render("8.SPACE-->Solve the CUBE", True, WHITE)
                screen.blit(text, [10, 220])
        
            clock.tick(60)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    welcome_screen()
    pygame.quit()
    cube = Cube(3)
    gui = Gui(cube)
    gui.run()
    