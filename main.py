import argparse
import time
import random

RUCH = []  # tabela możliwych ruchów- L U R D
WEZEL_POCZ = []
WEZEL_ROZW = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
PUSTE_POLE = [9, 9]
MAX_CZAS = 200
MAX_GLEBOKOSC = 20



class Node:
    def __init__(self, aktualna_tablica, rodzic, sciezka, poprzedni_ruch):
        self.tablica = aktualna_tablica
        if rodzic != "root":
            self.rodzic = rodzic
        self.dzieci = {}
        self.wynikfunkcji = {}
        self.sciezka = sciezka + poprzedni_ruch
        # self.sciezka.append(poprzedni_ruch)
        self.mozliwe_ruchy = RUCH.copy()
        self.poprzedni_ruch = poprzedni_ruch

        # ustal_puste_pole(self)
        # ustal_mozliwe_ruchy(self)

    def nowy_potomek(self, tab, kierunek):
        nowedziecko = Node(tab, self, self.sciezka, kierunek)
        # ustal_mozliwe_ruchy(nowedziecko)
        self.dzieci[kierunek] = nowedziecko

    def przesun_puste_pole(self, kierunek):
        # WEZEL.tablica[PUSTE_POLE[0]][PUSTE_POLE[1]] - miejsce 0 w tablicy
        ntablica = []
        for row in self.tablica:
            ntablica.append(row.copy())

        if (kierunek == 'L'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] - 1]
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] - 1] = '0'
            # PUSTE_POLE[1] -= 1

        if (kierunek == 'R'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] + 1]
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] + 1] = '0'
            # PUSTE_POLE[1] += 1

        if (kierunek == 'U'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0] - 1][PUSTE_POLE[1]]
            ntablica[PUSTE_POLE[0] - 1][PUSTE_POLE[1]] = '0'
            # PUSTE_POLE[0] -= 1

        if (kierunek == 'D'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0] + 1][PUSTE_POLE[1]]
            ntablica[PUSTE_POLE[0] + 1][PUSTE_POLE[1]] = '0'
            # PUSTE_POLE[0] += 1

        self.nowy_potomek(ntablica, kierunek)


def czy_gotowe(rw, rozw):
    for i in range(len(rw)):
        for j in range(len(rw)):
            if rw[i][j] != rozw[i][j]:
                return False
    return True


def BFS():
    liczba_odwiedzonych_wezlow = 1
    liczba_przetworzonych_wezlow = 1
    czas0 = time.time()
    AKT_WEZEL = Node(WEZEL_POCZ, 'Root', '', '')
    kolejka = []
    kolejka.append(AKT_WEZEL)
    licz = 0
    while True:
        licz += 1
        AKT_WEZEL = kolejka[0]
        ustal_puste_pole(AKT_WEZEL)
        ustal_mozliwe_ruchy(AKT_WEZEL)
        print(AKT_WEZEL.tablica, 'Licznik: ', licz, PUSTE_POLE, AKT_WEZEL.sciezka, AKT_WEZEL.mozliwe_ruchy, PUSTE_POLE)
        if czy_gotowe(AKT_WEZEL.tablica, WEZEL_ROZW):
            return AKT_WEZEL.tablica, AKT_WEZEL.sciezka, len(
                AKT_WEZEL.sciezka), liczba_odwiedzonych_wezlow, liczba_przetworzonych_wezlow, time.time() - czas0
        if time.time() - czas0 > MAX_CZAS:
            return [], '', -1, liczba_odwiedzonych_wezlow, liczba_przetworzonych_wezlow, time.time() - czas0
        for element in AKT_WEZEL.mozliwe_ruchy:
            liczba_przetworzonych_wezlow += 1
            AKT_WEZEL.przesun_puste_pole(element)
            NOWY_WEZEL = AKT_WEZEL.dzieci[element]
            kolejka.append(NOWY_WEZEL)
        kolejka.remove(AKT_WEZEL)
        liczba_odwiedzonych_wezlow += 1


def zapis_do_pliku_rozw(plik, dlugosc_rozw, pokonane_ruchy):
    file = open(plik, 'w+')
    file.write(str(dlugosc_rozw))
    if len(pokonane_ruchy) > 0:
        file.write('\n')
        file.write(str(pokonane_ruchy))
    file.close()


