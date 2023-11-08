#  <center>Report of Assignment #2
<b><p align="right">Name:HUANG Pizhu</p><b>
<b><p align="right">SID:12332298</p><b>
<b><p align="right">Date:2023/11/6</p><b>

## 1. Significant earthquakes since 2150 B.C.
Read data file Sig_Eqs.tsv, and do some preprocess.Name it as df.
### 1.1
Compute the total number of deaths caused by earthquakes since 2150 B.C. in each country.  
<u>The top ten countries along with the total number of deaths.</u>  
![](p11.png)  

### 1.2
<u>The total number of earthquakes with magnitude larger than 6.0 is as follows.</u> *(I learn the ticks in plotting Broken X-axis from https://zhuanlan.zhihu.com/p/205263612)*  
<img src="p.png" width="500" height="200"> 
<br/>   
The Ring of Fire, located at the boundary between the Pacific Plate, EuThe Ring of Fire, located at the boundary between the Pacific Plate, Eurasian Plate, Indian Plate, Antarctic Plate, and American Plate, is characterized by intense crustal activity and is the most extensive seismic zone in the world. This seismic zone hosts 80% of the world's earthquakes and is the primary location for most catastrophic earthquakes and large-scale (magnitude 8 or higher) global earthquakes.  
<u>Since the year 1600, the number of earthquakes with a magnitude greater than 6 has gradually increased, and this trend has further accelerated after 1850.</u>  This phenomenon can be attributed to the gradual activation of the corresponding tectonic plates within this seismic zone.  
<br/>  

### 1.3
Thw function `CountEq_LargestEq()` returns both (1) the total number of earthquakes since 2150 B.C. in a given country AND (2) the date of the largest earthquake ever happened in this country. *(I get information of some useful function access online https://zhuanlan.zhihu.com/p/340770847, https://blog.csdn.net/PY0312/article/details/88956795 and https://zhuanlan.zhihu.com/p/370851569)*

Output of 146 country   
<img src="p131.png" width="240" height="250"> 

Duplication of country  
<img src="p132.png" width="350" height="350">    

**Handle the duplication and concat. The last Dataframe tdf is as follows.**  
<img src="p132.png" width="450" height="300">   
<br/>  
<br/>  

# 2.Wind speed in Shenzhen during the past 10 years  
  
    
By reading the user guild, the information of wind is in the last column. the 4th part of WND is wind speed.Filter it and clean data with set missing values as average of the numbers before and after.By the way, it has a scale factor 10.  

```python
df['v'] = df['WND'].str.split(',').str[3].astype(int)
df.drop(columns=['WND'],inplace=True)
df = df[df['v'] != 9999]
df['v'] = df['v'].replace(9999,np.nan)
df['v']=df['v'].interpolate()/10  
```  

Resample the hourly data to monthly data  

```python
df['DATE'] = pd.to_datetime(df['DATE'])
df = df.set_index('DATE')
mw = df.resample('M').mean()
```  
Plot Monthly Observation Wind Speed  

![](p2.png) 
<br/>  

Linear fit. The trend of wind is ascending.*(I use the code from this website: https://blog.csdn.net/u013066730/article/details/103297380.)*   
<img src="p22.png" width="510" height="430">  
<br/> 
<br/> 
<br/> 

# 3.Explore a data set
## 3.1 & 3.2  

The Data set, precipitation and temperature of BeiJing, is comes from NCEI.For the precipitation the NaN are subtituded as value 0. And resample hourly data as monthly data and show.
![](p31.png)  
<br/>  

## 3.3  

Use  function `groupby()` to calculate the mean, variance, standard deviation,min,max of 12 month. The description is in PS2.ipynb.    
A boxplot is used to describe the data. Every month has anormal point.The summer has most precipitation which also max varince in the past 70 year.  
<img src="p33.png" width="620" height="350">   
A probability plot is used to Normal Test. p-value is equal to 4.83, so that data is not normally distributed. *(I learn konwledge of normally distribution form https://www.biaodianfu.com/python-normal-distribution-test.html)*  
<img src="p34.png" width="400" height="350">
