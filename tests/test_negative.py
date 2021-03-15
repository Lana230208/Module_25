from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_empty_user():
    status, result = pf.get_api_key("", None)
    assert status == 403


def test_get_api_key_for_invalid_user():
    status, result = pf.get_api_key("&&&&", "////")
    assert status == 403


def test_get_all_pets_with_invalid_key(filter=""):
    auth_key = "invalid key"
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403


def test_add_pet_with_wrong_name():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    name = ""
    animal_type = "dog"
    pet_age = 3
    status, result = pf.add_pet(auth_key, name, animal_type, pet_age)
    assert status == 200  # 400 Обнаружена уязвимость. Можно передавать неверные параметры.


def test_add_pet_with_wrong_animal_type():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    name = "Vasya"
    animal_type = ""
    pet_age = -5,5
    status, result = pf.add_pet(auth_key, name, animal_type, pet_age)
    assert status == 200  # 400 Обнаружена уязвимость. Можно передавать неверные параметры.

def test_change_pet_with_wrong_animal_type():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    pet_id = "856f6dd5-31b8-467d-b3ad-b48aefff5a82"
    name = "Vasya"
    animal_type = ""
    pet_age = -2
    status, result = pf.change_pet(auth_key, pet_id, name, animal_type, pet_age)
    assert status == 400


def test_delete_pet_with_wrong_pet_id():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    pet_id = "856f6dd5-31b8-467d"
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200


def test_get_all_pets_with_invalid_content_type(filter=""):
    content_type = "application/xml; application/x-www-form-urlencoded; application/form-data; text/plain"
    auth_key = "invalid key"
    status, result = pf.get_list_of_pets(auth_key, filter, content_type=content_type)
    assert status == 403
    