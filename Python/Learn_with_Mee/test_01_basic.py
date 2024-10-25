import pytest
import allure
import requests

"""
def test_addition():
    # assert - what you're verifying
    # Actual result == Expected result
    assert 1 + 1 == 2


def test_sub():
    assert 2 - 1 == 1


@pytest.mark.smoke
@allure.title("Smoke Test")
@allure.description("Verify that Test cases")
def test_sub2():
    assert 2 + 2 == 4


@pytest.mark.regression
@allure.title("Regression Test")
@allure.description("Verify that 0 == 0 ")
def test_sub3():
    assert 0 == 0


@pytest.mark.skip
@allure.title("Skip This Test")
def test_sub4():
    assert 1 + 1 == 2
"""


@allure.title("Test Get Request")
@allure.description("TC01 Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "shubham sutar")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_req_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    # print(response_data.json())
    assert response_data.status_code == 200


@allure.title("Test Get RequestL̥")
@allure.description("TC02 Verify that GET Request with invalid booking ID")
@pytest.mark.smoke
def test_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response = requests.get(url)
    assert response.status_code == 404


@allure.title("create a booking CRUD")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive():
    # to make req
    # URL
    # Method
    # Headers - Content-type = Application/json
    # Payload / Data / Body - Dict / JSON

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    # print(response.json())
    assert response.status_code == 200

