MuJetAnalysis
=============

Most updated branch: weishi10141993/for-CMSSW-94X

The structure of the code are documented below. Although one could navigate the whole repository on their own, the document provides a heuristic approach to facilitate this process. Meanwhile, in order to be new-user-friendly, the structure is described from downstream to upstream.

## Running the analyzer
The anlayzer works with CMSSW_12_4_11_patch3. By issuing the command:

`cmsRun MuJetAnalysis/DataFormats/scripts/patifyMC_13TeV/patTuple_cutana_mujets_MiniAOD_cfg.py`

The analyzer will runover a Run-3 sample. Ussing the command:

`cmsRun MuJetAnalysis/DataFormats/scripts/patifyMC_13TeV/patTuple_cutana_mujets_MiniAOD_Run-2_cfg.py`
The analyzer will run ober a Run-3 sample. In both cases a Run-3 configuration is used. In case the analyzer cannot access the files, these can be found here

`/afs/cern.ch/user/h/hencinas/public`

## Cut-and-count
A simple macro is available for quick cut-and-count based on the Ntuples: `CutFlowAnalyzer/scripts/cutflow_macros/CutFlow_2018L2Mu23.C`. More details on page.
