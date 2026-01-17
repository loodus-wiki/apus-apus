---
title: Teisese ülevaatus
layout: default
lang: est
is_home: false
---

### Nähtavad vigastused
Kas linnul on näha verd, ilmset vigastust või silmatorkavat asümmeetriat?
Kui vigastus on ilmne, antakse valuvaigistit (Melox) enne edasist läbivaatust.

<p>Melox (Meloksikaami) annuse kalkulaator</p>

Valem:  
(0,2) × (linnu kaal formaadis 0,030 kg 30-grammise linnu puhul) : (% meloksikaami, tavaliselt 0,5 või 1,5)

<h4>Linnu kaal (kg):</h4>
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
  <button onclick="setWeightFromButton(0.030)">30 g</button>
  <button onclick="setWeightFromButton(0.050)">50 g</button>
  <input type="number" id="weightInput" step="0.001" placeholder="Sisestage kaal käsitsi" style="width: 100px;">
</div>

<h4>Meloks %:</h4>
<div style="display: flex; align-items: center; gap: 10px;">
  <button onclick="setPercent(0.5)">0,5%</button>
  <button onclick="setPercent(1.5)">1,5%</button>
  <span>Valitud protsent: <strong id="selectedPercent">—</strong></span>
</div>

<br>
<div style="display: flex; align-items: center; gap: 15px;">
  <button onclick="calculateDose()">Arvuta annus</button>
  <p id="result" style="margin: 0; font-weight: bold;"></p>
</div>

<script>
  let percent = null;

  function setWeightFromButton(val) {
    // Kirjutab kaalu sisestusväljale
    document.getElementById("weightInput").value = 1000 * val.toFixed(3);
  }

  function setPercent(val) {
    percent = val;
    document.getElementById("selectedPercent").innerText = val + " %";
  }

  function calculateDose() {
    // Loeb kaalu sisestusväljalt
    let weight = parseFloat(document.getElementById("weightInput").value);
    if (isNaN(weight) || weight <= 0) {
      document.getElementById("result").innerText = "Sisestage linnu korrektne kaal.";
      return;
    }
    if (percent === null || percent === 0) {
      document.getElementById("result").innerText = "Palun valige lahuse protsent (mitte 0).";
      return;
    }

    let dose = (0.2 * weight) / percent / 1000;
    document.getElementById("result").innerText =
      "Annus: " + dose.toFixed(4) + " ml Meloks lahust.";
  }
</script>
<br>

30-grammise kaalu ja 0,5% lahuse puhul peaks saama umbes ühe väikese jaotise insuliinisüstlal (100 ühikut, maht 1 ml).

### Kolju-ajutrauma (KAT)
Kui linnul, olgu see poeg või täiskasvanud lind, on vähemalt üks kolju-ajutrauma tunnus, tuleb ravi kohe alustada.

Olulised KAT (Kolju-AjuTrauma) tunnused on:
- Liikumiste koordinatsiooni häired.
- Lind vajub ühele küljele, tõmbab selle külje jalga kokku, hoiab seda nõrgalt või üldse mitte, pigistab selle rusikasse, laseb tiiva longu, justkui ei suudaks seda keha ligi hoida, kuigi jalal ega tiival nähtavaid vigastusi pole.
- Vere olemasolu ninasõõrmetes, kõrvades või kurgus.
- Pupillide erinev kiirus valgusele reageerimisel (taskulambiga kontrollides).
- Erineva suurusega ja fookuseta pupillid.
- Ebaloomulik silmade kissitamine vms.
- Silmade turse, paistetanud silmad.
- Lind viskab pead ebaloomulikult tahapoole või keerab seda.
- "Jälgib ronge" suure või väikese amplituudiga – liigutab pead küljelt küljele, justkui loeks mööduva rongi vaguneid.

<div class="video-gallery">
  <figure>
    <video width="300" height="405" controls>
      <source src="{{ 'assets/video/swift-severe-tbi.mp4' | relative_url }}" type="video/mp4">
      Teie brauser ei toeta videot.
    </video>
    <figcaption>
      Piiritaja käitumine kolju-ajutrauma korral
    </figcaption>
  </figure>
</div>

Esmased tegevused:
- Rahu ja pimedus (kingakarp ventilatsiooniavadega).
- Ümbritseda lind toetavate rullidega, millele ta saaks pea toetada. Pea peaks olema 35–45 kraadi nurga all, et vältida vedeliku peavoolu ajju.
- Mitte anda vett (et vältida ajuturse ohtu).
- *Piisava kaalu korral* mitte toita (see võib tekitada iiveldust + täiskasvanud piiritajale on see suur stress).
- Teha valuvaigistus.
- Hapnikuballoon leevendab linnu seisundit.
- Pead ei tohi soojendada! Parim temperatuur (kui lind pole kurnatud) on 20–22 °C.

Pöörake tähelepanu väljaheitele. Kui väljaheites on midagi pruunikat, võib see olla hüübinud veri. Tilgutage vesinikperoksiidi – kui see kihiseb, on tegemist verega ja esineb sisemine verejooks.

Arvestage, et peapõrutuse korral esineb sageli "valgusaken" – see on ajutine periood, mil linnu seisund paraneb, millele järgneb järsk halvenemine. Tavaliselt toimub see esimeste tundide või paari päeva jooksul, seega veenduge, et lind on traumast tõesti taastunud.

### Seljalt ümberpööramise test
**Kui nähtavaid vigastusi pole**, võib piiritajat testida seljalt ümberpööramisega.  
Selleks peske käed põhjalikult või pange kindad, et vältida sule rasvaga määrimist.  
Seejärel keerake piiritaja ettevaatlikult selili ja eemaldage käed, püüdes mitte kinni jääda tema küünte taha.

Normaalselt peaks ta kiiresti tagasi ümber pöörama.

Libisemine või võimetus algasendisse naasta on tõsise trauma sümptom. See võib viidata muljumisele, õlavöötme vigastusele või mõnikord ka kolju-ajutraumale.

Proovige salvestada video, see annab kogenud spetsialistidele rohkem teavet vigastuse olemuse kohta.