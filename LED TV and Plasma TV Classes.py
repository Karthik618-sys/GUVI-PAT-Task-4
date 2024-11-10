# Define the base TV class
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

# Define the LedTV class inheriting from TV class
class LedTV(TV):
    # Constructor to initialize the LedTV attributes
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)  # Initialize parent class (TV) attributes
        self.screen_thickness = screen_thickness  # Thickness of the screen
        self.energy_usage = energy_usage  # Energy usage of the TV
        self.lifespan = lifespan  # Lifespan of the TV
        self.refresh_rate = refresh_rate  # Refresh rate of the TV

    # Method to display detailed features of the LED TV
    def display_details(self):
        return f'LED TV - Brand: {self.brand}, Channel: {self.channel}, Volume: {self.volume}, ' \
               f'Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, ' \
               f'Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}'

# Define the PlasmaTV class inheriting from TV class
class PlasmaTV(TV):
    # Constructor to initialize the PlasmaTV attributes
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)  # Initialize parent class (TV) attributes
        self.screen_thickness = screen_thickness  # Thickness of the screen
        self.energy_usage = energy_usage  # Energy usage of the TV
        self.lifespan = lifespan  # Lifespan of the TV
        self.refresh_rate = refresh_rate  # Refresh rate of the TV

    # Method to display detailed features of the Plasma TV
    def display_details(self):
        return f'Plasma TV - Brand: {self.brand}, Channel: {self.channel}, Volume: {self.volume}, ' \
               f'Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, ' \
               f'Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}'

# Example usage
led_tv = LedTV(brand="Samsung", price=1200, inches=55, screen_thickness=2.3, energy_usage=100, lifespan=60000, refresh_rate=120)
plasma_tv = PlasmaTV(brand="LG", price=1500, inches=60, screen_thickness=3.0, energy_usage=150, lifespan=50000, refresh_rate=60)

print(led_tv.display_details())
print(plasma_tv.display_details())
