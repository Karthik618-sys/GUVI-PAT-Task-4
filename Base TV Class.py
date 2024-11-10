class TV:
    # Constructor method to initialize the TV attributes
    def __init__(self, brand, price, inches):
        self.brand = brand  # Brand of the TV
        self.channel = 1  # Default channel is 1
        self.volume = 50  # Default volume is 50
        self.price = price  # Price of the TV
        self.inches = inches  # Size of the TV in inches
        self.is_on = False  # TV is initially turned off

    # Method to turn on the TV
    def turn_on(self):
        self.is_on = True

    # Method to turn off the TV
    def turn_off(self):
        self.is_on = False

    # Method to increase the volume
    def increase_volume(self):
        if self.volume < 100:  # Volume cannot exceed 100
            self.volume += 1

    # Method to decrease the volume
    def decrease_volume(self):
        if self.volume > 0:  # Volume cannot be below 0
            self.volume -= 1

    # Method to set the TV channel
    def set_channel(self, channel):
        if 1 <= channel <= 50:  # TV has only 50 channels
            self.channel = channel

    # Method to reset the TV to default settings
    def reset(self):
        self.channel = 1  # Reset channel to 1
        self.volume = 50  # Reset volume to 50

    # Method to return the status of the TV
    def status(self):
        on_off_status = "On" if self.is_on else "Off"
        return f'{self.brand} at channel {self.channel}, volume {self.volume}, status {on_off_status}'

# Example usage
tv = TV(brand="Panasonic", price=500, inches=42)
tv.turn_on()
tv.set_channel(8)
tv.increase_volume()
print(tv.status())
