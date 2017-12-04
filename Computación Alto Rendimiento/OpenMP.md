![Logo](http://www.aiuc.puc.cl/wp-content/themes/aiuc/images/Esc_Ingenieria-08.jpg)

# Actividad Clase 3:

- Grupo15:
	- Loreto Aguero
	- Manuel Ramos

## OpenMP

### Preparar archivos
  - Subir archivo ac3-openmp.zip a hercules.ing.puc.cl: `scp ~/Downloads/ac03-openmp.zip  grupo15@hercules.ing.puc.cl:/user/grupo15/lab3`.
  - Ir al directorio `cd lab3/`.
  - Descomprimir carpeta zip `unzip ac03-openmp.zip`.
  - Ir al directorio `cd ac03-openmp`.
  - Ir a carpeta del archivo y compilar ejecutando `make`.

### Selección de imagenes

- Las imagenes seleccionadas para esta actividad son:
  - ash.png (1280 x 800).
  - chrono.png(4635 x 3051).
  - really_big(15000 x 10800).

### Selección de nodo:

- El nodo seleccionado para hacer las purebas es el caleuche, para ingresar  `ssh grupo15@hercules.ing.puc.cl` y luego se ejecuta `ssh caleuche` para usar este nodo.

- La cantidad de iteraciones serán 1, 2, 4, 8, 16 y utilizaremos 10 iteraciones.

### Formulas:

- **speedup** = T1/TN = T1 / ( T1 / N ).
- **eff** = speedup / N.

## Pruebas imagen ash.png

- 1 threads:
  - `./masker -n 10 -t 1 /user/cruz/DipBD/2017-2/AC03/images/ash.png ash_blur_1_threads.png`
  - 3.455196   

- 2 threads:
  - `./masker -n 10 -t 2 /user/cruz/DipBD/2017-2/AC03/images/ash.png ash_blur_2_threads.png`
  - 2.067860

- 4 threads:
  - `./masker -n 10 -t 4 /user/cruz/DipBD/2017-2/AC03/images/ash.png ash_blur_4_threads.png`
  - 0.995155

- 8 threads:
  - `./masker -n 10 -t 8 /user/cruz/DipBD/2017-2/AC03/images/ash.png ash_blur_8_threads.png`
  - 0.601378

- 16 threads:
  - `./masker -n 10 -t 16 /user/cruz/DipBD/2017-2/AC03/images/ash.png ash_blur_16_threads.png`
  -  0.688396

### Original

![ash](https://user-images.githubusercontent.com/4138880/33526764-8d8c6022-d824-11e7-8020-fdceba238202.png)  

### Resultado imagen con efecto blur

![ash_blur_1_threads](https://user-images.githubusercontent.com/4138880/33526882-13cd4b82-d826-11e7-9eed-02b2f66c96de.png)

## Pruebas imagen chrono.png

- 1 threads:
  - `./masker -n 10 -t 1 /user/cruz/DipBD/2017-2/AC03/images/chrono.png chrono_blur_1_threads.png`
  - 47.975390   

- 2 threads:
  - `./masker -n 10 -t 2 /user/cruz/DipBD/2017-2/AC03/images/chrono.png chrono_blur_2_threads.png`
  - 28.555160

- 4 threads:
  - `./masker -n 10 -t 4 /user/cruz/DipBD/2017-2/AC03/images/chrono.png chrono_blur_4_threads.png`
  - 15.179359

- 8 threads:
  - `./masker -n 10 -t 8 /user/cruz/DipBD/2017-2/AC03/images/chrono.png chrono_blur_8_threads.png`
  - 8.960226

- 16 threads:
  - `./masker -n 10 -t 16 /user/cruz/DipBD/2017-2/AC03/images/chrono.png chrono_blur_16_threads.png`
  -  8.699309

### Original
![chrono](https://user-images.githubusercontent.com/4138880/33526770-9785fdb8-d824-11e7-9f66-f7fb7b104a8d.png)

### Resultado imagen con efecto blur
![chrono_blur_1_threads](https://user-images.githubusercontent.com/4138880/33527345-bd7eb470-d82d-11e7-88ea-33834b5147c8.png)


## Pruebas imagen really_big.png

- 1 threads:
  - `./masker -n 10 -t 1 /user/cruz/DipBD/2017-2/AC03/images/really_big.png really_big_blur_1_threads.png`
  - 594.896286   

- 2 threads:
  - `./masker -n 10 -t 2 /user/cruz/DipBD/2017-2/AC03/images/really_big.png really_big_blur_2_threads.png`
  - 326.654121

- 4 threads:
  - `./masker -n 10 -t 4 /user/cruz/DipBD/2017-2/AC03/images/really_big.png really_big_blur_4_threads.png`
  - 181.531983

- 8 threads:
  - `./masker -n 10 -t 8 /user/cruz/DipBD/2017-2/AC03/images/really_big.png really_big_blur_8_threads.png`
  - 119.688207

- 16 threads:
  - `./masker -n 10 -t 16 /user/cruz/DipBD/2017-2/AC03/images/really_big.png really_big_blur_16_threads.png`
  - 115.690361

### Original
![captura de pantalla 2017-12-03 a la s 12 25 52](https://user-images.githubusercontent.com/4138880/33526809-2c06968c-d825-11e7-8713-f55152ba02cf.png)

>   Está imagen es una referencia, la original es muy pesada y no se puede adjuntar.

### Resultado imagen con efecto blur
![captura de pantalla 2017-12-03 a la s 13 29 22](https://user-images.githubusercontent.com/4138880/33527364-08ca26b2-d82e-11e7-89cc-7faf7ff8ecff.png)

>   Está imagen es una referencia, la original es muy pesada y no se puede adjuntar, por el estilo de imagen no se nota mucho el efecto blur.

## Bonus

### instrucción collapse

- El comando collapse sirve para agrupar varios bubles en uno juntando sus iteraciones, basandonos en las pruebas que hicimos eliminando la linea de código `#pragma omp for collapse(2)` concluimos que sae distribye mejor la carga al usar collapse.

### Efecto emboss

-  Se genero un archivo con el kernel emboss y luego se aplicaron los efectos ejecutando los siguientes comandos:

  -  `./masker -n 10 -t 16 -m masks/emboss-3x3.txt /user/cruz/DipBD/2017-2/AC03/images/ash.png ash_blur_16_threads.png`

  -  `./masker -n 10 -t 16 -m masks/emboss-3x3.txt /user/cruz/DipBD/2017-2/AC03/images/chrono.png chrono_blur_16_threads.png`

  -  `./masker -n 10 -t 16 -m masks/emboss-3x3.txt /user/cruz/DipBD/2017-2/AC03/images/really_big.png really_big_blur_16_threads.png`

### Resultados

- Original ash

![ash](https://user-images.githubusercontent.com/4138880/33526764-8d8c6022-d824-11e7-8020-fdceba238202.png)  

- Efecto emboss ash

![ash_ emboss_16_threads](https://user-images.githubusercontent.com/4138880/33527533-651f588a-d831-11e7-9ef0-db829368dedd.png)

- Original chrono

![chrono](https://user-images.githubusercontent.com/4138880/33526770-9785fdb8-d824-11e7-9f66-f7fb7b104a8d.png)

- Efecto emboss chrono

![captura de pantalla 2017-12-03 a la s 13 54 09](https://user-images.githubusercontent.com/4138880/33527541-77e666de-d831-11e7-85c0-f8766bdc4192.png)

- Original really_big

![captura de pantalla 2017-12-03 a la s 12 25 52](https://user-images.githubusercontent.com/4138880/33526809-2c06968c-d825-11e7-8713-f55152ba02cf.png)

- Efecto emboss really_big

![captura de pantalla 2017-12-03 a la s 13 54 43](https://user-images.githubusercontent.com/4138880/33527545-8b458df4-d831-11e7-9e6a-548f727ced3b.png)

### Referencia del comando usado para descargar las imágenes

`scp -r grupo15@hercules.ing.puc.cl:/user/grupo15/lab3/ac03-openmp ~/Downloads`
