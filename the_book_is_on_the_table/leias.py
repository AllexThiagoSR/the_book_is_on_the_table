def leiaint(fra=''):
    while True:
        try:
            return int(input(fra).strip())
        except ValueError:
            print('\033[1;31mERRO: número inteiro inválido\033[m')
        except KeyboardInterrupt:
            print('\nInterrompido pelo usuário')
            return 0


def leiafloat(fra=''):
    while True:
        try:
            return float(input(fra).strip())
        except (ValueError, TypeError):
            print('\033[1;31mERRO: número real inválido\033[m')
        except KeyboardInterrupt:
            print('\nInterrompido pelo usuário')
            return 0.0
