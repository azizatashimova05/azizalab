# Наследование от нескольких классов
class Camera:
    def take_photo(self):
        print("Photo taken.")

class Phone:
    def call(self):
        print("Calling...")

class SmartDevice(Camera, Phone):
    pass

device = SmartDevice()
device.take_photo()
device.call()
