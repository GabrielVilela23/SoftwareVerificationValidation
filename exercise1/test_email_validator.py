from email_validator import is_valid_email

def test_valid_email():
    assert is_valid_email("usuario@example.com")
    assert is_valid_email("nome.sobrenome@dominio.com")
    assert is_valid_email("user123@site.net")

def test_invalid_email():
    assert not is_valid_email("usuarioexample.com")     # faltando @
    assert not is_valid_email("usuario@")               # faltando domínio
    assert not is_valid_email("@dominio.com")           # faltando nome
    assert not is_valid_email("usuario@dominio")        # faltando ponto no domínio
    assert not is_valid_email("")                       # string vazia
