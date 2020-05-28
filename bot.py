# importa l'API de Telegram
import os
import pickle
import shutil

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from antlr4 import *
from cl.SkylineLexer import SkylineLexer as Lexer
from cl.SkylineParser import SkylineParser as Parser
from cl.SkylineVisitor import SkylineVisitor as Visitor


def start(update, context):
    global next_user_id
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido a SkyLineBot!")
    context.user_data['id'] = next_user_id
    context.user_data['skylines'] = {}
    next_user_id += 1


def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot!\n @ Edgar Perez Blanco, 2020\n "
                                                                    "edgar.perez.blanco@est.fib.upc.edu")


def lst(update, context):
    msg = "Empty"
    for name, skln in context.user_data['skylines'].items():
        msg = str(name) + ":\t Area = " + str(skln.area)
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    if msg == "Empty":
        context.bot.send_message(chat_id=update.effective_chat.id, text="No hay ningun Skyline definido.")


def clean(update, context):
    context.user_data['skylines'] = {}
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tu lista de Skylines activos se ha vaciado.\n"
                                                                    "Puedes comprobarlo con el comando /lst")


def save(update, context):
    try:
        id = str(context.args[0])
        usr = str(context.user_data['id']).zfill(4)
        filename = "./data/" + usr + "_" + id + ".sky"
        skln = context.user_data['skylines'][id]
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Identificador incorrecto.')

    try:
        filehandler = open(filename, 'wb')
        pickle.dump(skln, filehandler)
        msg = id + " se ha guardado."
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ha habido un error al guardar.')


def load(update, context):
    try:
        id = str(context.args[0])
        usr = str(context.user_data['id']).zfill(4)
        filename = "./data/" + usr + "_" + id + ".sky"
        filehandler = open(filename, 'rb')
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Identficador incorrecto.')

    try:
        context.user_data['skylines'][id] = pickle.load(filehandler)
        msg = id + " se ha cargado."
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ha habido un error al cargar.')


def help(update, context):
    msg = ''' *SkylineBot*
     
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
    msg = '''*Lista de comandos*

/start :`     (Re)Inicia la conversacion con el Bot.`
/help :`      Consulta el manual de ayuda e informacion del bot.`
/author :`    Informacion sobre el autor del bot.`
/lst :`        Lista de Skylines definidos activos.`
/clean :`      Borra los Skylines definidos activos.`
/save `<id>` :`  Guarda el Skyline id en tu perfil.`
/load `<id>` :`  Carga el Skyline id guardado previamente en tu perfil en la lista de Skylines definidos activos.`

'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def guardar_y_cargar_skylines(update, context):
    msg = '''*Como guardar/cargar/borrar Skylines*

Puedes guardar tus Skylines por su nombre para o bien para recuparlos mas tarde si los sobreescribes, o bien porque \
quieres limpiar tu lista de identificadores pero sin perder los que consideras importantes:

Para guardar un Skyline tienes que haberlo definido como permanente previamente (+info en /permanente), asociado a un \
identificador <id>. Mediante el comando `/save <id>` podras guardar el Skyline con nombre <id>.

Para posteriormente recuperar un Skyline guardado basta con utilizar el comando `/load <id>` y este volvera a estar \
disponible en tu lista de Skylines activos (consultable mediante /lst). 

Si consideras que has definido demasiados identificadores, y ya has guardado los que querias, basta con ejecutar el \
comando /clean y este vaciara tu lista. De nuevo, puedes comprobar que ha quedado vacia mediante el comando /lst.
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def como_definir_un_skyline(update, context):
    msg = '''*Definicion de Skylines*
   
