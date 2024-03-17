from xlsx_function import import_xlsx_function
from GUI_function import create_gui
from condition_functions import (
    Ag_expression_flourophore_assignment,
    fluorophore_assignment,
)
from dict_functions import (
    overlap_function,
    intensety_function,
    ag_expression_level,
    available_flourophore
)

data_frames = import_xlsx_function('Abs_list.xlsx')

available_abs_df = data_frames[0]
antigen_info_df = data_frames[1]
fluorophore_info_df = data_frames[2]
fluorophore_overlap_df = data_frames[3]

# generate a list af all available antigens (Ag) from the excel
ab_list = antigen_info_df["Antigen_name"].to_list()

# create a dictionary with overlaping fluorophores (overlap is fluorophore similarity > 0.7)
overlap_dict = overlap_function(fluorophore_overlap_df)

# create intensety dict extracting the intensety data of each fluorophore from the excel
intensety_dict = intensety_function(fluorophore_info_df)

# Ask user to choose antigens calling GUI function
selected_ags = create_gui(ab_list)

# extract the expression levels of selected antigens
ag_intensety_dict = ag_expression_level(selected_ags, antigen_info_df)

# extract the fluorecence options for each selected antigen
ab_fluorescence_dict = available_flourophore (selected_ags, available_abs_df)

## filtering Abs based on antigen expression level
ab_option_dict = Ag_expression_flourophore_assignment(
    ab_fluorescence_dict, ag_intensety_dict, intensety_dict
)
print(ab_option_dict)

## assigning flourophores to each antigen avoiding overlap
final_assignment = fluorophore_assignment(ab_option_dict, overlap_dict)
print(final_assignment)