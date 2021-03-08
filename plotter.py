import os
import numpy as np
import pandas as pd
import shutil
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

Subject_Dir = "Subject_Dir"
Main_Excel = "Main_DB"
Main_Data = "Main_Data"
Graphs_Dir = "Graphs_Dir"


def plotit(fileat, fileName):
    df = pd.read_excel(fileat + fileName)
    df.plot(subplots=True, figsize=(30, 15), grid=True)
    plt.legend(loc="best")
    newName = fileName.replace(".xlsx", '')
    plt.savefig(f"{fileat}/{newName}.png", bbox_inches='tight')


def SaveGraphs(Main_Excel, Main_Data, Graphs_Dir):
    Main_df = pd.read_excel(f"{Main_Excel}.xlsx")
    DBdict = Main_df.to_dict('records')
    Mlist = os.listdir(f"./{Main_Data}")
    z = 0
    for i in DBdict:
        z += 1
        if i["Subject_Name"] in Mlist:
            print(f"Doing {z}")
            # Copy folder and rename it, if in DB
            try:
                shutil.copytree(
                    f"./{Main_Data}/{i['Subject_Name']}", f"./{Graphs_Dir}/{i['Subject_Name']}")
                Sub_Files = os.listdir(
                    f"./{Graphs_Dir}/{i['Subject_Name']}")
                filePos = f"{Graphs_Dir}/{i['Subject_Name']}/"
                for fileNms in Sub_Files:
                    plotit(filePos, fileNms)
                    os.remove(f"{filePos}{fileNms}")
            except OSError as error:
                print(error)

        else:
            print(f"{i['Subject_Name']} not found in Main_Data")


if __name__ == '__main__':
    SaveGraphs(Main_Excel, Main_Data, Graphs_Dir)
