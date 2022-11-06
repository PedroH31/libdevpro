class Enviador:
    def enviar(cls, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido. {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass
