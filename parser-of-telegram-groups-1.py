from telethon import TelegramClient
import asyncio

# Вставьте свои данные.
# Чтобы получить данные для ввода в переменные ниже, воспользуйтесь сайтом "my.telegram.org" (Авторизация ---> Создание приложения ---> Получение от него данных.)
api_id = ""
api_hash = ""
username_of_your_group = "" # Имя группы или её ID.
output_file = "selected.txt" # Название файла, куда будет сохраняться парсинг имён из Telegram группы.

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        # Получаем участников группы.
        participants = await client.get_parcitipant(username_of_your_group)

        # Сохраняем полученные ник-неймы в файл ".txt".
        with open(output_file, 'w', encoding='utf-8') as f:
            for user in participants:
                if user.username:
                    f.write(f"{user.username}\n")
                else:
                    f.write(f"{user.first_name} {user.last_name}\n")

# Проверка работы написанного кода.
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

