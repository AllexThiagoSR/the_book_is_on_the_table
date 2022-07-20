class User:
    from the_book_is_on_the_table.inventario import Livro

    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.__usuario = usuario
        self.__senha = senha
        self.livros = []
        self.logado = False

    @property
    def usuario(self):
        return self.__usuario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        for letra in nome:
            if letra.isnumeric():
                nome = nome.replace(letra, '')
        self._nome = nome

    def mudar_usuario(self):
        senha = input('Digite a senha antiga: ').strip()
        if senha == self.__senha:
            self.__usuario = input('Digite o novo usuário: ').strip()
        else:
            print('Senha incorreta.')

    def mudar_senha(self):
        senha = input('Digite a senha antiga: ').strip()
        if senha == self.__senha:
            self.__senha = input('Digite a nova senha: ').strip()
        else:
            print('Senha incorreta.')

    def pegar_livro(self, nome_livro, quantidade):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.quantidade += quantidade
                break
        else:
            self.livros.append(self.Livro(nome_livro, quantidade))

    def devolver_livro(self, nome_livro):
        for i in self.livros:
            if i.nome == nome_livro:
                self.livros.remove(i)
                break
        else:
            print('Não há livros para devolução.')


def empresta(users):
    with open('livros_emprestados.txt', 'w') as file:
        for user in users:
            file.write(f'{user.nome}')
            for livro in user.livros:
                file.write(f';{livro.nome}|{livro.quantidade}')
            file.write('\n')


def logar(usuario, senha, users):
    for user in users:
        if usuario == user.usuario and senha == user._User__senha:
            print('Logado com sucesso!!!')
            return [True, users.index(user)]
        elif usuario == user.usuario and senha != user._User__senh:
            print('Senha incorreta...Voltando para o menu principal.')
            return [False, '']
    else:
        print('Não há esse usuário.')
        return [False, '']


def cadastra(nome, usuario, senha):
    with open('users.txt', 'a') as file:
        file.write(f'{nome};{usuario};{senha}\n')
    return User(nome=nome, usuario=usuario, senha=senha)


def mostra_u(users):
    for i in users:
        print('=' * 50)
        print(f'{users.index(i) + 1}º - Cadastro')
        print(f'Nome: {i.nome}')
        print(f'Usuário: {i.usuario}')
        print('Livros')
        for j in i.livros:
            print('-' * 50)
            print(f'Nome: {j.nome}')
            print(f'Quantidade: {j.quantidade}')


def inicio_users():
    users = []
    with open('users.txt', 'rt+') as file:
        for i in file.readlines():
            j = i.split(';')
            users.append(User(nome=j[0], usuario=j[1], senha=j[2].replace('\n', '')))
    return users
