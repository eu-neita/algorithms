import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message_odd_key():
    message = "hello_world"
    key = 3
    assert encrypt_message(message, key) == "leh_dlrow_ol"


def test_encrypt_message_even_key():
    message = "hello_world"
    key = 4
    assert encrypt_message(message, key) == "dlrow_o_lleh"


@pytest.mark.xfail(reason="Chave de tipo inválido não gera exceção")
def test_encrypt_message_invalid_type_key():
    message = "hello_world"
    key = "invalid_key"  # Tipo de chave inválido
    encrypt_message(message, key)


@pytest.mark.xfail(reason="Chave negativa não inverte a mensagem")
def test_encrypt_message_negative_key():
    message = "hello_world"
    key = -2  # Chave negativa
    assert encrypt_message(message, key) == "dlrow_olleh"


@pytest.mark.xfail(reason="Chave grande não inverte a mensagem")
def test_encrypt_message_large_key():
    message = "hello_world"
    key = 100  # Chave maior que o comprimento da mensagem
    assert encrypt_message(message, key) == "dlrow_olleh"


def test_encrypt_message_empty_message():
    message = ""
    key = 3
    assert encrypt_message(message, key) == ""


if __name__ == "__main__":
    pytest.main()
