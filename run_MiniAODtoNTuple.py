import os
import glob
#Example fastSim inputfile
#'/afs/cern.ch/user/k/kakwok/eos/cms/store/user/kakwok/MiniAOD/Charybdis_BH10_CH_MD4000_MBH9000_n6/Charybdis_BH10_CH_MD4000_MBH9000_n6/160817_010102/0000/miniAOD-prod_PAT_1.root'
# Example FullSim inputfile
#/store/mc/RunIISummer16MiniAODv2/BlackHole_BH10_MD2000_MBH10000_n2_13TeV_TuneCUETP8M1-charybdis/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/004EAFEC-1DFB-E611-81BD-001E67E95BFA.root
#Topdir="/afs/cern.ch/user/k/kakwok/eos/cms/store/user/kakwok/MiniAOD/"
Topdir="/afs/cern.ch/user/k/kakwok/eos/cms/store/mc/RunIISummer16MiniAODv2"
Outdir=""
datasetClass = "BlackHole_BH2_MD6000_MBH*_n4*"
GlobalTag    = "80X_mcRun2_asymptotic_2016_TrancheIV_v6"
isFastSim=False

#Get all the files given a dataset name (one mass point)
def getFlist(isFastSim,Topdir,dataset):
    flist={}
    if(isFastSim):
        jobdate="161007"
        #jobdate="161004"
        #jobdate="160829"
        #print "%s%s/*/%s*/*/*.root"%(Topdir,dir,jobdate)
        #flist = glob.glob("%s%s/*/%s*/*/*.root"%(Topdir,dir,jobdate))
        flist['inputFile'] = glob.glob("%s/*%s*/*/*/*/*.root"%(Topdir,dataset))
    else:
        lsList = glob.glob("%s/%s/*MINIAODSIM*/*/*/*.root"%(Topdir,dataset))
        flist['inputFile']  = ','.join(lsList)
        flist['outputFile'] = Outdir+dataset+"_NTuple.root"
    return flist

#Get all the dataset names:
def getDatasetNames(Topdir,datasetClass):
    print "Looking for datasets %s in %s" %(Topdir,datasetClass) 
    datasets     = glob.glob("%s/%s"%(Topdir,datasetClass))
    for i,dataset in enumerate(datasets):
        datasets[i] = dataset.split("/")[-1]
    return datasets



datasets = getDatasetNames(Topdir,datasetClass)

for dataset in datasets:
    print " Working on this masspoint now: %s" % dataset
    flist = getFlist(isFastSim,Topdir,dataset)
    #print flist
    if(len(flist)>0):
    	cmd = "cmsRun bh80Xcfg.py inputFile=%s outputFile=%s isMC=True useHLT=True maxEvent=-1 reportEvery=1000 GlobalTag=%s "%(flist['inputFile'], flist['outputFile'],GlobalTag)
    	if not(os.path.exists(flist['outputFile'])):
    	        print cmd
    	        os.system(cmd)
    	else:
    	        print "Already produced this masspoint %s...skipping" % dataset
    else:
    	print "This mass point %s is empty" % (dataset) 
