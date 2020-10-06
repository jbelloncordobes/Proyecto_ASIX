# Project_ASIX

EN
  
Last year I finished studying the CFGS ASIX and these are the final files I used for the project. The reason why only the final files are here it's because I didn't use any VCS then and I had to go back through the files to get only the functional ones.
This project is about a remote “red button” software, what this means: it can clean an active user's data from the computer with a few commands. The original idea was to be able to also damage the OS enough to have to reinstall it but at the end I did a less destructive version, however, there is a client version called DANGER which still has the original purpose.

Here's how it works, the computers which are going to possibly be wiped will download the client and execute it, to make matters simple, if this is going to be something you want to always have on you should do so it gets executed in the background as soon as you log in the computer. The client's file has a variable called “host” in its first function which you're going to have to change to the server's IP (only experimented in local, don't know if public IP works but it's supposed too).

On the “command center” if you open the server file you'll get notifications if clients' connections are up, you can write “list” to refresh the list of connections. Here you only have to write “select [IP]” to execute commands directly in that computer's shell. Oh yeah, did I forget to mention that this also is a reverse shell? Please don't use this for bad things, that would make me sad, we only learn with a smile here. Whatever, if you write “execute” once you're in a client's shell the magic will start. It will erase everything in the home/user directory and recreate the default folders (documents, images and so) which will obviously be empty.

For the DESTROY version, which only exists for Linux, that thing destroys your root directory, seriously, don't try it. All the tests I've done end with the OS crashing and never starting again. Was a shame I didn't have enough time to do the Windows version, maybe one day.

So here are the files for that thing, pls remember that I'm still a newbie and that this thing was hard to experiment on, you can guess why. Also, everything is commented in Spanish as I had to present it that way.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

SP

El año pasado terminé de estudiar el CFGS de ASIX y estos son los archivos finales que usé para el proyecto. La razón por la que sólo están los archivos finales es porque no usaba ningún SCV en ese entonces y tuve que volver a revisar los archivos para obtener sólo los funcionales.
Este proyecto es sobre un software de "botón rojo" remoto, lo que significa: puede limpiar los datos de un usuario de su PC con unos pocos comandos. La idea original era poder también dañar el sistema operativo lo suficiente como para tener que reinstalarlo, pero al final hice una versión menos destructiva, sin embargo, hay una versión de cliente llamada DANGER que todavía tiene el propósito original.

Como funciona, los ordenadores que van a posiblemente ser borrados descargarán el cliente y lo ejecutarán, para simplificar las cosas, si esto va a ser algo que quieres tener siempre activo debes hacerlo para que se ejecute en segundo plano tan pronto como inicies sesión en el ordenador. El archivo del cliente tiene una variable llamada "host" en su primera función, la cual vas a tener que cambiar por la IP del servidor (sólo se ha experimentado en local, teóricamente las IPs públicas también funcionan pero no puedo confirmarlo).

En el "centro de mando", si abres el archivo de server recibirás notificaciones cuando las conexiones de los clientes están activas, puedes escribir "list" para refrescar la lista de conexiones. Aquí sólo tienes que escribir "select [IP]" para ejecutar los comandos directamente en el shell de ese ordenador. Oh sí, ¿me olvidé de mencionar que esto también es un shell inverso? Por favor no uses esto para cosas malas, eso me pondría triste, sólo aprendemos con una sonrisa aquí. Como sea, si escribes "execute" una vez que estás en el shell de un cliente la magia comenzará. Borrara todo en el directorio home/user y recreará las carpetas por defecto (documents, images y demás) que obviamente estarán vacías.

Para la versión DESTROY, que sólo existe para Linux, simplemente destruye tu directorio raíz, en serio, no lo intentes. Todas las pruebas que he hecho terminan con el sistema operativo colapsando y no volviendo a empezar. Fue una pena que no tuviera suficiente tiempo para hacer la versión de Windows, tal vez algún día.

Así que aquí están los archivos de esa cosa, por favor, un recordatorio de que todavía soy un novato y era muy dificil experimentar libremente debido a la naturaleza del programa.

