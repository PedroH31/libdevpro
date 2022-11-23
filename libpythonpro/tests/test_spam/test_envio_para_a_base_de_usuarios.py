import pytest as pytest
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import Enviador_de_spam
from libpythonpro.spam.modelos import Usuario
from unittest.mock import Mock


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Pedro', email='necromancerdoidao@outlook.com'),
            Usuario(nome='Silvio', email='silvio@python.pro.br')
        ],
        [

        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = Enviador_de_spam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'necromancerdoidao@Outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Pedro', email='necromancerdoidao@outlook.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = Enviador_de_spam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'silvio@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    enviador.enviar.assert_called_once_with(
        'silvio@python.pro.br',
        'necromancerdoidao@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
