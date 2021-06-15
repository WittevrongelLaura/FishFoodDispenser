# Projectgegevens

**VOORNAAM NAAM:** Laura Wittevrongel

**Sparringpartner:** Lotte Keyngnaert

**Projectsamenvatting in max 10 woorden:** Automatische visvoederbak voor vissen in een vijver

**Projecttitel:** FishFood Dispenser

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


## Gesprek 4 (Datum: 26/05/2021)

TOERMOMENT 1
Lectoren: Claudia, Geert, Frederik

Vragen voor dit gesprek:

- [x] vraag 1: / (geen vragen gesteld)


Dit is de feedback.

- feedback 1: alles al geschakeld, lichtsensor data in de console

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: /


## Gesprek 5 (Datum: 27/05/2021)

Lector: Dieter

Vragen voor dit gesprek:

- [x] vraag 1: Connection refused met socketio

Dit is de feedback op mijn vragen.

- feedback 1: surfen naar 192.168.168.168 ipv 127.0.0.1

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: surfen naar 192.168.168.168

## Gesprek 6 (Datum: 27/05/2021)

Lector: Frederik

Vragen voor dit gesprek:

- [x] vraag 1: Hoe mijn database verbeteren?
- [x] vraag 2: Waar kan ik de indexen best plaatsen?

Dit is de feedback op mijn vragen.

- feedback 1: Geen aparte tabellen per sensor of actuator, maar 1 tabel met alle componenten in.
- feedback 2: Index op component_naam en action omdat er daar het meest kan op gezocht worden.

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: 1 tabel voor alle componenten maken en een action tabel toevoegen. Die tabellen toevoegen aan de historiek tabel.
- [x] ToDo 2: Indexen plaatsen op de naam van het component en de actie beschrijving.

## Gesprek 7 (Datum: 28/05/2021)

Lector: Geert

Vragen voor dit gesprek:

- [x] vraag 1: Waardes uit de waterlevel zien er wat raar uit, hoe kan ik ze interpreteren?
- [x] vraag 2: Hoe soldeer ik de versterker? De pinnen in de kit zijn te groot om erin te passen.

Dit is de feedback op mijn vragen.

- feedback 1: Wat Arduino code op internet gevonden en daarop kan je de code baseren?
- feedback 2: Pinnen van male draden gebruiken om ze te solderen

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: Arduino code bekijken en proberen programmeren.
- [x] ToDo 2: Male pinnen solderen aan de versterker.

## Gesprek 8 (Datum: 3/06/2021)

TOERMOMENT 2
Lectoren: Pieter-Jan, Simon

Vragen voor dit gesprek:

- [x] vraag 1: / (geen vragen gesteld)

Dit is de feedback op mijn MVP.

- feedback 1: Het belangrijkste van de website moet op de homepage staan, niet nog eens op een 2e pagina


Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: De belangrijkste data op de homepagina plaatsen



## Gesprek 9 (Datum: 4/06/2021)

Lector: Dieter

Vragen voor dit gesprek:

- [x] vraag 1: website laadt niet op gsm.
- [x] vraag 2: Chrome neemt verkeerde script over dan dat er gelinkt werd in de html. Waardoor ik de hele tijd de naam verander in de html script-tag.

Dit is de feedback op mijn vragen.

- feedback 1: // (opgelost voordat consult begon, 5min laten openstaan en website laadde plots)
- feedback 2: Blijven duwen op de herlaad-knop in Chrome dan "Cache wissen en herladen"

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: Werkt nu iedere keer ik ernaartoe surf
- [x] ToDo 2: Naam van de scripts niet meer veranderen en op de knop cache wissen en herladen klikken.

## Gesprek 10 (Datum: 4/06/2021)

Lector: Pieter-Jan

Vragen voor dit gesprek:

- [x] vraag 1: fotodiode geeft weinig verschil in waarde bij het lezen van een licht en het lezen van een diode met minder licht (zoals hand erboven)

Dit is de feedback op mijn vragen.

- feedback 1: schakeling iets anders opbouwen, zoals de fotodiode wisselen met de weerstand of de fotodiode wisselen met een LDR

Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: Nog wat verder testen met de fotodiode die nu anders geschakeld is, als het niet lukt een LDR gaan kopen.


## Gesprek 11 (Datum: 7/06/2021)

Lector: Claudia

Vragen voor dit gesprek:

- [x] vraag 1: Aside "display: none" werkt niet.
- [x] vraag 2: Footer op het einde van de pagina krijgen, niet fixed.


Dit is de feedback op mijn vragen.

- feedback 1: display op none zetten voor iedere viewport en in js aanpassen
- feedback 2: body: display flexbox, column maken en dan proberen die footer beneden te krijgen


Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: display op none zetten en de aside zichtbaar maken met js
- [x] ToDo 2: kolommen maken van de body en die footer proberen op het einde te zetten


## Gesprek 12 (Datum: 8/06/2021)

Lector: Pieter-Jan

Vragen voor dit gesprek:

- [x] vraag 1: Bij het runnen van de temperatuur sensor krijg ik een exception "no such file or directory" terwijl alles aangesloten is en dat file wel degelijk te vinden is in de bestanden op de rpi.
- [x] vraag 2: Commando uitvoeren van de speaker met check_output werkt niet.


Dit is de feedback op mijn vragen.

- feedback 1: bij het opzoeken van de file en daarna het programma runnen lukt dit wel dus, eerst het commando runnen met check_output
Daarna shell=True instellen in de check_output functie.
- feedback 2: ook shell=True toevoegen


Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: commando eerst uitvoeren en shell=True instellen
- [x] ToDo 2: shell=True toevoegen



## Gesprek 13 (Datum: 9/06/2021)

Lector: Dieter

Vragen voor dit gesprek:

- [x] vraag 1: Socketio foutmelding bij 2e keer laden pagina (TypeError: expected str, bytes or os.PathLike object, not _io.TextIOWrapper)
- [x] vraag 2: Op welke manier 3 rows uit de db halen met dezelfde datum


Dit is de feedback op mijn vragen.

- feedback 1: bestand wordt niet geopend bij het 2e keer laden van de pagina (init staat boven en wordt maar 1 keer uitgevoerd)
- feedback 2: sorteren op datetime descending


Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: pad van het bestand meegeven in de functie die wordt opgeroepen in de main (app.py)
- [x] ToDo 2: query maken met datetime in de eerste kolom, value en dan 1 van de eerste 3 component_id's (id 1,2,3 zijn sensoren)


## Gesprek 8 (Datum: 10/06/2021)

TOERMOMENT 3
Lectoren: Claudia, Geert

Vragen voor dit gesprek:

- [x] vraag 1: / (geen vragen gesteld)

Dit is de feedback op mijn MVP.

- feedback 1: home-page -> data duidelijker maken met een titel te geven aan iedere waarde
- feedback 2: settings -> enkel speaker aan-/afleggen
- feedback 3: algemene design van de website moet beter, meer witruimte
- feedback 4: data live weergeven


Hier komt de feedforward: wat ga ik concreet doen?

- [x] ToDo 1: 

