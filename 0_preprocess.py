# # convert raw_excel to csv
# import pandas as pd
# import numpy as np
# folder_path = "/Users/apple/Desktop/202108eyeml/A/AP1_check/"
# for i in range(1,31):
#     if i <= 9:
#         path_xlsx = folder_path + "A0" + str(i) + ".xlsx"
#         path_csv = folder_path+ "A0" + str(i) + ".csv"
#         read_file = pd.read_excel (path_xlsx, engine='openpyxl')
#         read_file.to_csv (path_csv, index = None, header=True) 
#     else:
#         path_xlsx = folder_path + "A" + str(i) + ".xlsx"
#         path_csv = folder_path+ "A" + str(i) + ".csv"
#         read_file = pd.read_excel (path_xlsx, engine='openpyxl')
#         read_file.to_csv (path_csv, index = None, header=True) 


# keep column : "start time", "x", "y", "duration"
# keep duration between onset_time & onset_time+14000
# delete point outside AOI
# output as `Q1-1_new.csv`
folder_path = "/Users/apple/Desktop/202108eyeml/A/AP1_check/"
for i in range(1,31):
    if i <= 9:
        path_csv = folder_path + "A0" + str(i) + ".csv"
        new_path_csv = folder_path + "A0" + str(i) + "_allQ.csv"
        df = pd.read_csv(path_csv)
        df_p1_1 = df[df['CURRENT_FIX_START'] < 14000] # 1-1 Q
        df_p1_1 = df_p1_1[(df_p1_1['CURRENT_FIX_X'] >= 88) & (df_p1_1['CURRENT_FIX_X'] <= 854) & (df_p1_1['CURRENT_FIX_Y'] >= 124) & (df_p1_1['CURRENT_FIX_Y'] <= 603)] # xy in AOI
        df_drop_column = df_p1_1.drop(df_p1_1.columns[[1, 6, 7, 8]], axis=1) 
        df_drop_column.to_csv(new_path_csv, index = None, header=True) 
    else:
        path_csv = "/Users/apple/Documents/2021eye/testQ01_1/raw_fix/A" + str(i) + ".csv"
        new_path_csv = "/Users/apple/Documents/2021eye/testQ01_1/raw_fix/A" + str(i) + "_Q1-1.csv"
        df = pd.read_csv(path_csv)
        df_p1_1 = df[df['CURRENT_FIX_START'] < 14000]
        df_p1_1 = df_p1_1[(df_p1_1['CURRENT_FIX_X'] >= 88) & (df_p1_1['CURRENT_FIX_X'] <= 854) & (df_p1_1['CURRENT_FIX_Y'] >= 124) & (df_p1_1['CURRENT_FIX_Y'] <= 603)]
        df_drop_column = df_p1_1.drop(df_p1_1.columns[[1, 6, 7, 8]], axis=1)
        df_drop_column.to_csv(new_path_csv, index = None, header=True) 


###### new data not deleting fixation outside AOI ######
# delete duration<14000
# drop column : "start time", "previous distance", "x resolution", "yresolution"
# output as `A101_allAOI.csv`
 
import pandas as pd

for i in range(1,31):
    if i <= 9:
        path_csv = "/Users/apple/Documents/2021eye/testQ01_1/raw_fix/A0" + str(i) + ".csv"
        new_path_csv = "/Users/apple/Documents/2021eye/testQ01_1/raw_fix/A0" + str(i) + "_Q1-1_allxy.csv"
        df = pd.read_csv(path_csv)
        df_p1_1 = df[df['CURRENT_FIX_START'] < 14000] # 1-1 Q
        df_drop_column = df_p1_1.drop(df_p1_1.columns[[1, 6, 7, 8]], axis=1) 
        df_drop_column.to_csv(new_path_csv, index = None, header=True) 
    else:
        path_csv = "/Users/apple/Documents/2021eye/testQ01_1/raw_fix/A" + str(i) + ".csv"
        new_path_csv = "/Users/apple/Documents/2021eye/testQ01_1/raw_fix/A" + str(i) + "_Q1-1_allxy.csv"
        df = pd.read_csv(path_csv)
        df_p1_1 = df[df['CURRENT_FIX_START'] < 14000]
        df_drop_column = df_p1_1.drop(df_p1_1.columns[[1, 6, 7, 8]], axis=1)
        df_drop_column.to_csv(new_path_csv, index = None, header=True) 