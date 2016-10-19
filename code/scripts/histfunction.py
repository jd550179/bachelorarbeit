#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT


def hist(rootfile,tree, var,name,rootname,title="default" ,  xtitle="default",ytitle="default"):
	f=ROOT.TFile(rootfile)
	t=f.Get(tree)
	t.Draw(var +">>temph")
	h=ROOT.gDirectory.Get("temph")

	if title!='default':
		h.SetTitle(title)

	if xtitle!='default':
		h.SetXTitle(xtitle)
	if ytitle!='default':
		h.SetYTitle(ytitle)

	
	g=ROOT.TFile(rootname,"update")
	h.Write(name)
	g.Write()
	g.Close()
	return h



	
