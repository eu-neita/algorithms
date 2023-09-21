import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    """tests encrypt_message"""
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("hello_world", "invalid_key")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 12)

    assert encrypt_message("hello_world", 4) == "dlrow_o_lleh"

    assert encrypt_message("hello_world", 3) == "leh_dlrow_ol"

    assert encrypt_message("abc", 100) == "cba"
