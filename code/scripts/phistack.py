#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
ROOT.gROOT.SetBatch(True)
from Artus.HarryPlotter.utility.roottools import RootTools

from bachelorarbeit.code.histfunction import hist
from bachelorarbeit.code.stacked_hist import stackedhist

RF="dphi.root"

g=ROOT.TFile(RF,"recreate")

g.Close()

tree="ntuple;1"

DY="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8.root"

WJets="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/WJetsToLNu_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8/WJetsToLNu_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8.root"

tt="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/TT_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_powheg-pythia8/TT_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_powheg-pythia8.root"

merged="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/"

Diboson=["WWTo1L1Nu2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/WWTo1L1Nu2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root","WZJToLLLNu_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatno-pythia8/WZJToLLLNu_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatno-pythia8.root","WZTo1L1Nu2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/WZTo1L1Nu2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root","WZTo2L2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/WZTo2L2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root","WZTo1L3Nu_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/WZTo1L3Nu_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root ","ZZTo2L2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/ZZTo2L2Q_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root","ZZTo4L_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/ZZTo4L_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root","WZJets_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8/WZJets_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_amcatnlo-pythia8.root"]
for i in range(len(Diboson)):
	Diboson[i]=merged+Diboson[i]
print len(Diboson)

SM="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/SingleMuon_Run2015D_16Dec2015v1_13TeV_MINIAOD/SingleMuon_Run2015D_16Dec2015v1_13TeV_MINIAOD.root"

Cuts="(mt_1<40.0) *((q_1*q_2)<0.0) *(againstElectronVLooseMVA6_2 > 0.5) *(againstMuonTight3_2 > 0.5) *(extraelec_veto < 0.5)*(extramuon_veto < 0.5) *(dilepton_veto < 0.5) *(iso_1 < 0.1) *(byTightIsolationMVArun2v1DBoldDMwLT_2 > 0.5) *(jdphi>-900) *eventWeight"


hist(DY,tree,"jdphi","dphi1",RF,20,-4,4,"dphi/DY","HIST",Dir="mt_jecUncNom_tauEsNom", fillcolor=797,linecolor=797,cuts= Cuts+"*2.3*1000")

hist(WJets,tree,"jdphi","dphi1",RF,20,-4,4,"dphi/WJ","HIST",Dir="mt_jecUncNom_tauEsNom", fillcolor=892,linecolor=892,cuts= Cuts+"*2.3*1000")

hist(tt,tree,"jdphi","dphi1",RF,20,-4,4,"dphi/ttJ","HIST",Dir="mt_jecUncNom_tauEsNom", fillcolor=592,linecolor=592,cuts=Cuts+"*2.3*1000")

hist(Diboson,tree,"jdphi","dphi1",RF,20,-4,4,"dphi/VV","HIST",Dir="mt_jecUncNom_tauEsNom", fillcolor=432,linecolor=432,cuts= Cuts+"*2.3*1000")

hist(SM,tree,"jdphi","dphi1",RF,20,-4,4,"dphi/data_obs_errorbar","E0",Dir="mt_jecUncNom_tauEsNom", fillcolor=0,linecolor=1,cuts= Cuts)










RF2="phi_stacked.root"
g=ROOT.TFile(RF2,"recreate")
g.Close()


List=["dphi/WJ","dphi/DY","dphi/ttJ","dphi/VV"]
LegendList=["W+Jets","DY","tt+jets","Di-boson"]

Data="dphi/data_obs_errorbar"
Datalegend="SM-Data"

stackedhist(RF,RF2,"phistacked",List,LegendList,data=Data,datalegend=Datalegend,title="phi_stacked",xtitle="delta_phi", maximum=800)





