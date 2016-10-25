# -*- coding: utf-8 -*-

import ROOT

#from bachelorarbeit.code.histfunction import hist

f=ROOT.TFile("deltaphi.root")
from Artus.HarryPlotter.utility.roottools import RootTools

def stackedhist(ROOTfile, rootname,path, undergroundlist,undergroundlegendlist,signallist="default",signallegendlist="default",title="default",xtitle="default",ytitle="default",savename="default"):
	f=ROOT.TFile(ROOTfile)
	c=ROOT.TCanvas()	
	stack=ROOT.THStack(ROOTfile,"")
	legend=ROOT.TLegend(0.4,0.6,0.89,0.89)

	n=len(undergroundlist)
	for i in range(n):
		undergrounddata=f.Get(undergroundlist[i])			
		stack.Add(undergrounddata)
		legend.AddEntry(undergrounddata,undergroundlegendlist[i],"f")
	if signallist!="default":
		j=len(signallist)	
		for i in range(j):
			signal=f.Get(signallist[i])
			stack.Add(signal)
			if signallegendlist!="default":
				legend.AddEntry(signal,signallegendlist[i],"f")
			

	if title!='default':
		stack.SetTitle(title)

		
	stack.Draw()
	if xtitle!='default':
		stack.GetXaxis().SetTitle(xtitle)
	if ytitle!='default':
		stack.GetYaxis().SetTitle(ytitle)

	#c.Modified()
	legend.Draw()
	
	g=ROOT.TFile(rootname,"update")
	RootTools.write_object(g,stack,path)
	g.Close()
	
	if savename!="default":
		c.SaveAs(savename)
	else:
		c.SaveAs("data.png")
	
