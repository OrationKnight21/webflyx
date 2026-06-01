class Wall:
    def __init__(self, height):
        # the double underscore makes this a private property
        # but it's not strictly enforced, there are hacks to get around it
        self.__height = height

    def get_height(self):
        return self.__height
    
def main():
    k = Wall(7)
    print(k.get_height())
    
main()