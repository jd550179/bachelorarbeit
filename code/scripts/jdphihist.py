#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT

from bachelorarbeit.code.histfunction import hist
RF="deltaphi.root"
g=ROOT.TFile(RF,"recreate")
g.Close()



#File=ROOT.TFile("/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8.root")

Filename="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8.root"

#Directory=File.GetDirectory("tt_jecUncNom_tauEsNom;1")
tree="ntuple;1"

hist(Filename,tree,"jdphi","dphi",RF,Dir="tt_jecUncNom_tauEsNom;1")
hist(Filename,tree,"m_vis","m_vis",RF,Dir="tt_jecUncNom_tauEsNom;1")
hist(Filename,tree,"jdeta","jdeta",RF,Dir="tt_jecUncNom_tauEsNom;1")



