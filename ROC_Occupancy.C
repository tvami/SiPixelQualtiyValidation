#include <map>
#include <sstream>
#include <iostream>
#include "TFile.h"
#include "TChain.h"
#include "TChainElement.h"
#include "TCanvas.h"
#include "TH2.h"
#include "TStyle.h"
#include "TROOT.h"

#define NOVAL_I -9999
#define NOVAL_F -9999.0
//#define COMPLETE 0
#define SPLIT 1

//Defining Dataset Structures

// Event info
class EventData {
 public:
  int fill;
  int run;
  int ls;
  int orb;
  int bx;
  int evt;
  int nvtx;
  int trig;
  int nclu[4]; // [0: fpix, i: layer i]
  int npix[4]; // [0: fpix, i: layer i]
  unsigned int beamint[2];
  float l1_rate;
  float intlumi;
  float instlumi;
  float instlumi_ext;
  float pileup;
  float vtxndof;
  float vtxchi2;
  float vtxD0;
  float vtxX;
  float vtxY;
  float vtxZ;
  int vtxntrk;
  int good;
  float tmuon;
  float tmuon_err;
  float tecal;
  float tecal_raw;
  float tecal_err;
  float field;
  int wbc;
  int delay;
  int ntracks;
  int ntrackFPix[2]; // tracks crossing the pixels
  int ntrackBPix[3]; // tracks crossing the pixels
  int ntrackFPixvalid[2]; // tracks crossing the pixels with valid hits
  int ntrackBPixvalid[3]; // tracks crossing the pixels with valid hits
  float trackSep;
  int federrs_size;
  // must be the last variable of the object saved to TTree:
  int federrs[16][2]; // [error index] [0:Nerror, 1:errorType]

  std::string list;

  EventData() { init(); };
  void init() {
    fill=NOVAL_I;
    run=NOVAL_I;
    ls=NOVAL_I;
    orb=NOVAL_I;
    bx=NOVAL_I;
    evt=NOVAL_I;
    nvtx=NOVAL_I;
    trig=NOVAL_I;
    for (size_t i=0; i<4; i++) nclu[i]=npix[i]=NOVAL_I;
    beamint[0]=beamint[1]=abs(NOVAL_I);
    l1_rate=NOVAL_F;
    intlumi=NOVAL_F;
    instlumi=NOVAL_F;
    instlumi_ext=NOVAL_F;
    pileup=NOVAL_F;
    vtxndof=vtxD0=vtxZ=NOVAL_F;
    vtxX=vtxY=vtxchi2=NOVAL_F;
    vtxntrk=NOVAL_I;
    good=NOVAL_I;
    tmuon=NOVAL_F;
    tmuon_err=NOVAL_F;
    tecal=NOVAL_F;
    tecal_raw=NOVAL_F;
    tecal_err=NOVAL_F;
    field=NOVAL_F;
    wbc=NOVAL_I;
    delay=NOVAL_I;
    ntracks=NOVAL_I;
    ntrackFPix[0]=ntrackFPix[1]=NOVAL_I;
    ntrackBPix[0]=ntrackBPix[1]=ntrackBPix[2]=NOVAL_I;
    ntrackFPixvalid[0]=ntrackFPixvalid[1]=NOVAL_I;
    ntrackBPixvalid[0]=ntrackBPixvalid[1]=ntrackBPixvalid[2]=NOVAL_I;
    trackSep=NOVAL_F;
    federrs_size=0;
    for (size_t i=0; i<16; i++) federrs[i][0]=federrs[i][1]=NOVAL_I;

    list="fill/I:run:ls:orb:bx:evt:nvtx:trig:nclu[4]:npix[4]:beamint[2]/i:"
      "l1_rate/F:intlumi:instlumi:instlumi_ext:pileup:vtxndof:vtxchi2:vtxD0:"
      "vtxX:vtxY:vtxZ:vtxntrk/I:good:tmuon/F:tmuon_err:tecal:tecal_raw:"
      "tecal_err:field:wbc/I:delay:ntracks:ntrackFPix[2]:ntrackBPix[3]:"
      "ntrackFPixvalid[2]:ntrackBPixvalid[3]:trackSep/F:federrs_size/I:"
      "federrs[federrs_size][2]";
  }
  
};


