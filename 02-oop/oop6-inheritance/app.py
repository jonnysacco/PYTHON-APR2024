from models.pc import PC
from models.mac import Mac
from models.computer import Computer

computer1 = Computer("Macbook", 2022)
pc1 = PC()

computer1.display_info()
pc1.display_info()
print(pc1.case_material)

pc1.turn_on()

mac_style = input('What is your macbook?')

mac1 = Mac(mac_style, 2023)
mac1.display_info()




"""
BEHIND THE SCENE:
1. Go to PC class to search for turn_on()
2. If PC class has turn_on(), execute that
3a. If PC class doesn't have turn_on()
3b.search for that method from Computer class
"""