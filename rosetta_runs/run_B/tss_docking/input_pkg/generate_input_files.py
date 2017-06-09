# coding: utf-8
# set up the input files 

# params for this protein 
import json 
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('params', help="A JSON params file modeled on `params_template.json`")
args = parser.parse_args()

with open(args.params) as fn:
  params = json.load(fn)


# puzzle setup 
puz_setup = 'version: 1\n{{\n"backbone_locked": "{}||"\n}}'
puz_fn = params['handle'] + '.puzzle_setup'
with open( puz_fn, 'w' ) as fn:
    fn.write( puz_setup.format( params[ 'ligand' ] ) ) 


# constraint file 
cst_template = '''# chemical restraints for pNPG hydrolysis by {handle}

# pNPG (residue {ligand}) and acid/base E{acid_base}
AtomPair O2 {ligand} OE2 {acid_base} HARMONIC 1.8 0.18
Angle O2 {ligand} OE2 {acid_base} CD {acid_base} HARMONIC 0 10
Dihedral O2 {ligand} OE2 {acid_base} CD {acid_base} CG {acid_base} HARMONIC 0 10

# pNPG and nucleophile E{nucleophile}
AtomPair C5 {ligand} OE2 {nucleophile} HARMONIC 2.0 0.20
Angle O2 {ligand} C5 {ligand} OE2 {nucleophile} HARMONIC 0 10
Angle C5 {ligand} OE2 {nucleophile} CD {nucleophile} HARMONIC 0 10
Dihedral C5 {ligand} OE2 {nucleophile} CD {nucleophile} CG {nucleophile} HARMONIC 0 10

# nucleophile E{nucleophile} and Y{backup}
AtomPair OE2 {nucleophile} OH {backup} HARMONIC 3.0 0.30
'''

with open( '{}_pNPG.cnstr'.format( params[ 'handle' ] ), 'w' ) as fn:
    fn.write( cst_template.format( **params ) )


# enzyme design header for input PDB 

enzdes_header='''REMARK   0 NE TEMPLATE X LG1 1 MATCH MOTIF A GLU {nucleophile} 1
REMARK   0 NE TEMPLATE X LG1 1 MATCH MOTIF A GLU {acid_base} 2
REMARK   0 NE TEMPLATE A GLU {nucleophile} MATCH MOTIF A TYR {backup} 3
'''

with open( 'enzdes_header.txt', 'w' ) as fn:
    fn.write( enzdes_header.format( **params ) ) 


# would be nice to add the catting together here too 
