"""Polecenie 1.
Napisz program typu FizzBuzz – program ma wyświetlać listę liczb od 1 do 100, ale zamiast
liczb podzielnych przez 3 ma wyświetlić słowo „Fizz”, zamiast podzielnych przez 5 słowo
„Buzz”, a zamiast podzielnych jednocześnie przez 3 oraz przez 5 – słowo „FizzBuzz”.
Skorzystaj z operatora mod do sprawdzania podzielności.
"""
def zadanie1():
    for i in range(101):
        if(i>0):
            if (i%3==0 and i%5!=0 ):
                print("Fizz")
            elif(i%5==0 and i%3!=0 ):
                print("Buzz")
            elif(i%3==0 and i%5==0 ):
                print("FizzBuzz")
            else:
                print(i)
"""Napisz program, który iterując znak po znaku wyświetli każdą cyfrę liczby w postaci słownej,
np. 110 wyświetli jako „jeden jeden zero”.
"""
def zadanie2():
    liczby={"0":"zero","1":"jeden","2":"dwa","3":"trzy","4":"cztery","5":"pięć","6":"sześć","7":"siedem","8":"osiem","9":"dziewięć","10":"dziesięć"}
    x=str(input("Wprowadz liczbe: "))
    for i in x:
            print(liczby[i],end=' ')
"""Napisz program, który pozwoli na zamianę liczb arabskich (np. 123) na system rzymski (np.
CXXIII). Skorzystaj z funkcji input(), która pozwala wczytać tekst od użytkownika oraz
odpowiednich funkcji do konwersji. Możesz wykorzystać słowniki, aby powiązać liczby
arabskie i odpowiadające im łańcuchy znaków w systemie rzymskim.
"""
def zadanie3():
    print("Ten program służy do konwersji liczb z systemu arabskiego na rzymski,system ten obsługuje liczby CAŁKOWITE od 1 do 99999")
    do9 = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX"}
    od10do90 = {"10": "X", "20": "XX", "30": "XXX", "40": "XL", "50": "L", "60": "LX", "70": "LXX", "80": "LXXX", "90": "XC"}
    od100do1000 = {"100": "C", "200": "CC", "300": "CCC", "400": "CD", "500": "D", "600": "DC", "700": "DCC", "800": "DCCC", "900": "CM", "1000": "M"}

    liczba = []
    liczba1 = []
    x = float(input("Wprowadź liczbę: "))
    if(x>99999 or x<1 or int(x)<x):
        print("Wprowadzono nieprawidłową liczbę. Wprowadź liczbę prawidłową ( całkowitą, z zakresu 1-99999 ) i spróbuj ponownie.")
    else:
        x=int(x)
        if (str(x) in do9):
            print(do9[str(x)])
        elif (str(x) in od10do90):
            print(od10do90[str(x)])
        elif (str(x) in od100do1000):
            print(od100do1000[str(x)])
        else:

            while x != 0:
                liczba.append(x % 10)
                x = x // 10


            liczba1.extend(liczba)
            print(liczba)

            rzymska = []
            if(liczba[0]!=0):
                rzymska.append(do9[str(liczba[0])])
            if(liczba[1]!=0):
                rzymska.append(od10do90[str(liczba[1]*10)])
            if (liczba[2] != 0):
                rzymska.append(od100do1000[str(liczba[2]*100)])
            if(len(liczba)>=4):
                if (liczba[3]>0):
                    rzymska.append('M'*liczba[3])

            print("Liczba w systemie rzymskim:", end=' ')
            rzymska.reverse()
            for i in rzymska:
                print(i, end='')


#zadanie1()
#zadanie2()
zadanie3()
