import pytest
import requests
from selenium import webdriver
from data import Urls
from helpers import generate_data_for_registration
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    browser.get(Urls.URL_MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture
def generate_user_data():
    data = generate_data_for_registration()
    payload = {'email': data[0], 'password': data[1], 'name': data[2]}
    return payload, data


@pytest.fixture
def generate_user_register_and_delete_by_api(generate_user_data):
    payload = generate_user_data[0]
    data = generate_user_data[1]
    requests.post(f'{Urls.URL_MAIN_PAGE + Urls.URL_CREATE_USER}', json=payload)
    registration_info = []
    registration_info.append(data[0])
    registration_info.append(data[1])
    registration_info.append(data[2])
    payload = {'email': data[0], 'password': data[1]}
    login_response = requests.post(f'{Urls.URL_MAIN_PAGE + Urls.URL_LOGIN_USER}', json=payload)
    yield registration_info
    token = login_response.json()['accessToken']
    headers = {'Authorization': token}
    requests.delete(f'{Urls.URL_MAIN_PAGE + Urls.URL_DELETE_USER}', headers=headers)


@pytest.fixture
def login(driver, generate_user_register_and_delete_by_api):
    email = generate_user_register_and_delete_by_api[0]
    password = generate_user_register_and_delete_by_api[1]
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.go_to_account_profile()
    login_page.set_user_email(email)
    login_page.set_user_password(password)
    login_page.confirm_user_authorization()
    main_page.wait_for_load_main_page()
    return driver
