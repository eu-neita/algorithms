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


def test_encrypt_message_invalid_type():
    message = 123
    key = 3
    with pytest.raises(TypeError):
        encrypt_message(message, key)


def test_encrypt_message_negative_key():
    message = "hello_world"
    key = -2
    assert encrypt_message(message, key) == "dlrow_olleh"


def test_encrypt_message_large_key():
    message = "hello_world"
    key = 100
    assert encrypt_message(message, key) == "dlrow_olleh"


def test_encrypt_message_empty_message():
    message = ""
    key = 3
    assert encrypt_message(message, key) == ""


if __name__ == "__main__":
    pytest.main()
