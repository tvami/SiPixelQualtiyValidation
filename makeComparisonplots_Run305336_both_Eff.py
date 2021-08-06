#!/usr/bin/env python
from ROOT import *
import sys
import tdrstyle

#  Usage:
# python makeComparisonplots_Run305336_both_Eff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root  "Tracking/Run summary/TrackParameters/highPurityTracks/dzPV0p1/HitEffFromHitPatternAll/" globalEfficiencies -b


def drawandSaveHistos(pname, chisto, rhisto, xTitle="", yTitle="", xLow=0, xUp=0, yLow=0, yUp=0):
    tdrstyle.setTDRStyle()
    c1 = TCanvas(pname, "", 50,50,1200,1200)
    #c1.cd()

    chisto.SetTitle("")
    rhisto.SetTitle("")
    
    chisto.GetXaxis().SetBinLabel(1,"Layer 1");
    chisto.GetXaxis().SetBinLabel(2,"Layer 2");
    chisto.GetXaxis().SetBinLabel(3,"Layer 3");
    chisto.GetXaxis().SetBinLabel(4,"Layer 4");
    chisto.GetXaxis().SetBinLabel(5,"Disk 1");
    chisto.GetXaxis().SetBinLabel(6,"Disk 2");
    chisto.GetXaxis().SetBinLabel(7,"Disk 3");
    chisto.GetXaxis().SetLabelSize(0.15)
    
    rhisto.GetXaxis().SetBinLabel(1,"Layer 1");
    rhisto.GetXaxis().SetBinLabel(2,"Layer 2");
    rhisto.GetXaxis().SetBinLabel(3,"Layer 3");
    chisto.GetXaxis().SetBinLabel(4,"Layer 4");
    chisto.GetXaxis().SetBinLabel(5,"Disk 1");
    chisto.GetXaxis().SetBinLabel(6,"Disk 2");
    chisto.GetXaxis().SetBinLabel(7,"Disk 3");
    rhisto.GetXaxis().SetLabelSize(0.15)
        

    chisto.GetYaxis().SetTitle(yTitle)
    chisto.GetYaxis().SetTitleOffset(1.2);
    chisto.GetYaxis().SetTitleSize(0.05);
    rhisto.GetYaxis().SetTitle(yTitle)
    rhisto.GetYaxis().SetTitleOffset(1.2);
    rhisto.GetYaxis().SetTitleSize(0.05);
    
    chisto.GetXaxis().SetRangeUser(0, 7)
    rhisto.GetXaxis().SetRangeUser(0, 7)


    chisto.SetMarkerColor(kGreen+2)
    chisto.SetLineColor(kGreen+2)
    chisto.SetMarkerStyle(kFullTriangleDown)
    chisto.SetMarkerSize(2);
    chisto.Scale(0.01)

    rhisto.SetMarkerColor(kBlue)
    rhisto.SetLineColor(kBlue)
    rhisto.SetMarkerStyle(kOpenSquare)
    rhisto.SetMarkerSize(2);
    rhisto.Scale(0.01)
    
    x1_l = 0.92
    #y1_l = 0.91
    y1_l = 0.48

    dx_l = 0.6
    dy_l = 0.1
    x0_l = x1_l-dx_l
    y0_l = y1_l-dy_l

    leg = TLegend(x0_l,y0_l,x1_l, y1_l,"","brNDC");
    leg.SetBorderSize(1);
    leg.SetLineColor(1);
    leg.SetLineStyle(1);
    leg.SetLineWidth(1);
    leg.SetFillColor(0);
    leg.SetFillStyle(1001);
    entry=leg.AddEntry(chisto,"Dynamic, high granularity bad component list","lp");
    entry.SetMarkerSize(2); 
    
    entry2=leg.AddEntry(rhisto,"Static bad component list","lp");
    entry2.SetMarkerSize(2); 
    
    rp =  TRatioPlot(chisto,rhisto);
    rp.GetXaxis().SetRangeUser(0, 8)
    rp.GetXaxis().SetLimits(0,8.001)
    rp.SetH1DrawOpt("PESAMEAXIS");
    rp.SetH2DrawOpt("PESAMEAXIS");
    rp.Draw("PESAMEAXIS");
    rp.SetLeftMargin(0.13);
    rp.SetRightMargin(0.05);
    rp.SetUpTopMargin(0.1);
    rp.SetLowTopMargin(0.02);
    rp.SetLowBottomMargin(0.35);
    
    rp.GetLowerRefGraph().SetMinimum(0.98);
    rp.GetLowerRefGraph().SetMaximum(1.02);
    rp.GetLowerRefGraph().SetMarkerColor(kGreen+2)
    rp.GetLowerRefGraph().SetLineColor(kGreen+2)
    rp.GetLowerRefGraph().SetMarkerStyle(kFullTriangleDown)
    rp.GetLowerRefGraph().SetMarkerSize(2);
    
    rp.GetLowYaxis().SetNdivisions(505);
    rp.GetLowerRefYaxis().SetTitle("Ratio");
    rp.GetLowerRefYaxis().SetTitleSize(0.05);
    rp.GetLowerRefYaxis().SetTitleOffset(1.2);
    rp.GetLowerRefYaxis().SetLabelSize(0.035)
    
    rp.GetXaxis().SetBinLabel(1,"Layer 1");
    rp.GetXaxis().SetBinLabel(2,"Layer 2");
    rp.GetXaxis().SetLabelSize(0.035);
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(1,"Layer 1");
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(2,"Layer 2");
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(3,"Layer 3");
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(4,"Layer 4");
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(5,"Disk 1");
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(6,"Disk 2");
    rp.GetLowerRefGraph().GetXaxis().SetBinLabel(7,"Disk 3");
    rp.GetLowerRefGraph().GetXaxis().SetLabelSize(0.035)
    
    rp.GetUpperRefYaxis().SetRangeUser(0.75, 1.01)
    rp.GetUpperRefYaxis().SetLimits(0.75, 1.01)
    
    axis1 = TGaxis(-4.5,-0.2,5.5,-0.2,-6,8,510,"");
    axis1.SetName("axis1");
    axis1.Draw("SAME");
    gPad.Update()
    
    c1.Modified()
    c1.Update()
    
    leg.Draw("SAME");
    
    tex1 = TLatex(0.94,0.94,"0.142 pb^{-1} (13 TeV)");
    tex1.SetNDC();
    tex1.SetTextAlign(31);
    tex1.SetTextFont(42);
    tex1.SetTextSize(0.03);
    tex1.SetLineWidth(2);
    tex1.Draw("SAME");
    
    #tex2 = TLatex(0.1,0.96,"CMS");
    tex2 = TLatex(0.15,0.94,"CMS");#if there is 10^x
    tex2.SetNDC();
    tex2.SetTextFont(61);
    tex2.SetTextSize(0.0375);
    tex2.SetLineWidth(2);
    tex2.Draw("SAME");
    
    #tex3 = TLatex(0.18,0.96,"Preliminary 2017");
    tex3 = TLatex(0.23,0.94,"Preliminary 2017"); #if there is 10^x
    tex3.SetNDC();
    tex3.SetTextFont(52);
    tex3.SetTextSize(0.0285);
    tex3.SetLineWidth(2);
    tex3.Draw("SAME");
    
    #tex4 = TLatex(0.55,0.94,"L_{int} = 0.142 /pb");
    #tex4.SetNDC();
    #tex4.SetTextFont(52);
    #tex4.SetTextSize(0.0285);
    #tex4.SetLineWidth(2);
    #tex4.Draw("SAME");

    c1.SaveAs(pname + '.png')
    #c1.SaveAs(pname + '.C')
    c1.SaveAs(pname + '.pdf')

def extractPlot(cFile, rFile, run, folder, histo, xTitle="", yTitle="", xLow=0, xUp=0, yLow=0, yUp=0):
    basepath='DQMData/Run ' + str(run) + '/'
    histopath=basepath + folder
    print "Target histo=", histopath + histo
    chisto=cFile.Get(histopath + histo)
    rhisto=rFile.Get(histopath + histo)
    #pname='comparison' + histo
    pname='Run305336_both_Eff'
    drawandSaveHistos(pname, chisto, rhisto, xTitle, yTitle, xLow, xUp, yLow, yUp)

#run number
run=sys.argv[1]
#current file
iFilec=TFile.Open(sys.argv[2])
#reference file
iFiler=TFile.Open(sys.argv[3])
#folder name ### provide this inside ""
folder=sys.argv[4] # e.g. "Tracking/Run summary/TrackParameters/generalTracks/GeneralProperties/"
#histoname 
ht=sys.argv[5] # e,g,'TrackPhi_ImpactPoint_GenTk'
print ht
extractPlot(iFilec, iFiler, run, folder, ht, "", "N_{clust.}/N_{trk meas.}", 0., 7., 0.7, 1.09)