// Lumi info
class LumiData {
 public:
  int fill;
  int run;
  int ls;
  unsigned int time; // Unix time - seconds starting from 1970 Jan 01 00:00
  unsigned int beamint[2];
  float intlumi;
  float instlumi;
  float instlumi_ext;
  float pileup;
  int l1_size;
  int l1_prescale[1000]; // prescale for the L1 trigger with idx

  std::string list;

  LumiData() { init(); };
  void init() {
    fill=NOVAL_I;
    run=NOVAL_I;
    ls=NOVAL_I;
    time=abs(NOVAL_I);
    beamint[0]=beamint[1]=abs(NOVAL_I);
    intlumi=NOVAL_F;
    instlumi=NOVAL_F;
    l1_size=0;
    for (size_t i=0; i<1000; i++) l1_prescale[i]=NOVAL_I;
    
    list="fill/I:run:ls:time/i:beamint[2]:intlumi/F:instlumi:instlumi_ext:"
      "pileup:l1_size/I:l1_prescale[l1_size]";
  }

};


// Run info
class RunData {
public:
  int fill;
  int run;
  
  std::string list;
  
  RunData() { init(); };
  void init() {
    fill=NOVAL_I;
    run=NOVAL_I;
    
    list="fill/I:run";
  }
  
};

// Module info
class ModuleData {
 public:
  int det;
  int layer;
  int ladder;
  int half;
  int module;
  int disk;
  int blade;
  int panel;
  
  int federr;
  
  int side;
  int prt;
  int shl;
  int sec;
  
  int outer;
  
  unsigned int rawid;
  
  std::map<int, std::string> federrortypes;
  
  std::string list;
  
  ModuleData() { init(); }
  void init() {
    det=NOVAL_I;
    layer=NOVAL_I;
    ladder=NOVAL_I;
    half=NOVAL_I;
    module=NOVAL_I;
    disk=NOVAL_I;
    blade=NOVAL_I;
    panel=NOVAL_I;
    federr = NOVAL_I;
    side=NOVAL_I;
    prt=NOVAL_I;
    shl=NOVAL_I;
    sec=NOVAL_I;
    outer=NOVAL_I;
    rawid=abs(NOVAL_I);
    
    
    federrortypes.insert(std::pair<int, std::string>(25, "invalidROC"));
    federrortypes.insert(std::pair<int, std::string>(26, "gap word"));
    federrortypes.insert(std::pair<int, std::string>(27, "dummy word"));
    federrortypes.insert(std::pair<int, std::string>(28, "FIFO full error"));
    federrortypes.insert(std::pair<int, std::string>(29, "timeout error"));
    federrortypes.insert(std::pair<int, std::string>(30, "TBM error trailer"));
    federrortypes.insert(std::pair<int, std::string>(31, "event number error (TBM and FED event number mismatch)"));
    federrortypes.insert(std::pair<int, std::string>(32, "incorrectly formatted Slink Header"));
    federrortypes.insert(std::pair<int, std::string>(33, "incorrectly formatted Slink Trailer"));
    federrortypes.insert(std::pair<int, std::string>(34, "the event size encoded in the Slink Trailer is different than the size found at raw to digi conversion "));
    federrortypes.insert(std::pair<int, std::string>(35, "invalid FED channel number"));
    federrortypes.insert(std::pair<int, std::string>(36, "invalid ROC value "));
    federrortypes.insert(std::pair<int, std::string>(37, "invalid dcol or pixel value "));
    federrortypes.insert(std::pair<int, std::string>(38, "the pixels on a ROC weren't read out from lowest to highest row and dcol value"));
    federrortypes.insert(std::pair<int, std::string>(39, "CRC error"));
#ifdef COMPLETE
    list="det/I:layer:ladder:half:module:disk:blade:panel:federr:side:prt:shl:"
      "sec:outer:rawid/i";
#else
    list="det/I:layer:ladder:half:module:disk:blade:panel:federr";
#endif
  }
  
