# -*- coding: utf-8 -*-

import ROOT

#from bachelorarbeit.code.histfunction import hist

f=ROOT.TFile("deltaphi.root")

def stackedhist(ROOTfile, rootname,name, undergroundlist,signallist="default"):
	f=ROOT.TFile(ROOTfile)
	#undergrounddata=[]	
	stack=ROOT.THStack(ROOTfile,"")
	
	n=len(undergroundlist)
	for i in range(n):
		
		undergrounddata=f.Get(undergroundlist[i])	
		
		undergrounddata.Print()
		stack.Add(undergrounddata)	
		stack.Draw()

	g=ROOT.TFile(rootname,"update")
	stack.Write(name)
	g.Write()
	g.Close()
	return stack
	
