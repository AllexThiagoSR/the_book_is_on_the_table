from leias import leiaint
from user import User, empresta
from inventario import Livro, mostrar_inv, atualiza

users = []
livros = []
li = 0
with open('livros.txt', 'rt+') as file:
    for i in file.readlines():
        j = i.split(';')
        livros.append(Livro(j[0], int(j[1])))
with open('users.txt', 'rt+') as file:
    for i in file.readlines():
        j = i.split(';')
        users.append(User(nome=j[0], usuario=j[1], senha=j[2].replace('\n', '')))
with open('livros_emprestados.txt', 'rt+') as file:
    for empres in file.readlines():
        j = empres.split(';')
        for k in j[1:]:
            for user in users:
                if user.nome == j[0]:
                    user.pegar_livro(nome_livro=k.split('|')[0], quantidade=int(k.split('|')[1]))
                    break
while True:
    print('1 - Saída de livros\n2 - Devoluções\n3 - Cadastrar Usuário\n4 - Cadastrar livro\n5 - Sair')
    op = leiaint('O que deseja fazer? ')
    print('=' * 50)
    if op == 1:
        print('Login')
        u = input('Usuário: ').strip()
        s = input('Senha: ').strip()
        for user in users:
            if u == user.usuario and s == user.senha:
                print('Logado com sucesso.')
                while True:
                    mostrar_inv(livros)
                    print('999 se não for pegar mais nenhum livro.')
                    esc = leiaint('Qual livro deseja pegar(No.)? ')
                    if esc == 999:
                        break
                    try:
                        li = livros[esc].quantidade
                    except IndexError:
                        print('Não há essa opção.')
                        continue
                    q = leiaint('Quantos deseja pegar? ')
                    livros[esc].pegar(q)
                    if q <= li:
                        user.pegar_livro(livros[esc].nome, q)
                        atualiza(livros)
                        empresta(users)
                        print(f'{q} unidade(s) do livro {livros[esc].nome} emprestadas com sucesso.')
                break
            elif u == user.usuario and s != user.senha:
                print('Senha incorreta.')
                break
        else:
            print('Usuário não encontrado.')
            c = input('Criar um usuário? [s/n] ').strip().upper()[0]
            op = 3 if c == 'S' else op
    elif op == 2:
        print('Login')
        u = input('Usuário: ').strip()
        s = input('Senha: ').strip()
        for user in users:
            if u == user.usuario and s == user.senha:
                print('Logado com sucesso.')
                while True:
                    mostrar_inv(livros)
                    print('999 se não for devolver mais nenhum livro.')
                    esc = leiaint('Qual o nome do livros que deseja devolver(No.)? ')
                    if esc == 999:
                        break
                    try:
                        li = livros[esc].nome
                    except IndexError:
                        print('Não há essa opção.')
                        continue
                    for livro in user.livros:
                        if livro.nome == li:
                            livros[esc].devolver(livro.quantidade)
                            user.devolver_livro(livros[esc].nome)
                            atualiza(livros)
                            empresta(users)
                            print(livros[esc].nome, 'Devolvido')
                            break
                    else:
                        print('Esse usuário não pegou esse livro.')
                break
            elif u == user.usuario and s != user.senha:
                print('Senha incorreta.')
                break
        else:
            print('Usuário não encontrado.')
            c = input('Criar um usuário? [s/n] ').strip().upper()[0]
            op = 3 if c == 'S' else op
    if op == 3:
        print('Criar cadastro: ')
        nome = input('Nome: ').strip().title()
        u = input('Usuário: ').strip()
        while True:
            s = input('Senha: ').strip()
            s1 = input('Digite a senha novamente: ').strip()
            if s == s1:
                users.append(User(nome=nome, usuario=u, senha=s1))
                with open('users.txt', 'a') as file:
                    file.write(f'{nome};{u};{s1}\n')
                break
            print('Senhas não coincidem. Tente novamente.')
            print()
        print('Cadastro concluído.')
    elif op == 4:
        print('Adicionar um livro ao acervo.')
        nome = input('Qual o nome do livro? ').strip().title()
        s = leiaint('Quantos exemplares há? ')
        livros.append(Livro(nome, s))
        atualiza(livros)
    elif op == 5:
        print('Saindo')
        break
    print('=' * 50)
atualiza(livros)
empresta(users)
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