  std::string shell() {
    std::ostringstream ss;
    if (det==0) {
      ss << "B" << ((module>0) ? "p" : "m") << ((ladder>0) ? "I" : "O");
    } else if (det==1) {
      ss << "B" << ((disk>0) ? "p" : "m") << ((blade>0) ? "I" : "O");
    }
    return ss.str();
  }
  
  int shell_num() {
    if (det==0)      return ((module>0) ? 0 : 2) + ((ladder>0) ? 0 : 1);
    else if (det==1) return ((disk>0) ? 0 : 2) + ((blade>0) ? 0 : 1);
    return -1;
  }
  
  std::string federr_name() {
    std::map<int, std::string>::const_iterator it=federrortypes.find(federr);
    return (it!=federrortypes.end()) ? it->second : "FED error not interpreted";
  }
  
};


// Cluster info
class ClustData {
 public:
  // Paired branches (SPLIT mode)
  float x;
  float y;
  int sizeX;
  int sizeY;
  // From here Split mode (if SPLIT defined)
  int i; // serial num of cluster in the given module
  int edge;     // set if there is a valid hit
  int badpix;   // set if there is a valid hit
  int tworoc;   // set if there is a valid hit
  int size;
  float charge;
  // adc must be the last variable of the branch
  float adc[1000];
  float pix[1000][2];
  
  std::string list;
  
  ClustData() { init(); }
  void init() {
    x=NOVAL_F;
    y=NOVAL_F;
    sizeX=NOVAL_I;
    sizeY=NOVAL_I;
    i=NOVAL_I;
    edge=NOVAL_I;
    badpix=NOVAL_I;
    tworoc=NOVAL_I;
    size=0;
    charge=NOVAL_F;
    for (size_t it=0; it<1000; ++it) adc[it]=pix[it][0]=pix[it][1]=NOVAL_F;
    
    list="x:y:sizeX/I:sizeY:i:edge:badpix:tworoc:size:charge/F:adc[size]";
  }
  
};


class Cluster : public ClustData {
 public:

  ModuleData mod; // offline module number
  ModuleData mod_on; // online module number

  Cluster() { mod.init(); mod_on.init();}
  void init() {
    ClustData::init();
    mod.init();
    mod_on.init();
  }
  
};

class TreeReader {
 
 public:
  TreeReader() { }
  ~TreeReader() { }

 private:
  TFile f_;

  // Trees
  TTree *runTree_;
  TTree *lumiTree_;
  TTree *eventTree_;
  TTree *clustTree_;
  
  // Data structures
  RunData         run_;
  LumiData        lumi_;
  EventData       evt_;
  EventData       clu_evt_;
  Cluster         clu_;
  
  // Number of entries
  Long64_t nrun_;
  Long64_t nls_;
  Long64_t nevt_;
  Long64_t nclu_;

