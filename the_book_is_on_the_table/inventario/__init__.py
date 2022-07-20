class Livro:
    def __init__(self, nome, quantidade=None):
        self._nome = nome
        if quantidade is None:
            self._quantidade = 1
        else:
            self._quantidade = quantidade

    def pegar(self, q=1):
        if q <= self._quantidade:
            self._quantidade -= q
        else:
            print('Não temos estoque para isso.')

    def devolver(self, q=1):
        self._quantidade += q

    @property
    def _quantidade(self):
        return self.quantidade

    @_quantidade.setter
    def _quantidade(self, quantidade):
        if isinstance(quantidade, str):
            for i in quantidade:
                if not i.isnumeric():
                    quantidade = quantidade.replace(i, '')
        self.quantidade = int(quantidade)

    @property
    def _nome(self):
        return self.nome

    @_nome.setter
    def _nome(self, nome):
        self.nome = nome.strip().title()


def mostrar_inv(livros):
    print('-' * 50)
    print(f'No. {"Nome":<43}{"Qt.":>3}')
    print('-' * 50)
    if len(livros) == 0:
        print('Sem livros para devolução.')
    else:
        for j, i in enumerate(livros):
            print(f'{j} - {i._nome:.<43}{i._quantidade:>3}')
    print('-' * 50)


def atualiza(livros):
    with open('../livros.txt', 'w') as file:
        for i in livros:
            file.write(f'{i.nome};{i.quantidade}\n')


def menu(q, title, *options):
    print('=' * q)
    print(title)
    print('=' * q)
    for i in options:
        print(f'{options.index(i) + 1} - {i}')


def inicio_livros():
    livros = []
    with open('livros.txt', 'rt+') as file:
        for i in file.readlines():
            j = i.split(';')
            livros.append(Livro(j[0], int(j[1])))
    return livros


if __name__ == "__main__":
    livro = Livro('contos de uma criatura carente', '13 unidades')
    print(livro._nome)
    print(livro._quantidade)
