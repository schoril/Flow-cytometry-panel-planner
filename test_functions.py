from condition_functions import Ag_expression_flourophore_assignment, fluorophore_assignment

# Test case 1: High and low antigen intensity, options with intensity <= 3 and intensety >=3
       
def test_Ag_expression_flourophore_assignment():
    ab_fluorescence_dict = {"antigen1": ("fluorophore1", "fluorophore2"), "antigen2": ("fluorophore3", "fluorophore4")}
    ag_intensety_dict = {"antigen1": "High", "antigen2": "Low"}
    intensety_dict = {"fluorophore1": 2, "fluorophore2": 4, "fluorophore3": 3, "fluorophore4": 2}
    expected_result = {"antigen1": ["fluorophore1"], "antigen2": ["fluorophore3"]}

    result = Ag_expression_flourophore_assignment(ab_fluorescence_dict, ag_intensety_dict, intensety_dict)
    assert result == expected_result

# Test case 2: High antigen intensity, no options with intensity <= 3

def test_Ag_expression_flourophore_assignment():
    ab_fluorescence_dict1 = {"antigen1": ("fluorophore1", "fluorophore2"), "antigen2": ("fluorophore3", "fluorophore4")}
    ag_intensety_dict1 = {"antigen1": "High", "antigen2": "High"}
    intensety_dict1 = {"fluorophore1": 4, "fluorophore2": 5, "fluorophore3": 4, "fluorophore4": 5}
    expected_result1 = {"antigen1": ("fluorophore1", "fluorophore2"), "antigen2": ("fluorophore3", "fluorophore4")}

    result = Ag_expression_flourophore_assignment(ab_fluorescence_dict1, ag_intensety_dict1, intensety_dict1)
    assert result == expected_result1

 # Test case where all antigens can be assigned a fluorophore without conflict
def test_fluorophore_assignment():  
    Ab_options_dict = {"antigen1": ["fluorophore1", "fluorophore2"],
                       "antigen2": ["fluorophore3", "fluorophore4"]}
    overlap_dict = {"fluorophore1": "fluorophore3","fluorophore2": "fluorophore4"}
    expected_result = {"antigen1": "fluorophore1", "antigen2": "fluorophore4"}
    assert fluorophore_assignment(Ab_options_dict, overlap_dict) == expected_result

# Test case where some antigens cannot be assigned a fluorophore due to conflicts
def test_fluorophore_assignment():
    Ab_options_dict = {"antigen1": ["fluorophore1", "fluorophore2"],
                       "antigen2": ["fluorophore3", "fluorophore4"]}
    overlap_dict = {"fluorophore1": ["fluorophore3", "fluorophore4"],
                    "fluorophore2": ["fluorophore3", "fluorophore4"]}
    expected_result = "This staining panel cannot be performed with the currently available antibodies in the lab."
    assert fluorophore_assignment(Ab_options_dict, overlap_dict) == expected_result