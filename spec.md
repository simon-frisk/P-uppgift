# P uppgift

## Segling

## Ide för algoritmen

Detta problem är i grunden ett grafteoriproblem - sjön beskrivs som en viktad graf och det gäller att hitta den snabbaste vägen som minimerar den totala tiden mellan noderna som passeras. För att hitta den snabbaste vägen i en viktad graf på detta sätt kan Dijstra's algoritm användas.

Dijstra's algoritm bygger på att man har en prioritetskö med noder man inte besökt än. Man initierar viktningen från startnoden till nod A till oändligt stort, så att bara startnoden har sträcka 0. Sedan besöker man noderna genom att ta det minsta elementet i prioritetskön (detta tar konstant tid i en prioritetskö, varför just denna datastruktur används). Från denna nod räknar man ut sträckan till närliggande element, varpå även de kan besökas om de sedan är lägst i prioritetskön. När målnoden sedan besöks kommer den lägsta vägen vara funnen.
