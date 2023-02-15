# from loader import dp
# from aiogram.types import Message



# @dp.message_handler(commands=['start'])
# async def mes_start(message: Message):
#     await message.answer(f'Привет, {message.from_user.first_name}')


# @dp.message_handler(commands=['help'])
# async def mes_help(message: Message):
#     await message.answer(f'Чем могу помочь?')


# @dp.message_handler(commands=['OOP', 'oop'])
# async def mes_oop(message: Message):
#     await message.answer('Да что вы говорите')


# @dp.message_handler(commands=['set'])
# async def mes_set(message: Message):
#     global total
#     count = message.text.split()[1]
#     total = int(count)
#     await message.answer(f'Установили новое количество конфет в размере - {total}')


# @dp.message_handler(text=['лох'])
# async def mes_loh(message: Message):
#     await bot.delete_message(message.from_user.id, message.message_id)
#     await message.answer(f'Так говорить нельзя')
    
#     # await message.answer(f'Гляди, что поймал - {message.text}')

# @dp.message_handler()
# async def mes_comp(message: Message):
#     global total
#     if message.text.isdigit():
#         total -= int(message.text)
#         await bot.send_message(message.from_user.id, f'Конфет на столе '
#                                                      f'осталось - {total}')
#     else:
#         await bot.send_message(message.from_user.id, f'Введите число конфет не более 28: ')

