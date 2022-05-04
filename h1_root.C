Int_t h1_root(){

  long int n = 100000000;

  TRandom3 *rnd = new TRandom3(131231);

  TH1D *h1 = new TH1D("h1","h1",100000,-10,10);
  
  for(long int i = 0;i<n;i++){
    h1->Fill(rnd->Gaus());
  }

  h1->Draw();
  
  return 0;
}