  void read_(TFile &f) {
    // runTree
    runTree_ = (TTree*)f.Get("runTree");
    nrun_ = (Long64_t)runTree_->GetEntries();
    TBranch *b_r_run    = runTree_->GetBranch("run");
    b_r_run    ->SetAddress(&run_);
    // lumiTree
    lumiTree_ = (TTree*)f.Get("lumiTree");
    nls_ = (Long64_t)lumiTree_->GetEntries();
    TBranch *b_l_lumi    = lumiTree_->GetBranch("lumi");
    b_l_lumi    ->SetAddress(&lumi_);
    // eventTree
    eventTree_ = (TTree*)f.Get("eventTree");
    nevt_ = (Long64_t)eventTree_->GetEntries();
    TBranch *b_e_evt    = eventTree_->GetBranch("event");
    b_e_evt     ->SetAddress(&evt_);
    /************************************ Split mode - GetBranch ********************************/
    // clustTree
    clustTree_ = (TTree*)f.Get("clustTree");
    nclu_  = (Long64_t)clustTree_->GetEntries();
    // Non-splitted branches
    TBranch *clust_event               = clustTree_->GetBranch("event");
    TBranch *clust_module_on           = clustTree_->GetBranch("module_on");
    
    // clust
    // Paired branches
    TBranch *clust_clust_xy            = clustTree_->GetBranch("clust_xy");
    // Split-mode branches
    TBranch *clust_clust_i             = clustTree_->GetBranch("clust_i");
    TBranch *clust_clust_edge          = clustTree_->GetBranch("clust_edge");
    TBranch *clust_clust_badpix        = clustTree_->GetBranch("clust_badpix");
    TBranch *clust_clust_tworoc        = clustTree_->GetBranch("clust_tworoc");
    TBranch *clust_clust_size          = clustTree_->GetBranch("clust_size");
    TBranch *clust_clust_sizeXY        = clustTree_->GetBranch("clust_sizeXY");
    TBranch *clust_clust_charge        = clustTree_->GetBranch("clust_charge");
    TBranch *clust_clust_adc           = clustTree_->GetBranch("clust_adc");
    TBranch *clust_clust_pix           = clustTree_->GetBranch("clust_pix");
    
    /************************************ SetAddress ******************************************/
    // Non-splitted branches
    clust_event               -> SetAddress(&clu_evt_);
    clust_module_on           -> SetAddress(&clu_.mod_on);
    
    // clust
    // Paired branches
    clust_clust_xy            -> SetAddress(&clu_.x);
    // Split-mode branches
    clust_clust_i             -> SetAddress(&clu_.i);
    clust_clust_edge          -> SetAddress(&clu_.edge);
    clust_clust_badpix        -> SetAddress(&clu_.badpix);
    clust_clust_tworoc        -> SetAddress(&clu_.tworoc);
    clust_clust_size          -> SetAddress(&clu_.size);
    clust_clust_sizeXY        -> SetAddress(&clu_.sizeX);
    clust_clust_charge        -> SetAddress(&clu_.charge);
    clust_clust_adc           -> SetAddress(&clu_.adc);
    clust_clust_pix           -> SetAddress(&clu_.pix);
  }
  
 public:

  //Accessors
  // Entries
  Long64_t nrun() { return nrun_; }
  Long64_t nls()  { return nls_; }
  Long64_t nevt() { return nevt_; }
  Long64_t nclu() { return nclu_; }
  // Read Entries
  void run_read(Long64_t i)  { runTree_->GetEntry(i); }
  void lumi_read(Long64_t i) { lumiTree_->GetEntry(i); }
  void evt_read(Long64_t i)  { eventTree_->GetEntry(i); }
  Int_t clu_read(Long64_t i) { return clustTree_->GetEntry(i); }
  // Memory adress of entry
  const RunData&         run()      { return run_; }
  const LumiData&        lumi()     { return lumi_; }
  const EventData&       evt()      { return evt_; }
  const EventData&       clu_evt()  { return clu_evt_; }
  const Cluster&         clu()      { return clu_; }

  void readtrees(TFile &f) { read_(f); }
  
};


