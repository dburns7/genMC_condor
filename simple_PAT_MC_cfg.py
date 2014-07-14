## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

options.parseArguments()
## let it run
process.p = cms.Path(
   process.patDefaultSequence
   )


## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#SkipEvent = cms.untracked.vstring('ProductNotFound')

#process.GlobalTag.globaltag = 'auto:mc'
process.GlobalTag.globaltag = 'START53_V19::All'
#process.GlobalTag.globaltag = 'START53_V7N::All' ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)

#process.source.fileNames = ['file:/afs/cern.ch/cms/Tutorials/TWIKI_DATA/CMSDataAnaSch//CMSDataAnaSch_RelValZMM428.root']
#process.source.fileNames = ['file:/afs/cern.ch/cms/Tutorials/TWIKI_DATA/CMSDataAnaSch_RelValZMM525.root']
#process.source.fileNames = ['file:/afs/cern.ch/cms/Tutorials/TWIKI_DATA/CMSDataAnaSch_RelValZMM536.root']

#process.source.fileNames = ['file:/uscms_data/d3/dburns7/CrabWorkingArea/CMSSW_5_3_11/src/crab_0_140204_144942/res/outfile_1_1_j9g.root']

process.source.fileNames = options.inputFiles#['file:final_1.root']
#process.source.fileNames = ['file:Pythia_hxx_8TeV_1GeV_lhe_gen_cfg_TEMPLATE.root']
#process.source.fileNames = ['file:hzz4l_MC.root']


#process.source.fileNames = ['/ZZTo4e_8TeV-powheg-pythia6/Summer12_DR53X-PU_RD1_START53_V7N-v2/AODSIM']
#process.source.fileNames = ['/ZZTo2e2mu_8TeV-powheg-pythia6/Summer12_DR53X-PU_RD1_START53_V7N-v2/AODSIM']
#process.source.fileNames = ['/ZZTo4mu_8TeV-powheg-pythia6/Summer12_DR53X-PU_RD1_START53_V7N-v1/AODSIM']
#process.source.fileNames = ['/GluGluToZZTo2L2L_TuneZ2star_8TeV-gg2zz-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM']
#process.source.fileNames = ['/GluGluToZZTo4L_8TeV-gg2zz-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM']
#process.source.fileNames = ['/ZH_HToZZTo4L_M-126_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM']
#process.source.fileNames = ['/ZH_HToWWTo2L2Nu_M-130_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START44_V9B-v1/AODSIM']
#process.source.fileNames = ['/ZH_HToWWTo2L2Nu_M-120_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START44_V9B-v1/AODSIM']
#process.source.fileNames = ['/WH_ZH_TTH_HToZZTo2L2Nu_M-130_7TeV-pythia6/Fall11-PU_S6_START44_V9B-v1/AODSIM']
#process.source.fileNames = ['/WH_HToZZTo4L_M-126_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM']
#process.source.fileNames = ['/GluGluToHToZZTo4L_M-150_7TeV-powheg-pythia6/Fall10-START38_V12-v1/GEN-SIM-RAW']


#process.source.fileNames = ['file:/uscms_data/d3/dburns7/CrabWorkingArea/CMSSW_5_3_11/src/crab_0_140203_175650/res/outfile_1_1_kft.root']
#process.source.fileNames = ['/store/relval/CMSSW_5_3_6-START53_V14/RelValZMM/GEN-SIM-RECO/v2/00000/08C1D822-F629-E211-A6B1-003048679188.root']
# eos ls eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValZMM/GEN-SIM-RECO/v2/00000/08C1D822-F629-E211-A6B1-003048679188.root

process.maxEvents.input = 100      ##  ( -1 to run on all events)
process.out.fileName = options.outputFile #'hxx_pattuple.root' #'ZMM2_PAT_MC.root'            ##  (e.g. 'myTuple.root')

process.options = cms.untracked.PSet(
#SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#error: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookTroubleShooting
