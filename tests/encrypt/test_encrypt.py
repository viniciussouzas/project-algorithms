from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="borboleta", key="xablau")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=2, key=1)

    assert encrypt_message("borboleta", 1) == "b_atelobro"
    assert encrypt_message("borboleta", 10) == "atelobrob"
