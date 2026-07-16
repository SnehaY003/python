class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        print("Fahrenheit =", (c * 9 / 5) + 32)

    @staticmethod
    def fahrenheit_to_celsius(f):
        print("Celsius =", (f - 32) * 5 / 9)

TemperatureConverter.celsius_to_fahrenheit(30)
TemperatureConverter.fahrenheit_to_celsius(86)