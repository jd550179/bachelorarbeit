#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT

from histfunction import hist
g=ROOT.TFile("firsthistograms.root","recreate")
g.Close()
hist("/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src/bachelorarbeit/gaussians3.root","gaussians3","var2","hist1","firsthistograms.root",title="gaussdistribution",xtitle="x-axis",ytitle="y-axis")
hist("/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src/bachelorarbeit/gaussians3.root","gaussians1","var3","hist2","firsthistograms.root",title="gaussdistribution",xtitle="x-axis",ytitle="y-axis")


