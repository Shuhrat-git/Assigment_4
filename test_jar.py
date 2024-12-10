import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12  # Default capacity should be 12
    assert jar.size == 0  # Initial size should be 0

    jar_custom = Jar(15)
    assert jar_custom.capacity == 15  # Custom capacity should match input

    with pytest.raises(ValueError):
        Jar(-1)  # Negative capacity should raise ValueError

    with pytest.raises(ValueError):
        Jar("invalid")  # Non-integer capacity should raise ValueError

def test_str():
    jar = Jar()
    assert str(jar) == "" # No cookies initially
    jar.deposit(1)
    assert str(jar) == "🍪" # Should show one cookies
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪" # Should show 12 cookies


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3  # Jar should have 3 cookies after deposit

    jar.deposit(2)
    assert jar.size == 5  # Jar should have 5 cookies (max capacity)

    with pytest.raises(ValueError):
        jar.deposit(1)  # Exceeds capacity, should raise ValueError

    with pytest.raises(ValueError):
        jar.deposit(-1)  # Negative deposit should raise ValueError

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2  # Should leave 2 cookies after withdrawal

    jar.withdraw(2)# Should show five cookies
    assert jar.size == 0  # Should leave 0 cookies

    with pytest.raises(ValueError):
        jar.withdraw(1)  # Not enough cookies, should raise ValueError

    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Negative withdrawal should raise ValueError


if __name__ == "__main__":
    pytest.main()