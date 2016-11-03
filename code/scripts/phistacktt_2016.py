#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
ROOT.gROOT.SetBatch(True)
from Artus.HarryPlotter.utility.roottools import RootTools

from bachelorarbeit.code.histfunction import hist
from bachelorarbeit.code.stacked_hist import stackedhist

RF="dphitt_2016.root"

g=ROOT.TFile(RF,"recreate")

g.Close()


bins=40

tree="ntuple"

merged="/net/scratch_cms/institut_3b/hsert/artus/2016-10-20_16-45_Spring2016plus_CPconfig/merged/"

DY=merged+"DYJetsToLLM50_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_madgraph-pythia8_ext1/DYJetsToLLM50_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_madgraph-pythia8_ext1.root"

WJets=merged+"WJetsToLNu_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_madgraph-pythia8/WJetsToLNu_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_madgraph-pythia8.root"

tt=merged+"TT_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_powheg-pythia8_ext4/TT_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_powheg-pythia8_ext4.root"



Diboson=[merged+"WWTo1L1Nu2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8/WWTo1L1Nu2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8.root",merged+"WZTo1L1Nu2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8/WZTo1L1Nu2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8.root",merged+"WZTo1L3Nu_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8/WZTo1L3Nu_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8.root",merged+"WZTo2L2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8/WZTo2L2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8.root",merged+"ZZTo2L2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8/ZZTo2L2Q_RunIISpring16MiniAODv2_PUSpring16_13TeV_MINIAOD_amcatnlo-pythia8.root"]







sm="/net/scratch_cms/institut_3b/hsert/artus/2016-10-24_15-07_InitialStateCPmixing16_CPconfig/merged/GluGluH2JetsToTauTauM125CPmixingsmJHU_RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_13TeV_MINIAOD_unspecified/GluGluH2JetsToTauTauM125CPmixingsmJHU_RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_13TeV_MINIAOD_unspecified.root"

maxmix="/net/scratch_cms/institut_3b/hsert/artus/2016-10-24_15-07_InitialStateCPmixing16_CPconfig/merged/GluGluH2JetsToTauTauM125CPmixingmaxmixJHU_RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_13TeV_MINIAOD_unspecified/GluGluH2JetsToTauTauM125CPmixingmaxmixJHU_RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_13TeV_MINIAOD_unspecified.root"

pc="/net/scratch_cms/institut_3b/hsert/artus/2016-10-24_15-07_InitialStateCPmixing16_CPconfig/merged/GluGluH2JetsToTauTauM125CPmixingpseudoscalarJHU_RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_13TeV_MINIAOD_unspecified/GluGluH2JetsToTauTauM125CPmixingpseudoscalarJHU_RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_13TeV_MINIAOD_unspecified.root"







ggH=merged+"/GluGluHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8/GluGluHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8.root"

qqH=merged+"/VBFHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8/VBFHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8.root"

WH=[merged+"/WminusHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8/WminusHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8.root",merged+"/WplusHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8/WplusHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8.root"]

ZH=merged+"/ZHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8/ZHToTauTauM125_RunIISpring16MiniAODv2reHLT_PUSpring16RAWAODSIM_13TeV_MINIAOD_powheg-pythia8.root"





Data=[merged+"Tau_Run2016B_PromptRecov2_13TeV_MINIAOD/Tau_Run2016B_PromptRecov2_13TeV_MINIAOD.root",merged+"Tau_Run2016C_PromptRecov2_13TeV_MINIAOD/Tau_Run2016C_PromptRecov2_13TeV_MINIAOD.root",merged+"Tau_Run2016D_PromptRecov2_13TeV_MINIAOD/Tau_Run2016D_PromptRecov2_13TeV_MINIAOD.root",merged+"Tau_Run2016E_PromptRecov2_13TeV_MINIAOD/Tau_Run2016E_PromptRecov2_13TeV_MINIAOD.root"]




#Cuts="(jdphi>-900) *eventWeight"

#deltapseudorapidity=(log((sqrt(jm_1*jm_1+jpt_1*cosh(jeta_1)*jpt_1*cosh(jeta_1))+jpt_1*sinh(jeta_1))/sqrt(jm_1*jm_1+jpt_1*jpt_1))-log((sqrt(jm_2*jm_2+jpt_2*cosh(jeta_2)*jpt_2*cosh(jeta_2))+jpt_2*sinh(jeta_2))/sqrt(jm_2*jm_2+jpt_2*jpt_2)))<2

Cuts="(extraelec_veto < 0.5)*(extramuon_veto < 0.5) *(againstElectronVLooseMVA6_1 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5) *(againstMuonLoose3_1 > 0.5)*(againstMuonLoose3_2 > 0.5) *(byTightIsolationMVArun2v1DBoldDMwLT_1 > 0.5) *(byTightIsolationMVArun2v1DBoldDMwLT_2 > 0.5) *(jdphi>-900) *eventWeight *((log((sqrt(jm_1*jm_1+jpt_1*cosh(jeta_1)*jpt_1*cosh(jeta_1))+jpt_1*sinh(jeta_1))/sqrt(jm_1*jm_1+jpt_1*jpt_1))*log((sqrt(jm_2*jm_2+jpt_2*cosh(jeta_2)*jpt_2*cosh(jeta_2))+jpt_2*sinh(jeta_2))/sqrt(jm_2*jm_2+jpt_2*jpt_2)))<0)*((q_1*q_2)<0.0)"

