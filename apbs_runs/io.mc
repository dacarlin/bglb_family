##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Tue Jul 18 23:05:07 2017

##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path bglb_holo.pdb
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0, npot=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing lpbe...
PBEparm_parseToken:  trying lpbe...
NOsh: parsed lpbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (161, 161, 161)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Parsing PRINT section
NOsh: Done parsing PRINT section
NOsh: Done parsing PRINT section
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 7114 atoms
Valist_getStatistics:  Max atom coordinate:  (95.385, 76.222, 64.426)
Valist_getStatistics:  Min atom coordinate:  (13.604, 8.36, -9.315)
Valist_getStatistics:  Molecule center:  (54.4945, 42.291, 27.5555)
NOsh_setupCalcMGAUTO(/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1860):  coarse grid center = 54.4945 42.291 27.5555
NOsh_setupCalcMGAUTO(/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1865):  fine grid center = 54.4945 42.291 27.5555
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1877):  Coarse grid spacing = 0.671511, 0.603755, 0.640156
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1879):  Fine grid spacing = 0.520006, 0.48015, 0.501563
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1881):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 0.774383, 0.795273, 0.7835 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1975):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1977):  coarse mesh center = 54.4945 42.291 27.5555
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1982):  coarse mesh upper corner = 108.215 90.5914 78.768
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1987):  coarse mesh lower corner = 0.77365 -6.0094 -23.657
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1992):  initial fine mesh upper corner = 96.095 80.703 67.6805
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 1997):  initial fine mesh lower corner = 12.894 3.879 -12.5695
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 2058):  final fine mesh upper corner = 96.095 80.703 67.6805
NOsh_setupCalcMGAUTO (/Users/alex/Documents/apbs-pdb2pqr/apbs/src/generic/nosh.c, 2063):  final fine mesh lower corner = 12.894 3.879 -12.5695
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 64.0285
Vpbe_ctor2:  solute dimensions = 84.058 x 70.645 x 75.765
Vpbe_ctor2:  solute charge = -28.0002
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 7042.98
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 1.9 max radius
Vclist_setupGrid:  Grid lengths = (92.857, 78.938, 84.817)
Vclist_setupGrid:  Grid lower corner = (8.066, 2.822, -14.853)
Vclist_assignAtoms:  Have 2818540 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 191.134
Vacc_storeParms:  Using 1936-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 2.866405
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 6.558663e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (161, 161, 161)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 8.449820e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (081, 081, 081)
Vbuildops: Galer: (041, 041, 041)
Vbuildops: Galer: (021, 021, 021)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 4.094270e+00
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.176156e+01
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 1.085985e-01
Vprtstp: contraction number = 1.085985e-01
Vprtstp: iteration = 2
Vprtstp: relative residual = 1.257130e-02
Vprtstp: contraction number = 1.157594e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 1.444236e-03
Vprtstp: contraction number = 1.148836e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 2.113662e-04
Vprtstp: contraction number = 1.463516e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 4.680182e-05
Vprtstp: contraction number = 2.214252e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 1.328898e-05
Vprtstp: contraction number = 2.839415e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 4.957926e-06
Vprtstp: contraction number = 3.730855e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 1.846612e-06
Vprtstp: contraction number = 3.724565e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 7.444371e-07
Vprtstp: contraction number = 4.031368e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 1.625061e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 2.137991e+01
Vpmg_setPart:  lower corner = (0.77365, -6.0094, -23.657)
Vpmg_setPart:  upper corner = (108.215, 90.5914, 78.768)
Vpmg_setPart:  actual minima = (0.77365, -6.0094, -23.657)
Vpmg_setPart:  actual maxima = (108.215, 90.5914, 78.768)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vpmg_energy:  calculating only q-phi energy
Vpmg_qfEnergyVolume:  Calculating energy
Vpmg_energy:  qfEnergy = 1.670900336143E+05 kT
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 4.348200e-02
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 6.200000e-05
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 64.0285
Vpbe_ctor2:  solute dimensions = 84.058 x 70.645 x 75.765
Vpbe_ctor2:  solute charge = -28.0002
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 7042.98
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 1.9 max radius
Vclist_setupGrid:  Grid lengths = (92.857, 78.938, 84.817)
Vclist_setupGrid:  Grid lower corner = (8.066, 2.822, -14.853)
Vclist_assignAtoms:  Have 2818540 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 191.134
Vacc_storeParms:  Using 1936-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 2, mgsolv = 1
Setting PDE center to local center...
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = 12.894, 3.879, -12.5695
VPMG::focusFillBound -- New mesh maxs = 96.095, 80.703, 67.6805
VPMG::focusFillBound -- Old mesh mins = 0.77365, -6.0094, -23.657
VPMG::focusFillBound -- Old mesh maxs = 108.215, 90.5914, 78.768
VPMG::extEnergy:  energy flag = 1
Vpmg_setPart:  lower corner = (12.894, 3.879, -12.5695)
Vpmg_setPart:  upper corner = (96.095, 80.703, 67.6805)
Vpmg_setPart:  actual minima = (0.77365, -6.0094, -23.657)
Vpmg_setPart:  actual maxima = (108.215, 90.5914, 78.768)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
VPMG::extEnergy:   Finding extEnergy dimensions...
VPMG::extEnergy    Disj part lower corner = (12.894, 3.879, -12.5695)
VPMG::extEnergy    Disj part upper corner = (96.095, 80.703, 67.6805)
VPMG::extEnergy    Old lower corner = (0.77365, -6.0094, -23.657)
VPMG::extEnergy    Old upper corner = (108.215, 90.5914, 78.768)
Vpmg_qmEnergy:  Zero energy for zero ionic strength!
VPMG::extEnergy: extQmEnergy = 0 kT
Vpmg_qfEnergyVolume:  Calculating energy
VPMG::extEnergy: extQfEnergy = 0 kT
VPMG::extEnergy: extDiEnergy = 21.6084 kT
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vacc_SASA: Time elapsed: 2.832169
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 8.084400e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (Vmgdrv2: fine problem setup)..
Vbuildops: Fine: (161, 161, 161)
Vbuildops: Operator stencil (lev, numdia) = (1, 4)
Vnm_tstop: stopping timer 30 (Vmgdrv2: fine problem setup).  CPU TIME = 8.270740e-01
Vnm_tstart: starting timer 30 (Vmgdrv2: coarse problem setup)..
Vbuildops: Galer: (081, 081, 081)
Vbuildops: Galer: (041, 041, 041)
Vbuildops: Galer: (021, 021, 021)
Vnm_tstop: stopping timer 30 (Vmgdrv2: coarse problem setup).  CPU TIME = 4.065618e+00
Vnm_tstart: starting timer 30 (Vmgdrv2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 4.134958e+01
Vprtstp: iteration = 0
Vprtstp: relative residual = 1.000000e+00
Vprtstp: contraction number = 1.000000e+00
Vprtstp: iteration = 1
Vprtstp: relative residual = 1.186102e-01
Vprtstp: contraction number = 1.186102e-01
Vprtstp: iteration = 2
Vprtstp: relative residual = 1.388690e-02
Vprtstp: contraction number = 1.170802e-01
Vprtstp: iteration = 3
Vprtstp: relative residual = 1.624443e-03
Vprtstp: contraction number = 1.169767e-01
Vprtstp: iteration = 4
Vprtstp: relative residual = 2.305424e-04
Vprtstp: contraction number = 1.419208e-01
Vprtstp: iteration = 5
Vprtstp: relative residual = 4.947201e-05
Vprtstp: contraction number = 2.145897e-01
Vprtstp: iteration = 6
Vprtstp: relative residual = 1.537009e-05
Vprtstp: contraction number = 3.106825e-01
Vprtstp: iteration = 7
Vprtstp: relative residual = 6.097768e-06
Vprtstp: contraction number = 3.967296e-01
Vprtstp: iteration = 8
Vprtstp: relative residual = 2.527193e-06
Vprtstp: contraction number = 4.144455e-01
Vprtstp: iteration = 9
Vprtstp: relative residual = 1.099181e-06
Vprtstp: contraction number = 4.349416e-01
Vprtstp: iteration = 10
Vprtstp: relative residual = 4.775387e-07
Vprtstp: contraction number = 4.344495e-01
Vnm_tstop: stopping timer 30 (Vmgdrv2: solve).  CPU TIME = 1.917482e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 2.424831e+01
Vpmg_setPart:  lower corner = (12.894, 3.879, -12.5695)
Vpmg_setPart:  upper corner = (96.095, 80.703, 67.6805)
Vpmg_setPart:  actual minima = (12.894, 3.879, -12.5695)
Vpmg_setPart:  actual maxima = (96.095, 80.703, 67.6805)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vpmg_energy:  calculating only q-phi energy
Vpmg_qfEnergyVolume:  Calculating energy
Vpmg_energy:  qfEnergy = 2.602588519319E+05 kT
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 5.479000e-02
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 9.000000e-06
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
printEnergy:  Performing global reduction (sum)
Vcom_reduce:  Not compiled with MPI, doing simple copy.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 6.432499e+01
