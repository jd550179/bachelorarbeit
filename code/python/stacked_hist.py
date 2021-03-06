# -*- coding: utf-8 -*-

import ROOT

#from bachelorarbeit.code.histfunction import hist


from Artus.HarryPlotter.utility.roottools import RootTools


Colors={"QCD":820,"WJ":892,"TTJ":592,"ZTT":797,"ZLL":860,"qqH":1,"WH":7,"ZH":8,"VV":432}
histnames={"QCD":"QCD","WJ":"W+Jets","TTJ":"tt+jets","ZTT":"Z->tautau","ZLL":"Z->ll","qqH":"qqH","WH":"WH","ZH":"ZH","VV":"Diboson"}


def stackedhist(ROOTfile, rootname,path, undergroundlist,Directory,signallist="default",signallegendlist="default",data="default",datalegend="default",title="default",xtitle="default",ytitle="default",savename="default",maximum="default",minimum="default"):
	f=ROOT.TFile(ROOTfile)
	c=ROOT.TCanvas()	
	stack=ROOT.THStack(ROOTfile,"")
	legend=ROOT.TLegend(0.9,0.65,1.0,0.9)

	
	for i in undergroundlist:
		undergrounddata=f.Get(Directory+"/"+i)
		undergrounddata.SetFillColor(Colors[i])			
		stack.Add(undergrounddata)
		legend.AddEntry(undergrounddata,histnames[i],"f")


	if signallist!="default":
		j=len(signallist)	
		for i in range(j):
			signal=f.Get(signallist[i])
			stack.Add(signal)
			if signallegendlist!="default":
				legend.AddEntry(signal,signallegendlist[i],"f")
				

	if title!='default':
		stack.SetTitle(title)
		

		
	stack.Draw("HIST")

	
	if xtitle!='default':
		stack.GetXaxis().SetTitle(xtitle)
	if ytitle!='default':
		stack.GetYaxis().SetTitle(ytitle)
	
	if maximum!="default":
		stack.SetMaximum(maximum)
	if minimum!="default":
		stack.SetMinimum(minimum)


	if data!="default":
		d=f.Get(data)
		
		d.Draw("E0 same" )
	if datalegend!="default":
		legend.AddEntry(d,datalegend,"same")


	#c.Modified()
	legend.Draw()
	
	g=ROOT.TFile(rootname,"update")
	RootTools.write_object(g,stack,path)
	g.Close()
	
	if savename!="default":
		c.SaveAs(savename)
	else:
		c.SaveAs("data.png")
	
