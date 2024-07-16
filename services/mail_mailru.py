import smtplib
import json
import datetime

with open('C:\\Users\\evgen\\OneDrive\\Рабочий стол\\учёба\\6\\практика\\applications\\config.json', 'r') as f:
    config = json.load(f)

# данные почтового сервиса
user = config['smtp-server-mail']
password = config['smtp-server-password']
server = "smtp.gmail.com"
port = 587


def send_mail(to: str, conference_id, author_id):
    # тема письма
    subject = "Отмена заявки"
    # кодировка письма
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'
    # текущее время
    date = datetime.datetime.now().astimezone().isoformat()
    # текст письма
    text = f"Запрос об отмены заявки от автора с id {author_id} из конференции {conference_id}\nЗапрос произошёл в {date}"

    # формируем тело письма
    body = "\r\n".join((f"From: {user}", f"To: {to}",
                        f"Subject: {subject}", mime, charset, "", text))

    # подключаемся к почтовому сервису
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.ehlo()
    # логинимся на почтовом сервере
    smtp.login(user, password)
    # пробуем послать письмо
    smtp.sendmail(user, to, body.encode('utf-8'))

    smtp.quit()
