# %%
import os
import glob
import pandas as pd
import shutil

# * Copy raw files to Raw_Data_Reservoir and to Reservoir_Copy ✅
# ? Names of Raw Data - subject_base, subject_vest, subject_hand
# * Read files from Reservoir_Copy✅
# * Files from Raw_Data convert to xlsx ✅
# * Save xlsx files to a folder named "Subject" in Main_Data
# ? Main_Data->"Subject" Folder -> subject_base.xlxs, subject_vest.xlxs, subject_hand.xlxs

# %%

New_Raw_Data = "New_Raw_Data"
Raw_Data_Reservoir = "Raw_Data_Reservoir"
Reservoir_Copy = "Wk_dir"
Main_Data = "Main_Data"
Subject_Dir = "Subeject_Dir"


# %%


def CopMov(New_Raw_Data, Raw_Data_Reservoir, Reservoir_Copy):
    # * Copy raw files to Raw_Data_Reservior and move to Reservoir_Copy
    fileList = os.listdir(New_Raw_Data)
    for files in fileList:
        shutil.copy2(f'./{New_Raw_Data}/{files}',
                     f'./{Raw_Data_Reservoir}/{files}')
        shutil.move(f'./{New_Raw_Data}/{files}',
                    f'./{Reservoir_Copy}/{files}_copy')

# %%


def saveExcel(Reservoir_Copy, Save_loc):
    # * Read files from Reservoir_Copy
    # * Files from Raw_Data convert to xlsx
    fileList2 = os.listdir(Reservoir_Copy)
    df_new = []
    for files2 in fileList2:
        # Reading the csv file
        df_new = pd.read_csv(f'./{Reservoir_Copy}/{files2}')
        # saving xlsx file
        # To change folder according to Subject Name
        GFG = pd.ExcelWriter(f'{Save_loc}/{files2}.xlsx')
        df_new.to_excel(GFG, index=False)
        GFG.save()
    # pass
# print(df_new)

# %%


def creFol_saveXl(Main_Data, Reservoir_Copy):
    # * Save xlsx files to a folder named "Subject" in Main_Data
    fileList3 = os.listdir(Reservoir_Copy)
    sub_name_list = []
    for f in fileList3:
        sub_name_list.append(f.split()[0])

    # Check if all elements in array are equal

    def chkList(lst):
        return len(set(lst)) == 1

    if chkList(sub_name_list) == True:
        # path
        path = f'{Main_Data}/{sub_name_list[0]}'
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        saveExcel(Reservoir_Copy, path)
        print("Equal")

    else:
        print("Not Equal")

# %%


def del_copy(Reservoir_Copy):
    for file in glob.glob(f"{Reservoir_Copy}/*"):
        os.remove(file)


# %%
CopMov(New_Raw_Data, Raw_Data_Reservoir, Reservoir_Copy)
creFol_saveXl(Main_Data, Reservoir_Copy)
del_copy(Reservoir_Copy)
# %%
