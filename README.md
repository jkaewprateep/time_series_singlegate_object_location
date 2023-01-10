# time_series_singlegate_object_location
For study time series with channel window gate for location movement, forward - backward time series. Windowed channel or input mapping can perfrom stregthen or resize of data by reamin significants as you see in the signalings, communication but it also working for gate location in picutre too. Compare of time series location change and bitmap height width networks object location.

## Window series function ##

```
def windowed_dataset(series, time_step):
    dataX, dataY = [], []
    for i in range( math.ceil( len(series) / time_step ) ):
        source = ( time_step * i )
        dest = time_step * ( i + 1 )
        a = series[source : dest, 0]
        dataX.append(a)
        dataY.append(series[source : dest, 0])
	
    return np.array(dataX), np.array(dataY)
```

## Files and Directory ##

| File name | Description  |
--- | --- |
| sample.py | sample codes |
| Figure_1.png | result 100 samples windowed |
| Figure_2.png | result 10 samples windowed |
| Figure_3.png | result 100 samples windowed to image |
| camera_image_position.gif | height-width AI object location |
| README.md | readme file |

## Result ##

#### Window size 10 from the sample ####

![Alt text](https://github.com/jkaewprateep/time_series_singlegate_object_location/blob/main/Figure_1.png "Title")

#### Window size 100 from the sample ####

![Alt text](https://github.com/jkaewprateep/time_series_singlegate_object_location/blob/main/Figure_2.png "Title")

#### Window size 100 from the sample : image ####

![Alt text](https://github.com/jkaewprateep/time_series_singlegate_object_location/blob/main/Figure_3.png "Title")

#### Height - Width Object location ####

![Alt text](https://github.com/jkaewprateep/time_series_singlegate_object_location/blob/main/camera_image_position.gif "Title")


