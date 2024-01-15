import time

# The Snack make a cool message saying that the human liked the food  and then displays a happy face. You can do whatever you want with this.
class Snack():
    def __init__(self):
        self.name = "Snack"

    def eat(self):
        text = "The sensation is so good! The snack you just ate had a very nice and delicious taste, that opened your mind to eat even more food."

        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)  # Adjust the sleep duration to control the speed of digitization
        print("\n.^.......^.")
        print("...........")
        print("..._____...")