def zapis_do_pliku_stat(plik, glebokosc, odwiedzone, przetworzone, czas):
    file = open(plik, 'w+')
    file.write(str(glebokosc))
    file.write('\n')
    if glebokosc > 0:
        file.write(str(odwiedzone))
        file.write('\n')
        file.write(str(przetworzone))
        file.write('\n')
        file.write(str(glebokosc))
        file.write('\n')
        file.write(str(round((czas) * 1000, 3)))
    file.close()


def DFS():
    print('DFS :(    ')
    liczba_odwiedzonych_wezlow = 1
    liczba_przetworzonych_wezlow = 1
    czas0 = time.time()
    AKT_WEZEL = Node(WEZEL_POCZ, 'Root', '', '')
    ustal_puste_pole(AKT_WEZEL)
    ustal_mozliwe_ruchy(AKT_WEZEL)
    print(AKT_WEZEL.mozliwe_ruchy)
    aktualna_glebokosc = 1
    licz = 0
    while True:
        licz += 1
        print(licz, '___', aktualna_glebokosc, AKT_WEZEL.tablica, AKT_WEZEL.mozliwe_ruchy)
        if czy_gotowe(AKT_WEZEL.tablica, WEZEL_ROZW):
            print('Rozwiązane !!!')
            return AKT_WEZEL.tablica, AKT_WEZEL.sciezka, len(
                AKT_WEZEL.sciezka), liczba_odwiedzonych_wezlow, liczba_przetworzonych_wezlow, time.time() - czas0
        if time.time() - czas0 > MAX_CZAS:
            print('CZAS ZOSTAL  PRZEKROCZONY !!!!!!!!!!!!!!!!!!!!!!!')
            return [], '', -1, liczba_odwiedzonych_wezlow, liczba_przetworzonych_wezlow, time.time() - czas0
        elif aktualna_glebokosc >= MAX_GLEBOKOSC:
            print('max głębokość: ')
            NOWY_WEZEL = AKT_WEZEL.rodzic
            if aktualna_glebokosc == 1:
                print('Nie ma rozwiązania')
                return -1
            aktualna_glebokosc -= 1
            AKT_WEZEL = NOWY_WEZEL
            ustal_puste_pole(AKT_WEZEL)
        elif len(AKT_WEZEL.mozliwe_ruchy) == 0:
            print('mie ma już dzieci')
            NOWY_WEZEL = AKT_WEZEL.rodzic
            if aktualna_glebokosc == 1:
                print('Nie ma rozwiązania')
                return -1
            aktualna_glebokosc -= 1
            AKT_WEZEL = NOWY_WEZEL
            ustal_puste_pole(AKT_WEZEL)
        elif time.time() - czas0 > MAX_CZAS:
            print('przekroczony czas')
            return -1
        else:
            nowy_ruch = AKT_WEZEL.mozliwe_ruchy[0]  # ustalenie 1ego możliwego ruchu
            liczba_przetworzonych_wezlow += 1
            #print('działamy !!!', nowy_ruch, PUSTE_POLE)
            AKT_WEZEL.przesun_puste_pole(nowy_ruch)  # przesunięcie pustego pola w to miejsc i utworzenie "dziecka" w tym kierunku
            NOWY_WEZEL = AKT_WEZEL.dzieci[nowy_ruch]  # utworzenie nowego węzła
            AKT_WEZEL.mozliwe_ruchy.remove(nowy_ruch)  # w starym węźłe usuwamy ruch który już wykonaliśmy
            aktualna_glebokosc += 1  # zwiększenie głębokości bo przechodzimy do węzła
            AKT_WEZEL = NOWY_WEZEL  # aktualnym węzłem staje się "dziecko"
            ustal_puste_pole(AKT_WEZEL)
            ustal_mozliwe_ruchy(AKT_WEZEL)
        liczba_odwiedzonych_wezlow += 1


