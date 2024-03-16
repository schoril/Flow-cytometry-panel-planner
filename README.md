# Flow-cytometry-panel-planner
[Lior Schori](https://schoril.github.io/) 


I will write a script that:
- Contains information on all the antibodies in our lab, fluorophores intensety, expression levels of commonly used proteins in immunology research (Pandas dataframe).
- Receives input from the user on which proteins are planned to be labeled.
- Generates output indicating which fluorophore to use for each protein in the experiment based on the expression levels of the protein and fluorophore intensity.


# General description
1. Load the xlsx sheets containing antibodies information into dataframes using pandas.
2. Generate dictionaries of fluorescence overlap and fluorescence intensity.
3. Generate a list of all available antigens and load it into a user-friendly GUI, from which the user can choose which antibodies he wants to use.
4. Assignment of fluorophores to antigens based on antigen expression level and fluorescence overlap:
  - Lowly expressed antigens will receive high intensity fluorophores, and vice versa, unless no available option exists.
  - Fluorophores with an overlap of over 0.7 will not be used together.
5. Printing the final result: a dictionary with antigens and their assigned fluorophores. If no matching fluorophores are available, a message will be given.

