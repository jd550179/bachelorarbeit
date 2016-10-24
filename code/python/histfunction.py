# -*- coding: utf-8 -*-


import ROOT
from Artus.HarryPlotter.utility.roottools import RootTools

def hist(rootfile,tree, var,name,rootname,bins,xmin,xmax,path,Dir="default" ,title="default" ,  xtitle="default",ytitle="default", linecolor= "default", fillcolor="default",cuts="default"):
	
	t = ROOT.TChain("tree", "tree")
	t.Add(rootfile+"/"+(Dir+"/" if Dir!="default" else "")+tree)
	
	h=ROOT.TH1F("temph",name,bins,xmin,xmax)
	if cuts!="default":
		t.Project("temph",var,cuts)
	else:	
		t.Project("temph",var )
	

	

	if title!='default':
		h.SetTitle(title)

	if xtitle!='default':
		h.SetXTitle(xtitle)
	if ytitle!='default':
		h.SetYTitle(ytitle)

	if linecolor!='default':
		h.SetLineColor(linecolor)
	if fillcolor!='default':
		h.SetFillColor(fillcolor)

	
	g=ROOT.TFile(rootname,"update")
	RootTools.write_object(g,h,path)
	g.Close()
	return h



	
