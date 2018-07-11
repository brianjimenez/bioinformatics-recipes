from Bio.PDB.PDBParser import PDBParser

# We will use the parser object for loading the PDB structure.
parser = PDBParser(PERMISSIVE=True, QUIET=False)
# Load the PDB structure
structure = parser.get_structure('2mvh', 'data/2mvh.pdb')

# Iterate per model:
for model in structure.get_models():
    print 'Model:', model.id
    # Iterate per chain:
    for chain in model.get_chains():
        print '\tChain:', chain.id
        # Iterate per residue:
        for residue in chain.get_residues():
            # Get the atoms of this residue
            atoms = [atom for atom in residue.get_atoms()]
            # An example of how to get the complete identifier of a given residue
            residue_id = "\t\t{}.{}.{}".format(chain.id, residue.get_resname(), residue.get_id()[1])
            print residue_id, 'has', len(atoms), 'atoms'

