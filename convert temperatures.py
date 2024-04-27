def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")
    print("Enter the temperature value and the original unit of measurement:")
    temperature = float(input("Temperature: "))
    original_unit = input("Original Unit (Celsius/C, Fahrenheit/F, Kelvin/K): ").upper()

    if original_unit == 'C' or original_unit == 'CELSIUS':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif original_unit == 'F' or original_unit == 'FAHRENHEIT':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif original_unit == 'K' or original_unit == 'KELVIN':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit of measurement. Please enter Celsius/C, Fahrenheit/F, or Kelvin/K.")
        return

    print(f"\nConverted Temperatures:")
    print(f"Celsius: {celsius} °C")
    print(f"Fahrenheit: {fahrenheit} °F")
    print(f"Kelvin: {kelvin} K")

if __name__ == "__main__":
    main()
