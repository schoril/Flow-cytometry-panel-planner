def Ag_expression_flourophore_assignment(
    ab_fluorescence_dict, ag_intensety_dict, intensety_dict
):
    Ab_options_dict = {}
    sorted_antigens = sorted(ab_fluorescence_dict.keys(), key=lambda key: len(ab_fluorescence_dict[key]))
 
    for antigen in sorted_antigens:
        if ag_intensety_dict[antigen] == "High":
            # Get all fluorophores with intensity less than or equal to 3
            high_intensity_options = [
                fluorophore
                for fluorophore in ab_fluorescence_dict[antigen]
                if intensety_dict[fluorophore] <= 3
            ]
            # If there are no options with intensity less than or equal to 3, include all options
            if not high_intensity_options:
                Ab_options_dict[antigen] = ab_fluorescence_dict[antigen]
                print(
                    "warning- highly expressed antigen conjugated to high-intensity fluorophore"
                )
            else:
                Ab_options_dict[antigen] = high_intensity_options
        elif ag_intensety_dict[antigen] == "Low":
            # Get all fluorophores with intensity greater than or equal to 3
            low_intensity_options = [
                fluorophore
                for fluorophore in ab_fluorescence_dict[antigen]
                if intensety_dict[fluorophore] >= 3
            ]
            # If there are no options with intensity greater than or equal to 3, include all options
            if not low_intensity_options:
                Ab_options_dict[antigen] = ab_fluorescence_dict[antigen]
                print(
                    "warning- lowly expressed antigen conjugated to low-intensity fluorophore"
                )
            else:
                Ab_options_dict[antigen] = low_intensity_options
        else:
            Ab_options_dict[antigen] = ab_fluorescence_dict[antigen]
    return Ab_options_dict


def fluorophore_assignment(Ab_options_dict, overlap_dict):
    fluorophore_assignment = {}
    # Iterate through each antigen
    for antigen, fluorophores in Ab_options_dict.items():
        # Iterate through possible colors for the antigen
        for fluorophore in fluorophores:
            # Check if the color conflicts with already assigned colors
            conflict = False
            for assigned_fluorophore in fluorophore_assignment.values():
                if fluorophore in overlap_dict.get(assigned_fluorophore, []):
                    conflict = True
                    break
            # If no conflict, assign the color to the antigen and break the loop
            if not conflict:
                fluorophore_assignment[antigen] = fluorophore
                break

    # Print the final assignments
    if len(fluorophore_assignment) < len(Ab_options_dict):
        return "This staining panel cannot be performed with the currently available antibodies in the lab."
            
    else:
        for antigen, color in fluorophore_assignment.items():
            #print(f"{antigen}: {color}")
            return fluorophore_assignment
