# ***SCAV: S2-FFMPeg***

## **EJERCICIOS**

### EJERCICIO-1
#### ***Cut video (10s)***

<p align="justify">Con el fin de recortar el video 10 segundos procedí a ejecutar un comando desde el terminal usando <em>ffmpeg</em>. Este comando lo encontré en la página de <em>VIDAGNU</em>:</p><p align="center"><em>ffmpeg -ss 00:<strong>07:05.0</strong> -i BBB.mp4 -c copy -t 00:00:<strong>10.0</strong> BBB_10s.mp4</em></p><p align="justify">Donde asignamos que en el minuto 7 y segundo 5 empezamos a reproducir el video durante 10 segundos. El resultado de dicho video de diez segundos lo guardamos en el video-output (BBB_10s.mp4). De esta forma obtenemos un corte de 10 segundos del video original justo a partir del minuto 00:07:05.</p><p align="justify">Fuente:<br>https://www.vidagnu.com/como-recortar-o-tomar-una-porcion-de-un-video-con-ffmpeg-en-linux/</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-1/BBB_10s.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Link resultado del video (Mi Youtube): https://youtu.be/WndicksBocw</p>

<p align="justify">En el video final podemos ver que dura 10 segundos y que hace referencia al minuto 00:07:05 del video original. </p>

### EJERCICIO-2
#### ***YUV Histogram***

<p align="justify">Nuevamente mediante un comando usando <em>ffmpeg</em> procedemos a realizar el histograma YUV y plotearlo sobre la misma imagen o video. Para ello utilicé el comando dado por la misma página de <em>FFmpeg</em>:</p><p align="center"><em>ffmpeg -i BBB_10s.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" histo_BBB.mp4</em></p><p align="justify">Fuente:<br>https://trac.ffmpeg.org/wiki/Histogram</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-2/histo_BBB.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Link resultado del video (Mi Youtube): https://youtu.be/-1ttAqNjws4</p>

<p align="justify">En el resultado vemos el histograma de las tres componentes de YUV (Y, Cb y Cr). Donde Y nos informa sobre la luminancia, es decir información en blanco y negro, por esa razón la barra de color debajo del histograma que representa la Y esta en escala de grises. Vemos también el histograma de las componentes Cb y Cr, que hacen referencia a la crominancia, es decir, la información sobre el color. </p>

### EJERCICIO-3
#### ***Resize the BBB(10s) video***

<p align="justify">Igual que en la práctica 1, cuando realizamos la reducción de calidad de las imágenes con una reducción de escala, para el caso del video, usaremos el mismo comando, pero en vez de pasar una imagen al comando, le pasamos un video. </p><p align="center"><em>ffmpeg -i BBB_10s.mp4 -vf scale=<strong>1280:720</strong> 1280x720.mp4</em></p><p align="justify">Fuente:<br>https://trac.ffmpeg.org/wiki/Scaling</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-3/1280x720.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Link resultado del video 1280X720 (Mi Youtube): https://youtu.be/-zjsgdHLAMk</p>
<p align="center"> Link resultado del video 640X480 (Mi Youtube): https://youtu.be/qdyaH8BuRuA</p>
<p align="center"> Link resultado del video 360X240 (Mi Youtube): https://youtu.be/oTOrATpGNek</p>
<p align="center"> Link resultado del video 160X120 (Mi Youtube): https://youtu.be/qquzqcsQgkA</p>

<p align="justify">Como podemos ver en los distintos videos, a medida que reducimos la resolución de éstos, la calidad también lo hace.</p>

### EJERCICIO-4
#### ***Run-lenght encoding***

<p align="justify"></p> <p align="justify">Fuentes:<br>Pasar a mono: https://trac.ffmpeg.org/wiki/AudioChannelManipulation<br>Cambiar audio codec: https://superuser.com/questions/215430/would-like-to-change-audio-codec-but-keep-video-settings-with-ffmpeg</p>


##### **Comando + Terminal**
<p align="center">
   Pasamos a mono
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-4/pasarAMono.png" width="600"/>
   Cambiamos audio codec a mp3
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-4/pasarA-MP3.png" width="600"/>
</p>

##### **Antes y después de cambiar tipo de canal y codificación del audio**
###### **Antes**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-3/1280x720.png" width="600"/>
</p>

###### **Después**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S2-SCAV/blob/main/EJERCICIO-3/1280x720.png" width="600"/>
</p>

##### **Resultados**

<p align="center"> Video con audio original (Mi Youtube): https://youtu.be/WndicksBocw</p>
<p align="center"> Link resultado del video con canal audio mono (Mi Youtube): https://youtu.be/-zjsgdHLAMk</p>
<p align="center"> Link resultado del video con canal audio mono y diferente audio codec (MP3) (Mi Youtube): https://youtu.be/qdyaH8BuRuA</p>

<p align="justify">Como podemos escuchar, si comparamos el video original con el que tiene un único canal, se aprecia claramente con auriculares como se pierde esa sensación espacial que nos da el audio multicanal 5.1 surround que tenia el video original, como hemos podido ver en la captura de las propiedades el video.<br>En cambiar también el tipo de codificación del audio, las diferencias apenas son notorias.</p>


### EJERCICIO-5
#### ***DCT***

<p align="justify">La DCT (<em>Discrete Cosine Transform</em>) se caracteriza por tener una buena capacidad de concentración o compactación de la energía o la información en pocos coeficientes a diferencia de otros métodos como la DFT. Principalmente lo que hace es separar la imagen en partes con distintas frecuencias y procede a realizar la cuantización donde se realiza una compresión y las frecuencias menos relevantes o importantes son descartadas. Cabe destacar que el algoritmo no cambia los datos que recibe a diferencia de otros algoritmos que sí lo hacen.<br> En python esa función ya está implementada mediante el paquete <em>scipy</em>. Por ello al iniciar el script importamos ambas funciones, la DCT y la IDCT, a más de importar funciones como <em>imread</em> para poder leer la imagen a la que aplicar la DCT.<br>Dado que queremos aplicar la DCT a una imagen (2D), nos encontramos en un espacio bidimensional, por lo tanto, al usar las funciones <em>dct2()</em> y <em>idct2()</em> deberemos aplicar la DCT dos veces, para cada una de las dimensiones.<br>Cargaremos la imegen, le aplicaremos la DCT, la IDCT y posteriormente veremos el resultado final. </p><p align="justify">Fuente:<br>https://stackoverflow.com/questions/7110899/how-do-i-apply-a-dct-to-an-image-in-python</p>



```python
from scipy.fftpack import dct, idct

from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

##################### DCT & IDCT (2D)########################
# 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

#########################################################


# leemos una imagen RGB y la pasamos a grayscale
im = rgb2gray(imread('EJERCICIO-5/original.png'))
#DCT
im_DCT = dct2(im)
#IDCT
im_IDCT = idct2(im_DCT)

#comprobación de que se asemejan ambas imágenes
assert(np.allclose(im, im_IDCT) == True)

# plot de la imagen original y la reconstruida
plt.gray()
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Original image', size=20)
plt.subplot(122), plt.imshow(im_IDCT), plt.axis('off'), plt.title('Reconstructed image (DCT+IDCT)', size=20)
plt.show()
```
![](https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-5/Reconstructed_image(DCT%2BIDCT).png)
> Resultado.

<p align="justify">A simple vista no podemos ver o apreciar apenas ningún cambio, a más de que en realizar una comparación entre el resultado y la imagen original podemos ver que no estan muy lejos entre ellas. </p>
