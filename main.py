# %%

import os
import glob
import pandas as pd
import shutil

# * Copy raw files to Raw_Data_Reservoir and to Reservoir_Copy ✅
# ? Names of Raw Data - subject base, subject vest, subject hand, subject anything
# * Read files from Reservoir_Copy✅
# * Files from Raw_Data convert to xlsx ✅
# * Save xlsx files to a folder named "Subject" in Main_Data ✅
# ? Main_Data->"Subject" Folder -> subject base.xlsx, subject vest.xlsx, subject hand.xlsx, subject anything.xlsx✅
# Files with same name in New_Raw_Data will be replaced in Raw_Data_Reservoir - Fixed ✅

# %%

New_Raw_Data = "New_Raw_Data"
Raw_Data_Reservoir = "Raw_Data_Reservoir"
Reservoir_Copy = "Wk_dir"
Main_Data = "Main_Data"
Subject_Dir = "Subject_Dir"
Main_Excel = "Main_DB"

# %%

# Check Subject Name in DB and get new Name


def getName(SubName, names, z):
    if SubName in names:
        z = z + 1
        SubName = SubName + f"_{z}"
        return getName(SubName, names, z)
    else:
        return SubName


def getNewNamefromDB(SubName, Main_Excel):
    Main_df = pd.read_excel(f"{Main_Excel}.xlsx")
    nameSeries = Main_df['Subject_Name'].squeeze()
    names = nameSeries.tolist()
    z = 1
    NewSubName = getName(SubName, names, z)
    return NewSubName

# Save created Subject folder to DB


def SaveNewSubtoDB(SubName, Main_Excel):
    Main_df = pd.read_excel(f"{Main_Excel}.xlsx")
    Main_df.loc[len(Main_df.index)] = [SubName, len(Main_df.index)+1]
    Main_df.to_excel(f'{Main_Excel}.xlsx', index=False)

# %%


def chkList(lst):
    return len(set(lst)) == 1


def CopMov(New_Raw_Data, Raw_Data_Reservoir, Reservoir_Copy, Main_Excel):
    Main_df = pd.read_excel(f"{Main_Excel}.xlsx")

    # * Copy raw files to Raw_Data_Reservior and move to Reservoir_Copy
    fileList = os.listdir(New_Raw_Data)

    sub_name_list = []
    for f in fileList:
        sub_name_list.append(f.split()[0])

    nameSeries = Main_df['Subject_Name'].squeeze()
    names = nameSeries.tolist()

    if chkList(sub_name_list) == True:
        if sub_name_list[0] in names:
            NewName = getNewNamefromDB(sub_name_list[0], Main_Excel)
        else:
            NewName = sub_name_list[0]
        NewFiles = []

        for files in fileList:
            NewFiles.append(files.replace(sub_name_list[0], NewName))

        for a in range(len(NewFiles)):
            shutil.copy2(f'./{New_Raw_Data}/{fileList[a]}',
                         f'./{Raw_Data_Reservoir}/{NewFiles[a]}')
            shutil.move(f'./{New_Raw_Data}/{fileList[a]}',
                        f'./{Reservoir_Copy}/{NewFiles[a]}')
    else:
        print("Files in New_Raw_Data not of same subject")

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

    if chkList(sub_name_list) == True:
        # path
        NewName = sub_name_list[0]
        path = f'{Main_Data}/{NewName}'
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        saveExcel(Reservoir_Copy, path)
        SaveNewSubtoDB(NewName, Main_Excel)
        print("Equal")

    else:
        print("Not Equal")

# %%


def del_copy(Reservoir_Copy):
    for file in glob.glob(f"{Reservoir_Copy}/*"):
        os.remove(file)


# %%
if __name__ == '__main__':
    CopMov(New_Raw_Data, Raw_Data_Reservoir, Reservoir_Copy, Main_Excel)
    creFol_saveXl(Main_Data, Reservoir_Copy)
    del_copy(Reservoir_Copy)


# %%
