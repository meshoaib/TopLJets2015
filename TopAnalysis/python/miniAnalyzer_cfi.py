import FWCore.ParameterSet.Config as cms

analysis = cms.EDAnalyzer("MiniAnalyzer",
                          saveTree               = cms.bool(True),
                          savePF                 = cms.bool(True),
                          triggerBits            = cms.InputTag("TriggerResults","","HLT"),
                          prescales              = cms.InputTag("patTrigger"),
                          triggersToUse          = cms.vstring('HLT_Ele32_eta2p1_WPTight_Gsf_v',
                                                               'HLT_IsoMu24_v',
                                                               'HLT_IsoTkMu24_v',
                                                               'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v',
                                                               'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
                                                               'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v',
                                                               #'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v',
                                                               'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v',
                                                               'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v',
                                                               'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v',
                                                               'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',
                                                               'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v'),
                          rho                    = cms.InputTag("fixedGridRhoFastjetAll"),
                          vertices               = cms.InputTag("offlineSlimmedPrimaryVertices"),
                          applyLeptonCorrections = cms.bool(False),
                          muons                  = cms.InputTag("slimmedMuons"),
                          muonCorrFile           = cms.string("muon_MC.txt"),
                          electrons              = cms.InputTag("slimmedElectrons"),
                          calibElectrons         = cms.InputTag("calibratedPatElectrons"),
                          jets                   = cms.InputTag('selectedUpdatedPatJetsUpdatedJECBTag'),
                          metFilterBits          = cms.InputTag("TriggerResults","","PAT"),
                          metFiltersToUse        = cms.vstring('Flag_HBHENoiseFilter',
                                                               'Flag_HBHENoiseIsoFilter',
                                                               'Flag_EcalDeadCellTriggerPrimitiveFilter',
                                                               'Flag_goodVertices',
                                                               'Flag_eeBadScFilter',
                                                               'Flag_globalTightHalo2016Filter'), 
                          badChCandFilter        = cms.InputTag('BadChargedCandidateFilter'),
                          badPFMuonFilter        = cms.InputTag('BadPFMuonFilter'),
                          mets                   = cms.InputTag('slimmedMETs'),                          
                          puppimets              = cms.InputTag('slimmedMETsPuppi'),
                          pfCands                = cms.InputTag('packedPFCandidates'),                          
                          eleMvaIdMap            = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                          eleVetoIdMap           = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
                          eleLooseIdMap          = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
                          eleMediumIdMap         = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
                          eleTightIdMap          = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
                          eleVetoIdFullInfoMap   = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
                          eleLooseIdFullInfoMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
                          eleMediumIdFullInfoMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
                          eleTightIdFullInfoMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight")
                          )
