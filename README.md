> # Introducing my repository PyGameClasses.

![](https://camo.githubusercontent.com/1971c0a4f776fb5351c765c37e59630c83cabd52/68747470733a2f2f7777772e707967616d652e6f72672f696d616765732f6c6f676f2e706e67)

### In this repository you will find all my self-coded PyGame classes as well as PyGame classes from others which I use myself (If a PyGame class is from someone else, it will be linked in the README.md as well as in the Python file).

> ## About the project:

- 🐍 **In this repository, the language [Python](https://www.python.org/) is used, as well as the Python module [PyGame](https://www.pygame.org/).**
- 🟥 **If needed the versions of Python and PyGame used will always be in the description of each class of this README.**

## Before any of the classes shown below will work you must follow these steps:

- **Download the class and add it into your project folder.**
- **Import the class into your main file (you may need to specify the path of the file):**
- import Class_Name
- [How to specify the path of a File you wanna import](https://stackoverflow.com/questions/67631/how-do-i-import-a-module-given-the-full-path)

> ## PyGame Classes:

### Button Class:

``- 👥 This PyGame class was created by @EinfachNurN1C0``
``- 🔗 A link to this PyGame class:``
[Button Class](https://github.com/EinfachNurN1C0/PyGameClasses/blob/main/Button_Class.py)

```python
# Syntax: ButtonName = Button_Class.Button(Button Width, Button Height, Link to an Button Image, Button Scale)
# z.B.

BUTTON_IMAGE = pygame.image.load(os.path.join('Assets', 'Buttons', 'Button_Image.png'))
BUTTON = Button_Class.Button(250, 250, BUTTON_IMAGE, 1)
BUTTON.draw(Definition of the window)

# Check if a function has been clicked:
# z.B.

if BUTTON.draw(Definition of the window): #<-- If BUTTON is pressed
    print("Hello World")
```

