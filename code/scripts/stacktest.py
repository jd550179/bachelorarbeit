#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT

#from bachelorarbeit.code.histfunction import hist
#from bachelorarbeit.code.stacked_hist import stackedhist
from bachelorarbeit.code.stacked_hist import stackedhist

RF="stacked_phi.root"
g=ROOT.TFile(RF,"recreate")
g.Close()


ROOTfile="deltaphi.root"
List=["test2/data","test2/data2"]

stackedhist(ROOTfile,RF,"phistacked",List)