void ROC_Occupancy() {
  gStyle->SetPalette(1);

  TH2D* l1 = new TH2D("l1","Layer 1;Modules along Z;Ladders",72, -4.5, 4.5,  42, -10.5,  10.5);
  TH2D* l2 = new TH2D("l2","Layer 2;Modules along Z;Ladders",72, -4.5, 4.5,  66, -16.5,  16.5);
  TH2D* l3 = new TH2D("l3","Layer 3;Modules along Z;Ladders",72, -4.5, 4.5,  90, -22.5,  22.5);
  TH2D* fpixI = new TH2D("fpixI","FPix Inner Shells (+x);;Blades", 72, -4.5, 4.5, 144,   0.5,  12.5);
  TH2D* fpixO = new TH2D("fpixO","FPix Outer Shells (-X);;Blades", 72, -4.5, 4.5, 144, -12.5,  -0.5);
  fpixI->GetXaxis()->SetBinLabel(1, "Disk-2 Pnl2");
  fpixI->GetXaxis()->SetBinLabel(9, "Disk-2 Pnl1");
  fpixI->GetXaxis()->SetBinLabel(19, "Disk-1 Pnl2");
  fpixI->GetXaxis()->SetBinLabel(27, "Disk-1 Pnl1");
  fpixI->GetXaxis()->SetBinLabel(41, "Disk+1 Pnl1");
  fpixI->GetXaxis()->SetBinLabel(49, "Disk+1 Pnl2");
  fpixI->GetXaxis()->SetBinLabel(59, "Disk+2 Pnl1");
  fpixI->GetXaxis()->SetBinLabel(67, "Disk+2 Pnl2");
  fpixI->GetXaxis()->LabelsOption("d");
  fpixO->GetXaxis()->SetBinLabel(1, "Disk-2 Pnl2");
  fpixO->GetXaxis()->SetBinLabel(9, "Disk-2 Pnl1");
  fpixO->GetXaxis()->SetBinLabel(19, "Disk-1 Pnl2");
  fpixO->GetXaxis()->SetBinLabel(27, "Disk-1 Pnl1");
  fpixO->GetXaxis()->SetBinLabel(41, "Disk+1 Pnl1");
  fpixO->GetXaxis()->SetBinLabel(49, "Disk+1 Pnl2");
  fpixO->GetXaxis()->SetBinLabel(59, "Disk+2 Pnl1");
  fpixO->GetXaxis()->SetBinLabel(67, "Disk+2 Pnl2");
  fpixO->GetXaxis()->LabelsOption("d");

  TreeReader tr;
  TChain *filechain = new TChain("filechain");
  filechain->Add("Ntuple.root");

  
  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(0);
  TCanvas c("c","c",1200,800);
  c.Divide(3,2);

  TObjArray* files=filechain->GetListOfFiles();
  for (int nf=0; nf<files->GetEntries(); ++nf) {
    TFile* file = TFile::Open(files->At(nf)->GetTitle());
    tr.readtrees(*file);
    
    for (Long64_t i=0; i<tr.nclu(); i++) {
      tr.clu_read(i);
      Cluster clu = tr.clu();
      EventData e = tr.clu_evt();
      
      int clu_sdpx = ((clu.mod_on.disk>0) ? 1 : -1) * (2 * (abs(clu.mod_on.disk) - 1) + clu.mod_on.panel);
      // Roc BinX number for ROC map plots (clust branch)
      int clu_roc_binx = NOVAL_I;
      if (clu.mod_on.det==0) {
	for (int j=1;j<=8;j++) if (clu.y>=((8-j)*52.0)&&clu.y<((9-j)*52.0))
          clu_roc_binx = (clu.mod_on.module+4)*8 + j;
      } else if (clu.mod_on.det==1) {
        // Roc is left (0) or right (1) on the ROC map plot (+Z side)
        int binselx = (clu.mod_on.panel==1&&(clu.mod_on.module==1||clu.mod_on.module==4)) ? (clu.mod_on.module==1)
          : ((clu.mod_on.panel==1&&clu.x<80.0)||(clu.mod_on.panel==2&&clu.x>=80.0));
        // Gives the Roc location inside a panel (0 to 5 on +Z side)
        int nperpan = 2 * clu.mod_on.module + clu.mod_on.panel - 1 + binselx;
        clu_roc_binx = ((clu.mod_on.disk>0) ? nperpan : 9 - nperpan) + (clu_sdpx + 4) * 8 
          - 2 * ((abs(clu.mod_on.disk)==1) ? clu.mod_on.disk : 0);
      }
      // Roc BinY number for ROC map plots (c branch)
      int clu_roc_biny = NOVAL_I; 
      if (clu.mod_on.det==0) {
        // Roc is in bottom (0) or top bin (1) inside a ladder on th ROC map plot
        int binsely = ((clu.mod_on.half==1&&((clu.mod_on.ladder<0&&clu.mod_on.ladder%2==0)||clu.mod_on.ladder%2==1))
        	       ||(clu.mod_on.half==0&&((clu.mod_on.ladder<0 &&((clu.mod_on.ladder%2==-1&&clu.x<80.0)
        								   ||(clu.mod_on.ladder%2==0&&clu.x>=80.0)))
        					 ||(clu.mod_on.ladder>0 &&((clu.mod_on.ladder%2==0&&clu.x<80.0)
        								     ||(clu.mod_on.ladder%2==1&&clu.x>=80.0))))));
        clu_roc_biny = (clu.mod_on.layer * 6 + clu.mod_on.ladder + 4) * 2 + 1 + binsely;
      } else if (clu.mod_on.det==1) {
        // Gives the number of ROCs along ly
        int nrocly = clu.mod_on.module + clu.mod_on.panel;
        for (int j=0; j<nrocly; j++) {
          // ROC number = nrocly - 1 - j for + LX and nrocly + j for -LX.
          int k = (clu.mod_on.disk<0) ? j : nrocly - 1 - j;
          if (clu.y>=(k*52.0)&&clu.y<((k+1)*52.0))
            clu_roc_biny = 6 - nrocly + 2 * j + ((clu.mod_on.blade>0) ? clu.mod_on.blade-1 : clu.mod_on.blade + 12)*12 + 1;
        }
      }
      
      if (clu.mod_on.layer==1) l1->SetBinContent(clu_roc_binx,clu_roc_biny, l1->GetBinContent(clu_roc_binx,clu_roc_biny)+1);
      else if (clu.mod_on.layer==2) l2->SetBinContent(clu_roc_binx,clu_roc_biny, l2->GetBinContent(clu_roc_binx,clu_roc_biny)+1);
      else if (clu.mod_on.layer==3) l3->SetBinContent(clu_roc_binx,clu_roc_biny, l3->GetBinContent(clu_roc_binx,clu_roc_biny)+1);
      else if (clu.mod_on.blade>0) {
	fpixI->SetBinContent(clu_roc_binx,clu_roc_biny, fpixI->GetBinContent(clu_roc_binx,clu_roc_biny)+1);
	fpixI->SetBinContent(clu_roc_binx,clu_roc_biny+1, fpixI->GetBinContent(clu_roc_binx,clu_roc_biny+1)+1);
      } else if (clu.mod_on.blade<0) {
	fpixO->SetBinContent(clu_roc_binx,clu_roc_biny, fpixO->GetBinContent(clu_roc_binx,clu_roc_biny)+1);
	fpixO->SetBinContent(clu_roc_binx,clu_roc_biny+1, fpixO->GetBinContent(clu_roc_binx,clu_roc_biny+1)+1);
      }
	
      if (i%500000==0) {
	c.cd(1);
	l1->Draw("COLZ");
	c.cd(2);
	l2->Draw("COLZ");
	c.cd(3);
	l3->Draw("COLZ");
	c.cd(4);
	fpixI->Draw("COLZ");
	c.cd(5);
	fpixO->Draw("COLZ");
	gPad->Update();
      }
    }
	c.SaveAs("output.root");
  } std::cout<<"Done."<<std::endl;
}
