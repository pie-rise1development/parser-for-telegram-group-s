from telethon import TelegramClient
import asyncio

# Вставьте свои данные
api_id = ''
api_hash = ''
group_username = ''  # Имя группы или её ID
output_file = 'selected.txt'

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        # Получаем участников группы
        participants = await client.get_participants(group_username)
        
        # Сохраняем никнеймы в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            for user in participants:
                if user.username:
                    f.write(f"{user.username}\n")
                else:
                    f.write(f"{user.first_name} {user.last_name}\n")

# Запускаем асинхронную функцию
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

