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
    connect = cms.string('sqlite_file:SiPixelQuality_phase1_2017_v2.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('SiPixelQuality_phase1_2017_v2')
    ))
)

process.prod = cms.EDAnalyzer("SiPixelBadModuleByHandBuilder",
    BadModuleList = cms.untracked.VPSet(
#Layer 1
#BpI 
#BPix_BmO_SEC5_LYR1_LDR4H_MOD2
        cms.PSet(
            errortype = cms.string('none'),
            detid = cms.uint32(303067148),
            badroclist = cms.vuint32(8),
        ), 
#BPix_BmO_SEC5_LYR1_LDR4H_MOD2
        cms.PSet(
            errortype = cms.string('none'),
            detid = cms.uint32(303067148),
            badroclist = cms.vuint32(9),
        ), 
#BPix_BmO_SEC5_LYR1_LDR4H_MOD2
        cms.PSet(
            errortype = cms.string('none'),
            detid = cms.uint32(303067148),
            badroclist = cms.vuint32(10),
        ), 
#BPix_BmO_SEC5_LYR1_LDR4H_MOD2
        cms.PSet(
            errortype = cms.string('none'),
            detid = cms.uint32(303067148),
            badroclist = cms.vuint32(11),
        ),
#Layer 2
#BPix_BmO_SEC8_LYR2_LDR14F_MOD2
        cms.PSet(
            errortype = cms.string('tbmA'),
            detid = cms.uint32(304173068)
        ), 
 
#BPix_BmI_SEC2_LYR2_LDR3_MOD3
        cms.PSet(
            errortype = cms.string('tbmA'),
            detid = cms.uint32(304107528)
        ), 
 
#BPix_BmI_SEC4_LYR2_LDR7_MOD1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304091152)
        ), 
        
#BPix_BpI_SEC2_LYR2_LDR3F_MOD4
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304107552)
        ), 
#BpI_SEC8_LYR4_LDR32_MOD2
        cms.PSet(
            errortype = cms.string('tbmB'),
            detid = cms.uint32(306384920)
        ), 
#Layer 3
#BPix_BmI_SEC2_LYR3_LDR3_MOD4
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305172484)
        ), 

#BPix_BmI_SEC7_LYR3_LDR20_MOD2
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305283084)
        ), 
 
#BPix_BpO_SEC6_LYR3_LDR17F_MOD1 
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305250324)
        ), 
 
#BPix_BpO_SEC1_LYR3_LDR1F_MOD4
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305184800)
        ), 
#Layer 4
#BPix_BmO_SEC6_LYR4_LDR23F_MOD2
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(306343948)
        ), 
        
#BPix_BpO_SEC1_LYR4_LDR3_MOD1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(306262036)
        ),        
#FPIX
#FPix Disk 1
#BpO_D1_BLD10_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352650244)
        ), 

#BpO_D1_BLD16_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352777220)
        ), 

#BmI_D1_BLD6_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(344200196)
        ), 

#BpI_D1_BLD17_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352785412)
        ), 

#BpI_D1_BLD7_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352674820)
        ), 

#BpI_D1_BLD4_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352598020)
        ),
 
#Disk 2
#BpO_D2_BLD4_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352887812)
        ), 

#BpI_D2_BLD4_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352961540)
        ), 

#BpI_D2_BLD8_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352946180)
        ), 

#BmO_D2_BLD2_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(344593412)
        ), 

#BpO_D2_BLD1_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352876548)
        ), 

#BpO_D2_BLD2_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352880644)
        ), 

#BpO_D2_BLD3_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352884740)
        ), 

#BpO_D2_BLD1_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352875524)
        ), 

#BpO_D2_BLD2_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352879620)
        ), 

#BpO_D2_BLD3_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352883716)
        ), 

#BpO_D2_BLD1_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352978948)
        ), 

#BpO_D2_BLD2_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352983044)
        ), 

#BpO_D2_BLD3_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352987140)
        ), 

