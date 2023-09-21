import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message_odd_key():
    message = "hello_world"
    key = 3
    assert encrypt_message(message, key) == "wor_olldleh"


def test_encrypt_message_even_key():
    message = "hello_world"
    key = 4
    assert encrypt_message(message, key) == "olleh_dlrow"


def test_encrypt_message_invalid_type_key():
    message = "hello_world"
    key = "invalid_key"  # Tipo de chave inválido
    with pytest.raises(TypeError):
        encrypt_message(message, key)


def test_encrypt_message_negative_key():
    message = "hello_world"
    key = -2  # Chave negativa
    assert encrypt_message(message, key) == "dlrow_olleh"


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
