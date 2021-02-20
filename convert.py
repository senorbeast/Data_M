import os
import shutil
import pandas as pd
import numpy as np

Subject_Dir = "Subject_Dir"
Main_Excel = "Main_DB"
Main_Data = "Main_Data"


def Convert(Main_Excel, Main_Data, Subject_Dir):
    Main_df = pd.read_excel(f"{Main_Excel}.xlsx")
    DBdict = Main_df.to_dict('records')
    Mlist = os.listdir(f"./{Main_Data}")
    for i in DBdict:
        if i["Subject_Name"] in Mlist:
            # Copy folder and rename it, if in DB
            try:
                shutil.copytree(
                    f"./{Main_Data}/{i['Subject_Name']}", f"./{Subject_Dir}/SubjectID_{i['Subject_ID']}")
                Sub_Files = os.listdir(
                    f"./{Subject_Dir}/SubjectID_{i['Subject_ID']}")
                sub_names = []
                for j in range(len(Sub_Files)):
                    name1 = Sub_Files[j]
                    name2 = Sub_Files[j].split()[0]
                    name = name1.replace(name2, '')
                    sub_names.append(name)
                    os.rename(f"./{Subject_Dir}/SubjectID_{i['Subject_ID']}/{Sub_Files[j]}",
                              f"./{Subject_Dir}/SubjectID_{i['Subject_ID']}/SubjectID_{i['Subject_ID']}{sub_names[j]}")
            except OSError as error:
                print(error)

        else:
            print(f"{i['Subject_Name']} not found in Main_Data")


if __name__ == '__main__':
    Convert(Main_Excel, Main_Data, Subject_Dir)
