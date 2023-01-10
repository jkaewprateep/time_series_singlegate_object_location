
import numpy as np
import math
import tensorflow as tf

import matplotlib.pyplot as plt

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Class / Functions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def windowed_dataset(series, time_step):
	dataX, dataY = [], []
	for i in range( math.ceil( len(series) / time_step ) ):
		source = ( time_step * i )
		dest = time_step * ( i + 1 )
		a = series[source : dest, 0]
		dataX.append(a)
		dataY.append(series[source : dest, 0])
	
	return np.array(dataX), np.array(dataY)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: DataSet
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
contents = tf.io.read_file("F:\\temp\\Python\\Speech\\temple_of_love-sisters_of_mercy.wav")
audio, sample_rate = tf.audio.decode_wav(
    contents, desired_channels=-1, desired_samples=-1, name=None
)

contents = tf.io.read_file("F:\\temp\\20230109\\273328879_505895800898439_1279231174142803565_n.bmp")
image = image_original = tf.io.decode_bmp(
    contents, channels=0, name=None
)

train_data, test_data = audio[50 * 1237:51 * 1237].numpy(), audio[52 * 1237:53 * 1237].numpy()

X_train, y_train = windowed_dataset(train_data, time_step=100)
X_test, y_test = windowed_dataset(test_data, time_step=100)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Plottings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
plt.figure(figsize=( 2, 1 ))
plt.suptitle("Windowed Datasets")

plt.subplot( 2, 1, 1 )
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.plot( audio[50 * 1237:51 * 1237].numpy() )
plt.xlabel( "Original" )

plt.subplot( 2, 1, 2 )
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.plot( X_train[1] )
plt.xlabel( "Windowed" )

plt.show()
plt.close()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: DataSet
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
image = tf.image.rgb_to_grayscale(image)
image = tf.image.resize(image, [24, 18])
( height, width, channel ) = image.shape
train_data, test_data = image[:,:,0:1], image[:,:,0:1]
X_train, y_train = windowed_dataset(train_data[0:24,2:3,0:1], time_step=100)
X_train = tf.constant(X_train, shape=(24, 1))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Plottings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
plt.figure(figsize=( 2, 1 ))
plt.suptitle("Windowed Datasets")

plt.subplot( 2, 1, 1 )
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow( image )
plt.xlabel( "Original" )

plt.subplot( 2, 1, 2 )
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.plot( X_train )
plt.xlabel( "Windowed" )

plt.show()
plt.close()
