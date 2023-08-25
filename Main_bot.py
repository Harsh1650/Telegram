from __future__ import annotations
from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

from llama_cpp import Llama

from telebot.async_telebot import AsyncTeleBot
import asyncio
bot = AsyncTeleBot('5904051369:AAFhqvfLPy1A5WhvDPYTZTDe46eIIG84PY0')

llm = Llama(model_path="C:\kandikits\gpt4all-content-generator\gpt4all-content-generator\models\gpt4all-lora-quantized-ggml.bin", seed=0)

ins = '''### Instruction:
{}
### Response:
'''

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am Arya.
I am here to answer your queries with kind words to you. Just say anything nice!\
""")

def generate(instruction, max_tokens=256, temperature=0.75, top_p=0.9, repeat_penalty=1.1, top_k=40): 
    result = ""
    for x in llm(ins.format(instruction), max_tokens=max_tokens, top_p=top_p, repeat_penalty=repeat_penalty, top_k=top_k, stop=['### Instruction:', '### End'], stream=True):
        result += x['choices'][0]['text']
        yield result
        
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    output = list(generate(message.text))
    print(message.text)
    await bot.reply_to(message, output[-1])
    
asyncio.run(bot.polling())