# -*- coding: utf-8 -*-

import ROOT

#from bachelorarbeit.code.histfunction import hist

f=ROOT.TFile("deltaphi.root")
from Artus.HarryPlotter.utility.roottools import RootTools

def stackedhist(ROOTfile, rootname,path, undergroundlist,signallist="default"):
	f=ROOT.TFile(ROOTfile)
	c=ROOT.TCanvas()	
	stack=ROOT.THStack(ROOTfile,"")
	
	n=len(undergroundlist)
	for i in range(n):
		undergrounddata=f.Get(undergroundlist[i])			
		stack.Add(undergrounddata)
	if signallist!="default":
		j=len(signallist)	
		for i in j:
			signal=f.Get(signallist[j])
			stack.Add(signal)

	
	stack.Draw()
	
	g=ROOT.TFile(rootname,"update")
	RootTools.write_object(g,stack,path)
	g.Close()
	return c.SaveAs("data.png")
	
