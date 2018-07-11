# 1. Reading and parsing a PDB structure

## BioPython

[BioPython](http://biopython.org/) is an awesome library with many *omics* and structural biology useful data structures and functions ready to be applied to solve our specific problem. 

We will cover in this section the problem of reading, parsing and manipulating molecular structure data in PDB format. Refer to the [official tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc158) for more in deep details.

## 1.1. Parsing a simple PDB file

In the [data](data/) folder there is a small PDB file corresponding to the [Stage V sporulation protein M (SpoVM)](http://www.rcsb.org/structure/2MVH), with PDB code [2MVH](data/2mvh.pdb). A PDB file is a plain text file containing structural data of molecules (proteins, nucleic acids, etc.).

### Source code:

The code is almost self-explanatory, but it iterates over the diffeerent models of the structure. Then, for every chain in the model, iterates over the residues and the atoms of the given chain:

File: [parse_1.py](parse_1.py)

```python
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

```

### Output:

```
Model: 0
	Chain: A
		A.MET.1 has 19 atoms
		A.LYS.2 has 22 atoms
		A.PHE.3 has 20 atoms
		A.TYR.4 has 21 atoms
		A.THR.5 has 14 atoms
		A.ILE.6 has 19 atoms
		A.LYS.7 has 22 atoms
		A.LEU.8 has 19 atoms
		A.PRO.9 has 14 atoms
		A.LYS.10 has 22 atoms
		A.PHE.11 has 20 atoms
		A.LEU.12 has 19 atoms
		A.GLY.13 has 7 atoms
		A.GLY.14 has 7 atoms
		A.ILE.15 has 19 atoms
		A.VAL.16 has 16 atoms
		A.ARG.17 has 24 atoms
		A.ALA.18 has 10 atoms
		A.MET.19 has 17 atoms
		A.LEU.20 has 19 atoms
		A.GLY.21 has 7 atoms
		A.SER.22 has 11 atoms
		A.PHE.23 has 20 atoms
		A.ARG.24 has 24 atoms
		A.LYS.25 has 22 atoms
		A.ASP.26 has 12 atoms
```