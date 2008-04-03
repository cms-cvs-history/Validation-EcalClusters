import re, sys, os

file = open("output", "r")

lines = file.readlines()
file.close()

variable = []
eta1 = []
eta2 = []
mean = []
error= []
effS = []

for line in lines:
    elements = re.split("\t", line)
    variable += [elements[1],]
    
    eta1 += [re.split(">", re.split("&&", elements[2])[0])[1],]
    eta2 += [re.split("<", elements[2])[1],]

    mean += [elements[3],]
    error+= [elements[4],]
    effS += [elements[5][:-1],]

header = """void plot_performance(){
//   TH1F* h_emCorrBR1_et      = new TH1F("h_emCorrBR1_et",    "",300,0,300);
//   TH1F* h_emCorrBR1Full_et  = new TH1F("h_emCorrBR1Full_et","",300,0,300);
   TH1F* h_emCorr_et  = new TH1F("h_emCorr_et","",300,0,300);
   TH1F* h_em_et      = new TH1F("h_em_et","",300,0,300);
"""
file = open("plot_performance.C", "w")
file.write(header)

#for i in ("emCorrBR1Full_et", "emCorrBR1_et", "em_et"):
for i in ("emCorr_et", "em_et"):
    for j in range(0, len(eta1)):
        if variable[j] <> i:
            continue
        bin = str(int((float(eta1[j]) + float(eta2[j]))/2))
        file.write("  h_" + i + "->SetBinContent(" + bin + ", " + mean[j] + ");\n")
        file.write("  h_" + i + "->SetBinError  (" + bin + ", " + error[j] +");\n")

#file.write("  h_emCorrBR1_et    ->SetMarkerStyle(22);\n")
#file.write("  h_emCorrBR1Full_et->SetMarkerStyle(23);\n")
file.write("  h_emCorr_et->SetMarkerStyle(23);\n")
file.write("  h_em_et    ->SetMarkerStyle(20);\n")


#file.write("  h_emCorrBR1_et    ->SetMarkerColor(2);\n")
#file.write("  h_emCorrBR1Full_et->SetMarkerColor(3);\n")
file.write("  h_emCorr_et->SetMarkerColor(4);\n")
file.write("  h_em_et    ->SetMarkerColor(1);\n")

file.write("  gStyle->SetOptStat(0);\n")

file.write("  h_em_et    ->Draw();\n")
file.write("  h_emCorr_et->Draw(\"SAME\");\n")
#file.write("  h_emCorrBR1_et    ->Draw(\"SAME\");\n")
#file.write("  h_emCorrBR1Full_et->Draw(\"SAME\");\n")
file.write("  TLine* line = new TLine(0,1,300,1);\n")
file.write("  line->Draw();\n")

header ="""  

  TAxis* ax = h_em_et->GetXaxis();
  ax->SetTitle("Et (GeV)");
  TAxis* ay = h_em_et->GetYaxis();
  ay->SetTitle("E_{T}^{RECO}/E_{T}^{MC}");

  TLegend *leg = new TLegend(0.2, 0.2, 0.4, 0.4);
  leg->AddEntry(h_em_et, "Before correction");
  leg->AddEntry(h_emCorr_et, "After correction  ");
//  leg->AddEntry(h_emCorrBR1_et, "F(#sigma_{#phi}/#sigma_{#eta}) correction  ");
//  leg->AddEntry(h_emCorrBR1Full_et, "Full correction  ");
  leg->Draw();
  TLine* line = new TLine(0,1,1.5,1);
  line->SetLineWidth(2);
  line->SetLineColor(2);
  line->Draw();

  TFile* MeanVSEta = TFile::Open("MeanVSEta.root", "RECREATE");
  h_em_et->Write();
  h_emCorr_et->Write();
  leg->Write();
"""
file.write(header)

file.write("}\n")