Como definir un Skyline:
1) `Skyline simple`: Se introduce un solo edificio.
2) `Skyline compuesto`: Se introduce un conjunto de edificios.
3) `Skyline aleatorio`: Se genera un conjunto de edificios de forma aleatoria dadas unas pautas.
4) `Operacion entre Skylines`: Se puede generar un Skyline en base a la operacion entre otros ya existentes o \
definiciones de los mismos.

    Guia para definir Skyline:
        1) /simple
        2) /compuesto
        3) /aleatorio
        4) /operacionesEntreSkylines
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def operaciones_entre_skylines(update, context):
    msg = ''' *Operaciones entre Skylines*
    
Podemos definir un Skyline mediante modificaciones a uno existente o fusiones entre ellos. Las operaciones modifican \
a un solo Skyline o generan uno nuevo a partir de dos.

Modificar un Skyline, donde <Skyline> es la definicion de un SKyline y <N> es un numero:

    `<Skyline> + N`: Desplazar el Skyline N posiciones a la derecha.
    `<Skyline> - N`: Desplazar el Skyline N posiciones a la izquierda.
    `<Skyline> * N`: Replica el Skyline N veces, copiandolo uno al lado del otro.
    `- <Skyline> `: Invierte un Skyline, como si de un espejo se tratase.

Fusionar un par de Skylines:
    `<Skyline> * <Skyline>`: Interseccion entre Skylines, es decir, nos quedamos las partes comunes entre ellos.
    `<Skyline> + <Skyline>`: Union entre Skylines, es decir, unimos los dos Skylines completos en uno solo.

Ejemplos:
```
 // Skyline espejo de un Skyline compuesto
 -[(1,7,4), (5,4,8), (8,2,10)]
 
 // Skyline aleatorio, replicado 4 veces, y posteriormente desplazado 8 unidades
 {100, 20, 30, 1, 500} * 4 + 8
 
 // a1 invertido
 - a1
 
 // Desplazamos a3 en 5 unidades, lo unimos a a2, y lo intersecamos con un Skyline compuesto.
 (a2 + (a3 + 5)) * [(1,7,4), (5,4,8), (8,2,10)]
```

Las operaciones se pueden combinar y encadenar unas tras otras. Se puede dar preferencia a operaciones mediante el uso \
de '( )', los cuales cuanto mas anidados esten, mas preferencia tendran.

Ejemplos:
```
 // a1 es equivalente a a2
 a1 := (1,2,4) + [(1,7,4), (5,4,8), (8,2,10)] + 3 + (2,7,8) 
 a2 := ( (1,2,4) + [(1,7,4), (5,4,8), (8,2,10)] + 3 ) + (2,7,8)
 
 // a3 y a4 son diferentes de a1 y a2
 a3 := (1,2,4) + ( [(1,7,4), (5,4,8), (8,2,10)] + 3 + (2,7,8) ) 
 a4 := ( (1,2,4) + [(1,7,4), (5,4,8), (8,2,10)] ) + 3 + (2,7,8) 
```
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def tipos_de_skylines(update, context):
    msg = '''*Tipos de Skylines*
   
Tipos de Skyline a introducir:
1) `Skyline temporal`: se visualiza el resultado del Skyline definido pero no se guarda.
2) `Skyline permamente`: se visualiza el resultado del Skyline definido y se guarda con un nombre dado. 

    Guia sobre tipos de Skyline:
        1) /temporal
        2) /permanente
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def help_simple(update,context):
    msg = '''*Skyline Simple*
   
Un Skyline simple esta formado por un solo edificio y tiene la siguiente estructura:
   
   `(xmin,h,xmax)`:
   
      - `xmin`: donde empieza el edificio
      - `h`: altura del edificio.
      - `xmax`: donde acaba el edificio
   
Para todo edificio definido, la altura debe ser siempre mayor a 0 y xmin debe ser estrictamente mayor que xmax.
   
   Ejemplos correctos:
   ```
   (1,7,4)   // Edificio que va del 1 al 4 (anchura = 3), y de altura = 7.
   (33,4,38) // Edificio que va del 33 al 38 (anchura = 5), y de altura = 4.
   ```
   Ejemplos incorrectos
   ```
   (1,0,3) // Altura Nula !!
   (5,4,3) // El inicio esta antes que el final !! 
   ```
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def help_compuesto(update,context):
    msg = '''*Skyline Compuesto*
   
Un Skyline compuesto esta formado por un conjunto de simples entre corchetes '[ ]' separados por comas:
   
   [(xmin1,h1,xmax1), (xmin2,h2,xmax2), (xmin3,h3,xmax3), ...]
   
El conjunto de edicios no tiene porque estar ordenado y entre ellos pueden solaparse sin problema alguno, el propio \
sistema se encargara de todo. Es importante que cada uno de los edificios este definido correctamente. Para mas \
informacion sobre como definir un Skyline/Edificio simple consulta: /simple
   
   Ejemplo:
   ```
   // Lista de 5 edificios sin solapamientos
   [(1,7,4), (5,4,8), (8,2,10), (10,9,20), (30,18,34)]
   
   // Lista de 5 edificios con solapamientos  
   [(1,7,4), (33,4,38), (1,2,4), (1,9,3), (30,7,34)]    
   ```
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def help_aleatorio(update,context):
    msg = '''*Skyline Aleatorio*
   
Un Skyline aleatorio, como dice su nombre, se genera de forma aleatoria en base a unos limites y directrices concretas.\
 Para ello se deben dar los siguientes datos entre llaves '{ }' separados por comas y ordenados de la siguiente forma:
   
   `{n, h, w, xmin, xmax}`:
   
      - `n`: cantidad de edificios a generar.
      - `h`: altura maxima de los edificios a generar.
      - `w`: anchura maxima de los edificios a generar.
      - `xmin`: donde empieza la generacion de edificios
      - `xmax`: donde acaba la generacion de edificios
   
   Ejemplo 1: _Lista de 100 edificios, de anchura entre 1 y 20, de altura entre 1 y 30, generados entre el punto 1 y el punto 500_
   ```
   {100, 20, 30, 1, 500}
   ```
   Ejemplo 2: _Lista de 60 edificios, de altura entre 1 y 20, de anchura entre 1 y 5, generados entre el punto 250 y el punto 300_
   ```
   {60, 20, 5, 250, 300}
   ```
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def help_temporal(update, context):
    msg = '''*Skyline Temporal*
   