#BpO_D2_BLD4_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352991236)
        ), 

#BpO_D2_BLD1_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352977924)
        ), 

#BpO_D2_BLD2_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352982020)
        ), 

#BpO_D2_BLD3_PNL1_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352986116)
        ), 

#BpO_D2_BLD4_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(352990212)
        ),
 
#Disk 3
#BpO_D3_BLD9_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(353171460)
        ), 

#BmI_D3_BLD1_PNL2_RNG1
        cms.PSet(
            errortype = cms.string('tbmB'),
            detid = cms.uint32(344848388)
        ),
# BpO Sector 4 layer2-3
#BPix_BpO_SEC4_LYR2_LDR7F_MOD1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304144404)
        ), 
#BPix_BpO_SEC4_LYR2_LDR6F_MOD1
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304140308)
        ), 
#BPix_BpO_SEC4_LYR2_LDR7F_MOD2
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304140312)
        ), 
#BPix_BpO_SEC4_LYR2_LDR7F_MOD3
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304140316)
        ),
#BPix_BpO_SEC4_LYR2_LDR6F_MOD4
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304140320)
        ), 
#BPix_BpO_SEC4_LYR2_LDR7F_MOD2
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304144408)
        ), 
#BPix_BpO_SEC4_LYR2_LDR7F_MOD3
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304144412)
        ), 
#BPix_BpO_SEC4_LYR2_LDR7F_MOD4
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304144416)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305217556)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305217560)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305217564)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305217568)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305221652)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305221656)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305221660)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305221664)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305225748)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305225752)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305225756)
        ), 
#
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305225760)
        ), 
#New from May 2
#BPix_BmI_SEC3_LYR2_LDR5F_MOD2 (304099340)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304099340)
        ), 
#BPix_BmI_SEC3_LYR2_LDR5F_MOD3 (304099336)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(304099336)
        ), 
#BPix_BmO_SEC2_LYR3_LDR5F_MOD1 (305201168)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305201168)
        ),  
#BPix_BmO_SEC2_LYR3_LDR5F_MOD2 (305201164)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305201164)
        ),  
#BPix_BmO_SEC2_LYR3_LDR5F_MOD3 (305201160)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305201160)
        ),  
#BPix_BmO_SEC2_LYR3_LDR5F_MOD4 (305201156)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305201156)
        ), 
 #BPix_BmI_SEC6_LYR3_LDR16F_MOD2 (305299468)
        cms.PSet(
            errortype = cms.string('whole'),
            detid = cms.uint32(305299468)
        ), 
#clustTree->Scan("rawid","mod_on.sec==5&&mod_on.layer==4&&(mod_on.ladder==-17||mod_on.ladder==-18||mod_on.ladder==-19||mod_on.ladder==-20)&&(mod_on.module==-1||mod_on.module==-2||mod_on.module==-3||mod_on.module==-4)")
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306319364)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306319368)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306319372)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306319376)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306323460)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306323464)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306323468)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306323472)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306327556)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306327560)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306327564)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306327568)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306331652)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306331656)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306331660)
        ), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(306331664)
        ), 
#FPix_BpO_D2_BLD4_PNL1_RNG2 (352990212)
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(352990212)
        ), 
#FPix_BpI_D2_BLD10_PNL1_RNG1 (352924676)
	cms.PSet(
		errortype = cms.string('none'),
		detid = cms.uint32(352924676),
		badroclist = cms.vuint32(0),
        ), 
#FPix_BpI_D3_BLD1_PNL2_RNG1 (353134596) 
	cms.PSet(
		errortype = cms.string('none'),
		detid = cms.uint32(353134596),
		badroclist = cms.vuint32(7),
        ), 
#New from May 18
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344238084)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344237060)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344241156)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344242180)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344343556)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344344580)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344245252)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344246276)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344347652)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344348676)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344352772)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344351748)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344356868)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344355844)
	), 
	cms.PSet(
		errortype = cms.string('whole'),
		detid = cms.uint32(344819716)
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


