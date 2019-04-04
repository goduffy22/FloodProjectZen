# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:50:55 2019

@author: Alex Charlesworth
"""
# =============================================================================
# Temperature
# =============================================================================
import pandas as pd

file_path = r'C:\Floods\data\CEDA data\UK daily temperature\midas_tempdrnl_{}01-{}12.csv'

temp_data=pd.DataFrame()
list1 = list()
for i in range(2008,2020):
    list1.append(pd.read_csv(file_path.format(i,i),
                 names=('date','id_type','id','hour_count','version_num','domain_name',
                        'src_id','state_indicator','max_air_temp_(degC)','min_air_temp_(degC)',
                        'min_grass_temp_(degC)','min_conc_temp_(degC)','max_air_temp_q','min_air_temp_q',
                        'min_grass_temp_q','min_conc_temp_q','met_timestamp',
                        'midas_timestamp','max_air_temp_j','min_air_temp_j',
                        'min_grass_temp_j','min_conc_temp_j')
                 ) # Close dataframe constructor
    ) # Close list

temp_data= pd.concat(list1)

#df = pd.DataFrame(temp_data.iloc[0:500,:])

temp_data.drop(["hour_count","version_num","max_air_temp_q","min_air_temp_q",
                "min_grass_temp_q","min_conc_temp_q","midas_timestamp","max_air_temp_j",
                "min_air_temp_j","min_grass_temp_j","min_conc_temp_j","state_indicator"],
                axis=1,inplace=True)

# Checking column for uniqueness
#list3 = []
#for i in temp_data['id_type'].unique():
#    list3.append(i)

mini_temp_df = temp_data.sample(1000)

#test_mask = (temp_data['src_id'] == 56906)
#test_df = temp_data[test_mask]
# =============================================================================
# Rainfall
# =============================================================================

import pandas as pd
import numpy as np

file_path = r'C:\Floods\data\CEDA data\UK daily rainfall\midas_raindrnl_{}01-{}12.csv'

#read data into dataframe
rain_data=pd.DataFrame()
list1 = list()
for i in range(2008,2020):
    list1.append(pd.read_csv(file_path.format(i,i),
                 usecols=list(np.arange(0,15)),
                 names=("id","id_type","ob_date","version_num","met_domain_name",
                        "observation_time","observation_day_count","src_id","state_indicator",
                        "precipitation_amount_(mm)","day_cnt_Q","prcp_cnt_Q","met_timestamp",
                        "midas_TS","prcp_J")
                 ) # close dataframe constructor
    ) # close list
rain_data= pd.concat(list1)

#Drop Columns
rain_data.drop(["observation_day_count","version_num","day_cnt_Q","prcp_cnt_Q",
                "midas_TS","prcp_J","state_indicator","observation_time"],axis=1,inplace=True)

# Checking column for uniqueness
#list2 = []
#for i in rain_data['id_type'].unique():
#    list2.append(i)
    
#df_17 = list1[-3].head()

#df_15 = list1[-5].head()
#df_15=list1[-5]
#import numpy as np
#pp = df_15[df_15['prcp_J'] != np.nan].sample(50)

mini_rain_df = rain_data.sample(1000)

# =============================================================================
# Wind
# =============================================================================

import pandas as pd

file_path = r'C:\Floods\data\CEDA data\UK daily wind\midas_wind_{}01-{}12.csv'

#read data into dataframe
wind_data=pd.DataFrame()
list1 = list()
for i in range(2008,2020):
    list1.append(pd.read_csv(file_path.format(i,i),
                 #usecols=list(np.arange(0,15)),
                 names=("date","id_type","id","ob_hour_count","met_domain_name","version_num",
                        "src_id","state_indicator","mean_wind_dir","mean_wind_speed_(knots)",
                        "max_gust_dir","max_gust_speed","max_gust_ctime","mean_wind_dir_q",
                        "mean_wind_speed_q","max_gust_dir_q","max_gust_speed_q","max_gust_ctime_q",
                        "met_timestamp","midas_stmp_etime","mean_wind_dir_j","mean_wind_speed_j",
                        "max_gust_dir_j","max_gust_speed_j")
                 ) # close dataframe constructor
    ) # close list
wind_data = pd.concat(list1)

#Drop Columns
wind_data.drop(["ob_hour_count","version_num","state_indicator","mean_wind_dir","max_gust_dir",
                "max_gust_ctime","mean_wind_dir_q","mean_wind_speed_q","max_gust_dir_q","max_gust_speed_q",
                "max_gust_ctime_q","midas_stmp_etime","mean_wind_dir_j","mean_wind_speed_j",
                "max_gust_dir_j","max_gust_speed_j"],axis=1,inplace=True)
# Checking column for uniqueness
#list2 = []
#for i in wind_data['met_domain_name'].unique():
#    list2.append(i)

#test random points in df
mini_wind_df = wind_data.sample(1000)

# =============================================================================
# Weather
# =============================================================================
import pandas as pd

file_path = r'C:\Floods\data\CEDA data\UK daily weather\midas_wxdrnl_{}01-{}12.csv'

#read data into dataframe
weather_data=pd.DataFrame()
list1 = list()
for i in range(2008,2020):
    list1.append(pd.read_csv(file_path.format(i,i),
                 #usecols=list(np.arange(0,15)),
                 names=("date","id","id_type","observation_hour","version_num","met_domain_name",
                        "src_id","rec_st_ind","cs_24hr_sun_dur","concrete_state","lying_snow_flag","snow_depth_(cm)",
                        "frsh_snw_amt_(cm)","snow_day_id","hail_day_id","thunder_day_flag","gale_day_flag",
                        "frsh_mnt_snwfall_flag","wmo_24hr_sun_dur","cs_24hr_sun_dur_q","conc_state_id_q",
                        "snow_depth_q","frsh_snw_amt_q","snow_day_id_q","hail_day_id_q",
                        "thunder_day_flag_q","gale_day_flag_q","wmo_24hr_sun_dur_q","met_timestamp",
                        "midas_stmp_etime","drv_24hr_sun_dur","drv_24hr_sun_dur_q",
                        "lying_snow_ht","lying_snow_ht_q")
                 ) # close dataframe constructor
    ) # close list
weather_data = pd.concat(list1)

#Drop Columns
weather_data.drop(["observation_hour","version_num","rec_st_ind","cs_24hr_sun_dur",
                "conc_state_id_q","cs_24hr_sun_dur_q","wmo_24hr_sun_dur","snow_depth_q",
                "frsh_snw_amt_q","snow_day_id_q","hail_day_id_q","thunder_day_flag_q",
                "gale_day_flag_q","wmo_24hr_sun_dur_q","midas_stmp_etime","drv_24hr_sun_dur",
                "drv_24hr_sun_dur_q","lying_snow_ht","lying_snow_ht_q"],axis=1,inplace=True)

# Checking column for uniqueness
#list2 = []
#for i in weather_data['met_domain_name'].unique():
#    list2.append(i)

#test random points in df
mini_weather_df = weather_data.sample(1000)

# %% ==========================================================================
# Importing to SQL
# =============================================================================

import pyodbc
import sqlalchemy
import csv

engine = sqlalchemy.create_engine("mssql+pyodbc://ffk:8vCWsT@192.168.101.109/floodforce?driver=SQL+Server+Native+Client+11.0", echo=False)

##ALREADY IMPORTED## temp_data.to_sql('temperature', con=engine, if_exists='replace',index=False)
##ALREADY IMPORTED## wind_data.to_sql('wind', con=engine, if_exists='replace',index=False)
##ALREADY IMPORTED## weather_data.to_sql('weather', con=engine, if_exists='replace',index=False)
##RAIN DATA DONE##
# =============================================================================
# # Batch importing to SQL
# =============================================================================


data = wind_data        # Set DataFrame to import to SQL
n=50000                 # Batch size
file_path = r'C:\Floods\data\CEDA data\failed SQL imports\wind\\' #Set filepath for failed imports
table_name = 'wind' # Set imported tablename

for i in np.arange(0,len(data),n):
    if i == 0:
        data.head(n).to_sql(table_name, con=engine, if_exists='replace',index=False)
        print("Succesfully imported the first {} data points".format(n))
    elif len(data) - i > n:
        try:
            data[i:i+n].to_sql(table_name, con=engine, if_exists='append',index=False)
            print("Succesfully imported 50000 data points above {}".format(i))
        except:
            print("FAILED to import the 50000 data points above {}".format(i))
            data[i:i+n].to_csv(file_path+'failed_'+'wind'+'_import'+str(i)+"_"+str(i+n)+'.csv'
                        ,index=None
                        ,header=True)
    else:
        try:
            data[i:len(data)].to_sql(table_name, con=engine, if_exists='append',index=False)
            print("Succesfully imported the last {} data points ".format(len(data)-i))
        except:
            print("FAILED to import the 50000 data points above {}".format(i))
            data[i:len(data)].to_csv(file_path+'failed_'+'wind'+'_import'+str(i)+"_"+str(len(data))+'.csv'
                        ,index=None
                        ,header=True)

engine.dispose()
























