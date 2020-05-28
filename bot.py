# importa l'API de Telegram
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from antlr4 import *
from cl.SkylineLexer import SkylineLexer as Lexer
from cl.SkylineParser import SkylineParser as Parser
from cl.SkylineVisitor import SkylineVisitor as Visitor


def get_next_id() -> int:
    global next_user_id
    next_user_id += 1
    return next_user_id


def id_to_str(id: int) -> str:
    return str(id).zfill(4)

## COMMANDS

# Initilization

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido a SkyLineBot!")
    context.user_data['id'] = get_next_id()
    context.user_data['skylines'] = {}

    # Inicializaciones


def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot!\n @ Edgar Perez Blanco, 2020\n "
                                                                    "edgar.perez.blanco@est.fib.upc.edu")


# Skylines management zone

def lst(update, context):
    for name, skln in context.user_data['skylines'].items():
        msg = str(name) + ":\t Area = " + str(skln.area)
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def clean(update, context):
    return 0


def save(update, context):
    return 0


def load(update, context):
    return 0

# End of Skylines management zone

# HELP ZONE

def help(update, context):
    msg = ''' 
*SkylineBot* 
Bot de Telegram para representar Skylines. Con el podras facilmente disenar tu propio Skyline introduciendo eficicios \
y operando entre ellos, ya sea uniendo diferentes Skylines, replicandolos, desplazandolos ... e incluso guardarlos \
para usarlos posteriormente. Para comenzar solo debes introdcuir el comando /start y empezar a manipular tus Skylines.

        Si quieres aprender las distintas funcionalidades puedes consultar las siguientes guias:
        1) /comoDefinirUnSkyline
        2) /tiposDeSkylines
        3) /comoGuardarYCargarSkylines
        4) /listaDeComandosDisponibles
'''

    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def command_lst(update, context):
    msg = ''' salu2'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def guardar_y_cargar_skylines(update, context):
    msg = '''
    Como definir un Skyline:
        '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def como_definir_un_skyline(update, context):
    msg = '''
Como definir un Skyline:
1) *Skyline simple*: Se introduce un solo edificio.
2) *Skyline compuesto*: Se introduce un conjunto de edificios.
3) *Skyline aleatorio*: Se genera un conjunto de edificios de forma aleatoria dadas unas pautas.

    Guia para definir Skyline:
        1) /simple
        2) /compuesto
        3) /aleatorio
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def tipos_de_skylines(update, context):
    msg = '''
Tipos de Skyline a introducir:
1) *Skyline temporal*: se visualiza el resultado del Skyline definido pero no se guarda.
2) *Skyline permamente*: se visualiza el resultado del Skyline definido y se guarda con un nombre dado. 

    Guia sobre tipos de Skyline:
        1) /temporal
        2) /permanente
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


# END OF HELP ZONE

## END OF COMMANDS

def compile_command(update, context):
    command = update.message.text
    input_stream = InputStream(command)
    print("Command [", command, "] received.")

    lexer = Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Parser(token_stream)
    tree = parser.root()

    visitor = Visitor(context.user_data['skylines'])
    skln = visitor.visit(tree)
    send_info(update, context, skln)


def send_info(update, context, skln):
    picture_path = id_to_str(context.user_data['id']) + ".png"
    skln.save_plot(picture_path)
    skln_info = 'area: ' + str(skln.area) + '\n' + 'alçada: ' + str(skln.height)

    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(picture_path, 'rb'))
    context.bot.send_message(chat_id=update.message.chat_id, text=skln_info)

    # ToDo: Delete .png file after sending the image.


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
dispatcher.add_handler(CommandHandler('comoDefinirUnSkyline', como_definir_un_skyline))
dispatcher.add_handler(CommandHandler('tiposDeSkylines', tipos_de_skylines))
dispatcher.add_handler(CommandHandler('comoGuardarYCargarSkylines', guardar_y_cargar_skylines))
dispatcher.add_handler(CommandHandler('listaDeComandosDisponibles', command_lst))

dispatcher.add_handler(MessageHandler(Filters.text, compile_command))

# Initialize user manager
next_user_id = 0

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
