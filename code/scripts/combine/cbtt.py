#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import logging
#import Artus.Utility.logger as logger
#log = logging.getLogger(__name__)

import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards

import ROOT


import CombineHarvester.CombineTools.ch as ch


auxshapes="/home/home2/institut_3b/degens/bachelorarbeit/CMSSW_7_4_7/src"

cb = ch.CombineHarvester()





cb.AddObservations(["*"],["htt"],["13TeV"],["tt"],[(0,"dphi")])

bkg_procs=["ZTT","ZLL","WJ","TTJ","QCD","qqH125","WH125","ZH125"]

cb.AddProcesses(["*"],["htt"],["13TeV"],["tt"],bkg_procs,[(0,"dphi")], False)

signal_procs=["ggH125_000"]

cb.AddProcesses(["125"],["htt"],["13TeV"],["tt"],signal_procs,[(0,"dphi")], True)



cb.cp().process(["ZTT","ZLL","WJ","TTJ","qqH125","WH125","ZH125"]).AddSyst(cb, "lumi_$ERA", "lnN",ch.SystMap("era") (["13TeV"], 1.027))
cb.cp().signals().AddSyst(cb, "lumi_$ERA", "lnN",ch.SystMap("era") (["13TeV"], 1.027))



cb.cp().backgrounds().ExtractShapes(auxshapes+"/dphitt_2016.root","$BIN/$PROCESS","$BIN/$PROCESS$MASS_$SYSTEMATIC")

cb.cp().signals().ExtractShapes(auxshapes+"/dphitt_2016.root","$BIN/$PROCESS","$BIN/$PROCESS$MASS_$SYSTEMATIC")

g=ROOT.TFile("htt_tt.input.root","recreate")
g.Close()

cb.WriteDatacard("cardtt.txt", "htt_tt.input.root")


print cb.PrintAll()
