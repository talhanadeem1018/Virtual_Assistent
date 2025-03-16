from os import link   
import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=1000, height=600, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200), (190, 200), (180, 200)]  # Adjusted initial positions
        self.direction = "Right"
        self.food = self.create_food()

        self.master.bind("<Key>", self.change_direction)

        self.update()

    def create_food(self):
        x = random.randint(1, 49) * 20
        y = random.randint(1, 29) * 20
        self.food_id = self.canvas.create_oval(x, y, x + 20, y + 20, fill="red")
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if (key == "Up" and not self.direction == "Down" or
                key == "Down" and not self.direction == "Up" or
                key == "Left" and not self.direction == "Right" or
                key == "Right" and not self.direction == "Left"):
            self.direction = key

    def move(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= 20
        elif self.direction == "Down":
            y += 20
        elif self.direction == "Left":
            x -= 20
        elif self.direction == "Right":
            x += 20

        x = x % 1000  # Wrap around for a 50 by 30 grid
        y = y % 600   # Wrap around for a 50 by 30 grid

        self.snake.insert(0, (x, y))

        if x == self.food[0] and y == self.food[1]:
            self.canvas.delete(self.food_id)
            self.food = self.create_food()
        else:
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

    def check_collision(self):
        x, y = self.snake[0]
        if (x < 0 or x >= 1000 or
                y < 0 or y >= 600 or
                (x, y) in self.snake[1:]):
            return True
        return False

    def update(self):
        if not self.check_collision():
            self.move()
            self.draw()
            self.master.after(100, self.update)
        else:
            self.canvas.create_text(500, 300, text="Game Over", fill="white", font=("Helvetica", 16, "bold"))

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")

        x, y = self.food
        self.canvas.create_oval(x, y, x + 20, y + 20, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