def ASTAR(wybor):
    print('ASTAR : ' + wybor)

    liczba_odwiedzonych_wezlow = 1
    liczba_przetworzonych_wezlow = 1
    czas0 = time.time()
    AKT_WEZEL = Node(WEZEL_POCZ, 'Root', '', '')
    ustal_puste_pole(AKT_WEZEL)
    ustal_mozliwe_ruchy(AKT_WEZEL)
    print(AKT_WEZEL.tablica, AKT_WEZEL.mozliwe_ruchy)
    aktualna_glebokosc = 1
    licz = 0
    while True:
        licz += 1
        # print(':/')
        # print('Licznik : ', licz, AKT_WEZEL.tablica)
        if czy_gotowe(AKT_WEZEL.tablica, WEZEL_ROZW):
            print('Rozwiązane ! ', AKT_WEZEL.sciezka)
            return AKT_WEZEL.tablica, AKT_WEZEL.sciezka, len( AKT_WEZEL.sciezka), liczba_odwiedzonych_wezlow, liczba_przetworzonych_wezlow, time.time() - czas0
        elif time.time() - czas0 > MAX_CZAS:
            print('Czas przekroczony')
            return [], '', -1, liczba_odwiedzonych_wezlow, liczba_przetworzonych_wezlow, time.time() - czas0
        elif len(AKT_WEZEL.mozliwe_ruchy) == 0:
            print('Nie ma ruchów')
            return -1
        else:
            for indeks in AKT_WEZEL.mozliwe_ruchy:
                liczba_przetworzonych_wezlow += 1
                # print('Tu jestem : ', indeks)
                #liczba_przetworzonych_wezlow = 1
                AKT_WEZEL.przesun_puste_pole(indeks)  # przesunięcie pustego pola w to miejsc i utworzenie "dziecka" w tym kierunku
                NOWY_WEZEL = AKT_WEZEL.dzieci[indeks]  # utworzenie nowego węzła
                print('Nowy węzeł tablica: ', NOWY_WEZEL.tablica)
                if wybor == 'MANH':
                    wynik1 = Manhattan(NOWY_WEZEL.tablica)
                elif wybor == 'HAMM':
                    print('Hamming tu jest ')
                    wynik1 = Hamming(NOWY_WEZEL.tablica)

                AKT_WEZEL.wynikfunkcji[indeks] = wynik1

            #print('Słownik: ', AKT_WEZEL.wynikfunkcji)
            minimalnawart = min(AKT_WEZEL.wynikfunkcji.values())
            tymcz = []
            for i in AKT_WEZEL.wynikfunkcji:
                if AKT_WEZEL.wynikfunkcji[i] == minimalnawart:
                    tymcz.append(i)
            print('TYMCZ', tymcz)
            nr = random.randint(0, len(tymcz) - 1)
            print('Losowanie: ', tymcz[nr])
            AKT_WEZEL.przesun_puste_pole(tymcz[nr])
            NOWY_WEZEL = AKT_WEZEL.dzieci[tymcz[nr]]
            AKT_WEZEL = NOWY_WEZEL
            ustal_puste_pole(AKT_WEZEL)
            ustal_mozliwe_ruchy(AKT_WEZEL)

        liczba_odwiedzonych_wezlow += 1


def Hamming(tablica):
    wynik = 0
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] != WEZEL_ROZW[i][j]:
                wynik += 1
    return wynik


def Manhattan(tablica):
    wynik = 0

    def ustal_wspolrzedne(liczba, tab):
        tzwr = [9, 9]
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tab[i][j] == liczba:
                    tzwr = [i, j]
        return tzwr

    for i in range(16):
        tb = ustal_wspolrzedne(str(i), tablica)  # współrzędne i w tablicy biezącej  [1,3]
        tw = ustal_wspolrzedne(str(i), WEZEL_ROZW)  # współrzędne i w tablicy rozwiązań  [0,0]
        wynik += (abs(tb[0] - tw[0]) + abs(tb[1] - tw[1]))  # |1-0| + |3-0|

    return wynik


def wczytaj_plik_poczatkowy():
    with open(parametry.uklad_poczatkowy) as uklad_p:
        pierwsza_linia = True
        for linia in uklad_p:
            if pierwsza_linia:
                pierwsza_linia = False
                continue
            else:
                WEZEL_POCZ.append(linia.split())


