import FWCore.ParameterSet.Config as cms

process = cms.Process("ICALIB")
process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    ),
    destinations = cms.untracked.vstring('cout')
)

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
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
    connect = cms.string('sqlite_file:SiPixelQuality_v26.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('SiPixelQuality_v26')
    ))
)

process.prod = cms.EDAnalyzer("SiPixelBadModuleByHandBuilder",
    BadModuleList = cms.untracked.VPSet(

###The whole SEC3_LYR1 and the whole SEC3_LYR2
#Layer1
#BPix_BmO_SEC3_LYR1LDR4_MOD4
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302057732),
    badroclist = cms.vuint32(6),
    ), 

#BPix_BmO_SEC3_LYR1LDR4_MOD3
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302057736),
    badroclist = cms.vuint32(6)
    ), 
  
#BPix_BmO_SEC3_LYR1LDR4_MOD2
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302057740),
    badroclist = cms.vuint32(6),
    ), 
  
#BPix_BmO_SEC3_LYR1LDR4_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302057744),
    badroclist = cms.vuint32(6)
    ), 
  


#Layer2
#BPix_BmO_SEC3_LYR2LDR5_MOD4
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124292),
    badroclist = cms.vuint32(6)
    ), 

#BPix_BmO_SEC3_LYR2LDR5_MOD3
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124296),
    badroclist = cms.vuint32(6)
    ), 
  
#BPix_BmO_SEC3_LYR2LDR5_MOD2
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124300),
    badroclist = cms.vuint32(6)
    ), 
  
#BPix_BmO_SEC3_LYR2LDR5_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124304),
    badroclist = cms.vuint32(6)
    ), 
  

#BPix_BmO_SEC3_LYR2LDR6_MOD4
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124548),
    badroclist = cms.vuint32(6)
    ), 

#BPix_BmO_SEC3_LYR2LDR6_MOD3
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124552),
    badroclist = cms.vuint32(6)
    ), 
  
#BPix_BmO_SEC3_LYR2LDR6_MOD2
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124556),
    badroclist = cms.vuint32(6)
    ), 
  
#BPix_BmO_SEC3_LYR2LDR6_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302124560),
    badroclist = cms.vuint32(6)
    ), 

#old bad ones
#Lay1
# BPix_BpO_SEC2_LYR1_LDR3_MOD2
    cms.PSet(
    errortype = cms.string('tbmA'),
    detid = cms.uint32(302057496)
    ), 

#Lay2
# BPix_BpO_SEC1_LYR2_LDR1H_MOD4 
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
    ),
#BPix_BmI_SEC1_LYR2_LDR2F_MOD1 TBM-B (302122768)
    cms.PSet(
    errortype = cms.string('tbmB'),
    detid = cms.uint32(302122768)
    ),
#BPix_BpO_SEC7_LYR2_LDR14F_MOD4 (302126624),
#    cms.PSet(
#    errortype = cms.string('whole'),
#    detid = cms.uint32(302126624) 
#    ),  
#BPix_BpO_SEC3_LYR2_LDR5F_MOD1 TBM-B (302124308)
    cms.PSet(
    errortype = cms.string('tbmB'),
    detid = cms.uint32(302124308) 
    ), 

#BPix_BpO_SEC7_LYR3_LDR19F_MOD2 (302194200), 
#    cms.PSet(
#    errortype = cms.string('whole'),
#    detid = cms.uint32(302194200) 
#    ), 
# BPix_BpI_SEC1_LYR3_LDR3_MOD1
    cms.PSet(
    errortype = cms.string('whole'),
    detid = cms.uint32(302188820) 
    ), 
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


