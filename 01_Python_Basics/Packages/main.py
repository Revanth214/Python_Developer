from utilities.greetings import greet
from utilities.square import square
print(greet('Rama'))
print(square(5))


# after importing greetins.py, square.py files into __init__.py. Now we can directly import functions of greetings,square modules.
from utilities import greet
from utilities import square
print(greet('Shiva'))
print(square(50))