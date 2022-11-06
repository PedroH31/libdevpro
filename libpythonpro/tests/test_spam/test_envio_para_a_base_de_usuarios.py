from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import Enviador_de_spam


def test_envio_de_spam(sessao):
    enviador_de_spam = Enviador_de_spam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'necromancerdoidao@Outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'

    )
