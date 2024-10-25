# fixture concept in python
# You can use fixture
# context to the test
# similar - pre condition , post conditions
import pytest

# Pre Condition - Token, booking Id -Fixture
# test_Update_negative 1
# test_Update_positive 2
"""
@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    if is_married == True:
        print("You are Married")
"""


@pytest.fixture()
def sample_data():
    data = [1, 2, 4, 5, 6, 7, 8]
    return data


@pytest.fixture()
def sample_data2():
    return True


def test_consume_data1_2(sample_data, sample_data2):
    print(sample_data)
    print(sample_data2)
