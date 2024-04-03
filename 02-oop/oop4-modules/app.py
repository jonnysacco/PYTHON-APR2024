# import computer class & developer class
from models.computer import Computer
from models.developer import Developer
import random
import utilities

computer1 = Computer(utilities.random_model(), utilities.random_year(), 1200) # Create the instance
computer2 = Computer(utilities.random_model(), utilities.random_year())
computer3 = Computer(utilities.random_model(), utilities.random_year())


computer1.turn_on()
computer1.open_tabs()
computer1.open_tabs(10)

computer1.turn_on().open_tabs().open_tabs(10)


dev1 = Developer("pepper", "peppergit")
print(dev1.computer.model)
dev1.display_status()

print(random.randint(1, 10))


print(computer1)
print(computer2)
print(computer3)
