def MolecularGeoMaker():
    print("Remember, the Electronic Arrangement ranges from (2-6) and possible Lone Pairs (0-2)!")
    Electronic_Arrangement = input("What is the total number of bonds?: ")
    Lone_Pairs = input("How many Lone Pairs are at the Central Atom?: ")

    if Electronic_Arrangement == str(2) and Lone_Pairs == str(0):
        return "The molecule has a Linear electronic-group arrangement and molecular geometry."
    
    if Electronic_Arrangement == str(3) and Lone_Pairs == str(0):
        return "The molecule has a Trigonal Planar electronic-group arrangement and molecular geometry."
    
    if Electronic_Arrangement == str(3) and Lone_Pairs == str(1):
        return "The molecule has a Trigonal Planar electronic-group arrangement and Bent molecular geometry."

    if Electronic_Arrangement == str(4) and Lone_Pairs == str(0):
        return "The molecule has a Tetrahedral electronic-group arrangement and molecular geometry."

    if Electronic_Arrangement == str(4) and Lone_Pairs == str(1):
        return "The molecule has a Tetrahedral electronic-group arrangement and Trigonal Pyramidal molecular geometry."

    if Electronic_Arrangement == str(4) and Lone_Pairs == str(2):
        return "The molecule has a Tetrahedral electronic-group arrangement and Bent molecular geometry."
  
    if Electronic_Arrangement == str(5) and Lone_Pairs == str(0):
        return "The molecule has a Trigonal Bipyramidal electronic-group arrangement and molecular geometry."

    if Electronic_Arrangement == str(5) and Lone_Pairs == str(1):
        return "The molecule has a Trigonal Bipyramidal electronic-group arrangement and See-saw molecular geometry."

    if Electronic_Arrangement == str(5) and Lone_Pairs == str(2):
        return "The molecule has a Trigonal Bipyramidal electronic-group arrangement and T-shaped molecular geometry."

    if Electronic_Arrangement == str(5) and Lone_Pairs == str(3):
        return "The molecule has a Trigonal Bipyramidal electronic-group arrangement and Linear molecular geometry."

    if Electronic_Arrangement == str(6) and Lone_Pairs == str(0):
        return "The molecule has a Octahedral electronic-group arrangement and molecular geometry."

    if Electronic_Arrangement == str(6) and Lone_Pairs == str(1):
        return "The molecule has a Octahedral electronic-group arrangement and Square Pyramidal molecular geometry."

    if Electronic_Arrangement == str(6) and Lone_Pairs == str(2):
        return "The molecule has a Octahedral electronic-group arrangement and Square Planar molecular geometry."    

    else:
        return "I don't think that is a molecule..."
    
print(MolecularGeoMaker())
    
