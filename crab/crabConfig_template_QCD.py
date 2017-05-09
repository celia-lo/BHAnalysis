from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'

config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 200
config.Data.outLFNDirBase = '/store/user/%s/QCD' % (getUsernameFromSiteDB())
config.Data.publication = False

#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T3_US_Brown'
