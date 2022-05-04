Int_t gr_root(){

  long int n = 10000000;

  TRandom3 *rnd = new TRandom3(131231);

  TGraph *gr = new TGraph();
  
  for(long int i = 0;i<n;i++){
    gr->SetPoint(gr->GetN(),i,rnd->Gaus());
  }

  gr->Draw("APL");
  
  return 0;
}
