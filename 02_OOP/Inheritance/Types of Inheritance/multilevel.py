class GameEntity:
    def __init__(self, x, y):
        self.x=x
        self.y=y
class Character(GameEntity):
    def move(self, dx, dy):
        self.x+=dx
        self.y+=dy
        return f"Moved to position ({self.x}, {self.y})"
class Hero(Character):
    def __init__(self, x, y, name):
        super().__init__(x,y)
        self.name=name
        self.health=100

player=Hero(0,0,"Aragorn")
print(player.move(5,10))
print(player.health)