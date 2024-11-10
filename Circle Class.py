class Circle:
    # Constructor method to initialize the list of radii and a private variable for pi
    def __init__(self, radius_list):
        self.radius_list = radius_list
        self.__pi = 3.141  # Private variable for the value of pi

    # Method to calculate the area for each radius in the list
    def calculate_area(self):
        area_list = []
        for radius in self.radius_list:
            area = self.__pi * (radius ** 2)  # Calculate area using pi * r^2
            area_list.append(area)  # Append the calculated area to the list
        return area_list

    # Method to calculate the perimeter for each radius in the list
    def calculate_perimeter(self):
        perimeter_list = []
        for radius in self.radius_list:
            perimeter = 2 * self.__pi * radius  # Calculate perimeter using 2 * pi * r
            perimeter_list.append(perimeter)  # Append the calculated perimeter to the list
        return perimeter_list

# Example usage
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
print(f'Areas: {circle.calculate_area()}')  # Print the list of calculated areas
print(f'Perimeters: {circle.calculate_perimeter()}')  # Print the list of calculated perimeters
