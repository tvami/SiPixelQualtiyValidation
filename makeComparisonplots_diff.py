#!/usr/bin/env python
from ROOT import *
import sys
import tdrstyle

# https://tinyurl.com/y63du2m4
'''
#  Usage:
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/" clusterposition_zphi_ontrack -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXBarrel/" clusterposition_zphi_ontrack_PXLayer_1 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXBarrel/" clusterposition_zphi_ontrack_PXLayer_2 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXBarrel/" clusterposition_zphi_ontrack_PXLayer_3 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXBarrel/" clusterposition_zphi_ontrack_PXLayer_4 -b
 
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXForward/" clusterposition_xy_ontrack_PXDisk_+1 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXForward/" clusterposition_xy_ontrack_PXDisk_+2 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXForward/" clusterposition_xy_ontrack_PXDisk_+3 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXForward/" clusterposition_xy_ontrack_PXDisk_-1 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXForward/" clusterposition_xy_ontrack_PXDisk_-2 -b
 python makeComparisonplots_diff.py 305336 ZBbased_PromptRECO_Run305336_DQM.root ZBbased_RECO_Run305336_DQM.root "PixelPhase1/Run summary/Tracks/PXForward/" clusterposition_xy_ontrack_PXDisk_-3 -b


'''


def drawandSaveHistos(pname, chisto, rhisto, xTitle="", yTitle="", xLow=0, xUp=0, yLow=0, yUp=0):
    tdrstyle.setTDRStyle()
    gStyle.SetPalette(1);
    c1 = TCanvas(pname, "", 50,50,1200,1200)
    #c1.cd()

    chisto.SetTitle("")
    rhisto.SetTitle("")
    

    if xLow != xUp :
        chisto.GetXaxis().SetRangeUser(xLow, xUp)
        rhisto.GetXaxis().SetRangeUser(xLow, xUp)
    #if yLow != yUp:
        #chisto.GetYaxis().SetRangeUser(yLow, yUp)
        #rhisto.GetYaxis().SetRangeUser(yLow, yUp)

    if xTitle != "":
        chisto.GetXaxis().SetTitle(xTitle)
        chisto.GetXaxis().SetTitleOffset(0.8);
        chisto.GetXaxis().SetTitleSize(0.05);
        rhisto.GetXaxis().SetTitle(xTitle)
        rhisto.GetXaxis().SetTitleOffset(0.8);
        rhisto.GetXaxis().SetTitleSize(0.05);
        
    if yTitle != "":
        chisto.GetYaxis().SetTitle(yTitle)
        chisto.GetYaxis().SetTitleOffset(0.8);
        chisto.GetYaxis().SetTitleSize(0.05);
        rhisto.GetYaxis().SetTitle(yTitle)
        rhisto.GetYaxis().SetTitleOffset(0.8);
        rhisto.GetYaxis().SetTitleSize(0.05);
        
    if pname == "comparisonclusterposition_zphi_ontrack_PXLayer_1":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 1")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 1")
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);
    elif pname == "comparisonclusterposition_zphi_ontrack_PXLayer_2":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 2")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 2")
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);
    elif pname == "comparisonclusterposition_zphi_ontrack_PXLayer_3":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 3")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 3")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);
    elif pname == "comparisonclusterposition_zphi_ontrack_PXLayer_4":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 4")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Layer 4")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_+1":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +1")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +1")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_+1":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +1")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +1")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);    
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_+2":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +2")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +2")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);    
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_+3":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +3")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk +3")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_-1":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk -1")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk -1")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);    
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_-2":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk -2")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk -2")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);    
    elif pname == "comparisonclusterposition_xy_ontrack_PXDisk_-3":
        chisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk -3")
        rhisto.GetZaxis().SetTitle("Relative variation of on-track clusters in % on Disk -3")        
        chisto.GetZaxis().SetTitleOffset(1.3);
        chisto.GetZaxis().SetTitleSize(0.035);        
        rhisto.GetZaxis().SetTitleOffset(1.3);
        rhisto.GetZaxis().SetTitleSize(0.035);



    c1.SetLeftMargin(0.1);
    c1.SetRightMargin(0.18);
    c1.SetTopMargin(0.05);
    c1.SetBottomMargin(0.1);
    
    x1_l = 0.92
    y1_l = 0.91

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
    
    diffhisto = rhisto.Clone()
    diffhisto.Add(chisto,-1)
    
    diffhisto.Divide(diffhisto,rhisto,100,1)
    #diffhisto.GetZaxis().SetRangeUser(0, 15.5)
    diffhisto.GetZaxis().SetRangeUser(0, 10) #forBPixel
    diffhisto.Draw("COLZ0")
    c1.Modified()
    c1.Update()
    
    #leg.Draw("SAME");

    #if pname == "comparisonclusterposition_zphi_ontrack_PXLayer_1":
        #tex0 = TLatex(0.80,0.90,"Layer 1");
    #elif pname == "comparisonclusterposition_zphi_ontrack_PXLayer_2":
        #tex0 = TLatex(0.84,0.96,"Layer 2");
    #elif pname == "comparisonclusterposition_zphi_ontrack_PXLayer_3":
        #tex0 = TLatex(0.84,0.96,"Layer 3");
    #elif pname == "comparisonclusterposition_zphi_ontrack_PXLayer_4":
        #tex0 = TLatex(0.84,0.96,"Layer 4");
    #tex0.SetNDC();
    #tex0.SetTextAlign(31);
    #tex0.SetTextFont(42);
    #tex0.SetTextSize(0.03);
    #tex0.SetLineWidth(2);
    #tex0.Draw("SAME");
    
    
    
    tex1 = TLatex(0.84,0.96,"0.142 pb^{-1} (13 TeV)");
    tex1.SetNDC();
    tex1.SetTextAlign(31);
    tex1.SetTextFont(42);
    tex1.SetTextSize(0.03);
    tex1.SetLineWidth(2);
    tex1.Draw("SAME");
    
    #tex2 = TLatex(0.1,0.96,"CMS");
    tex2 = TLatex(0.1,0.96,"CMS");#if there is 10^x
    tex2.SetNDC();
    tex2.SetTextFont(61);
    tex2.SetTextSize(0.0375);
    tex2.SetLineWidth(2);
    tex2.Draw("SAME");
    
    #tex3 = TLatex(0.18,0.96,"Preliminary 2017");
    tex3 = TLatex(0.18,0.96,"Preliminary 2017"); #if there is 10^x
    tex3.SetNDC();
    tex3.SetTextFont(52);
    tex3.SetTextSize(0.0285);
    tex3.SetLineWidth(2);
    tex3.Draw("SAME");
    
    #tex4 = TLatex(0.45,0.96,"L_{int} = 0.142 /pb");
    #tex4.SetNDC();
    #tex4.SetTextFont(52);
    #tex4.SetTextSize(0.0285);
    #tex4.SetLineWidth(2);
    #tex4.Draw("SAME");

    c1.SaveAs(pname + '.png')
    c1.SaveAs(pname + '.pdf')

def extractPlot(cFile, rFile, run, folder, histo, xTitle="", yTitle="", xLow=0, xUp=0, yLow=0, yUp=0):
    basepath='DQMData/Run ' + str(run) + '/'
    histopath=basepath + folder
    print "Target histo=", histopath + histo
    chisto=cFile.Get(histopath + histo)
    rhisto=rFile.Get(histopath + histo)
    pname='comparison' + histo
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
#extractPlot(iFilec, iFiler, run, folder, ht, "Global Z [cm]", "Global #phi [rad]", -30., 30., 0, 0)
extractPlot(iFilec, iFiler, run, folder, ht, "Global X [cm]", "Global Y [cm]", 0., 0., 0, 0)
