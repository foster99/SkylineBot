# SkylineBot

Bot de Telegram para representar Skylines. Con el podras facilmente disenar tu propio Skyline introduciendo eficicios
y operando entre ellos, ya sea uniendo diferentes Skylines, replicandolos, desplazandolos ... e incluso guardarlos
para usarlos posteriormente. Para comenzar solo debes introdcuir el comando /start y empezar a manipular tus Skylines.

## Preparacion

## Ejecucion

## Guia de uso

### Tipos de Skylines
Tipos de Skyline a introducir:
1) **Skyline temporal**: se visualiza el resultado del Skyline definido pero no se guarda.
2) **Skyline permamente**: se visualiza el resultado del Skyline definido y se guarda con un nombre dado. 

#### 1. Skyline temporal
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

#### 2. Skyline permamente
Crear un Skyline permanente consiste en definir un Skyline y guardarlo dentro de una variable con un nombre. \
El nombre de la variable debe comenzar con una letra y puede estar formado por letras y numeros. Para ello debes \
escribir el nombre, seguido del operador ':=' y la definicion del Skyline:

`<nombre> := <Skyline>`:

* `<nombre>`: nombre asignado a una variable.
* `<Skyline>`: definicion del Skyline a guardar.
    
Ejemplos:
   ```
   s1 := (1,3,7)
   s2 := {100, 20, 30, 1, 500}
   s3 := (s1 + 3) + [(1,7,4), (5,4,8), (30,18,34)]
   s4 := s1 + s3
   s5 := s1
   ```

### Como definir un Skyline:
1) **Skyline simple**: Se introduce un solo edificio.
2) **Skyline compuesto**: Se introduce un conjunto de edificios.
3) **Skyline aleatorio**: Se genera un conjunto de edificios de forma aleatoria dadas unas pautas.
4) **Operacion entre Skylines**: Se puede generar un Skyline en base a la operacion entre otros ya existentes o
definiciones de los mismos.

#### 1. Skyline Simple
Un Skyline simple esta formado por un solo edificio y tiene la siguiente estructura:
   
   `(xmin,h,xmax)`:
   * `xmin`: donde empieza el edificio
   * `h`: altura del edificio.
   * `xmax`: donde acaba el edificio
   
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
#### 2. Skyline Compuesto
Un Skyline compuesto esta formado por un conjunto de simples entre corchetes `[ ]` separados por comas `,`:
   
   `[(xmin1,h1,xmax1), (xmin2,h2,xmax2), (xmin3,h3,xmax3), ...]`
   
El conjunto de edicios no tiene porque estar ordenado y entre ellos pueden solaparse sin problema alguno, el propio 
sistema se encargara de todo. Es importante que cada uno de los edificios este definido correctamente segun la 
estructura de Skyline Simple.
   
   Ejemplos:
   ```
   // Lista de 5 edificios sin solapamientos
   [(1,7,4), (5,4,8), (8,2,10), (10,9,20), (30,18,34)]
   
   // Lista de 5 edificios con solapamientos  
   [(1,7,4), (33,4,38), (1,2,4), (1,9,3), (30,7,34)]    
   ```

#### 3. Skyline Aleatorio
Un Skyline aleatorio, como dice su nombre, se genera de forma aleatoria en base a unos limites y directrices concretas.
Para ello se deben dar los siguientes datos entre llaves `{ }` separados por comas `,` y ordenados de la siguiente forma:
   
   `{n, h, w, xmin, xmax}`:
   
   * `n`: cantidad de edificios a generar.
   * `h`: altura maxima de los edificios a generar.
   * `w`: anchura maxima de los edificios a generar.
   * `xmin`: donde empieza la generacion de edificios
   * `xmax`: donde acaba la generacion de edificios
   
   Ejemplo 1: _Lista de 100 edificios, de anchura entre 1 y 20, de altura entre 1 y 30, generados entre el punto 1 y el punto 500_
   ```
   {100, 20, 30, 1, 500}
   ```
   Ejemplo 2: _Lista de 60 edificios, de altura entre 1 y 20, de anchura entre 1 y 5, generados entre el punto 250 y el punto 300_
   ```
   {60, 20, 5, 250, 300}
   ```

