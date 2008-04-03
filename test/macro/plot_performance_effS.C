void plot_performance_effS(){
//   TH1F* h_emCorrBR1_et       = new TH1F("h_emCorrBR1_et","",300,0,300);
//   TH1F* h_emCorrBR1Full_et   = new TH1F("h_emCorrBR1Full_et","",300,0,300);
   TH1F* h_emCorr_et   = new TH1F("h_emCorrBR1Full_et","",300,0,300);
   TH1F* h_em_et       = new TH1F("h_em_et","",300,0,300);
   TH1F* add                 = new TH1F("add","",300,0,300);
   TH1F* ratio               = new TH1F("ratio","",300,0,300);
  h_emCorr_et->SetMarkerStyle(23);
  h_em_et    ->SetMarkerStyle(20);
  h_emCorr_et->SetMarkerColor(4);
  h_em_et    ->SetMarkerColor(1);
  gStyle->SetOptStat(0);
  h_em_et       ->Draw();
  h_emCorr_et->Draw("SAME");
  

  TAxis* ax = h_em_et->GetXaxis();
  ax->SetTitle("E (GeV)");
  TAxis* ay = h_em_et->GetYaxis();
  ay->SetTitle("#sigma_{EFF}");

  TLegend *leg = new TLegend(0.2, 0.2, 0.4, 0.4);
  leg->AddEntry(h_em_et, "Before correction");
  leg->AddEntry(h_emCorr_et, "After correction  ");
//  leg->AddEntry(h_emCorrBR1_et, "F(#sigma_{#phi}/#sigma_{#eta}) correction  ");
//  leg->AddEntry(h_emCorrBR1Full_et, "Full correction  ");
  leg->Draw();
//  add->Add(h_emCorrBR1Full_et, h_em_et, -1, 1);
  add->Add(h_emCorr_et, h_em_et, -1, 1);
  ratio->Divide(add, h_em_et);

  ratio->SetMarkerStyle(21);
  ratio->SetMarkerColor(4);
  ratio->GetYaxis()->SetTitle("Improvement in #sigma_{eff}");
  ratio->GetXaxis()->SetTitle("Et (GeV)");

  TFile* effSigmaVSEta = TFile::Open("effSigmaVSEta.root", "RECREATE");
  h_em_et->Write();
  h_emCorr_et->Write();
  ratio->Write();
  leg->Write();
}
