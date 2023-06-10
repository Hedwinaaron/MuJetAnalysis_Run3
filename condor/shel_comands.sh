#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
## run the job
cmsRun /afs/cern.ch/user/h/hencinas/CMSSW_12_4_11_patch3/src/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff_py_GEN_SIM.py || exit $?; 
