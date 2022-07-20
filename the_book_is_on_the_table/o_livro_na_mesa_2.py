from leias import leiaint
from user import empresta, logar, cadastra, inicio_users  # , mostra_u
from inventario import Livro, mostrar_inv, atualiza, menu, inicio_livros

li = None
logado = [False, '']
livros = inicio_livros()
users = inicio_users()
with open('livros_emprestados.txt', 'rt+') as file:
    for empres in file.readlines():
        j = empres.split(';')
        for k in j[1:]:
            for user in users:
                if user.nome == j[0]:
                    user.pegar_livro(nome_livro=k.split('|')[0], quantidade=int(k.split('|')[1]))
                    break
usar = [i.usuario for i in users]
while True:
    menu(100, 'Menu principal', 'Login', 'Cadastrar', 'Cadastrar livro', 'sair')
    op = leiaint('O que deseja fazer? ')
    print('-' * 100)
    if op == 1:
        u = input('Usuário: ').strip()
        s = input('Senha: ').strip()
        logado = logar(u, s, users)
        if not logado[0] and u not in usar:
            c = input('Fazer cadastro? [s/n]').strip().upper()[0]
            op = 2 if c == 'S' else op
            print('-' * 50 if c == 'S' else '', end='')
            print()
    if op == 2:
        print('Criar cadastro: ')
        print('-' * 50)
        nome = input('Nome: ').strip().title()
        u = input('Usuário: ').strip()
        if u not in usar:
            while True:
                s = input('Senha: ').strip()
                s1 = input('Digite a senha novamente: ').strip()
                if s == s1:
                    users.append(cadastra(nome=nome, usuario=u, senha=s1))
                    usar.append(u)
                    break
                print('Senhas não coincidem. Tente novamente.')
                print()
            print('Cadastro concluído.')
        else:
            print('Usuário já existente.')
    elif op == 3:
        print('Adicionar um livro ao acervo.')
        print('-' * 50)
        nome = input('Qual o nome do livro? ').strip().title()
        s = leiaint('Quantos exemplares há? ')
        livros.append(Livro(nome, s))
        atualiza(livros)
    elif op == 4:
        print('Saindo')
        break
    while logado[0]:
        print('=' * 50)
        print(f'Usuário logado atualmente: {users[logado[1]].usuario}')
        menu(50, 'Menu de ações', 'Saída de livros', 'Devoluções', 'Deslogar')
        op = leiaint('O que deseja fazer? ')
        print('=' * 50)
        if op == 1:
            while True:
                mostrar_inv(livros)
                print('Digite 999 se não for pegar mais nenhum livro.')
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
                    users[logado[1]].pegar_livro(livros[esc].nome, q)
                    atualiza(livros)
                    empresta(users)
                    print(f'{q} unidade(s) do livro "{livros[esc].nome}" emprestadas com sucesso.')
        elif op == 2:
            while True:
                print('-' * 50)
                print('Livros pegos por esse usuário')
                mostrar_inv(users[logado[1]].livros)
                if len(users[logado[1]].livros) <= 0:
                    break
                print('Digite 999 se não for devolver mais nenhum livro.')
                esc = leiaint('Qual o nome do livros que deseja devolver(No.)? ')
                if esc == 999:
                    break
                if esc > len(users[logado[1]].livros):
                    print('Não há essa opção.')
                    continue
                li = users[logado[1]].livros[esc].nome
                for livro in livros:
                    if livro.nome == li:
                        livro.devolver(users[logado[1]].livros[esc].quantidade)
                        users[logado[1]].devolver_livro(users[logado[1]].livros[esc].nome)
                        atualiza(livros)
                        empresta(users)
                        print(f'"{li}", Devolvido')
        elif op == 3:
            print('Voltando para o menu principal')
            logado[0] = False
