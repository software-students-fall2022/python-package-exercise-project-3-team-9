import src.pypassgen.wisdom as wisdom


def test_generate_password():
  # Test the default case
    assert len(wisdom.generate_password(8, 0, 0, 0, 0)) == 8
