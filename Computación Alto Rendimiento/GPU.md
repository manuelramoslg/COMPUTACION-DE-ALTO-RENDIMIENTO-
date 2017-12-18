![Logo](http://www.aiuc.puc.cl/wp-content/themes/aiuc/images/Esc_Ingenieria-08.jpg)

# Actividad Clase 5:

- Grupo15:
	- Loreto Agüero
	- Manuel Ramos

## GPU

### Preparar archivos
  - Subir archivo 05-matrixMulCUBLAS.zip a hercules.ing.puc.cl: `scp ~/Downloads/05-matrixMulCUBLAS.zip grupo15@hercules.ing.puc.cl:/user/grupo15/lab5`.
  - Conectar a titan `ssh titan`.
  - Ir al directorio `cd lab5/`.
  - Descomprimir carpeta zip `unzip 05-matrixMulCUBLAS.zip`.
  - Ir al directorio `cd matrixMulCUBLAS`.
  - Ir a carpeta del archivo y compilar ejecutando `make`.


### Ejecutar la ./matrixMulCUBLAS -sizemult= 5

[Matrix Multiply CUBLAS] - Starting...
GPU Device 0: "Tesla C2075" with compute capability 2.0

MatrixA(640,480), MatrixB(480,320), MatrixC(640,320)
Computing result using CUBLAS...done.
Performance= 522.25 GFlop/s, Time= 0.376 msec, Size= 196608000 Ops
Computing result using host CPU...done.
Elapsed time in CPU: 691 msec
Comparing CUBLAS Matrix Multiply with CPU results: PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.


### Ejecutar la ./matrixMulCUBLAS -sizemult= 10000

[Matrix Multiply CUBLAS] - Starting...
GPU Device 0: "Tesla C2075" with compute capability 2.0

MatrixA(640,480), MatrixB(480,320), MatrixC(640,320)
Computing result using CUBLAS...done.
Performance= 519.70 GFlop/s, Time= 0.378 msec, Size= 196608000 Ops
Computing result using host CPU...done.
Elapsed time in CPU: 730 msec
Comparing CUBLAS Matrix Multiply with CPU results: PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.


## Resultados

- | sizemult 5 | sizemult 10000
:-- | :-- | :-- | :-- | :--
Elapsed time in GPU en microsegundos  | 0,376 | 0,378
Elapsed time in CPU en microsegundos | 691| 730
Elapsed time in CPU | 0,000690 | 0,00073
speedup | 1,00 | 1,00
eficiencia | 1,00 | 1,00


- En este caso se puede observar que el rendimiento de la CPU es bueno pero el rendimiento de la GPU es muy superior.

### Características de GPU

- **Tesla C2075:**

  - 448 GPU cores, 14 SMs (32 SP en cada SM).
  - Core clock: 1.15GHz.
  - Memoria: 1.50GHz, 6 GB GDDR5, 384-bit, Bandwidth 144GB/sec.
  - 515 GFLOPS, double-precision.
  - 128 KB Registros por cada SM.
  - 16 + 48 = 64KB shared memory (L1) por cada SM.
  - 14 × 64 = 896 KB shared memory (L1).
  - 786KB cache L2.
  - 3 × 10 elevado a la 9 transistores.

### Preguntas

- ¿En qué parte del código se realiza el llamado a la GPU?

271 // execute the kernel
272 int nIter = 30;
