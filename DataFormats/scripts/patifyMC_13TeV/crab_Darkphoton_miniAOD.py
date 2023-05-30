import CRABClient
from CRABClient.UserUtilities import config

config = config()

configParams = ['resonance=MUONJET']
configParams.append('isMC=True')
configParams.append('fromCRAB=True')
configParams.append('outputFile=output.root')


config.General.workArea = 'crab_projects'

config.General.requestName = 'Darkphoton-MiniAOD'

config.General.transferOutputs = True
config.General.transferLogs = True
config.General.instance = 'prod'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'patTuple_cutana_mujets_MiniAOD_cfg.py'
config.JobType.maxMemoryMB = 2500
#config.JobType.numCores = 2 # to match with nThreads set in reduceCosmics_cfg.py
config.JobType.allowUndistributedCMSSW = True
config.JobType.outputFiles = ['out_ana_1.root']
config.JobType.pyCfgParams = configParams

config.Data.inputDataset ='/MSSMD_mH_125_mN1_60_mGammaD_0p7_cT_0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
#config.Data.lumiMask = 'certTools/Cert_Ian_Cosmics18_Completed_GoodTracking_JSON.txt'
config.Data.inputDBS = 'global'


config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 # automatic splitting: runtime > 180 minutes
config.Data.outLFNDirBase = '/store/user/hencinas'
#config.Data.publication = False
config.Data.outputDatasetTag = 'private-trial-Darkphoton-MiniAOD'


config.Site.storageSite = 'T3_CH_CERNBOX'