#Cuts="(jdphi>-900) *eventWeight *((log((sqrt(jm_1*jm_1+jpt_1*cosh(jeta_1)*jpt_1*cosh(jeta_1))+jpt_1*sinh(jeta_1))/sqrt(jm_1*jm_1+jpt_1*jpt_1))*log((sqrt(jm_2*jm_2+jpt_2*cosh(jeta_2)*jpt_2*cosh(jeta_2))+jpt_2*sinh(jeta_2))/sqrt(jm_2*jm_2+jpt_2*jpt_2)))<0)"





hist(DY,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/ZTT","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=797,linecolor=1,cuts= Cuts+"*12.9*1000 *(gen_match_2 == 5)")
hist(DY,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/ZLL","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=860,linecolor=1,cuts= Cuts+"*12.9*1000 *(gen_match_2 < 5 || gen_match_2 == 6)")

hist(WJets,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/WJ","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=892,linecolor=1,cuts= Cuts+"*12.9*1000")
hist(tt,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/TTJ","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=592,linecolor=1,cuts=Cuts+"*12.9*1000")
hist(Diboson,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/VV","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=432,linecolor=1,cuts= Cuts+"*12.9*1000")
hist(Data,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/QCD","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=820,linecolor=1,cuts= Cuts.replace("(q_1*q_2)<0.0)", "(q_1*q_2)>0.0)"))
hist(Data,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/data_obs","E0",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=1,cuts= Cuts)


hist(sm,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/ggH125_000","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=798,cuts=Cuts+"*12.9*1141")
hist(maxmix,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/ggH125_050","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=2,cuts=Cuts+"*12.9*1606")
hist(pc,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/ggH125_100","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=4,cuts=Cuts+"*12.9*2411")


hist(qqH,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/qqH","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=1,cuts=Cuts+"*12.9*1000")
hist(WH,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/WH","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=7,cuts=Cuts+"*12.9*1000")
hist(ZH,tree,"jdphi","dphi1",RF,bins,-4,4,"dphi/ZH","HIST",Dir="tt_jecUncNom_tauEsNom", fillcolor=0,linecolor=8,cuts=Cuts+"*12.9*1000")




#stack


RF2="phi_stackedtt_2016.root"
g=ROOT.TFile(RF2,"recreate")
g.Close()


List=["QCD","WJ","TTJ","VV","ZTT","ZLL","qqH","WH","ZH"]
LegendList=["QCD","W+Jets","tt+jets","Z->tautau","Z->ll","qqH","WH","ZH"]

Signallistsm=["dphi/ggH125_000"]
smlegend=["sm"]

Signallistmm=["dphi/ggH125_050"]
mmlegend=["maxmixing"]

Signallistpc=["dphi/ggH125_100"]
pclegend=["pseudoscalar"]

Data="dphi/data_obs"
Datalegend="SM-Data"

stackedhist(RF,RF2,"phistacked",List,"dphi",Signallistsm,smlegend,data=Data,datalegend=Datalegend,title="phitt_stacked",xtitle="delta_phi",maximum=150, savename="dphitt_2016sm.png")

stackedhist(RF,RF2,"phistacked",List,"dphi",Signallistmm,mmlegend,data=Data,datalegend=Datalegend,title="phitt_stacked",xtitle="delta_phi",maximum=150, savename="dphitt_2016mm.png")

stackedhist(RF,RF2,"phistacked",List,"dphi",Signallistpc,pclegend,data=Data,datalegend=Datalegend,title="phitt_stacked",xtitle="delta_phi",maximum=150, savename="dphitt_2016pc.png")







c2=ROOT.TCanvas()
c2.Divide(1,3)



legend1=ROOT.TLegend(0.15,0.8,0.3,0.9)
legend2=ROOT.TLegend(0.15,0.8,0.3,0.9)
legend3=ROOT.TLegend(0.15,0.8,0.3,0.9)

f=ROOT.TFile(RF)

c2.cd(1)

smdraw=f.Get("dphi/ggH125_000")

smscala=smdraw.Integral()


smdraw.Scale(1/smscala)
smdraw.Draw("same L")
legend1.AddEntry(smdraw,"standardmodel", "f")
legend1.Draw()

c2.cd(2)

mmdraw=f.Get("dphi/ggH125_050")

mmscala=mmdraw.Integral()
mmdraw.Scale(1/mmscala)

mmdraw.Draw("same L")

legend2.AddEntry(mmdraw,"maxmixing", "f")
legend2.Draw()


c2.cd(3)
pcdraw=f.Get("dphi/ggH125_100")
pcscala=pcdraw.Integral()


pcdraw.Scale(1/pcscala)


pcdraw.Draw("same L")



#smdraw.SetMaximum(0.2)



legend3.AddEntry(pcdraw,"pseudoscalar", "f")

legend3.Draw()

c2.SaveAs("dphitt_cp.png")



zzhist=f.Get("dphi/ZTT")
print zzhist.Integral()





