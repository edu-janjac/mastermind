# mastermind

vad som behövs:
random 4 tal (1-6)
input för gissning
checkmark för rätt siffra rätt ställa (vet inte plats)
box för rätt siffra fel ställe
2 svårighetsgrader:
1 - inte upprepande siffror
2 - kan vara upprepande siffror

([] = box, {} = checkmark)
ska ha output:
Drag # Drag Feedback

---

1 gissning
2 6 4 5 3 [][]{}
3
4
5
6
7
8
9
10
11
12

Ange gissning som föjld av 4 siffror -> (input ny gissning)

Om vinst:
Du vann!

Om förlust:
Attans du hade råkade ha fel, aja bättre lycka nästa gång!
Korrekt rad var: 6767

när spelet är slut:
Vill du spela igen (j/n) -> j (spelar igen)
-> n (avslutar programet)

funktioner:
main
random tal - random
gissning av tal - input från användare
checkning av gissning och tal - if bla bla bla
print gissningarna och resultat - print(f"") med updatering (loop)
spela igen - loop programet

//Logg 2025-11-13
vi har gjort arbete och ska fortsätta med error vid svårighetsgrad nästa gång

easy:
om nytt nummer = nummer innan, gör nytt nummer, repetera tills 4 siffror

//Logg 2025-11-17
har gjort klart error och gjort klart hur man väljer svårighetsgrad och generarar olika kod beroende på vilken svårighetsgrad det är. nästa gång kolla om användare har gissat rätt/själva spel delen

kolla om input är samma som guess

//Logg 2025-11-20
håller på med layouten för rundor och så och har problem med hur man ska få ut gissningarna och att kolla om det stämmer överens med själva talet, vet inte hur man ska fixa det.

kollar om input är samma

//Logg 2025-11-24
håller på med guess funktionen/filen för att se till så att användaren inte kan skicka in något annat än siffrorna 1 - 6. trodde jag hade fixat det men hittade en bug där man kan skriva in en bokstav som gissning, programet säger att det är fel men returnerar ändå reseten om de finns andra gissningar.

tar in koden, tar in gissning, kollar om det finns likheter i list, om ja vilka, kolla index om det är samma, om ja --> grön, annars --> grå

får likheter, ersätter alla andra i listan med " ", kolla index för att se om ordning/plats är rätt

kolla att du INTE callar en funktion flera gånger

bug, error om du skriver in något annat än siffra i difficulty

//Logg 2025-11-27
har gjort så att det finns en check guess funktion som kollar om man har gissat rätt på något och ger tillbaka rätt respons. har inte gjort så det loopar så man kan gissa 12 gånger. har kopplat alla python filar så de hänger ihop. det som är kvar är att göra så man kan gissa 12 gånger, flera error meddelanden så användaren kan förstå vad som är fel med deras input, layout och så man kan välja att spela igen. även namn bytten på filer, variablar och funktioner så att de är lättare att förstå, och kommentarer i koden så man kan läsa vad som är vad.

kvar att göra:
du kan vinna/förlora
layout
kör igen
kommentarer (i koden)

notering för layout:
ska börja nedifrån och upp som ett riktigt mastermind bräde

har bara kvar layout 😊

måste göra så att man inte vet vilken som är rätt på rätt plats, osv
måste sort så att alla ✅ är först sen 🌫️

//Logg 2025-12-01
vi är snart klara och har gjort så att man kan förlora och vinna samt gjort så att man kan köra om, om man vill. det har gått ganska felfritt under lektionen, hade några få buggar där man inte kunde köra om även om man valde det, men vi fixade det genom att sätta i = 0 igen så funkade det. vi har bara layout och sortering av checkmarks och grå så att det blir lite svårare, samt att göra så det inte printas ut en lista för det är lite fult.
