import FWCore.ParameterSet.Config as cms

process = cms.Process("ICALIB")
process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    ),
    destinations = cms.untracked.vstring('cout')
)

process.source = cms.Source("EmptyIOVSource",
    lastValue = cms.uint64(1),
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:SiPixelQuality_v25.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('SiPixelQuality_v25')
    ))
)

process.prod = cms.EDAnalyzer("SiPixelBadModuleByHandBuilder",
    BadModuleList = cms.untracked.VPSet(

# BPix_BpO_SEC2_LYR1_LDR3_MOD
    cms.PSet(
    errortype = cms.string('tbmA'),
    detid = cms.uint32(302057496) # OK
    ), 
# BPix_BpI_SEC1_LYR3_LDR3_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302188820) #OK
    ), 
# BPix_BpI_SEC1_LYR3_LDR3_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302123296) 
    ), 
# BPix_BpO_SEC8_LYR2_LDR16_MOD4
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302127136)
    ),   
# BPix_BmI_SEC1_LYR2_LDR1_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302123024)
    )


    ),
    Record = cms.string('SiPixelQualityFromDbRcd'),
    SinceAppendMode = cms.bool(True),
    IOVMode = cms.string('Run'),
    printDebug = cms.untracked.bool(True),
    doStoreOnDB = cms.bool(True)
)

#process.print = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.prod)
#process.ep = cms.EndPath(process.print)


