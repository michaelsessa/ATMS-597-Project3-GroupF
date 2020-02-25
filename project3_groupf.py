# -*- coding: utf-8 -*-
"""Project3_GroupF

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qEpQ7pr3JbotG-1hH5s_h5dscpfTPeUW
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline
import xarray as xr
import pandas as pd

!pip install netcdf4
!pip install pydap
!pip install wget

#Download the data using wget for each year by asking for all .nc daily precipitation files
!wget -r -A gpcp_v01r03_daily_d*.nc 'https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/'

# Save the precipitation data by year and for the gridpoint closest to Cordoba, Argentina
data_1996 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/1996/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_1997 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/1997/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_1998 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/1998/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_1999 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/1999/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2000 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2000/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2001 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2001/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2002 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2002/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2003 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2003/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2004 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2004/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2005 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2005/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2006 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2006/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2007 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2007/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2008 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2008/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2009 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2009/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2010 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2010/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2011 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2011/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2012 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2012/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2013 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2013/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2014 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2014/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2015 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2015/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2016 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2016/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2017 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2017/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2018 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2018/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')
data_2019 = xr.open_mfdataset('www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2019/*.nc').sel(longitude=-64.188+360.,latitude=31.4201, method='nearest')

#Remove duplicate days to allow for the merging of the yearly datasets
data_2014_d=data_2014.sel(time=~data_2014.indexes['time'].duplicated())
data_2017_d=data_2017.sel(time=~data_2017.indexes['time'].duplicated())
data_2018_d=data_2018.sel(time=~data_2018.indexes['time'].duplicated())

#Merge the data 
yearly_data=xr.merge([data_1996,data_1997,data_1998,data_1999,data_2000,data_2001,data_2002,data_2003,data_2004,data_2005,data_2006,data_2007,data_2008,data_2009,data_2010,data_2011,data_2012,data_2013,data_2014_d,data_2015,data_2016,data_2017_d,data_2018_d,data_2019])

# Create a date range to select only the desired DJF months from the larger precipitation dataset
dates=pd.date_range('19961001','20191130')
df = pd.DataFrame({'a': range(8461)}, index=dates)  

season = ((df.index.month % 12 + 3) // 3).map({1:'DJF', 2: 'MAM', 3:'JJA', 4:'SON'})

df_winter = df[season == 'DJF']
dates2=df_winter.index.strftime("%Y%m%d")
dates2

date_index = df_winter.index

# Save the precipitation variable
yearly_precip = yearly_data['precip']

# Save only DJF data
DJF_daily_precip=yearly_precip.sel(time=date_index)

#Convert xarray DataArray to a pandas dataframe
pd_DJF_daily_precip = xr.DataArray.to_dataframe(DJF_daily_precip)

#Replace -99999.0000 values with NaN
DJF_daily_precip=pd_DJF_daily_precip.replace(-99999.000000,NaN)

#Save 95th precentile data
DJF_daily_precip['precip'].quantile(.95)

DJF_daily_precip['precip']>16.757933
rslt_df = dataframe[dataframe['Percentage'] > 80]

DJF_daily_precip_95=DJF_daily_precip[DJF_daily_precip['precip']>DJF_daily_precip['precip'].quantile(0.95)]

DJF_daily_precip_95

print(DJF_daily_precip_95.index)

