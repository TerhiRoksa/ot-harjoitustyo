```mermaid
sequenceDiagram
  participant Main
  participant laitehallinto
  participant rautatietori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  participant kallen_kortti
  
  Main ->> +laitehallinto: new HKLLaitehallinto()
  laitehallinto --> -Main: laitehallinto
  Main ->> +rautatietori: new Lataajalaite()
  rautatietori ->> -Main: rautatietori
  Main ->> +ratikka6: new Lukijalaite()
  ratikka6 ->> -Main: ratikka6
  Main ->> +bussi244: new Lukijalaite()
  bussi244 ->> -Main: bussi 244
  Main ->> +laitehallinto: lisaa_lataaja(rautatietori)
  Main ->> +laitehallinto: lisaa_lukija(ratikka6)
  Main ->> +laitehallinto: lisaa_lukija(bussi244)
  Main ->> lippu_luukku: new Kioski()
  lippu_luukku ->> -Main: lippu_luukku
  Main ->> +lippu_luukku: new Matkakortti("Kalle")
  kallen_kortti ->> -Main: kallen_kortti
  Main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
  Main ->> ratikka6: osta_lippu(kallen_kortti, 0)
  Main -->> bussi244: osta_lippu(kallen_kortti, 2)     
  laitehallinto --> -Main: 

   

  

```