Un Skyline temporal consiste en introducir la definicion de un Skyline sin guardarlo en ninguna variable, \
simplemente con el objetivo de visualizar el resultado de dicho Skyline. Dado que el nombre de un Skyline definido \
previamente tambien se considera la definicion de uno, se puede utilizar el conepto de Skyline temporal para visualizar \
el Skyline contenido en una variable o que resultado daria una operacion entre estos: 
       
    `<Skyline>`: definicion del Skyline a mostrar.
    
    Ejemplos:
    ```
       (1,3,7)
       {100, 20, 30, 1, 500}
       (s1 + 3) + [(1,7,4), (5,4,8), (30,18,34)]
       s1 + s3
       s1
    ```
Para aprender a definir un Skyline consulta la guia /comoDefinirUnSkyline
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


def help_permanente(update, context):
    msg = '''*Skyline Permanente*
   
Crear un Skyline permanente consiste en definir un Skyline y guardarlo dentro de una variable con un nombre. \
El nombre de la variable debe comenzar con una letra y puede estar formado por letras y numeros. Para ello debes \
escribir el nombre, seguido del operador ':=' y la definicion del Skyline:

    `<nombre> := <Skyline>`:

          - `<nombre>`: nombre asignado a una variable.
          - `<Skyline>`: definicion del Skyline a guardar.
    
   Ejemplos:
   ```
   s1 := (1,3,7)
   s2 := {100, 20, 30, 1, 500}
   s3 := (s1 + 3) + [(1,7,4), (5,4,8), (30,18,34)]
   s4 := s1 + s3
   s5 := s1
   ```
Todos los Skylines guardados con un nombre se guardan para que los uses cuando quieras. Para consultar informacion \
sobre como guardar, cargar o borrar los Skylines definidos con nombres, consulta la siguiente guia: \
/comoGuardarYCargarSkylines

Para aprender a definir un Skyline consulta la guia /comoDefinirUnSkyline
'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, parse_mode=ParseMode.MARKDOWN)


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
    picture_path = "./tmp/" + str(context.user_data['id']).zfill(4) + ".png"
    skln.save_plot(picture_path)
    skln_info = 'area: ' + str(skln.area) + '\n' + 'alçada: ' + str(skln.height)

    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(picture_path, 'rb'))
    context.bot.send_message(chat_id=update.message.chat_id, text=skln_info)
    os.remove(picture_path)



# Set Token
TOKEN = open('token.txt').read().strip()


# Initialize Telegram elements
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


# Link bot commands to functions
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('comoDefinirUnSkyline', como_definir_un_skyline))
dispatcher.add_handler(CommandHandler('operacionesEntreSkylines', operaciones_entre_skylines))
dispatcher.add_handler(CommandHandler('tiposDeSkylines', tipos_de_skylines))
dispatcher.add_handler(CommandHandler('comoGuardarYCargarSkylines', guardar_y_cargar_skylines))
dispatcher.add_handler(CommandHandler('listaDeComandosDisponibles', command_lst))
dispatcher.add_handler(CommandHandler('simple', help_simple))
dispatcher.add_handler(CommandHandler('compuesto', help_compuesto))
dispatcher.add_handler(CommandHandler('aleatorio', help_aleatorio))
dispatcher.add_handler(CommandHandler('temporal', help_temporal))
dispatcher.add_handler(CommandHandler('permanente', help_permanente))
dispatcher.add_handler(MessageHandler(Filters.text, compile_command))


# Initialize user id counter
next_user_id = 0


# Clean old data and tmp directory and create a new one if not exists
try:
    if os.path.exists('./data'):
        shutil.rmtree('./data')

    if not os.path.exists('./data'):
        os.makedirs('./data')

    if os.path.exists('./tmp'):
        shutil.rmtree('./tmp')

    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

except Exception as e:
        print(e, "Error en la gestion de las carpetas de datos temporales.")


# Turn on the bot
updater.start_polling()
