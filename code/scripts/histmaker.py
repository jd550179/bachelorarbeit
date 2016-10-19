#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ROOT


f=ROOT.TFile("/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src/bachelorarbeit/gaussians3.root")

t1=f.Get("gaussians1")
t2=f.Get("gaussians2")
t3=f.Get("gaussians3")

t1.Draw("var1>>hist1_1")
t2.Draw("var1>>hist2_1")
t3.Draw("var1>>hist3_1")

h1 = ROOT.gDirectory.Get("hist1_1")
h2 = ROOT.gDirectory.Get("hist2_1")
h3 = ROOT.gDirectory.Get("hist3_1")

h1.SetTitle("histogram1_1" )
h1.SetXTitle("x-axis" )
h1.SetYTitle("counts" )

h2.SetTitle("histogram2_1" )
h2.SetXTitle("x-axis" )
h2.SetYTitle("counts" )

h3.SetTitle("histogram3_1" )
h3.SetXTitle("x-axis" )
h3.SetYTitle("counts" )






g=ROOT.TFile("firsthistograms.root","recreate")

h1.Write("histogram1_1")
h2.Write("histogram2_1")
h3.Write("histogram3_1")

g.Write()
g.Close()

