import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_1.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_10.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_11.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_12.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_13.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_14.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_15.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_16.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_17.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_18.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_19.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_2.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_20.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_3.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_4.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_5.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_6.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_7.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_8.root',
	'/store/user/tvami/MC_GENSIMDIG2RAW_PerfectDet_20k/MinBias/MC_GENSIMDIG2RAW_20k_PerfectDet/150331_100202/0000/MinBias_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM_DIGI_L1_DIGI2RAW-PerfectDet_9.root',
	)
)

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('TimingStudy_cfg.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

## ------------------- Output ---------------------------
# we do not save the output from the standard sequance 
# only the output of the NTuplizer (TimingStudy)
#-------------------------------------------------------

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

from CalibTracker.Configuration.Common.PoolDBESSource_cfi import *
# --------------------- SiPixelQuality -----------------
process.siPixelDigis.UseQualityInfo = cms.bool(True)
process.SiPixelQualityDBReader = cms.ESSource("PoolDBESSource",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0),
        authenticationPath = cms.untracked.string('')
    ),
    #connect = cms.string ('sqlite_file:SiPixelQuality_v37.db'), # for local files
	connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS'), 
	toGet = cms.VPSet(
        	cms.PSet(
                        record = cms.string('SiPixelQualityFromDbRcd'),
                        tag = cms.string('SiPixelQuality_v37') # local file tag name 
        )
    )

)
process.es_prefer_Quality = cms.ESPrefer("PoolDBESSource","SiPixelQualityDBReader")

#-------------------------------------------------------

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)

#--------------- Added for TimingStudy ---------------
process.MessageLogger.cerr.FwkReport.reportEvery = 10

#-------------------------
#  Track Refitter
#-------------------------

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.Refitter = process.TrackRefitterP5.clone()
process.Refitter.src = 'generalTracks'
process.Refitter.TrajectoryInEvent = True

# TimingStudy
process.TimingStudy = cms.EDAnalyzer("TimingStudy",
    trajectoryInput = cms.string('Refitter'),
    fileName = cms.string("Ntuple.root"),
    extrapolateFrom = cms.int32(2),
    extrapolateTo = cms.int32(1),
    keepOriginalMissingHit = cms.bool(False),
    usePixelCPE= cms.bool(True),
    minNStripHits = cms.int32(0),
    triggerNames=cms.vstring(
        "HLT_L1SingleMuOpen_DT",
        "HLT_L1SingleMuOpen",
        "HLT_L1Tech_HBHEHO_totalOR",
        "HLT_L1TrackerCosmics",
        "HLT_Random"),
)

process.TimingStudy_step = cms.Path(process.Refitter*process.TimingStudy)

# Schedule definition
process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.reconstruction_step,
    process.TimingStudy_step
    )
