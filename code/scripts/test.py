#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT

from bachelorarbeit.code.histfunction import hist
RF="firsthistograms.root"
g=ROOT.TFile(RF,"recreate")
g.Close()
#red=ROOT.TColor.GetColor(204,7,30)
hist("/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src/bachelorarbeit/gaussians3.root","gaussians3","var2","hist1",RF,title="gaussdistribution",xtitle="x-axis",ytitle="y-axis", linecolor=2,fillcolor=5)
hist("/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src/bachelorarbeit/gaussians3.root","gaussians1","var3","hist2",RF,title="gaussdistribution",xtitle="x-axis",ytitle="y-axis")
hist("/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src/bachelorarbeit/gaussians3.root","gaussians2","var0","hist3",RF,title="gaussdistribution",xtitle="x-axis",ytitle="y-axis",linecolor=2,fillcolor=20)



