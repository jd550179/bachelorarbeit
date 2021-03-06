#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
ROOT.gROOT.SetBatch(True)
from Artus.HarryPlotter.utility.roottools import RootTools

from bachelorarbeit.code.histfunction import hist
from bachelorarbeit.code.stacked_hist import stackedhist

RF="ttdphipostfit.root"

RF2="phi_postfit_stackedtt_2016.root"
g=ROOT.TFile(RF2,"recreate")
g.Close()


List=["QCD","WJ","TTJ","ZTT","VV","ZLL","qqH","WH","ZH"]
LegendList=["QCD","W+Jets","tt+jets","Z->tautau","Z->ll","qqH","WH","ZH"]

Signallistsm=["dphi_postfit/TotalSig"]
smlegend=["sm"]

Signallistmm=["dphi_postfit/ggH125_050"]
mmlegend=["maxmixing"]

Signallistpc=["dphi_postfit/ggH125_100"]
pclegend=["pseudoscalar"]

Data="dphi_postfit/data_obs"
Datalegend="SM-Data"

stackedhist(RF,RF2,"phistacked",List,"dphi_postfit",Signallistsm,smlegend,data=Data,datalegend=Datalegend,title="phitt_stacked",xtitle="delta_phi",maximum=150, savename="dphitt_postfit_2016sm.png")
