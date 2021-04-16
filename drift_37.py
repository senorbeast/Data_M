# %%
import os
import pandas as pd
import time
# %%

Subject_Dir = "Subject_Dir"

Drifts_DB = "Drift_37"


# Calculate Drifts for each column
def drift(df, chlNo):
    return max(df[f"{chlNo}"]) - min(df[f"{chlNo}"])


def calc_drift(Sub_ID):
    # Files in Subject ID
    Flist = os.listdir(f"./{Subject_Dir}/{Sub_ID}")
    Drift_df = pd.read_excel(f'{Drifts_DB}.xlsx', engine="openpyxl")

    # Just initialized to zero (if any problem then 0 will be used)
    hb_1, hb_2 = 0, 0
    hc_1, hc_2 = 0, 0
    vb_1, vb_2 = 0, 0
    vc_1, vc_2 = 0, 0

    for i in Flist:  # (FList is a subject)
        if (i == f"{Sub_ID} handbase.xlsx"):
            Main_df = pd.read_excel(f"./{Subject_Dir}/{Sub_ID}/{i}")
            hb_1, hb_2 = drift(Main_df, 'Channel 3'), drift(
                Main_df, 'Channel 7')
        elif (i == f"{Sub_ID} handcog.xlsx"):
            Main_df = pd.read_excel(f"./{Subject_Dir}/{Sub_ID}/{i}")
            hc_1, hc_2 = drift(Main_df, 'Channel 3'), drift(
                Main_df, 'Channel 7')
        elif (i == f"{Sub_ID} vestbase.xlsx"):
            Main_df = pd.read_excel(f"./{Subject_Dir}/{Sub_ID}/{i}")
            vb_1, vb_2 = drift(Main_df, 'Channel 3'), drift(
                Main_df, 'Channel 7')
        elif (i == f"{Sub_ID} vestcog.xlsx"):
            Main_df = pd.read_excel(f"./{Subject_Dir}/{Sub_ID}/{i}")
            vc_1, vc_2 = drift(Main_df, 'Channel 3'), drift(
                Main_df, 'Channel 7')
    # Saving data collected from each file to df
    Drift_df.loc[len(Drift_df.index)] = [Sub_ID,
                                         hb_1, hb_2,
                                         hc_1, hc_2,
                                         vb_1, vb_2,
                                         vc_1, vc_2, ]
    # print(Drift_df)

    Drift_df.to_excel(f'{Drifts_DB}.xlsx', index=False)


if __name__ == '__main__':
    Slist = os.listdir(f"{Subject_Dir}")
    for i in Slist:
        print(f"-> Calculating Drifts Channel 3 and 7 of {i}")
        begin = time.time()
        calc_drift(i)
        end = time.time()
        print(f"        {round(end-begin,4)} secs")
