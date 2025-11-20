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
