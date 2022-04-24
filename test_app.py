from app import home


def test_home():
    assert 100 == home().shape[0]
