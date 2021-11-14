import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Strategia, akronim, uklad_poczatkowy, plik_z_rozwiazaniem, plik_statystyka")
    parser.add_argument('strategia', type=str, help='DFS, BFS, A*')
    parser.add_argument('akronim', type=str, help='permutacja liter L,R,U,D lub hamm lub manh')
    parser.add_argument('uklad_poczatkowy', type=str, help='Plik wejściowy z wygenerowanym ukaładem układanki')
    parser.add_argument('plik_z_rozwiazaniem', type=str, help='Plik do którego zapisujemy rozwiązanie')
    parser.add_argument('plik_statystyka', type=str, help='Plik do statystyk z procesu obliczeniowego ')
    parametry = parser.parse_args()


    # Uruchamianie programu
    # python main.py bfs RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt
    # python main.py dfs LUDR 4x4_01_0001.txt 4x4_01_0001_dfs_ludr_sol.txt 4x4_01_0001_dfs_ludr_stats.txt
    # python main.py astr manh 4x4_01_0001.txt 4x4_01_0001_astr_manh_sol.txt 4x4_01_0001_astr_manh_stats.txt

