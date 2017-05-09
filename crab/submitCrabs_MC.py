import os

def AddLines(crab,pSet):
	outputfileID= crab["outputfileID"]
	dataSetName = crab["dataSetName"]
	GlobalTag   = crab["GlobalTag"]

	lines = []
	lines.append("config.General.requestName   = 'BHnTuples_%s'\n"     %outputfileID )
	lines.append("config.General.workArea      = 'crab_jobs_%s'\n"     %outputfileID )
	lines.append("config.Data.inputDataset     = '%s'\n"               %dataSetName )
	lines.append("config.Data.outputDatasetTag = 'BHnTuples_%s'\n"     %outputfileID )
	lines.append("config.JobType.psetName      =  '%s'\n"              % pSet)
	lines.append("config.JobType.pyCfgParams   = ['GlobalTag=%s','isMC=True','useHLT=True']\n"   % GlobalTag  )
	return lines

def makeConfigFromTemplate(crab, template, pSet):
	if not os.path.exists(template):
		print "%s does not exits"%template
		return ""
	outputfileID = crab["outputfileID"]
	tempF  = open(template,"r")
	configName = "CrabConfig_%s.py"%outputfileID
	config     = open(configName,"w")
	for line in tempF:
		config.write(line)
	tempF.close()
	for line in AddLines(crab,pSet):
		config.write(line)
	print "	Writing %s"%configName
	return configName

def makeCrabsFromFile(fname):
    datasetTxt = open(fname,"r")
    crabs=[]
    for line in datasetTxt:
        line = line.strip()
        if(line[0]=="#"): 
            continue
        if(len(line.split())<3):
            print "Invalid dataset.txt format! Must be:outputfileID datasetName GlobalTag, skipping this line"
            continue
        outputfileID    = line.split()[0]
        fulldatasetName = line.split()[1]
        GlobalTag       = line.split()[2]
        crabs.append({"outputfileID":outputfileID,"dataSetName":fulldatasetName,"GlobalTag":GlobalTag})
    return crabs


template     = "crabConfig_template_QCD.py"
pSet         = "/afs/cern.ch/user/k/kakwok/work/public/Blackhole/CMSSW_8_0_26_patch1/src/BH/BHAnalysis/bh80Xcfg.py"
crabs        = makeCrabsFromFile("dataset_QCD.txt")


for crab in crabs:
	CrabConfig = makeConfigFromTemplate(crab,template,pSet)
	print "Submitting %s" % CrabConfig
	os.system("crab submit %s" % CrabConfig)
