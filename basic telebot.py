from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('5904051369:AAFhqvfLPy1A5WhvDPYTZTDe46eIIG84PY0')



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    print(message.text)
    await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling())
