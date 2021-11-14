import argparse



RUCH = []                   # tabela możliwych ruchów
WEZEL_AKT = []
WEZEL_ROZW = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]



def BFS():
    print('BFS')


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
                WEZEL_AKT.append(linia.split())











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
    # python main.py bfs RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt
    # python main.py dfs LUDR 4x4_01_0001.txt 4x4_01_0001_dfs_ludr_sol.txt 4x4_01_0001_dfs_ludr_stats.txt
    # python main.py astr manh 4x4_01_0001.txt 4x4_01_0001_astr_manh_sol.txt 4x4_01_0001_astr_manh_stats.txt

    for i in parametry.ruch:
        RUCH.append(i)

    wczytaj_plik_poczatkowy()

    if parametry.strategia == 'BFS':
        BFS()
    elif parametry.strategia == 'DFS':
        DFS()
    elif parametry.strategia == 'ASTAR':
        RUCH = ['L', 'U', 'R', 'D']
        ASTAR(parametry.ruch)
