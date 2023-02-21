# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierias
## Departamento de ciencias computacionales
Computacion Tolerante a fallas - Seccion D06

Profesor: *Lopez Franco Michel Emanuel*

Alumno: *Lomeli Flores Jesus Isaac*

## Creacion de servicios para revisar estado de aplicación

### Introducción

<p align="justify">
  Retomando el desarrollo de la pagina web con React, si esta llegase a fallar seria necesario volver a ejecutar un comando para volver a ponerla "en linea" en el menor 
  tiempo posible, es por eso por lo que resulta necesario el desarrollo de un servicio en el dispositivo que desempeña hace de servidor cuya función sea revisar el
  estado de la aplicación y de detectar que la aplicación fue detenida volver a ejecutarla, reduciendo de esta manera el tiempo en que no esta disponible.
</p>


</div>

### Desarrollo

<p align="justify">
Para el desarrollo de esta practica se utilizo el lenguaje de programación python en su versión 3.11 para implementar un código capaz de detectar el estado del puerto
que utiliza la pagina realizada con React.js, cuyo código principal es el siguiente.

</p>


```py
def verificar(ip, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        status = sock.connect_ex((ip, puerto))
        if status == 0:
            print(f"Puerto: {port} - Abierto")
        else:
            print(f"Port: {port} - Cerrado")
            os.system("npm run dev --port={puerto}")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")    
        sys.exit()
```


<p align="justify">
El servicio se debe ejecutar indefinidamente, por lo que se implemento dentro de un bucle sin fin dentro del punto de entrada del programa, lugar donde también se
asignan los valores de los argumentos requeridos.
</p>


```py
if __name__ == '__main__':
    ip_address = "192.168.1.75"
    port = 5173
    url = "D:/6to semestre/ComputacionToleranteFallos/Codigos/persistenciaDatos/"
    
    os.chdir(url)
    while(True):
        verificar(ip_address, port)
        time.sleep(300)
```


<p align="justify">
Para convertir el script realizado en un servicio se utilizo nssm.
</p>

![Creación del servicio con nssm](/imagenes/Screenshot_17.png)

<p align="justify">
Posteriormente se inicia el servicio utilizando una terminal con permisos de administrador.
</p>

![Ejecución del servicio](/imagenes/Screenshot_18.png)

<p align="justify">
Una vez iniciado el servicio se comprueba su ejecución con ayuda del administrador de tareas de Windows.
</p>

![Comprobar ejecución del servicio](/imagenes/Screenshot_19.png)


<p align="justify">
Posteriormente la ejecucion de Nodejs en los procesos del sistema.
</p>

![Comprobar ejecución del nodejs](/imagenes/Screenshot_20.png)


<p align="justify">
Y finalmente se comprueba accediendo desde el navegador a la ip y puerto donde se ubica la pagina.
</p>

![Comprobar ejecución desde navegador](/imagenes/Screenshot_21.png)


<p align="justify">
El servicio se ejecutara cada vez que el dispositivo se encienda y realizara la comprobación del estado de ejecución de la página cada 5 minutos.
</p>


### Conclusion

<p align="justify">
Se logró comprender la importancia de los servicios y como es que estos se implementan. Estos tipos de servicios encargados de revisar el estatus de un programa o aplicación
resultan muy utiles si se necesita que dicha aplicación permanezca siempre activa como es el caso de algunas paginas gubernamentales.
</p>


### Bibliografia
* H. (2022, 27 junio). Escáner de puertos con python básico. HackCode. Recuperado el 18 de Febrero de 2023, de https://hackcode.club/escaner-de-puertos-con-python-basico/ *
