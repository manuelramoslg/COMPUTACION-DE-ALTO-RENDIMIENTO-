![Logo](http://www.aiuc.puc.cl/wp-content/themes/aiuc/images/Esc_Ingenieria-08.jpg)

# Actividad Clase 3:

- Grupo15:
	- Loreto Aguero
	- Manuel Ramos

## Preparar entorno laboratorio MPI

- Descargar el archivo Actividad Clase 04 - MPI.zip(mpi 2.zip) desde la pagina ep.ingenieriauc.cl.

- Subir archivo mpi 2.zip a hercules ejecutando: `scp ~/Downloads/mpi\ 2.zip  grupo15@hercules.ing.puc.cl:/user/grupo15/lab4`.
- Descomprimir `unzip mpi\ 2.zip`.

- Crear archivos de hosts (hostfile.txt) con nodos del cluster.

- Compilar versiones secuenciales y distribuidas (make).

## Ejecutar programa con 12 ciudades

### Versión secuencial (12 ciudades):

```
grupo15@caleuche:~$ time ./secuential.o ./test/12.txt

Route cost 17: 0 6 1 2 4 10 8 5 7 9 3 11

real	0m0.036s
user	0m0.032s
sys	0m0.000s

```

### Múltiples procesos locales (12 ciudades, 4 Nodos):

```
grupo15@caleuche:~$ time mpirun -N 4 ./parallel.o ./test/12.txt

node 3
Route cost 24: 0 4 8 10 6 1 2 5 7 9 3 11
node 0
Route cost 21: 0 1 6 10 8 4 2 5 7 9 3 11
node 1
Route cost 17: 0 6 1 2 4 10 8 5 7 9 3 11
node 2
Route cost 20: 0 11 3 9 7 4 8 10 6 1 2 5

real	0m0.155s
user	0m0.232s
sys	0m0.072s

```

### Múltiples procesos en múltiples nodos (12 ciudades, 4 Nodos):

```
grupo15@caleuche:~$ time mpirun -hostfile ./hosts.txt -N 4 ./parallel.o ./test/12.txt

node 11
Route cost -1: 0 0 0 0 0 0 0 0 0 0 0 0
node 5
Route cost 17: 0 6 1 2 4 10 8 5 7 9 3 11
node 4
Route cost 25: 0 5 2 1 6 10 8 4 7 9 3 11
node 10
Route cost 20: 0 11 3 9 7 4 8 10 6 1 2 5
node 9
Route cost 23: 0 10 4 8 5 2 1 6 3 9 7 11
node 7
Route cost 26: 0 8 4 10 6 1 2 5 7 9 3 11
node 8
Route cost 22: 0 9 7 4 10 8 5 2 1 6 3 11
node 0
Route cost 21: 0 1 6 10 8 4 2 5 7 9 3 11
node 3
Route cost 24: 0 4 8 10 6 1 2 5 7 9 3 11
node 1
Route cost 22: 0 2 1 6 10 4 8 5 7 9 3 11
node 6
Route cost 26: 0 7 9 3 11 6 1 2 4 10 8 5
node 2
Route cost 27: 0 3 9 7 4 10 8 5 2 1 6 11

real	0m1.656s
user	0m0.220s
sys	0m0.156s

```

## Ejecutar programa con 18 ciudades y 4 nodos

### Versión secuencial(18 ciudades y 4 nodos):

```
grupo15@caleuche:~$ time ./secuential.o ./test/18.txt

Route cost 29: 0 5 9 8 6 11 3 13 2 16 7 15 1 12 10 14 17 4

real	5m7.021s
user	5m6.980s
sys	0m0.000s

```

### Múltiples procesos locales (18 ciudades y 4 Nodos):

```
grupo15@caleuche:~$ time mpirun -N 4 ./parallel.o ./test/18.txt

node 3
Route cost 30: 0 4 17 1 12 10 14 15 7 16 2 13 3 5 9 8 6 11
node 2
Route cost 30: 0 3 5 9 8 6 11 13 2 16 7 15 1 12 10 14 17 4
node 0
Route cost 29: 0 5 9 8 6 11 3 13 2 16 7 15 1 12 10 14 17 4
node 1
Route cost 32: 0 6 11 3 5 9 8 7 16 2 13 10 12 1 15 14 17 4

real	2m46.419s
user	8m34.132s
sys	0m1.760s

```

### Múltiples procesos en múltiples nodos (18 ciudades y 4 Nodos):

```
grupo15@caleuche:~$ time mpirun -hostfile ./hosts.txt -N 4 ./parallel.o ./test/18.txt

node 11
Route cost 32: 0 12 1 17 4 10 14 15 7 16 2 13 3 5 9 8 6 11
node 10
Route cost 37: 0 11 6 8 9 5 3 13 2 16 7 15 1 12 10 14 17 4
node 5
Route cost 32: 0 6 11 3 5 9 8 7 16 2 13 10 12 1 15 14 17 4
node 4
Route cost 29: 0 5 9 8 6 11 3 13 2 16 7 15 1 12 10 14 17 4
node 8
Route cost 35: 0 9 5 3 11 6 8 7 16 2 13 10 12 1 15 14 17 4
node 7
Route cost 35: 0 8 9 5 3 11 6 1 12 10 13 2 16 7 15 14 17 4
node 9
Route cost 34: 0 10 12 1 6 11 3 5 9 8 14 15 7 16 2 13 17 4
node 3
Route cost 30: 0 4 17 1 12 10 14 15 7 16 2 13 3 5 9 8 6 11
node 2
Route cost 30: 0 3 5 9 8 6 11 13 2 16 7 15 1 12 10 14 17 4
node 6
Route cost 35: 0 7 8 9 5 3 11 6 14 15 1 12 10 4 17 13 2 16
node 1
Route cost 33: 0 2 13 3 5 9 8 7 16 17 4 10 12 1 15 14 6 11
node 0
Route cost 32: 0 13 2 16 3 5 9 8 7 15 1 12 10 4 17 14 6 11

real	3m5.703s
user	4m16.288s
sys	0m8.888s

```
## Ejecutar programa con 18 ciudades y 6 nodos

### Múltiples procesos locales (18 ciudades y 6 Nodos):

```
grupo15@caleuche:~$ time mpirun -N 6 ./parallel.o ./test/18.txt

node 4
Route cost 29: 0 5 9 8 6 11 3 13 2 16 7 15 1 12 10 14 17 4
node 5
Route cost 32: 0 6 11 3 5 9 8 7 16 2 13 10 12 1 15 14 17 4
node 3
Route cost 30: 0 4 17 1 12 10 14 15 7 16 2 13 3 5 9 8 6 11
node 2
Route cost 30: 0 3 5 9 8 6 11 13 2 16 7 15 1 12 10 14 17 4
node 1
Route cost 33: 0 2 13 3 5 9 8 7 16 17 4 10 12 1 15 14 6 11
node 0
Route cost 32: 0 13 2 16 3 5 9 8 7 15 1 12 10 4 17 14 6 11

real	3m27.682s
user	11m17.092s
sys	0m5.888s

```

### Múltiples procesos en múltiples nodos (18 ciudades y 6 Nodos):

```
grupo15@caleuche:~$ time mpirun -hostfile ./hosts.txt -N 6 ./parallel.o ./test/18.txt

node 17
Route cost -1: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
node 14
Route cost 30: 0 15 1 12 10 4 17 14 6 11 3 13 2 16 7 8 9 5
node 16
Route cost 35: 0 17 4 10 12 1 6 11 3 13 2 16 7 15 14 8 9 5
node 11
Route cost 32: 0 12 1 17 4 10 14 15 7 16 2 13 3 5 9 8 6 11
node 10
Route cost 37: 0 11 6 8 9 5 3 13 2 16 7 15 1 12 10 14 17 4
node 15
Route cost 32: 0 16 2 13 3 5 9 8 7 15 1 12 10 4 17 14 6 11
node 13
Route cost 33: 0 14 10 12 1 15 7 16 2 13 3 5 9 8 6 11 17 4
node 12
Route cost 32: 0 13 2 16 3 5 9 8 7 15 1 12 10 4 17 14 6 11
node 7
Route cost 35: 0 8 9 5 3 11 6 1 12 10 13 2 16 7 15 14 17 4
node 4
Route cost 29: 0 5 9 8 6 11 3 13 2 16 7 15 1 12 10 14 17 4
node 8
Route cost 35: 0 9 5 3 11 6 8 7 16 2 13 10 12 1 15 14 17 4
node 9
Route cost 34: 0 10 12 1 6 11 3 5 9 8 14 15 7 16 2 13 17 4
node 2
Route cost 30: 0 3 5 9 8 6 11 13 2 16 7 15 1 12 10 14 17 4
node 5
Route cost 32: 0 6 11 3 5 9 8 7 16 2 13 10 12 1 15 14 17 4
node 0
Route cost 35: 0 1 12 10 4 17 14 15 7 16 2 13 3 5 9 8 6 11
node 3
Route cost 30: 0 4 17 1 12 10 14 15 7 16 2 13 3 5 9 8 6 11
node 1
Route cost 33: 0 2 13 3 5 9 8 7 16 17 4 10 12 1 15 14 6 11
node 6
Route cost 35: 0 7 8 9 5 3 11 6 14 15 1 12 10 4 17 13 2 16

real	2m37.699s
user	4m42.756s
sys	0m10.412s

```

## Reporte tabla con tiempo de ejecución, speedup y eficiencia.
### Versión Secuencial

  -| 12 Ciudades | 18 Ciudades
:-- | :-- | :--
Secuencial | 0,0036 | 5,7021
speedup | 1,00 | 1,00
eficiencia | 1,00 | 1,00

- En este caso se puede observar que el mejor rendimiento es de 12 ciudades en modo secuencial, esto se debe a que hay muy pocas tareas para para paralelizar.

### Versión Múltiples procesos locales

	- | 12 Ciudades (4 Nodos) | 18 Ciudades (4 Nodos) | 18 Ciudades (6 Nodos)
:-- | :-- | :-- | :-- | :--
Múltiples procesos locales | 0,0155 | 2,4642 | 3,2768
speedup | 0,232 | 2,314 | 1,740
eficiencia | 0,058 | 0,578 | 0,290

- En este caso se puede observar que el mejor rendimiento se obtiene la versión de múltiples procesos locales con 4 nodos y 18 ciudades, es probable que el equipo en que se ejecuto no tiene más de 4 nodos por lo tanto al quedar en fila hay un tiempo de espera que perjudica un poco el desempeño.

### Versión Múltiples procesos en múltiples nodos
 - | 12 Ciudades (4 Nodos) | 18 Ciudades (4 Nodos) | 18 Ciudades (6 Nodos)
:-- | :-- | :-- | :-- | :--
Múltiples procesos en múltiples nodos  | 0,1656 | 3,5703 | 2,3770
speedup | 0,022 | 1,597 | 2,399
eficiencia | 0,004 | 0,399 | 0,400

- En este caso se puede observar que el mejor rendimiento se obtiene la versión de Múltiples procesos en múltiples nodos con 6 nodos y 18 ciudades, esto se debe a que asignaron 6 rutas para tripio, 6 para trauco y y 6 para el caleuche.


# Preguntas:

- ¿En qué consiste esta tarea y cómo se distribuyó?
  -  Consiste en encontrar la ruta más óptima dependiendo la cantidad de ciudades y se distribuyó entre los nodos de tripio, trauco, caleuche.

- ¿Cuán eficiente es esta paralelización?
  -  Es eficiente dependiendo de la cantidad de tareas que hay que realizar, por ejemplo al ejecutar el programa con 12 ciudades el resultado más óptimo fue el secuencial, esto se debe a que las tareas eran muy pequeñas para ejecutarlas de forma paralela, en cambio cuando se ejecuta el programa pero 18 ciudades y 6 nodos el rendimiento del programa mejora considerablemente ya que se dividen las tareas entre los nodos y el resultado es entregado en la mitad del tiempo de lo que tardaría la versión secuencial.

- ¿	Porque ocurre esto ?

	```
	grupo15@caleuche:~/lab4/mpi 2$ time mpirun -hostfile ./hosts.txt -N 9 ./parallel.o ./test/18.txt
	--------------------------------------------------------------------------
	A request was made to bind to that would result in binding more
	processes than cpus on a resource:

	   Bind to:     NONE:IF-SUPPORTED
	   Node:        trauco
	   #processes:  5
	   #cpus:       4

	You can override this protection by adding the "overload-allowed"
	option to your binding directive.
	--------------------------------------------------------------------------

	real	0m1.299s
	user	0m0.048s
	sys	0m0.032s
	```

	  - Esto se debe a que la suma de los nodos físicos virtuales es igual a 8, por lo tanto no se pueden asignar más nodos de los que existen.

- ¿Porque ocurre esto `Route cost -1: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0`?

 - Al hacer todas las combinaciones posibles siempre va a quedar una combinación menos, es decir de 18 ciudades siempre se van a calcular 17, eso es porque una de ellas es la misma combinación pero inversa, ejemplo la distancia más óptima del trabajo a la casa es la misma distancia que de la casa al trabajo por ende entre estos dos punto la ruta más óptima es la misma.
