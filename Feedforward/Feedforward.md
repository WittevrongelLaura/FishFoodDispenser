# Projectgegevens

**VOORNAAM NAAM:** Laura Wittevrongel

**Sparringpartner:** schrijf hier de naam van jouw sparring partner. Deze persoon is jouw klankbord, redder in nood, motivator, partner in crime :-)

**Projectsamenvatting in max 10 woorden:** schrijf hier jouw samenvatting

**Projecttitel:** plaats hier een catchy werktitel van jouw project

# Tips voor feedbackgesprekken

## Voorbereiding

> Bepaal voor jezelf waar je graag feedback op wil. Schrijf op voorhand een aantal punten op waar je zeker feedback over wil krijgen. Op die manier zal het feedbackgesprek gerichter verlopen en zullen vragen, die je zeker beantwoord wil hebben, aan bod komen.

## Tijdens het gesprek:

> **Luister actief:** Schiet niet onmiddellijk in de verdediging maar probeer goed te luisteren. Laat verbaal en non-verbaal ook zien dat je aandacht hebt voor de feedback door een open houding (oogcontact, rechte houding), door het maken van aantekeningen, knikken...

> **Maak notities:** Schrijf de feedback op zo heb je ze nog nadien. Noteer de kernwoorden en zoek naar een snelle noteer methode voor jezelf. Als je goed noteert,kan je op het einde van het gesprek je belangrijkste feedback punten kort overlopen.

> **Vat samen:** Wacht niet op een samenvatting door de docenten, dit is jouw taak: Check of je de boodschap goed hebt begrepen door actief te luisteren en samen te vatten in je eigen woorden.

> **Sta open voor de feedback:** Wacht niet op een samenvatting door de docenten, dit is jouw taak: Check of je de boodschap goed hebt begrepen door actief te luisteren en samen te vatten in je eigen woorden.`

> **Denk erover na:** Denk na over wat je met de feedback gaat doen en koppel terug. Vind je de opmerkingen terecht of onterecht? Herken je je in de feedback? Op welke manier ga je dit aanpakken?

## NA HET GESPREK

> Herlees je notities en maak actiepunten. Maak keuzes uit alle feedback die je kreeg: Waar kan je mee aan de slag en wat laat je even rusten. Wat waren de prioriteiten? Neem de opdrachtfiche er nog eens bij om je focuspunten te bepalen.Noteer je actiepunten op de feedbackfiche.

# Feedforward gesprekken

## Gesprek 1 (Datum: 09/03/2021)

Lector: Geert en Claudia

Vragen voor dit gesprek:

- [x] vraag 1: Wat kan er gebruikt worden als de force sensor niet nauwkeurig genoeg is om het potje te wegen?
- [x] vraag 2: Wat kan ik gebruiken als waterbestendige behulzing?

Dit is de feedback op mijn vragen.

- feedback 1: Water Level Sensor kan eventueel gebruikt worden om het waterniveau te meten. Maakt gebruik van i2C bus om dit component aan te sturen, wordt nog gezien in de les Sensors & Interfacing.
- feedback 2: https://www.conrad.be/p/hammond-electronics-rp1135c-rp1135c-universele-behuizing-125-x-85-x-55-abs-lichtgrijs-1-stuks-539099 dit kan gebruikt worden maar waarschijnlijk niet groot genoeg. Nog even verder googlen

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: oplossing zoeken voor de force sensor. Eventueel vervangen door andere sensor en het probleem met het vullen van het potje oplossen door gebruik van een timer.
- [x] ToDo 2: blokschema aanpassen, hij was niet specifiek genoeg. Iedere led, servo, fotodiode wordt apart getoont met specifieke uitleg wat het component precies doet.

## Gesprek 2 (Datum: 21/05/2021)

Lector: Pieter-Jan

Vragen voor dit gesprek:

- [x] vraag 1: Fritzing --> geen gevonden fritzing component voor de amplifier
- [x] vraag 2: Hoe werkt de amplifier en hoe kan ik die schakelen aan de pi en aan de speaker
- [x] vraag 3: Geen fritzing component gevonden voor Groove Water Level Sensor
- [x] vraag 4: LCD --> R/W pin op een GPIO pin aansluiten om te kunnen lezen wat er op het scherm staat?

Dit is de feedback op mijn vragen.

- feedback 1: Fritzing component gevonden, maar niet helemaal dezelfde pinout (maar lukt om het schema te maken)
- feedback 2: Amplifier werkt met links en rechts input. Aangezien ik maar 1 speaker heb kan ik maar op 1 kant aansluiten.
- feedback 3: Andere water level sensor part nemen met ongeveer dezelfde pinnen.
- feedback 4: LCD softwarematig uitlezen

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: Dit component ga ik importeren en verbinden met de pi en speaker
- [x] ToDo 2: De "L input", "R input" en "G input" verbinden met de pi via een audio jack 3.5mm tussenstuk.
      De "R out -" en "R out +" verbinden met de speaker. De "GND" en "5V" verbinden met externe power supply.
      Wordt nog verder overlegd met Geert.
- [ ] ToDo 3: Wordt nog overlegd met Geert.
- [x] ToDo 4: R/W pin kan je via levelshifter aan een GPIO pin aansluiten, maar softwarematig is het gemakkelijker
      om het uit te lezen. Dus R/W pin op GND connecteren.

## Gesprek 3 (Datum: 25/05/2021)

Lector: Dieter

Vragen voor dit gesprek:

- [x] vraag 1: 404 error bij het starten van de liveserver
- [x] vraag 2: compiler gaat niet in de routes

Dit is de feedback op mijn vragen.

- feedback 1: (was plots bij het opstarten opgelost)
- feedback 2: verkeerde waarde weergegeven bij return waarde van die route

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: /
- [x] ToDo 2: print statements vervangen door return waarde
