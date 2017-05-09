import os
import subprocess
import json
from sys import argv

datasetTxt = open(argv[1],"r")
datasets = []
for line in datasetTxt:
    if(line[0]=="#"):
        continue
    line = line.strip()
    pDataSet = line.split("/")[1]
    fullDataSet = line
    datasets.append({'pDataSet':pDataSet,'fullDataSet':fullDataSet})

for dataset in datasets:
    #os.system("python ~/das_client.py --query='summary dataset=%s | grep summary.nevents'"%dataset['fullDataSet'])
    #p = subprocess.Popen(["python ~/das_client.py --query='summary dataset=%s | grep summary.nevents'"%dataset['fullDataSet']],stdout=subprocess.PIPE, shell=True)
    #(out,err) = p.communicate()
    jsonString = subprocess.check_output(["python ~/das_client.py --query='summary dataset=%s | grep summary.nevents' --format=json"%dataset['fullDataSet']], shell=True)
    #Dictionary of data
    data    =  json.loads(jsonString)['data']
    summary =  data[0]['summary']
    nevents =  summary[0]['nevents']
    print "%s    %s"%(dataset['pDataSet'], nevents)
