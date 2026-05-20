# task 1
from pathlib import Path
from collections import Counter


p = Path('app.log')

message_type = []
error_message_description = []

for line in p.read_text().splitlines():
    parts_by_category = line.split(" ", maxsplit=3)
    message_type.append(parts_by_category[2])
    if parts_by_category[2] == "ERROR":
        error_message_description.append(parts_by_category[3])


message_type_frequency = Counter(message_type)

error_message_description_frequency = Counter(error_message_description)

print('app.log contains the following message types:')

for message, frequency in message_type_frequency.items():
    print(f'Message of type {message} appeared in {frequency} time(s).')

most_frequent_error_message_description = error_message_description_frequency.most_common(1)

print(f'And the most common ERROR message is "{most_frequent_error_message_description[0][0]}" and it appeared {most_frequent_error_message_description[0][1]} time(s).')


# from abc import ABC, abstractmethod


# # --- Модели ---
# class User:
#     def __init__(self, name: str, mail: str):
#         self.name = name
#         self.mail = mail


# # --- Генератор писем ---
# class EmailGenerator:
#     @staticmethod
#     def generate_mail_body(user_mail: str) -> str:
#         return f"Привет! Это письмо для {user_mail}"


# # --- Контракт ---
# class MailClient(ABC):
#     @abstractmethod
#     def send_mail(self, body: str):
#         pass


# # --- Фейковые "настоящие" библиотеки (заглушки) ---
# class FakeGmailLib:
#     def send_message(self, body):
#         print(f"[Gmail] {body}")


# class FakeOutlookLib:
#     def send(self, body):
#         print(f"[Outlook] {body}")


# class FakeYahooLib:
#     def deliver(self, body):
#         print(f"[Yahoo] {body}")


# # --- Адаптеры под наш интерфейс ---
# class GmailClient(MailClient):
#     def __init__(self, client):
#         self.client = client
    
#     def send_mail(self, body: str):
#         self.client.send_message(body)


# class OutlookClient(MailClient):
#     def __init__(self, client):
#         self.client = client
    
#     def send_mail(self, body: str):
#         self.client.send(body)


# class YahooClient(MailClient):
#     def __init__(self, client):
#         self.client = client
    
#     def send_mail(self, body: str):
#         self.client.deliver(body)


# # --- Координатор ---
# class UserNotifier:
#     def __init__(self, email_generator, client: MailClient):
#         self.email_generator = email_generator
#         self.client = client
    
#     def notify_user_about_changes(self, user: User):
#         message_body = self.email_generator.generate_mail_body(user.mail)
#         self.client.send_mail(message_body)


# # --- Запуск ---
# ivan = User("Иван", "ivan@mail.ru")
# generator = EmailGenerator()

# # Пробуем все три!
# for client in [GmailClient(FakeGmailLib()),
#                OutlookClient(FakeOutlookLib()),
#                YahooClient(FakeYahooLib())]:
#     notifier = UserNotifier(generator, client)
#     notifier.notify_user_about_changes(ivan)