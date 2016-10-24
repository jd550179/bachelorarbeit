#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
from Artus.HarryPlotter.utility.roottools import RootTools

from bachelorarbeit.code.histfunction import hist
RF="deltaphi.root"


g=ROOT.TFile(RF,"recreate")

g.Close()
bins=40
xmin=0
xmax=1000


#File=ROOT.TFile("/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8.root")

Filename="/net/scratch_cms/institut_3b/tmuller/artus/2016-10-15_13-04_Run2CPStudies_SM_Run2Analysis_Fall15_a1PolarisationChannel/merged/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8/DYJetsToLLM50_RunIIFall15MiniAODv2_PU25nsData2015v1_13TeV_MINIAOD_madgraph-pythia8.root"

#Directory=File.GetDirectory("tt_jecUncNom_tauEsNom")

tree="ntuple;1"

dphi1=hist(Filename,tree,"jdphi","dphi1",RF,10,-7,7,"test/data1",Dir="mt_jecUncNom_tauEsNom", fillcolor=0,cuts= "jdphi>-900")
dphi2=hist(Filename,tree,"jdphi","dphi2",RF,10,0,7,"test/data2",Dir="mt_jecUncNom_tauEsNom", fillcolor=2)


hist(Filename,tree,"m_vis","m_vis1",RF,bins,xmin,xmax,"test2/data",Dir="tt_jecUncNom_tauEsNom",fillcolor=1)
hist(Filename,tree,"m_vis","m_vis2",RF,bins,xmin,xmax,"test2/data2",Dir="tt_jecUncNom_tauEsNom",fillcolor=2)
#deta=hist(Filename,tree,"jdeta","jdeta",RF,Dir="tt_jecUncNom_tauEsNom",fillcolor=2)



