import telebot
from telebot import types
from datetime import datetime
from pyyoutube import Api

api = Api(api_key="AIzaSyD2xVNDgW20m0rna45bklUBI68otCnLjXQ")

bot = telebot.TeleBot('6925497075:AAGiVTHPOjPDkTMH_7AasvtaSws2go8HO3Q')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я готов ответить на твой вопрос или найти нужное видео на YouTube.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Данный бот отвечает на заданные вопросы и ищет видео на YouTube. Чтобы начать просто задайте вопрос, либо воспользуйтесь командой /search и ключевое слово или фразу, чтобы найти видео. База вопросов ещё дорабатывается.")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Автор проекта - студент ОЗИВТ-22-2-У, Ческидов Родион.")

@bot.message_handler(commands=['searchvideo'])
def info(message):
    bot.send_message(message.chat.id, "Для того чтоб найти нужное вам видео необходимо написать команду /search и ключевое слово или фразу в одной строке.")

@bot.message_handler(commands=['search'])
def search_youtube(message):
    query = message.text.replace('/search', '').strip()

    try:
        response = api.search_by_keywords(q=query, count=1)
        video = response.items[0]
        video_title = video.snippet.title
        video_url = f"https://www.youtube.com/watch?v={video.id.videoId}"
        response = f"Вот видео, которое я нашел:\n\n{video_title}\n\n{video_url}"
    except:
        response = "К сожалению, я не смог найти видео на YouTube по вашему запросу."

    bot.reply_to(message, response, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def answer_question(message):
    question = message.text.lower()
    answer = get_answer(question)
    bot.send_message(message.chat.id, answer)

@bot.inline_handler(lambda query: True)
def inline_query(query):
    results = []
    question = query.query.lower()
    answer = get_answer(question)
    results.append(types.InlineQueryResultArticle(
        id='1',
        title='Ответ на вопрос',
        input_message_content=types.InputTextMessageContent(message_text=answer)
    ))
    bot.answer_inline_query(query.id, results)

def get_answer(question):
    if "как дела" in question:
        return "У меня всё отлично, спасибо!"
    elif "который час" in question:
        return "Сейчас " + datetime.now().strftime("%H:%M")
    elif "сколько времени" in question:
        return "Сейчас " + datetime.now().strftime("%H:%M")
    elif "погода" in question:
        return "Сейчас оооочень холодно."
    elif "привет" in question:
        return "Приветики!"
    elif "помощь" in question:
        return "Я могу отвечать на вопросы. Просто спросите меня!"
    elif "кто ты" in question:
        return "Я бот, созданный для отвечания на вопросы. Чем могу помочь?"
    elif "кто я" in question:
        return "Вы пользователь, данного бота!"
    elif "видео" in question:
        return "Просто отправьте мне команду /search и ключевое слово или фразу, чтобы найти видео."
    elif "не ищет" in question:
        return "Попробуйте снова."
    else:
        return "Извините, я не понимаю вопрос. Попробуйте задать другой вопрос."


bot.polling()
