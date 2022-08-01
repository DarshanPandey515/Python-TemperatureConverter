# C to F = (0°C × 9/5) + 32 = 32°F
# F to C = (32°F − 32) × 5/9 = 0°C


def convertion(user):
    if user == 1:
        Celsius = int(input("Enter celsius:"))
        output1 = ( (Celsius * 9/5) + 32 )
        return output1
    elif user == 2:
        Fahrenheit = int(input("Enter fahrenheit :"))
        output2 = ( (Fahrenheit - 32) * 5/9 )
        return output2
    else:
        print("error")


user = int(input("Enter your convertion type\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius\n:"))
result = convertion(user)
print(result)

