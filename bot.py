# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from antlr4 import *
from cl.SkylineLexer import SkylineLexer as Lexer
from cl.SkylineParser import SkylineParser as Parser
from cl.SkylineVisitor import SkylineVisitor as Visitor


# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido a SkyLineBot!")
    print(context.user_data)
    # Inicializaciones


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


def msg(update, context):
    return 0

def compile_command(update, context):
    command = update.message.text

    input_stream = InputStream(command)
    print("Command [", command, "] received.")

    lexer = Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Parser(token_stream)
    tree = parser.root()

    visitor = Visitor()
    visitor.visit(tree)
    # TODO: pillar el retorno

# Set Token
TOKEN = open('token.txt').read().strip()

# Initialize Telegram elements
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Link bot commands to functions
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(MessageHandler(Filters.text, compile_command))

# Turn on the bot
updater.start_polling()

# Exception treatment
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
