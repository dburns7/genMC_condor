#! /bin/sh -f

unset CMS_PATH
source /share/apps/cmssoft/cmsset_default.sh
pushd /home/dburns/WorkingArea/gentest/CMSSW_5_3_11/src
cmsenv
popd

JOB=30
EVTS=2900
INFILE=file:hxx_8TeV_500GeV.lhe
OUTFILE=final_PAT_$JOB.root
maxEvents=100

echo "Processing events $EVTS to $(($EVTS+$maxEvents)) in $INFILE. Outputting to $OUTFILE."

cmsDriver.py Configuration/Generator/python/Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff.py -s GEN,SIM --eventcontent RAWSIM --datatier GEN-SIM --mc --conditions auto:mc --filein=$INFILE --fileout=step1.root -n $maxEvents --no_exec

sed -i '/import FWCore.ParameterSet.Config as cms/r varParsing1.txt' Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py
sed -i "/    fileNames = cms.untracked.vstring('$INFILE')/a \ \ \ \ , skipEvents = cms.untracked.uint32($EVTS)" Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py

cmsRun Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py

cmsDriver.py Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py -s DIGI,L1,DIGI2RAW,HLT:@relval,RAW2DIGI,L1Reco --eventcontent FEVTDEBUGHLT --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --conditions auto:startup -n $maxEvents --filein=file:step1.root --fileout=step2.root

cmsDriver.py Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM_py_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco.py --datatier GEN-SIM-RECO,DQM --conditions auto:startup -s RAW2DIGI,L1Reco,RECO,VALIDATION,DQM --eventcontent RECOSIM,DQM -n $maxEvents --filein=file:step2.root --fileout=step3.root

cmsRun simple_PAT_MC_cfg.py inputFiles=file:step3.root outputFile=$OUTFILE
