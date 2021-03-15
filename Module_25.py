from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://petfriends1.herokuapp.com/login")

login = driver.find_element_by_xpath('//*[@id="email"]')
login.send_keys("office@jakera.com.ua")

password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("ASDfg230208")

button = driver.find_element_by_xpath('//form/div[3]/button')
button.click()

driver.get("http://petfriends1.herokuapp.com/my_pets")

my_pets_count = driver.find_element_by_xpath('//div[1]/div/div[1]')
# Забираем вторую строку, поэтому разделяем по переносам строк(\n)
my_pets_count_text = my_pets_count.text.split('\n')[1]
# Берём второе от пробела слово (количество животных)
my_pets_count = int(my_pets_count_text.split(' ')[1])
print(my_pets_count)

my_pets_names = driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')


if len(my_pets_names) == my_pets_count:
     print("Присутствуют все питомцы")

my_pets_images = driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/th/img')
if len(my_pets_images) >= my_pets_count//2:
     print("Хотя бы у половины питомцев есть фото")

my_pets_ages = driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

my_pets_rasas = driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[2]')


has_names, has_ages, has_rasas = True, True, True
pet_names = []
pets = {}
copy_count = 0
for name, age, rasa in zip(my_pets_names, my_pets_ages, my_pets_rasas):
     pet_name = name.text.strip()
     pet_age = age.text.strip()
     pet_rasa = rasa.text.strip()

     pet_copy = pets.get(pet_name)
     if pet_copy is not None:
          if pet_copy[0] == pet_age and pet_copy[1] == pet_rasa:
               copy_count += 1

     pet_names.append(pet_name)
     pets[pet_name] = [pet_age, pet_rasa]
     if len(name.text) == 0: # Если нет имени
          has_names = False
     if len(age.text) == 0: # Если нет возраста
          has_ages = False
     if len(rasa.text) == 0: # Если нет породы
          has_rasas = False
if has_names and has_ages and has_rasas:
     print("У всех питомцев есть имя и возраст и порода")

unique_names = set(pet_names)
if len(unique_names) == len(pet_names):
     print("У всех питомцев разные имена")

if copy_count == 0:
     print("В списке нет повторяющихся питомцев.")
else:
     print("В списке {} повторяющихся питомцев.".format(copy_count))
