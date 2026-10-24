class Appliance:
    def turn_on_cooling(self):
        return "Cooling compressor activated."

class MediaConnectedDevice:
    def stream_music(self, playlist):
        return f"Now playing: '{playlist}'"

class SmartRefrigerator(Appliance, MediaConnectedDevice):
    def check_inventory(self):
        return "Inventory: 3 Milk, 5 Eggs remainig."

fridge=SmartRefrigerator()
print(fridge.turn_on_cooling())
print(fridge.stream_music("Chilli"))
print(fridge.check_inventory())