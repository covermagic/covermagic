import time
import os
import requests
import webbrowser
import subprocess
import sys
from pystyle import Colorate, Colors, Write, Anime, Center
import faker
import random
import string
import csv


def clear_console():
    """Очистить консоль"""
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def display_license_agreement():
    """Вывести лицензионное соглашение"""
    clear_console()
    license_text = """
    Лицензионное соглашение

    Продолжая использовать данный код, вы соглашаетесь со следующими условиями:

    1. Автор данного программного обеспечения не несет ответственности за любые последствия,
       которые могут возникнуть в результате использования данного кода. Вы используете его на свой собственный риск.

    2. Этот код предназначен для образовательных целей и не должен использоваться для любых незаконных действий.

    3. Все действия, предпринятые с использованием этого программного обеспечения, должны соответствовать 
       действующему законодательству вашей страны.

    4. Запрещается распространять данный код без указания авторства и лицензий. Убедитесь, что вы 
       не нарушаете права третьих лиц.

    5. Вы несете личную ответственность за любые действия, осуществляемые с помощью этого кода, и
       обязуетесь соблюдать все применимые законы и правила.

    Если вы понимаете и принимаете все условия выше, нажмите Enter для продолжения использования.
    Если вы не согласны, закройте данное приложение.

    НАЖМИТЕ ENTER ЕСЛИ ВЫ СОГЛАСНЫ
    """
    Write.Print(license_text.strip(), Colors.red_to_white, interval=0.0001)
    input()


def search_in_files(query, files):
    results = []
    for file in files:
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8-sig', errors='ignore') as f:
                    if file.endswith('.csv'):
                        csv.field_size_limit(10 * 1024 * 1024)
                        reader = csv.DictReader(f)
                        for row in reader:
                            if any(query in str(value) for value in row.values() if value is not None):
                                results.append((file, row))
                                if len(results) >= 10000:
                                    return results
                    else:
                        for line in f:
                            if query in line:
                                results.append((file, line.strip()))
                                if len(results) >= 1000000:
                                    return results
            except Exception as e:
                print(f"Ошибка при чтении файла {file}: {e}")
    return results


def print_menu():
    menu = Colorate.Vertical(Colors.blue_to_red, f"""

                                   +&                            +&&x         
                              X.    &&&$                      +&&&&&.         
                               +     $&&&&+                 :&&&&&&X          
                               x&     &&&&&&+              :&&&&&&$           
                                  X&    &&&&&&             &&&&&&     +       
                                 x&$&x    X&&&&+          +&&$       :;       
                                  x$&X&X       &:        :.         $.x       
                                   +;&& X&                     ..X$:&::       
                                   +:x&$+  :                 . $&&&X;.        
                                   .++.&&$x X +          :;X  &&&&+.          
                                   . : &&&&&&+: . $    ; & ;&&&&x;&+          
                                   .  +$X.&&&&&&x &+$  &:&&&&&;; &.           
                                        + X:$&&&&&&&&&&&&&&&$; +              
                                          &;x+$&&&&&&&&&&&&$::;               
                                          $:+X &x &&&&&.$ $ ;+                
                                               &$ x $   :                     
                                               .&.:                       

                █████╗ ██████╗  █████╗ ████████╗██╗  ██╗██╗   ██╗    ██╗   ██╗██████╗ 
               ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║╚██╗ ██╔╝    ██║   ██║╚════██╗
               ███████║██████╔╝███████║   ██║   ███████║ ╚████╔╝     ██║   ██║ █████╔╝
               ██╔══██║██╔═══╝ ██╔══██║   ██║   ██╔══██║  ╚██╔╝      ╚██╗ ██╔╝██╔═══╝ 
               ██║  ██║██║     ██║  ██║   ██║   ██║  ██║   ██║        ╚████╔╝ ███████╗
               ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝         ╚═══╝  ╚══════╝

                                             Главное меню
     ╔══════════════════════════╦══════════════════════════════════╦═══════════════════════════╗      
     ║         SEARCH           ║        Author : @Fell1ksx        ║        ГЕНЕРАТОРЫ         ║
╔════╩══════════════════════════╩═══════════════╗   ╔══════════════╩═══════════════════════════╬════╗   
║ [1] Начать поиск                              ║   ║ [7] Сгенерировать пароль                 ║ V2 ║  
║ [2] Поиск по IP                               ║   ║ [8] Сгенерировать стих                   ╚════╣
║ [3] Поиск по почте                            ║   ║ [9] Сгенерировать цитаты                      ║
║ [4] Сократить ссылку                          ║   ║ [10] ВАЖНО ПРОЧИТАТЬ                          ║
║ [5] Скинуть копеечку автору <3                ║   ║ [11] Добавить свою базу                       ║
║ [6] Создать новую личность                    ║   ║ [12] Soon....                                 ║
╚════════════════════════════════╦══════════════╩═══╩══════════════╦════════════════════════════════╝
                                 ║                                 ║        
                                 ║           [0] ВЫХОД             ║        
                                 ║                                 ║        
                                 ╚═════════════════════════════════╝                
""")
    print(menu)


