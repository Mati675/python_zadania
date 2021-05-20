'''
Napisz program, który wyświetla liczby od 1 do 100.
Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
dla liczb podzielnych przez 5 niech wyświetli `Buzz`;
a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.

​
'''

for liczba in range(1, 101):
    if liczba % 3 == 0 and not liczba % 5 == 0 and not liczba % 15 == 0:
        print("Fizz")
    elif liczba % 5 ==0 and not liczba % 3 == 0 and not liczba % 15 ==0:
        print("Buzz")
    elif liczba % 15 == 0:
        print("FizzBuzz")
    else:
        print(liczba)
