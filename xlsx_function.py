def import_xlsx_function(filename):
    import pandas as pd
    data_frames = []

    # List of sheet names
    filename = filename  # Abs = antibodies
    sheet_names = [
        "Available_Abs",
        "Ab_expression_level",
        "Fluorophore_info",
        "Fluorophore_overlap",
    ]

     # Load each sheet into a DataFrame
    for sheet_name in sheet_names:
        data_frames.append(pd.read_excel(filename, sheet_name=sheet_name))
    
    return data_frames

