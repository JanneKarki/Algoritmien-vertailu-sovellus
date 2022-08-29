# Testausdokumentti


## Yksikkötestit

[Visualization-luokan](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/tests/visualization_test.py) yksikkötestit, testaavat luokan moinpuolisesti. Sen että kuva muodostuu ja että sen solun ja seinien paksuudet mukautuvat labyrintin koon mukaan. Myös piirrettävän ratkaisun täytyy muuttua samassa suhteessa. Nämä tulevat testatuksi.

[Explorer-luokan](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/tests/explore_test.py) yksikkötestit kattavat kaikki luokan metodit. Testaavat että labyrintissä liikkumisesta vastaavat metodit toimivat. Onko edessä, oikealla tai vasemmalla seinää. Oikealle-, vasemmalle ja ympärikääntyminen. Eeteenpäinliikkuminen etenee oikeaan soluun.

[WallFollower-luokan](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/tests/wall_follower_test.py) yksikkötestit

[Tremaux-luokan](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/tests/tremaux_test.py) yksikkötestit

[Maze-luokan](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/src/tests/maze_test.py) yksikkötestit

### Testien kattavuus

![](./pictures/test_pictures/coverage_4.png)

UI-käyttöliittymäluokka on jätetty testien ulkopuolelle.




# Suorituskykytestit

### Kruskalin algoritmi

Labyrintin luomisessa käytettävän Kruskalin-algoritmin suorituskykyä testattiin eri kokoisillla syötteillä.

![](./pictures/kruskal_aika.png)

Kulunut aika kasvaa logaritmisesti ja jo yli 100 kokoiset labyrintit alkavat olla todella raskaita algoritmille rakentaa. Yli 130 kokoiset ovat jo algoritmille liian suuria ja luonti päättyy RecursionError-virheeseen.

## Labyrintin ratkaisualgoritmien testit

### Wall Follower vs Tremaux

Wall-Follower suoritui ratkaisusta huomattavasti nopeammin kaikilla syötteillä ja niiden vertailu vaati samaan kuvaajaan erilliset aika-akselit. Kuvaajassa vasemmalla on Wall-Followerin aika-akseli ja oikealla Tremauxin.

![](./pictures/test_pictures/versus_chart.png)




### Wall Follower

Wall-Follower-algoritmin suoritusaika kasvaa lineaarisesti labyrintin koon kasvaessa.

![](./pictures/test_pictures/wall_follower_chart.png)





### Treamux
Tremauxi-algoritmin suoritusaika kasvaa logaritmisesti labyrintin koon kasvaessa.

![](./pictures/test_pictures/tremaux_chart.png)





## Testitulokset taulukossa

Suuren hajonnan vuoksi, Wallfollower- ja Tremaux-algoritmeja verrattiin keskenään erikokoisilla labyrinteillä suorittamalla molemmilla kymmenen toistoa ja vertailemalla niiden keskiarvoja. 


![](./pictures/test_pictures/result_chart.png)
