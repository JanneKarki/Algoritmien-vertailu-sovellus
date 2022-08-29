# Toteutusdokumentti


## Labyrintin generointi

Satunnaisen labyrintin generointiin käytetään Kruskalin algoritmia, joka ensin muodostaa labyrintin koon mukaisen määrän soluja. Union-Find rakenteen avulla verrataan satunnaisesti kahta vierekkäistä(pysty tai vaaka) solua keskenään. Jos ne eivät ole vielä samassa joukossa, niiden välille luodaan yhteys ja lisätään ne yhteen samaan joukkoon. Soluja käydään läpi kunnes, kaikki solut ovat yhdessä samassa joukossa, josta muodostuu lopulta täysin yhtenäinen verkko, eli joka solusta voi matkustaa mihin tahansa soluun. Labyrintin alkuruutu on aina vasemmassa yläkulmassa ja loppuruutu oikassa alakulmassa. Generoinnin aikavaativuus on O(log(nm)).

Muodostuneesta Kruskalin ratkaisusta muodostetaan python-sanakirja(air_directed_maze), jossa avain:arvo pareina ovat solu:ilmansuunnat, joissa on tieto mihin ilmansuuntaan kustakin solusta on yhteys. Näin labyrintissä liikkuminen on helpompi toteuttaa. Muodostuksen aikavaativuus O(nm).

## Labyrintin ratkaiseminen

### Wall Follower

Ensimmäiseksi ratkaisualgoritmiksi valikoitui Wall Follower algoritmi, joka selviytyy hyvin Kruskalin luomasta labyrintistä, joka on yhtenäinen. Jos labyrintti ei olisi yhtenäinen, eli siellä olisi rakenteesta irrallaan olevia seiniä, niin vaarana olisi, että se jäisi kiertämään sellaista, eikä selviäisi labyrintistä ulos. Ratkaisussani algoritmi seuraa oikeanpuoleista seinustaa, jolloin reitti labyrintistä löytyy aina ulos. Yhtä hyvin se voisi seurata myös vasemmanpuoleista seunustaa. Samassa labyrintissä ratkaisu on aina sama. Algoritmin aikavaativuus on O(n).


### Tremaux

Toisena ratkaisualgoritmina on Treamux, joka selviää hyvin yhtenäisestä labyrintistä, mutta selviäisi myös epäyhtenäisestä labyrintistä. Tremaux-algrotmi merkitsee jo kulkemansa reitin sitä mukaan, kun se etenee labyrintissä. Kaksi kertaa merkatulle reitille se ei enään mene, niin ulosjohtamattomat reitit "sulkeutuvat", ja reitti ulos aina lopulta löytyy. Koska algoritmi valitsee suunna risteyksissä satunnaisesti, niin samassa labyrintissä voi tulla lukuisia erilaisia ratkaisuja, joiden suoritusaika vaihtelee. Aikavaativuus Treamux-algoritmille on O(log(n)).

## Pakkausrakenne

Sovelluksen koodin pakkausrakenne on seuraava:

![Pakkausrakenne](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/pictures/pakkausrakenne.png)

- Pakkaus "ui" sisältää käyttöliittymästä ja sovelluslogiikasta vastaavan luokan [UI](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/ui/ui.py), joka tarjoaa sovelluksen graafisen käyttöliittymän. 

- Pakkaus "algorithms" sisältää labyrintin luomiseen rakennetun  [Kruskalin](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/algorithms/maze.py)-algoirtmin ja sen ratkaisuun käytettävät [Wall Follower-](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/algorithms/wall_follower.py) ja [Tremaux](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/algorithms/tremaux.py)-algoritmit. 

- Pakkaus "Functionalities" sisältää luokan [Visualization](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/functionalities/visualization.py), joka tarjovaa algoritmeille tominnot labyrintin piirtämisen kuvaksi ja ratkaisun piirtämisen labyrintin kuvaan, sekä luokan [Explorer](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/functionalities/explore.py) joka tarjoaa ratkaisualgoritmeille toiminnot labyrintissä liikkumisen.

- /src-hakemistossa [index](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/index.py)-moduuli alustaa sovelluksen ikkunan ja käynnistää sovelluksen.


## Lähteet

  - Wikipedia, Maze-solving algorithm https://en.wikipedia.org/wiki/Maze-solving_algorithm
  - Kruskal Algorithm Maze Generation (Lauren K Williams, 2019) http://www.integral-domain.org/lwilliams/Applets/algorithms/kruskalmaze.php
