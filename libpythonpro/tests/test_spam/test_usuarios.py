def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    Usuario(nome='Pedro')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Silvio'), Usuario(nome='Pedro')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    sessao.salvar(usuario)
    assert usuario == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

