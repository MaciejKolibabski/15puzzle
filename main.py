import argparse

RUCH = []  # tabela możliwych ruchów- L U R D
WEZEL_POCZ = []
WEZEL_ROZW = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
PUSTE_POLE = [9,9]

class Node:
    def __init__(self, aktualna_tablica, rodzic, sciezka, poprzedni_ruch):
        self.tablica = aktualna_tablica
        if rodzic != "root":
            self.rodzic = rodzic
        self.dzieci = {}
        self.sciezka = sciezka + poprzedni_ruch
        # self.sciezka.append(poprzedni_ruch)
        self.mozliwe_ruchy = RUCH.copy()
        self.poprzedni_ruch = poprzedni_ruch

        #ustal_puste_pole(self)
        #ustal_mozliwe_ruchy(self)


    def nowy_potomek(self, tab, kierunek):
        nowedziecko=Node(tab, self, self.sciezka ,kierunek)
        #ustal_mozliwe_ruchy(nowedziecko)
        self.dzieci[kierunek] = nowedziecko


    def przesun_puste_pole(self,kierunek):
        # WEZEL.tablica[PUSTE_POLE[0]][PUSTE_POLE[1]] - miejsce 0 w tablicy
        ntablica=[]
        for row in self.tablica:
            ntablica.append(row.copy())


        if (kierunek == 'L'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] - 1]
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] - 1] = '0'
            #PUSTE_POLE[1] -= 1

        if (kierunek == 'R'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] + 1]
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1] + 1] = '0'
            #PUSTE_POLE[1] += 1

        if (kierunek == 'U'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0] - 1][PUSTE_POLE[1]]
            ntablica[PUSTE_POLE[0] - 1][PUSTE_POLE[1]] = '0'
            #PUSTE_POLE[0] -= 1

        if (kierunek == 'D'):
            ntablica[PUSTE_POLE[0]][PUSTE_POLE[1]] = ntablica[PUSTE_POLE[0] + 1][PUSTE_POLE[1]]
            ntablica[PUSTE_POLE[0] + 1][PUSTE_POLE[1]] = '0'
            #PUSTE_POLE[0] += 1

        self.nowy_potomek(ntablica, kierunek)



def czy_gotowe(rw, rozw):
    for i in range(len(rw)) :
        for j in range(len(rw)) :
            if rw[i][j] != rozw[i][j] :
                return False
    return True



def BFS():
    AKT_WEZEL = Node(WEZEL_POCZ,'Root','','')
    kolejka = []
    kolejka.append(AKT_WEZEL)
    licz=0
    while True:
        licz+=1
        AKT_WEZEL = kolejka[0]
        ustal_puste_pole(AKT_WEZEL)
        #print('LEN3: ', len(kolejka),PUSTE_POLE,AKT_WEZEL.mozliwe_ruchy)
        ustal_mozliwe_ruchy(AKT_WEZEL)
        #print('LEN3: ', len(kolejka), PUSTE_POLE)
        #print(AKT_WEZEL.tablica, 'tab')
        print(AKT_WEZEL.tablica, 'Licznik: ' ,licz, PUSTE_POLE,AKT_WEZEL.sciezka,AKT_WEZEL.mozliwe_ruchy,PUSTE_POLE)
        if czy_gotowe(AKT_WEZEL.tablica,WEZEL_ROZW):
            return 'Rozwiązane poprawnie', AKT_WEZEL.tablica
        for element in AKT_WEZEL.mozliwe_ruchy:
            AKT_WEZEL.przesun_puste_pole(element)
            NOWY_WEZEL = AKT_WEZEL.dzieci[element]
            #print('_____n_', NOWY_WEZEL.tablica)
            kolejka.append(NOWY_WEZEL)
        kolejka.remove(AKT_WEZEL)

        zapis_do_pliku_rozw(parametry.plik_z_rozwiazaniem, str(AKT_WEZEL.sciezka), AKT_WEZEL.sciezka)



def zapis_do_pliku_rozw(plik, dlugosc_rozw, pokonane_ruchy):
    file = open(plik, 'w+')
    file.write(str(len(dlugosc_rozw)))
    file.write('\n')
    file.write(str(pokonane_ruchy))
    file.close()





def DFS():
    print('DFS')


def ASTAR(wybor):
    print('ASTAR : ' + wybor)


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
    for i in range(len(WEZEL.tablica)) :
        for j in range(len(WEZEL.tablica[i])) :
            if WEZEL.tablica[i][j] == '0' :
                PUSTE_POLE[0] = i     #współrzędne pustego pola
                PUSTE_POLE[1] = j


def ustal_mozliwe_ruchy(WEZEL):

    TabRob = WEZEL.mozliwe_ruchy  # ['L','R','U','D']
    #TabRob = RUCH  # ['L','R','U','D']
    #print('umr___',TabRob)

    #możliwości ruchu w zaleności od pozycji pustego miejsca w tablicy
    if (PUSTE_POLE[0] == 0 and 'U' in TabRob) :
        TabRob.remove('U')
    if (PUSTE_POLE[0] == 3 and 'D' in TabRob):
        TabRob.remove('D')
    if (PUSTE_POLE[1] == 0 and 'L' in TabRob):
        TabRob.remove('L')
    if (PUSTE_POLE[1] == 3 and 'R' in TabRob):
        TabRob.remove('R')
    #wykluczenie cofania się w te same miejsca
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
    # python main.py BFS RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt
    # python main.py DFS LUDR 4x4_01_0001.txt 4x4_01_0001_dfs_ludr_sol.txt 4x4_01_0001_dfs_ludr_stats.txt
    # python main.py ASTR manh 4x4_01_0001.txt 4x4_01_0001_astr_manh_sol.txt 4x4_01_0001_astr_manh_stats.txt

    for i in parametry.ruch:
        RUCH.append(i)

    wczytaj_plik_poczatkowy()

    if parametry.strategia == 'BFS':
        print(BFS())

    elif parametry.strategia == 'DFS':
        DFS()
    elif parametry.strategia == 'ASTAR':
        RUCH = ['L', 'U', 'R', 'D']
        ASTAR(parametry.ruch)
