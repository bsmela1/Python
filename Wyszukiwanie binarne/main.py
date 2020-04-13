def wyszukiwanie_binarne(lista, a):

    firstIndex = 0 #zmienna firstIndex oznacza indeks pierwszego elementu w aktualnym fragmencie zbioru
    endIndex = len(lista)-1 #zmienna endIndex oznacz indeks ostatniego elementu w aktualnym fragmencie zbioru

    #powtarzamy dopoki indeks pierwszego elemntu z aktualnego fragmentu zbioru jest mniejszy lub rowny indeksowi ostatniego elementu
    while(firstIndex<=endIndex):
        midIndex = firstIndex + int((endIndex-firstIndex)/2) #obliczamy srodkowy indeks za pomoca wzoru
    #jesli znalezlismy szukana liczbe, zwracamy jej indeks
        if(lista[midIndex] == a):
            return midIndex
    #jesli liczba, ktora szukamy jest wieksza od liczby o indeksie srodkowym z aktualnego fragmentu zbioru, ustawiamy pierwszy indeks na pozycje o jeden wieksza niz indeks srodkowy
        elif(lista[midIndex] < a):
            firstIndex = midIndex+1
    #jesli liczba, ktora szukamy jest mniejsza od liczby o indeksie srodkowym z aktualnego fragmentu zbioru, indeks ostatniego elementu ustawiamy na indeks srodkowego elementu-1
        elif(lista[midIndex] > a):
            endIndex = midIndex-1
    #jesli liczby nie uda nam sie znalezc to zwracamy -1
    return -1


lista1 = [4, 2, 8, 9, 10, 22, 67, 77, 3, 4, 7, 1]

#sortujemy liste, poniewaz wyszukiwanie binarne dziala prawidlowo tylko na uporzadkowanych zbiorach
lista1.sort()

print(lista1)
print(wyszukiwanie_binarne(lista1, 77))
print(wyszukiwanie_binarne(lista1, 9))