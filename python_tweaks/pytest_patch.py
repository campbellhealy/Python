import secrets


def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'


def test_gen_key(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeefd'}"


print(gen_token)