def check_ip(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_email_info(email):
    try:
        username, domain = email.split('@')
        email_services = {
            "gmail.com": "Google (Gmail)",
            "yahoo.com": "Yahoo Mail",
            "hotmail.com": "Microsoft (Hotmail)",
            "outlook.com": "Microsoft (Outlook)",
            "mail.ru": "Mail.ru",
            "yandex.ru": "Yandex.Mail"
        }
        service_name = email_services.get(domain, "Неизвестный почтовый сервис")
        print("Данные о почте:")
        print(f"Имя почты: {username}")
        print(f"Домен: {domain}")
        print(f"Сайт: {service_name}")
    except ValueError:
        print("Неверный формат E-mail.")


def shorten_url(long_url):
    url = 'http://tinyurl.com/api-create.php'
    params = {'url': long_url}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        shortened_link = response.text
        return shortened_link
    else:
        print('Ошибка при сокращении ссылки.')


def generate_fake_data(num_persons):
    fake = faker.Faker('ru_RU')
    generated_data = []
    with open('Incognits.txt', 'w', encoding='utf-8') as file:
        for _ in range(num_persons):
            fake_name = fake.name()
            fake_gender = fake.random_element(elements=('Мужчина', 'Женщина'))
            fake_address = fake.address()
            fake_email = fake.email()
            fake_phone = fake.phone_number()
            fake_job = fake.job()
            fake_company = fake.company()
            fake_birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
            fake_ssn = fake.ssn()
            fake_username = fake.user_name()
            fake_password = fake.password()
            fake_credit_card = fake.credit_card_full()
            fake_ip = fake.ipv4()
            fake_country = fake.country()
            fake_city = fake.city()

            data_entry = {
                "Имя": fake_name,
                "Пол": fake_gender,
                "Адрес": fake_address,
                "Email": fake_email,
                "Телефон": fake_phone,
                "Профессия": fake_job,
                "Компания": fake_company,
                "Дата рождения": fake_birthdate,
                "Социальный номер": fake_ssn,
                "Имя пользователя": fake_username,
                "Пароль": fake_password,
                "Кредитная карта": fake_credit_card,
                "IP адрес": fake_ip,
                "Страна": fake_country,
                "Город": fake_city,
            }
            generated_data.append(data_entry)

            file.write(f"Имя: {fake_name}\n")
            file.write(f"Пол: {fake_gender}\n")
            file.write(f"Адрес: {fake_address}\n")
            file.write(f"Email: {fake_email}\n")
            file.write(f"Телефон: {fake_phone}\n")
            file.write(f"Профессия: {fake_job}\n")
            file.write(f"Компания: {fake_company}\n")
            file.write(f"Дата рождения: {fake_birthdate}\n")
            file.write(f"Социальный номер: {fake_ssn}\n")
            file.write(f"Имя пользователя: {fake_username}\n")
            file.write(f"Пароль: {fake_password}\n")
            file.write(f"Кредитная карта: {fake_credit_card}\n")
            file.write(f"IP адрес: {fake_ip}\n")
            file.write(f"Страна: {fake_country}\n")
            file.write(f"Город: {fake_city}\n")
            file.write("\n\n")

    if num_persons <= 100:
        for data in generated_data:
            for key, value in data.items():
                Write.Print(f"{key}: {value}", Colors.blue_to_white, interval=0.0001)
                print()
            print()
        print()
        Write.Print("Личности сгенерированы и сохранены в файл Incognits.txt.", Colors.blue_to_white, interval=0.0001)


def create_new_identity():
    clear_console()
    Write.Print("Создание новой личности...", Colors.green_to_blue, interval=0.0001)
    num_persons = 1
    generate_fake_data(num_persons)
    Write.Print("\nНовая личность сгенерирована и сохранена в файл Incognits.txt.", Colors.green_to_blue,
                interval=0.0001)
    Write.Print("\nНажмите Enter, чтобы вернуться в меню...", Colors.green_to_blue, interval=0.0001)
    input()


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password_menu():
    clear_console()
    Write.Print("Генерация пароля...", Colors.green_to_blue, interval=0.0001)
    length_input = input("Укажите длину пароля (по умолчанию 12): ")
    length = 12
    if length_input.isdigit():
        length = int(length_input)

    password = generate_password(length)
    Write.Print(f"Сгенерированный пароль: {password}", Colors.green_to_blue, interval=0.0001)
    Write.Print("\nНажмите Enter, чтобы вернуться в меню...", Colors.green_to_blue, interval=0.0001)
    input()


def generate_poem():
    clear_console()
    Write.Print("Выберите тип стихотворения:", Colors.green_to_blue, interval=0.0001)
    Write.Print("[1] Любовный", Colors.green_to_blue, interval=0.0001)
    Write.Print("[2] Смешной", Colors.green_to_blue, interval=0.0001)

    choice = input("Ваш выбор: ")

    if choice == '1':
        poems = [
            "Ты — моя утренняя заря,\nНаполняешь жизнь теплом.\nС тобой каждый миг — как праздник,\nНапоминание о том, что я дома.\n"
        ]
        poem = random.choice(poems)

    elif choice == '2':
        poems = [
            "На завтрак съел я три пирога,\nА потом подумал: 'Что за ерунда?'\nШкаф открываю — там кукуруза,\nУпс, кто не знал? Это просто каша!\n"
        ]
        poem = random.choice(poems)

    else:
        Write.Print("Некорректный выбор. Попробуйте снова.", Colors.red_to_white, interval=0.0001)
        input("Нажмите Enter, чтобы вернуться в меню.")
        return

    Write.Print("Сгенерированное стихотворение:\n", Colors.green_to_blue, interval=0.0001)
    Write.Print(poem, Colors.green_to_blue, interval=0.0001)
    Write.Print("\nНажмите Enter, чтобы вернуться в меню...", Colors.green_to_blue, interval=0.0001)
    input()


def generate_quote():
    quotes = [
        "Жизнь — это не ожидание штормов, а умение танцевать под дождём.",
        "Тем, кто не рискует, приходится довольствоваться тем, что у них есть.",
        "Секрет успеха в том, чтобы начать.",
        "Не бойтесь провалов. Бойтесь того, что вы не попробуете.",
        "Мечтайте как будто у вас вся жизнь впереди. Живите как будто это ваш последний день.",
        "Не важно, что вы делаете, главное — делать это с любовью.",
        "Каждый день — это новая возможность изменить свою жизнь.",
        "Самое большое богатство человека — это его здоровье.",
        "Вы — архитектор своей судьбы.",
        "Будьте изменением, которое хотите видеть в мире.",

    ]
    return random.choice(quotes)


def generate_quote_menu():
    clear_console()
    Write.Print("Генерация цитаты...", Colors.green_to_blue, interval=0.0001)

    quotes = generate_quote()

    Write.Print(f"Сгенерированная цитата: {quotes}", Colors.green_to_blue, interval=0.0001)
    Write.Print("\nНажмите Enter, чтобы вернуться в меню...", Colors.green_to_blue, interval=0.0001)
    input()


def display_readme():
    clear_console()
    readme_text = """
                Введение                               Цели и назначения
        Описание и Правовые аспекты     Основные функции данного программного обеспечения

        заключаются в обучении             Создатель данного программного обеспечения
        пользователей основам работы       не несет ответственности за действия пользователей,
        с компьютерными технологиями,      которые могут неуместно использовать функциональность
        демонстрации принципов             приложения. Все инструменты и возможности,
        кодирования и разработки           предлагаемые программным обеспечением, должны
        программ. Это приложение           использоваться строго в рамках закона и с соблюдением
        может также использоваться          правовых норм.
        для иллюстрации возможностей       
        программирования как на уровне    
        базовых операций, так и более  
        сложных алгоритмов.                      Это выражается в следующем:

                                           Лицензионное соглашение: Перед использованием
                                           пользователям будет предложено ознакомиться с
                                           лицензионным соглашением, в котором среди прочего
                                           подчеркивается, что приложение не предназначено
                                           для выполнения незаконных действий.

     Важность законного использования             Ответственность пользователей

    Пользователи, взаимодействующие с            Каждый пользователь имеет право 
    данным программным обеспечением,            и обязанность действовать добросовестно 
    должны понимать, что любые                 и ответственно. Использование 
    неправомерные действия, предпринятые        данного программного обеспечения 
    с использованием этого приложения,           должно быть направлено на достижение 
    будут иметь правовые последствия.           образовательных и профессиональных целей. 
    Незаконные действия могут включать,         При этом необходимы: 
    но не ограничиваться:                       Этические нормы: Пользователи обязаны 
                                                 следовать этическим нормам, избегать 
                                                 действий, которые могут нанести ущерб 
                                                 другим лицам или организациям. 
                                                 Знание законодательства: Важно, чтобы 
                                                 пользователи были в курсе законов своей 
                                                 страны и международного законодательства, 
                                                 касающегося использования программного 
                                                 обеспечения и программирования. 

                            Заключение

               Данное программное обеспечение создано с
               благими намерениями, и его основная цель
               заключается в образовательной деятельности.
               Каждый пользователь должен осознавать свою
               ответственность и использовать приложение в
               рамках закона. В случае нарушения правовых
               норм соответствующие лица несут полную
               личную ответственность за свои действия,
               и создатель программы не может быть
               привлечен к ответственности за эти действия.
               Важно помнить, что законное и этичное
               использование технологий — это залог
               безопасного и эффективного общества.
"""

    Write.Print(readme_text.strip(), Colors.green_to_blue, interval=0.0001)
    Write.Print("\nНажмите Enter, чтобы вернуться в меню...", Colors.green_to_blue, interval=0.0001)
    input()


def add_database():
    clear_console()
    Write.Print("Добавьте свою базу данных...", Colors.green_to_blue, interval=0.0001)
    Write.Print("Чтобы добавить базу данных, поместите файл в папку 'Database'.\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("Поддерживаемые форматы файлов: csv, sql, txt\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("Пример добавления:\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("1. Создайте или скопируйте файл базы данных.\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("2. Перейдите в папку, где находится данный скрипт.\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("3. Найдите папку 'Database' и откройте её.\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("4. Поместите файл в эту папку.\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("5. Запустите программу снова и используйте функцию поиска.\n", Colors.green_to_blue, interval=0.0001)
    Write.Print("\nНажмите Enter, чтобы вернуться в меню...", Colors.green_to_blue, interval=0.0001)
    input()


def get_database_files():
    """Получить список файлов из папки Database"""
    database_folder = 'Database'
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)  # Создать папку Database, если она не существует
    # Получаем список всех файлов в папке Database
    return [os.path.join(database_folder, f) for f in os.listdir(database_folder) if os.path.isfile(os.path.join(database_folder, f)) and f.endswith(('.csv', '.sql', '.txt'))]


def main():
    display_license_agreement()
    print("Перед использованием подпишитесь на мой канал @FreeBestSoft...")
    time.sleep(1)

    intro = """                                                                                                                                                                                     
                                                &&&&&&&& &                                                    
                                            &&&&&&&&&&&&&&&&&  &&                                             
                                            &&&&&&&&&&&&&&&&&&&&&&&&&&                                        
                                      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                                   
                                 &&&&&&&&&&&&&&&&     &&&&&&&&&&&&&&&&&&&&&&&&&&&                             
                              &&&&&&&&&&&& &&                     &&&&&&&&&&&&&&&&&&                          
                           &&&&&&&&&&       &&                         &&&&&&&&&&&&&&& &&&&                   
                           &&&&&&    & &        &&&&&& &&&&&&&              &&&&&&&&&&&&&                     
                         &&&&&&              + &&&&&&&&&&& &&&&&&&&            &&&&&&&&&&&&   &               
                   & &&&&&&   & &   &&      &&&&&&&&x            ; &                  &&&&&&&&&               
                  &&&&&&& & &  &&        &&&&&&&&                 && &                  &&&&&&&&&&            
               &&&&&&  & X  &            &&&&&x    &&&              &&                     &&&&&&&            
             &&&&&&&&&&&&&              &&&      &&&&&&&&&&          & &&              &&  & &&&&&&           
         &&&&&&&    &&&&                &&&      &&&&&&&&&&&&&                            && &&&&&&&&         
        &&&&&&& &&&&&&                  &&&     &&&&&&&&&&&&&&&        &                  &&&&&&&&&&&&&&      
        &&&&&&& &&&&                    &&&     &&&&&&&&&&&&&&&      & &                &&& && &&&&&&& &      
       &&&&&&& &&&&                     &&&      &&&&&&&&&&&&&&      +&                x &&  &&&&&&&&&        
    && &&&&&& &&&&&                     &&&&     &&&&&&&&&&&&&        &                 &&&& &&&&&&&& &&      
          &&&&&&&&&                     &&&&       &&&&&&&&            &               &&&&&&&&&&&&&&&        
           &&&&&&&&&                     &&&&                      &                  ; &&&&&&&&&& &&&        
             &&&&&&&&                    &&&&&&         &        &&                     &&&&&&&&&&&&&&        
               &&&&&&&&&                  &&&&&&&&:            &&                    &&&&&&&&&&&&&&&&&&       
                  &&&&&&&&&&                 &&&&&&&&&&&&&&&&&&                    &&&&&&&&&&&&&&&&&&&&&      
                       &&&&&&&&&                &&&&&&&&&&&&&&&                &&&&&&&&&&&&&&&&&&&&&          
                          &&&&&&&&&&&                      & &            &&&&&&&&&&&&&&&&&     &&            
                               &&&&&&&&&&&&&&             &&+ &&&&&& &&&&&&&&&&&&&&&&&&&&&                    
                                  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                      
                                       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                       
                                                X&&&&&&&&&&&&&&   &&&&&&&&&&                                  
                                                                    &&                                        



                      ██▓███   ██▀███   ▓█████  ██████   ██████     ▓█████ ███▄    █ ▄▄▄█████▓ ▓█████ ██▀███  
                     ▓██░  ██ ▓██ ▒ ██▒ ▓█   ▀▒██    ▒ ▒██    ▒     ▓█   ▀ ██ ▀█   █ ▓  ██▒ ▓▒ ▓█   ▀▓██ ▒ ██▒
                     ▓██░ ██▓▒▓██ ░▄█ ▒ ▒███  ░ ▓██▄   ░ ▓██▄       ▒███  ▓██  ▀█ ██▒▒ ▓██░ ▒░ ▒███  ▓██ ░▄█ ▒
                     ▒██▄█▓▒ ▒▒██▀▀█▄   ▒▓█  ▄  ▒   ██▒  ▒   ██▒    ▒▓█  ▄▓██▒  ▐▌██▒░ ▓██▓ ░  ▒▓█  ▄▒██▀▀█▄  
                     ▒██▒ ░  ░░██▓ ▒██▒▒░▒████▒██████▒▒▒██████▒▒    ░▒████▒██░   ▓██░  ▒██▒ ░ ▒░▒████░██▓ ▒██▒
                     ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░░ ▒░ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ░░ ▒░ ░ ▒░   ▒ ▒   ▒ ░░   ░░░ ▒░ ░ ▒▓ ░▒▓░
                     ░▒ ░       ░▒ ░ ▒ ░ ░ ░  ░ ░▒  ░ ░░ ░▒  ░ ░     ░ ░  ░ ░░   ░ ▒░    ░    ░ ░ ░    ░▒ ░ ▒ 
                     ░░         ░░   ░     ░  ░  ░  ░  ░  ░  ░         ░     ░   ░ ░   ░          ░    ░░   ░ 
                     ░     ░   ░        ░        ░         ░           ░          ░   ░     ░     
"""

    Anime.Fade(Center.Center(intro), Colors.blue_to_red, Colorate.Vertical, interval=0.045, enter=True)

    all_files = get_database_files()

    # Предустановленные файлы
    preloaded_files = [
        "GetContact_2020_19kk.csv",
        "hlbd_form_results.sql",
        "Rostelecom_2021_700k.csv",
        "Clients.csv",
        "enter_data_copy.sql",
        "getcontact.com numbuster.com(2022).txt",
        "boo.wf_100mln_0.csv",
        "boo.wf_100mlн_1.csv",
        "burgerkingrus.ru_08.2024_(5.627.676)_orders.csv.csv",
        "Avito.ma_2022_2,7kk.sql"
    ]

    all_files.extend(preloaded_files)  # Добавляем предустановленные файлы к списку

    while True:
        print_menu()
        choice = input("Выберите: ")

        if choice == '1':
            query = input("Введите доступную информацию: ")
            start_time = time.time()
            results = search_in_files(query, all_files)
            elapsed_time = time.time() - start_time

            if results:
                match_count = len(results)
                print(f"Найдено совпадений: {match_count}")
                for file_name, result in results:
                    print(f"Файл: {file_name}, Данные: {result}")
                print(f"Поиск завершён за {elapsed_time:.2f} секунд.")
            else:
                print("Совпадений не найдено.")

            input("Нажмите Enter, чтобы вернуться в меню.")

        elif choice == '2':
            ip_address = input("Введите IP-адрес для проверки: ")
            info = check_ip(ip_address)

            if info:
                print(f"Результаты для IP-адреса {ip_address}:")
                for key, value in info.items():
                    print(f"{key}: {value}")
            else:
                print("Не удалось получить информацию об IP.")

            input("Нажмите Enter, чтобы вернуться в меню.")

        elif choice == '3':
            email = input("Введите E-mail для поиска: ")
            get_email_info(email)
            input("Нажмите Enter, чтобы вернуться в меню.")

        elif choice == '4':
            long_url = input("Введите длинную ссылку для сокращения: ")
            shortened_link = shorten_url(long_url)
            if shortened_link:
                print(f"Сокращенная ссылка: {shortened_link}")
            input("Нажмите Enter, чтобы вернуться в меню.")

        elif choice == '5':
            webbrowser.open("https://t.me/send?start=IVRkJCUm6A25")
            print("Ссылка открыта в браузере.")
            input("Нажмите Enter, чтобы вернуться в меню.")

        elif choice == '6':
            create_new_identity()

        elif choice == '7':
            generate_password_menu()

        elif choice == '8':
            generate_poem()

        elif choice == '9':
            generate_quote_menu()

        elif choice == '10':
            display_readme()

        elif choice == '11':
            add_database()

        elif choice == '0':
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            time.sleep(2)

if __name__ == "__main__":
    main()