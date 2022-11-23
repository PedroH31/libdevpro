from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Pedro', email='necromancerdoidao@outlook.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Pedro', email='necromancerdoidao@outlook.com'),
        Usuario(nome='Silvio', email='silvio@python.pro.br')
                ]

    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
