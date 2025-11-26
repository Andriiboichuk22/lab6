from app.password_generator import generate_password


def test_default_length():
    password = generate_password()
    assert len(password) == 8


def test_custom_length():
    password = generate_password(length=12)
    assert len(password) == 12


def test_no_uppercase():
    password = generate_password(uppercase=False)
    assert password.lower() == password


def test_length_error():
    try:
        generate_password(0)
        assert False, "Function should raise ValueError"
    except ValueError:
        assert True
