import requests
import log


@log.logger
def api_call(url, *args, **kwargs):
    return requests.get(url, *args, **kwargs)


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):

        headers = {
            "email": email,
            "password": password
        }
        res = api_call(self.base_url+"api/key", headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter, content_type=None):
        headers = {"auth_key": auth_key}
        if content_type is not None:
            headers.update({"content-type": content_type})
        filter = {"filter": filter}

        res = requests.get(self.base_url+"api/pets", headers=headers, params=filter)

        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_pet(self, auth_key, name, animal_type, pet_age):
        headers = {"auth_key": auth_key}
        data = {"name": name, "animal_type": animal_type, "age": pet_age}
        res = requests.post(self.base_url + "/api/create_pet_simple", headers=headers, data=data)

        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def change_pet(self, auth_key, pet_id, name, animal_type, pet_age):
        headers = {"auth_key": auth_key}
        data = {"pet_id": pet_id, "name": name, "animal_type": animal_type, "age": pet_age}
        res = requests.put(self.base_url + f"/api/pets/{pet_id}", headers=headers, data=data)

        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        headers = {"auth_key": auth_key}
        res = requests.delete(self.base_url + f"/api/pets/{pet_id}", headers=headers)

        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