def ustal_puste_pole(WEZEL):
    for i in range(len(WEZEL.tablica)):
        for j in range(len(WEZEL.tablica[i])):
            if WEZEL.tablica[i][j] == '0':
                PUSTE_POLE[0] = i  # współrzędne pustego pola
                PUSTE_POLE[1] = j


def ustal_mozliwe_ruchy(WEZEL):
    TabRob = WEZEL.mozliwe_ruchy  # ['L','R','U','D']
    # możliwości ruchu w zaleności od pozycji pustego miejsca w tablicy
    if (PUSTE_POLE[0] == 0 and 'U' in TabRob):
        TabRob.remove('U')
    if (PUSTE_POLE[0] == 3 and 'D' in TabRob):
        TabRob.remove('D')
    if (PUSTE_POLE[1] == 0 and 'L' in TabRob):
        TabRob.remove('L')
    if PUSTE_POLE[1] == 3 and 'R' in TabRob:
        TabRob.remove('R')
    # wykluczenie cofania się w te same miejsca
    if (WEZEL.poprzedni_ruch == 'D' and 'U' in TabRob):
        TabRob.remove('U')
    if (WEZEL.poprzedni_ruch == 'U' and 'D' in TabRob):
        TabRob.remove('D')
    if (WEZEL.poprzedni_ruch == 'R' and 'L' in TabRob):
        TabRob.remove('L')
    if (WEZEL.poprzedni_ruch == 'L' and 'R' in TabRob):
        TabRob.remove('R')

    WEZEL.mozliwe_ruchy = TabRob


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="strategia, ruch, uklad_poczatkowy, plik_z_rozwiazaniem, plik_statystyka")
    parser.add_argument('strategia', type=str, help='DFS, BFS, A*')
    parser.add_argument('ruch', type=str, help='permutacja liter L,R,U,D lub hamm lub manh')
    parser.add_argument('uklad_poczatkowy', type=str, help='Plik wejściowy z wygenerowanym ukaładem układanki')
    parser.add_argument('plik_z_rozwiazaniem', type=str, help='Plik do którego zapisujemy rozwiązanie')
    parser.add_argument('plik_statystyka', type=str, help='Plik do statystyk z procesu obliczeniowego ')
    parametry = parser.parse_args()

    # Uruchamianie programu
    # python main.py BFS RDUL 4x4_01_00001.txt 4x4_01_00001_bfs_rdul_sol.txt 4x4_01_00001_bfs_rdul_stats.txt
    # python main.py DFS DRLU 4x4_06_00001.txt 4x4_06_00001_DFS_drlu_sol.txt 4x4_06_00001_DFS_drlu_stats.txt
    # python main.py ASTAR HAMM 4x4_01_00001.txt astr_manh_sol.txt 4astr_manh_stats.txt

    for i in parametry.ruch:
        RUCH.append(i)

    wczytaj_plik_poczatkowy()

    if parametry.strategia == 'BFS':
        tab_zwr = BFS()
        if tab_zwr[2] == -1:
            zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, -1, '')
        else:
            print(tab_zwr[0])
            zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, len(str(tab_zwr[1])), tab_zwr[1])
            zapis_do_pliku_stat(parametry.plik_statystyka, len(str(tab_zwr[1])), tab_zwr[3], tab_zwr[4], tab_zwr[5])


    elif parametry.strategia == 'DFS':
        tab_zwr = DFS()
        if tab_zwr[2] == -1:
            zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, -1, '')
        else:
            print(tab_zwr[0])
            zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, len(str(tab_zwr[1])), tab_zwr[1])
            zapis_do_pliku_stat(parametry.plik_statystyka, len(str(tab_zwr[1])), tab_zwr[3], tab_zwr[4], tab_zwr[5])


    elif parametry.strategia == 'ASTAR':
        RUCH = ['L', 'R', 'U', 'D']
        tab_zwr = ASTAR(parametry.ruch)
        if tab_zwr[2] == -1:
            zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, -1, '')
        else:
            print(tab_zwr[0])
            zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, len(str(tab_zwr[1])), tab_zwr[1])
            zapis_do_pliku_stat(parametry.plik_statystyka, len(str(tab_zwr[1])), tab_zwr[3], tab_zwr[4], tab_zwr[5])