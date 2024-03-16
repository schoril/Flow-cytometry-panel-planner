import pandas as pd
from GUI_function import create_gui
from condition_functions import (
    Ag_expression_flourophore_assignment,
    fluorophore_assignment,
)

data_frames = []

# List of sheet names
filename = "Abs_list.xlsx"  # Abs = antibodies
sheet_names = [
    "Available_Abs",
    "Ab_expression_level",
    "Fluorophore_info",
    "Fluorophore_overlap",
]

# Load each sheet into a DataFrame
for sheet_name in sheet_names:
    data_frames.append(pd.read_excel(filename, sheet_name=sheet_name))

Available_Abs_df = data_frames[0]
antigen_info_df = data_frames[1]
Fluorophore_info_df = data_frames[2]
Fluorophore_overlap_df = data_frames[3]

# generate a list af all available antigens (Ag) from the excel
Ab_list = antigen_info_df["Antigen_name"].to_list()

# create a dictionary with overlaping fluorophores (overlap is fluorophore similarity > 0.7)
overlap_dict = {}
for index, row in Fluorophore_overlap_df.iterrows():
    fluorophore = row["Fluorophore"]
    overlaps = row.drop("Fluorophore").to_dict()
    similar_fluorophores = [key for key, value in overlaps.items() if value >= 0.7]
    overlap_dict[fluorophore] = similar_fluorophores

# to print the dict:
# for key, value in overlap_dict.items():
#    print(f"{key}: {', '.join(value)}")

# create intensety dict extracting the intensety data of each fluorophore from the excel
intensety_dict = {}
for color in Fluorophore_info_df["Fluorophore"]:
    intensety_dict[color] = (
        Fluorophore_info_df["fluorophore intensety"]
        .loc[Fluorophore_info_df["Fluorophore"] == color]
        .values[0]
    )
intensety_dict

# Ask user to choose antigens calling GUI function
selected_ags = create_gui(Ab_list)

# extract the expression levels of choosen antigens
ag_intensety_dict = {}
for antigen in selected_ags:
    ag_row = antigen_info_df.loc[antigen_info_df["Antigen_name"] == antigen]
    ag_intensety_dict[antigen] = ag_row["expression_levels"].values[0].strip()


# extract the fluorecence options for each selected antigen
ab_fluorescence_dict = {}
for antigen in selected_ags:
    antibody_row = Available_Abs_df.loc[Available_Abs_df["Antigen"] == antigen, "Fluorophore"]
    fluorophores_list = antibody_row.tolist()  # Convert specific column values to list
    ab_fluorescence_dict[antigen] = fluorophores_list

print(type(ab_fluorescence_dict))


## filtering Abs based on antigen expression level
Ab_option_dict = Ag_expression_flourophore_assignment(
    ab_fluorescence_dict, ag_intensety_dict, intensety_dict
)
print(Ab_option_dict)

## assigning flourophores to each antigen avoiding overlap
final_assignment = fluorophore_assignment(Ab_option_dict, overlap_dict)
print(final_assignment)