#### 4. Operacion entre Skylines
Podemos definir un Skyline mediante modificaciones a uno existente o fusiones entre ellos. Las operaciones modifican \
a un solo Skyline o generan uno nuevo a partir de dos.

Modificar un Skyline, donde <Skyline> es la definicion de un SKyline y <N> es un numero:
  * `<Skyline> + N`: Desplazar el Skyline N posiciones a la derecha.
  * `<Skyline> - N`: Desplazar el Skyline N posiciones a la izquierda.
  * `<Skyline> * N`: Replica el Skyline N veces, copiandolo uno al lado del otro.
  * `- <Skyline> `: Invierte un Skyline, como si de un espejo se tratase.

Fusionar un par de Skylines:
  *  `<Skyline> * <Skyline>`: Interseccion entre Skylines, es decir, nos quedamos las partes comunes entre ellos.
  *  `<Skyline> + <Skyline>`: Union entre Skylines, es decir, unimos los dos Skylines completos en uno solo.

Ejemplos:
*  Skyline espejo de un Skyline compuesto
```
 -[(1,7,4), (5,4,8), (8,2,10)]
```
* Skyline aleatorio, replicado 4 veces, y posteriormente desplazado 8 unidades
```
 {100, 20, 30, 1, 500} * 4 + 8
```
* a1 invertido
```
 - a1
```
* Desplazamos a3 en 5 unidades, lo unimos a a2, y lo intersecamos con un Skyline compuesto.
```
 (a2 + (a3 + 5)) * [(1,7,4), (5,4,8), (8,2,10)]
```

Las operaciones se pueden combinar y encadenar unas tras otras. Se puede dar preferencia a operaciones mediante el uso \
de `( )`, los cuales cuanto mas anidados esten, mas preferencia tendran.

Ejemplos:
* a1 es equivalente a a2
```
 a1 := (1,2,4) + [(1,7,4), (5,4,8), (8,2,10)] + 3 + (2,7,8) 
 a2 := ( (1,2,4) + [(1,7,4), (5,4,8), (8,2,10)] + 3 ) + (2,7,8)
```
* a3 y a4 son diferentes de a1 y a2
```
 a3 := (1,2,4) + ( [(1,7,4), (5,4,8), (8,2,10)] + 3 + (2,7,8) ) 
 a4 := ( (1,2,4) + [(1,7,4), (5,4,8), (8,2,10)] ) + 3 + (2,7,8) 
```

### Como guardar/cargar/borrar Skylines
Puedes guardar tus Skylines por su nombre para o bien para recuparlos mas tarde si los sobreescribes, o bien porque
quieres limpiar tu lista de identificadores pero sin perder los que consideras importantes:

* Para **guardar** un Skyline tienes que haberlo definido como permanente previamente, asociado a un
identificador `<id>`. Mediante el comando `/save <id>` podras guardar el Skyline con nombre `<id>`.

* Para posteriormente **recuperar** un Skyline guardado basta con utilizar el comando `/load <id>` y este volvera a estar
disponible en tu lista de Skylines activos (consultable mediante `/lst`). 

* Si consideras que has definido demasiados identificadores, y ya has guardado los que querias, basta con ejecutar el
comando `/clean` y este **vaciara** tu lista. De nuevo, puedes comprobar que ha quedado vacia mediante el comando `/lst`.

### Lista de comandos

  * `/start`: Inicia la conversacion con el Bot.
  * `/help`: Consulta el manual de ayuda e informacion del bot.
  * `/author`: Informacion sobre el autor del bot.
  * `/lst`: Lista de Skylines definidos activos.
  * `/clean`: Borra los Skylines definidos activos.
  * `/save <id>`: Guarda el Skyline id en tu perfil.
  * `/load <id>`: Carga el Skyline id guardado previamente en tu perfil en la lista de Skylines definidos activos.`

## Metodologia

## Herramientas utilizadas

## Autores