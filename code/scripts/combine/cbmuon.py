#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import logging
#import Artus.Utility.logger as logger
#log = logging.getLogger(__name__)

import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards


import CombineHarvester.CombineTools.ch as ch


auxshapes="/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src"

cb = ch.CombineHarvester()





cb.AddObservations(["125"],["htt"],["13TeV"],["mt"],[(0,"dphi")])

bkg_proc=["ZTT","ZLL","WJ","TTJ","QCD"]

cb.AddProcesses(["*"],["htt"],["13Tev"],["mt"],bkg_proc,[(0,"dphi")], False)

signal_proc=["qqH125","WH125","ZH125","ggH125_000"]

cb.AddProcesses(["125"],["htt"],["13Tev"],["mt"],signal_proc,[(0,"dphi")], True)

#cb.cp().process(bkg_proc).AddSyst(cb, "lumi_$ERA", "lnN", 1.022)


cb.cp().backgrounds().ExtractShapes(auxshapes+"/dphi_2016.root","$BIN/$PROCESS","$BIN/$PROCESS$MASS_$SYSTEMATIC")

cb.cp().signals().ExtractShapes(auxshapes+"/dphi_2016.root","$BIN/$PROCESS","$BIN/$PROCESS$MASS_$SYSTEMATIC")


print cb.PrintAll()
