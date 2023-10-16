#===========================import================================================
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import geocoder, carrier
import requests
#==============================banner=============================================
banner="""
▒██   ██▒ ▄▄▄       ▄████▄   ██ ▄█▀▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒▒ █ █ ▒░▒████▄    ▒██▀ ▀█   ██▄█▒ ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
░░  █   ░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
 ░ █ █ ▒ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒▒ ░ ░▓ ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░░   ░▒ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
 ░    ░    ░   ▒   ░        ░ ░░ ░   ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
 ░    ░        ░  ░░ ░      ░  ░                ░ ░      ░ ░      ░  ░      ░  
                   ░                                                           
"""
print(banner)
#============================menu==================================================
menu="""
[1]пробив по номеру/punching by number     | это не релиз , а только бета версия 
                                           | по этому очень мало данных по проб-
[2]пробив по номеру(beta)                  | иву по номеру . (by Dizzzackl)
                                           |
[3]выход/exit                              |
"""
print(menu)
#============================select================================================
vibor=input("select➤")
#============================выбор 1===============================================
if vibor=='1':
    telephon = input('Введите код страны  / enter the country code ➤')
    nomer = input('введите полный номер телефона только RU/ enter the full phone number one RU ➤')
    if telephon == "+7":
        result = "ru/это русский номер"
    elif telephon == '+3':
        result = "это телефон какой-то украинской свинки/this is a Ukrainian number"
    elif telephon == '+1':
        result = "США"
    elif telephon == '+1':
        result = "Канада"
    elif telephon == '+1242':
        result = "Багамские Острова"
    elif telephon == '+1246':
        result = "Барбадос"
    elif telephon == '+375':
        result = "Белоруссия"
    elif telephon == '+375':
        result = "Белоруссия"
    elif telephon == '+998':
        result = "Узбекистан"
    elif telephon == '+996':
        result = "Киргизия"
        result = "Киргизия"
    elif telephon == '+995':
        result = "Грузия"
    elif telephon == '+994':
        result = "Азербайджан"
    elif telephon == '+993':
        result = "Туркменистан"
    elif telephon == '+992':
        result = "Таджикистан"
    elif telephon == '+7':
        result = "Казахстан"
    elif telephon == '+7840':
        result = "Абхазия"
    else:
        result = "Введен неизвестный код страны/Unknown country code entered"
        print(result)
        telephon = input('Введите код страны  /enter the country code ➤')
    # ============================оператор==========================================
    def process_number(phone_number_str):
        phone_number = phonenumbers.parse(phone_number_str, None)

        # Get the country
        country = geocoder.description_for_number(phone_number, "en")

        # Get the carrier
        oper = carrier.name_for_number(phone_number, "en")

        return country, oper


    # Test the function
    country, operator = process_number(nomer)  # You may change to your desired phone number

    timezone = timezone.time_zones_for_number(zone)

    print('Страна/country:', result ,  country ,  '\nОператор/operator:', operator ,"часовой пояс/timezone:", timezone , )
    vibor=input("select➤")
    if nomer=='skip':
        print('Страна/country:', result, country, '\nОператор/operator:', operator, "часовой пояс/timezone:",
              timezone, )
        vibor = '3'




#============================выбор 2===============================================
if vibor=='2':
    def NumVerify(api_key_num):
        clear_terminal()
        user_input = input("   Номер должен быть без '+' и пробелов\n    Введите номер ➤")

        url = f"http://apilayer.net/api/validate?access_key=3ed49c6d0b5c3b282e6281389c5461c3&number=CYB3RST4LK3R&country_code=&format=1"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                phone_number_info = response.json()

                if 'error' in phone_number_info:
                    print(f"Ошибка: {phone_number_info['error']['info']}")
                else:
                    print(f"Телефонный номер: {phone_number_info['number']}")
                    print(f"Валидность: {phone_number_info['valid']}")
                    print(f"Код страны: {phone_number_info['country_code']}")
                    print(f"Страна: {phone_number_info['country_name']}")
                    print(f"Возможная локация: {phone_number_info['location']}")
                    print(f"Оператор: {phone_number_info['carrier']}")
            else:
                print(f"Ошибка при выполнении запроса. Код состояния HTTP: {response.status_code}")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
else:
    print('эта хуйня не работает')
    vihod=input('выйти в главное меню? Y/N ➤')
    if vihod=='Y' and 'y' and 'н':
        print(banner)
        print(menu)
        vibor = input("select➤")
    if vihod=='N' and 'n' and 'т':
        input('ENTER to exit➤')
#============================выбор 3===============================================
if vibor=='3':
    input('ENTER to exit➤')


    
    
