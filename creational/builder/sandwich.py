import pygame
import sys
from abc import ABC, ABCMeta, abstractmethod


class Sandwich:
    def __init__(self):
        self.ingredients = []
    
    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)

    def display(self):
        print("Sandwich with the following ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")


class SandwichBuilder(ABC):
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass

    def get_result(self):
        return self.sandwich


class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredients("Wheat Bread")
    
    def add_filling(self):
        self.sandwich.add_ingredients("Lettuce")
        self.sandwich.add_ingredients("Tomato")
        self.sandwich.add_ingredients("Cucumber")

class HamSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredients("Wheat Bread")
    
    def add_filling(self):
        self.sandwich.add_ingredients("Ham")
        self.sandwich.add_ingredients("Cheese")
        self.sandwich.add_ingredients("Mayo")   


class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()


def draw_text(screen, text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Sandwich Builder')
    font = pygame.font.Font(pygame.font.get_default_font(), 18)

    veggie_builder = VeggieSandwichBuilder()
    director = SandwichDirector(veggie_builder)
    veggie_sandwich = director.build_sandwich()

    ham_builder = HamSandwichBuilder()
    director.builder = ham_builder
    ham_sandwich = director.build_sandwich()

    # Main game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear screen
        screen.fill((255, 255, 255))
            
        draw_text(screen, "Veggie Sandwich:", 10, 10, font, (0, 0, 0))
        for index, ingredients in enumerate(veggie_sandwich.ingredients):
            draw_text(screen, f"- {ingredients}", 10, 40 + index * 30, font, (0, 0, 0))

        draw_text(screen, "Ham Sandwich:", 300, 10, font, (0, 0, 0))
        for index, ingredients in enumerate(ham_sandwich.ingredients):
            draw_text(screen, f"- {ingredients}", 300, 40 + index * 30, font, (0, 0, 0))

        # Update display
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()
