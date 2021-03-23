# Instructions

Run the Organise.bat after ALL subject1 files (2-4 files) are in the New_Raw_Data folder
Name your raw files as 

        "subject1 handbase", 
        "subject1 handcog", 
        "subject1 vestbase", 
        "subject1 vestcog",

                the inbetween space is necessary 

Different Scripts:
    1)Organise - Converts to xlsx and stores name in Main_Data.xlsx
    2)Convert - Hides the SubjectName and replaces by Subject ID
    3)Graph_Plotter - Plots Graphs in Graphs_Dir
    4)Drift_Excel - Fills in Drifts_DB.xlsx  (More on that here .....)


#Additional Info

Will be organised as follows

Main_Data/
├── Subject1/
│   ├── Subject1 handbase.xlsx
│   ├── Subject1 handcog.xlsx
│   ├── Subject1 vestbase.xlsx
│   └── Subject1 vestcog.xlsx
├── Subject2/
│   ├── Subject1 handbase.xlsx
│   ├── Subject1 handcog.xlsx
│   ├── Subject1 vestbase.xlsx
│   └── Subject1 vestcog.xlsx
└─ ...

Repeated Names will stored as 
-> Gopal, Gopal_2, Gopal_2_3, Gopal_2_3_4

!!! Will Require a minimum of 2 names in DB to work properly 

All raw files will be saved in Raw_Data_Reservoir
