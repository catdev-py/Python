class Motor: 
    def encender(self):
        return "Motor encendido 🚗"

class Auto:
    def __init__(self):
        self.motor = Motor()  # Relación colaborativa

    def arrancar(self):
        return self.motor.encender()

auto = Auto()
print(auto.arrancar())
