# create a dictionary with overlaping fluorophores (overlap is fluorophore similarity > 0.7)
def overlap_function(df):
    overlap_dict = {}
    for index, row in df.iterrows(): 
        fluorophore = row["Fluorophore"]
        overlaps = row.drop("Fluorophore").to_dict()
        similar_fluorophores = [key for key, value in overlaps.items() if value >= 0.7]
        overlap_dict[fluorophore] = similar_fluorophores
    return overlap_dict

# create intensety dict extracting the intensety data of each fluorophore from the excel
def intensety_function(df):
    intensety_dict = {}
    for color in df["Fluorophore"]:
        intensety_dict[color] = (
            df["fluorophore intensety"]
            .loc[df["Fluorophore"] == color]
            .values[0]
            )
    return intensety_dict

# extract the expression levels of choosen antigens
def ag_expression_level(list, df):
    ag_intensety_dict = {}
    for antigen in list:
        ag_row = df.loc[df["Antigen_name"] == antigen]
        ag_intensety_dict[antigen] = ag_row["expression_levels"].values[0].strip()
    return  ag_intensety_dict


# extract the fluorecence options for each selected antigen
def available_flourophore (list, df):
    ab_fluorescence_dict = {}
    for antigen in list:
        antibody_row = df.loc[df["Antigen"] == antigen, "Fluorophore"]
        fluorophores_list = antibody_row.tolist()  # Convert specific column values to list
        ab_fluorescence_dict[antigen] = fluorophores_list

    return ab_fluorescence_dict