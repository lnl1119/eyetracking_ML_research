# convert raw_excel to csv
import pandas as pd
folder_path = "/Users/apple/Desktop/deep_eye/dataset/onset_time_C/"
for i in range(1,31):
    if i <= 9:
        path_xlsx = folder_path + "C0" + str(i) + ".xlsx"
        path_csv = folder_path + "C0" + str(i) + ".csv"
        read_file = pd.read_excel (path_xlsx, engine='openpyxl')
        read_file.to_csv (path_csv, index = None, header=True) 
    else:
        path_xlsx = folder_path + "C" + str(i) + ".xlsx"
        path_csv = folder_path + "C" + str(i) + ".csv"
        read_file = pd.read_excel (path_xlsx, engine='openpyxl')
        read_file.to_csv (path_csv, index = None, header=True) 
