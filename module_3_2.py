def send_email (message, recipient, sender = "university.help@gmail.com") :
    a = recipient.find("@")
    b = recipient.find(".com")
    c = recipient.find(".ru")
    d = recipient.find(".net")
    aa = sender.find("@")
    bb = sender.find(".com")
    cc = sender.find(".ru")
    dd = sender.find(".net")
    if a == -1 :
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif aa == -1:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif b == -1 and c == -1 and d == -1 :
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif bb == -1 and cc == -1 and dd == -1 :
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender :
        print ("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com" :
        print ("Письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
    else :
        print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')