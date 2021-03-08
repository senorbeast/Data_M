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
    newName = fileName.replace(".xlsx", '')
    path = f"{fileat}/{newName}"
    try:
        os.mkdir(path)
        X1 = df.iloc[:, :6]
        X2 = df.iloc[:, 6:12]
        xSca = np.linspace(0, len(df), len(df))

        #print(len(df['Channel 13']), len(xSca))
        plt.figure(1)
        plt.figure(figsize=(30, 15))
        plt.scatter(xSca, df['Channel 13'], s=7)
        plt.grid(True)
        plt.savefig(f"{path}/Channel13.png", bbox_inches='tight')
        plt.figure(2)
        plt.figure(figsize=(30, 15))
        plt.scatter(xSca, df['Channel 14'], s=7)
        plt.grid(True)
        plt.savefig(f"{path}/Channel14.png", bbox_inches='tight')
        plt.figure(5)
        plt.figure(figsize=(30, 15))
        plt.scatter(xSca, df['Channel 13'], s=7)
        plt.scatter(xSca, df['Channel 14'], s=7)
        plt.grid(True)
        plt.savefig(f"{path}/Combine13-14.png", bbox_inches='tight')
        plt.figure(3)
        X1.plot(subplots=True, figsize=(30, 15), grid=True,)
        plt.legend(loc="best")
        plt.savefig(f"{path}/1-6.png", bbox_inches='tight')
        plt.figure(4)
        X2.plot(subplots=True, figsize=(30, 15), grid=True)
        plt.legend(loc="best")
        plt.savefig(f"{path}/6-12.png", bbox_inches='tight')

    except OSError as error:
        print(error)


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
