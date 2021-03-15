from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result


def test_get_all_pets_with_valid_key(filter=""):
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0


def test_pet_api():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result
    auth_key = result["key"]
    name = "Vasya"
    animal_type = "dog"
    pet_age = 3
    status, result = pf.add_pet(auth_key, name, animal_type, pet_age)
    assert status == 200
    assert "id" in result
    pet_id = result["id"]
    assert len(pet_id) > 0

    status, result = pf.change_pet(auth_key, pet_id, name, animal_type, pet_age)
    assert status == 200

    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200
