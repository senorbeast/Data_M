import os
import numpy as np
import pandas as pd
import shutil
from matplotlib.pyplot import figure, legend
import matplotlib.pyplot as plt
import time

Subject_Dir = "Subject_Dir"
Main_Excel = "Main_DB"
Main_Data = "Main_Data"
Graphs_Dir = "Graphs_Dir"


def plotit(fileat, fileName):
    df = pd.read_excel(fileat + fileName)
    newName = fileName.replace(".xlsx", '')
    path = f"{fileat}/{newName}"
    try:
        begin = time.time()
        os.mkdir(path)
        X1 = df.iloc[:, :6]
        X2 = df.iloc[:, 6:12]
        xSca = np.linspace(0, len(df), len(df))
        #print(len(df['Channel 13']), len(xSca))
        plt.figure(1)
        plt.figure(figsize=(30, 15))
        plt.scatter(xSca, df['Channel 13'], s=20, c=["#1f77b4"])
        plt.grid(True)
        plt.legend(["Channel13"], loc="best")
        plt.title(f"{newName}_Channel13")
        plt.yticks(np.linspace(
            min(df['Channel 13']), max(df['Channel 13']), 16))
        plt.savefig(f"{path}/{newName}_Channel13.png", bbox_inches='tight')
        plt.close()

        plt.figure(2)
        plt.figure(figsize=(30, 15))
        plt.scatter(xSca, df['Channel 14'], s=20, marker="^", c=["#ff7f0e"])
        plt.grid(True)
        plt.legend(["Channel14"], loc="best")
        plt.title(f"{newName}_Channel14")
        plt.yticks(np.linspace(
            min(df['Channel 14']), max(df['Channel 14']), 16))
        plt.savefig(f"{path}/{newName}_Channel14.png", bbox_inches='tight')
        plt.close()

        plt.figure(3)
        px1 = X1.plot(subplots=True, figsize=(30, 15),
                      grid=True, title=f"{newName}_1-6", use_index=True, legend=True)[0]
        fig = px1.get_figure()
        fig.tight_layout()
        fig.subplots_adjust(top=0.95)
        plt.savefig(f"{path}/{newName}_1-6.png", bbox_inches='tight')
        plt.close()

        plt.figure(4)
        px2 = X2.plot(subplots=True, figsize=(30, 15),
                      grid=True, title=f"{newName}_7-12")[0]
        fig = px2.get_figure()
        fig.tight_layout()
        fig.subplots_adjust(top=0.95)
        plt.savefig(f"{path}/{newName}_7-12.png", bbox_inches='tight')
        plt.close()

        plt.figure(5)
        plt.figure(figsize=(30, 15))
        plt.scatter(xSca, df['Channel 13'], s=20, c=["#1f77b4"])
        plt.scatter(xSca, df['Channel 14'], s=20, marker="^", c=["#ff7f0e"])
        plt.grid(True)
        plt.legend(["Channel13", "Channel14"], loc="best")
        plt.title(f"{newName}_Combined Channels 13-14")
        cdf = df['Channel 13'].append(df['Channel 14'], ignore_index=True)
        plt.yticks(np.linspace(
            min(cdf), max(cdf), 16))
        plt.savefig(f"{path}/{newName}_Combined_13-14.png",
                    bbox_inches='tight')
        plt.close()

        end = time.time()
        print(f"        {round(end-begin,4)} secs")
    except OSError as error:
        print(error)


def SaveGraphs(Main_Excel, Main_Data, Graphs_Dir):
    Main_df = pd.read_excel(f"{Main_Excel}.xlsx")
    DBdict = Main_df.to_dict('records')
    Mlist = os.listdir(f"./{Main_Data}")
    for i in DBdict:
        if i["Subject_Name"] in Mlist:
            print(f"-> Plotting \033[1m{i['Subject_Name']}\033[0m's Data ")
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
            print(
                f"\033[1m{i['Subject_Name']} \033[0m not found in Main_Data")


if __name__ == '__main__':
    SaveGraphs(Main_Excel, Main_Data, Graphs_Dir)
