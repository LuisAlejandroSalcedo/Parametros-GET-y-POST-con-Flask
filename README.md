# Parametros-GET-y-POST-con-Flask

¿GET y POST? ¿Qué es eso?
Para los que todavía no conocen los parámetros GET y POST. Aquí una breve explicación.

Como la mayoría debe saber, la comunicación entre clientes y el servidores en Internet, se realizan a través del protocolo HTTP (Protocolo de Transferencia de Hipertexto). Un usuario envía una solicitud a un servidor, el cual da como respuesta una pagina web (un documento HTML). Los métodos utilizados para este tipo de comunicación son los parámetros GET y POST.

La diferencia entre estos dos parámetros es que GET, envía la información haciéndola visible en la URL de la pagina web. Mientras que POST, envía la información ocultándola del usuario.

Veamos un ejemplo:

http://www.pythondiario.com/articulos.html?tag=Flask 

En la url anterior podemos ver varias cosas. Primero tenemos el dominio, pythondiario.com. Luego tenemos el nombre del documento, articulos.html. Luego esto vemos un simbolo de interrogación. Esto indica que luego del símbolo estarán los parámetros, la información que se le ha pasado a la pagina. 

Podemos ver claramente que la información se ha enviado utilizando GET, ya que la información es visible para el usuario.

Por lo contrario en la siguiente url no se muestra la información , por lo que es claro que se a utilizado POST:

http://www.pythondiario.com/articulos.html


## Lee el articulo completo: http://www.pythondiario.com/2019/01/parametros-get-y-post-con-flask.html



