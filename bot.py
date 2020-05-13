# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler


# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido a SkyLineBot!")


def help(update, context):
    return 0


def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot!\n @ Edgar Perez Blanco, 2020\n "
                                                                    "edgar.perez.blanco@est.fib.upc.edu")


def lst(update, context):
    return 0


def clean(update, context):
    return 0


def save(update, context):
    return 0


def load(update, context):
    return 0


# def suma(update, context):
#     try:
#         x = float(context.args[0])
#         y = float(context.args[1])
#         s = x + y
#         context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text=str(s))
#     except Exception as e:
#         print(e)
#         context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text='💣')


# Establecemos el TOKEN en base al fichero token.txt
TOKEN = open('token.txt').read().strip()

# Inicializacion de elementos de Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Linkeo de los comandos que recibira el bot a las respectivas funciones
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))

# engega el bot
updater.start_polling()
