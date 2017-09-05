from Bio.Blast.Applications import NcbiblastpCommandline
from Bio import SeqIO

# general notes:
# - really should be using JSON data here
# - really should be using Jinja templates for the input files

TARGET_FASTA='target.fasta'

known_sequence = '''>BglB
NTFIFPATFMWGTSTSSYQIEGGTDEGGRTPSIWDTFCQIPGKVIGGDCGDVACDHFHHF
KEDVQLMKQLGFLHYRFSVAWPRIMPAAGIINEEGLLFYEHLLDEIELAGLIPMLTLYHW
DLPQWIEDEGGWTQRETIQHFKTYASVIMDRFGERINWWNTINEPYCASILGYGTGEHAP
GHENWREAFTAAHHILMCHGIASNLHKEKGLTGKIGITLNMEHVDAASERPEDVAAAIRR
DGFINRWFAEPLFNGKYPEDMVEWYGTYLNGLDFVQPGDMELIQQPGDFLGINYYTRSII
RSTNDASLLQVEQVHMEEPVTDMGWEIHPESFYKLLTRIEKDFSKGLPILITENGAAMRD
ELVNGQIEDTGRHGYIEEHLKACHRFIEEGGQLKGYFVWSFLDNFEWAWGYSKRFGIVHI
NYETQERTPKQSALWFKQMMAKNGFGSLE
'''

known_params = {
    'handle': '2jie',
    'nucleophile': 353,
    'acid_base': 164,
    'backup': 295,
    'ligand': 446,
}

with open('known.fa', 'w') as fn:
    fn.write(known_sequence)

# setting it up this way will allow us to feed in JSON 
# of as many proteins as we want, allowing us to use a 
# Bayesian approach 

cmd = NcbiblastpCommandline(subject='known.fa', query=TARGET_FASTA, outfmt='"6 sseq qseq sstart qstart"')
r = cmd() # weird syntax, BioPython people! 
# r is a tuple of groups of blast hits 
print('r:', r) 
sseq, qseq, sstart, qstart, *rest = r[0].split()
print('r[0].split() for debugging', r[0].split())
# we don't care about the list rest, it contains short alignments 

mmap = {}
scount = qcount = 0
for i, j in zip(sseq, qseq):

    if i != '-':
        scount += 1

    if j != '-':
        qcount += 1

    sstart = int(sstart)
    qstart = int(qstart)

    subject_index = scount + sstart - 1
    query_index = qcount + qstart - 1

    if subject_index in known_params.values():
        if i == j:
            print('Mapping:', i, j, subject_index, query_index)
            mmap.update({subject_index: query_index})
        else:
            print("Aligned residues aren't the same residue")

record = next(SeqIO.parse(TARGET_FASTA, 'fasta'))

params = {
  'handle': record.id,
  'nucleophile': mmap[353],
  'acid_base': mmap[164],
  'backup': mmap[295],
  'ligand': 1+len(record.seq)
}

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

def get_atoms():
    with open('cm_low_energy.pdb') as fn:
        lines = [line for line in fn.readlines() if line.startswith('ATOM')]
    return ''.join(lines)

def get_ligand_atoms():
    with open('pnpg.pdb') as fn:
        lines = fn.readlines()
    return ''.join(lines) 

with open( 'input_pose.pdb', 'w' ) as fn:
    fn.write(enzdes_header.format( **params ))
    fn.write(get_atoms())
    fn.write(get_ligand_atoms())
