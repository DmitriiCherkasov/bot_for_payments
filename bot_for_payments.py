from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other


async def on_start(_):
    print('Бот онлайн')


client.register_handlers_client(dp)
# admin.register_handles_admin(dp)
# other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_start)

