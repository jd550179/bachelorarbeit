# -*- coding: utf-8 -*-

import ROOT

from bachelorarbeit.code.histfunction import hist

f=ROOT.TFile("deltaphi.root")

def stackedhist(ROOTfile, undergroundlist,signallist="default"):
	f=ROOT.TFile(ROOTfile)
	undergrounddata=[]	
	stack=ROOT.THStack(ROOTfile,"")
	
	n=len(undergroundlist)
	for i in range(n):
		
		undergrounddata.append(f.Get(undergroundlist[i])		
	
		stack.add(undergrounddata[i])	
	
