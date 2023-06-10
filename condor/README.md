MadGraph5
============
This directory contains some scripts and a Run-3 sample produced using MadGraph5 2.7.2. The instructions to make the LHE file in MadGraph5 can be found [here](https://github.com/weishi10141993/DarkSUSY_MC_MG5/tree/master).

NOTE: The production of the LHE files does not require a CMS release.

cmsDrivers
============
NOTE: Unless you have produced a new LHE file using MadGraph5, the steps in this section do not need to be performed, you can just skip to the Condor JObs section. This is just the path followed to produce the 'DarkSUSY_mH_125_mN1_10_mND_1_mGammaD_0p25_13p6TeV_cT_0p1_events100k.root' file.

Once the LHE file has been produced, this will need to be converted into a root file for further processing. This is done using
the cmsDrivers command:

    cmsDriver.py step1 --filein file:/path/to/input_file.lhe  --fileout file:/path/to/store/file_out.root --mc --eventcontent LHE --datatier LHE --conditions 124X_mcRun3_2022_realistic_v12 --step NONE --era Run3 -n -1  --no_exec

If run as is, only changing the location of the input and output files, the command will produce a Python script named 'step1_NONE.py' that will convert the LHE file to a root file, by using the 'cmsRun' command as follows:

    cmsRun step1_NONE.py
    
The file 'DarkSUSY_mH_125_mN1_10_mND_1_mGammaD_0p25_13p6TeV_cT_0p1_events100k.root' has already been converted from an LHE file to a root file.
   
The second step is the Hadronization of the events, again this is done using cmsDrivers:

    cmsDriver.py Configuration/Generator/python/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --mc --eventcontent RAWSIM --datatier RAWSIM --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step GEN,SIM  --nThreads 4 --era Run3 --geometry DB:Extended  --beamspot  Realistic25ns13p6TeVEarly2022Collision  --filein file:DarkSUSY_mH_125_mN1_10_mND_1_mGammaD_0p25_13p6TeV_cT_0p1_events100k.root --fileout file:DarkSUSY_mH_125_mN1_10_mND_1_mGammaD_0p25_13p6TeV_cT_0p1_events100k_GEN-SIM.root  -n -1 --no_exec

This command will produce the python script 'Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff_py_GEN_SIM.py', which will Hadronize the events in the 'DarkSUSY_mH_125_mN1_10_mND_1_mGammaD_0p25_13p6TeV_cT_0p1_events100k.root'.
In this step, it is best to let a job system handle the workload.

Condor Jobs
===========

The bash script 'shel_comands.sh' contains in command to run the hadronizer script. It will need to be compiled using the command:

    chmod u+x shel_comands.sh
    
otherwise, the script may not work. Once the bash script is compiled, the workload can be submitted to the condor jobs system, using the 'condor_cff.sub' configuration file. A more detailed explanation on how to make this configuration
file can be found [here](https://batchdocs.web.cern.ch/local/quick.html). By runing the command:

    condor_submit condor_cff.sub
    
The job will be submitted to the Condor jobs system and the ID of the job will be printed. The status of all the jobs submitted can be viewed using:

    condor_q
 
 or
 
    condor_q *JOB-ID*
    
 to view the status of a specific job.
 
 NOTE
 ====
 The condor jobs system can only be used within the Lxplus environment, running from an EOS repository will not work.



