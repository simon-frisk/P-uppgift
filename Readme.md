# P uppgift

Spec

## Segling

Detta program är tänkt att ge den snabbaste vägen att segla genom ett hav. Programmet tar in data om vinden i olika punkter på havet, samt mellan vilka punkter man vill segla och ger som resultat den snabbaste vägen man ska segla.

## Utmaningar och svårigheter

En stor utmaning med detta program är att utveckla en bra algoritm. Detta problem är en shortest-path grafteoriproblem, vilket är ett utmanande matematiskt problem.

## Användningsområden

Ett användsområde för detta program är seglingstävlingar. För att kunna placera sig bra i en seglingstävling är det viktigt att optimera vägvalet man tar för att det ska ta så lite tid som möjligt. Detta är ganska svårt att tänka ut intuitivt. Båten åker olika snabbt i olika vindriktningar, och dessutom blåser det olika på olika ställen. Är det mest värt att segla en kortare väg så man behöver åka en kortare sträcka, eller en lite längre väg där vinden blåser mer gynnsamt? Istället för att chansa på den bästa vägen kan en tävlingsseglare använda detta program, som hjälper till med vägvalet och förbättrar chansen att vinna tävlingen!

## Ide för algoritmen

Detta problem är i grunden ett grafteoriproblem - sjön beskrivs som en viktad graf och det gäller att hitta den snabbaste vägen som minimerar den totala tiden mellan noderna som passeras. För att hitta den snabbaste vägen i en viktad graf på detta sätt kan Dijstra's algoritm användas.

Dijstra's algoritm bygger på att man har en prioritetskö med noder man inte besökt än. Man initierar viktningen från startnoden till nod A till oändligt stort, så att bara startnoden har sträcka 0. Sedan besöker man noderna genom att ta det minsta elementet i prioritetskön (detta tar konstant tid i en prioritetskö, varför just denna datastruktur används). Från denna nod räknar man ut sträckan till närliggande element, varpå även de kan besökas om de sedan är lägst i prioritetskön. När målnoden sedan besöks kommer den lägsta vägen vara funnen.

## Programskelett

```python

class Node:
    #En ruta i havet. Håller reda på vindriktningen i rutan.
    # Har attribut distance och previous, som används i dijstras algoritm för att hålla reda på sträckan till noden samt vilken nod som ligger innan i den kortaste vägen till denna nod.
    # Har även referenser till grannnoder för att snabbt kunna hitta dessa.

    def visit():
        # Besök denna nod i Dijstras. Iterera igenom grannar och räkna ut hur långt det kommer bli till dem, samt spara denna information om detta bildar den kortaste vägen.

class Graph:
    # Håller reda på alla noder i havet samt har övergripande funktioner för att hantera grafen.
    def __init__():
        # Skapar havet genom att gå igenom indata från inläst fil och bygger upp grafen. Itererar genom alla noder som ska skapas och skapar relationer mellan noderna genom att sätta attribut med grannar i respektive nod.
    def calculateFastestRoute():
        # Grundmetoden för Dijstras algoritm. Går igenom priority queuen tills man kommer till målnoden, funktionen avslutas och den bästa vägen returneras.
```

## Program- och dataflöde

Programmet startar med att vinddata läses från en fil. Med hjälp av denna data initieras grafen och alla noder. Sedan kommer indata från användaren om vilka noder som är start respektive mål. Sedan körs dijstras med hjälp av den uppbyggda datastrukturen.

User interface delen av programmet har tillgång till objektet som innehåller havet och kan därför rita ut havet och den bästa vägen. Den kan även ta in nya indata och köra algoritmen igen, så att grafen uppdateras.
