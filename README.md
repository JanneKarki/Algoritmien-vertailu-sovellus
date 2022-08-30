# Labyrintin ratkaisualgoritmien vertailu

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/testausdokumentti.md)
- [Käyttöohje](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/kayttoohje.md)
- [Toteutusdokumentti](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/toteutusdokumentti.md)
## Viikkoraportit

- [Viikkoraportti 1](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/Viikkoraportti_1.md)
- [Viikkoraportti 2](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/Viikkoraportti_2.md)
- [Viikkoraportti 3](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/Viikkoraportti_3.md)
- [Viikkoraportti 4](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/Viikkoraportti_4.md)
- [Viikkoraportti 5](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/Viikkoraportti_5.md)
- [Viikkoraportti 6](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/blob/master/dokumentaatio/Viikkoraportti_6.md)


## Sovelluksen käyttöönotto

Lataa viimeisimmän [releasen](https://github.com/JanneKarki/Algoritmien-vertailu-sovellus/releases/tag/Loppupalautus) lähdekoodi valitsemalla Assets-osion alta Source code.


## Ohjelman käynnistäminen

Sovellus käyttää riippuvuuksien hallintaan poetrya, joten se tulee olla asennettuna koneelle. Asennuksen voit tarkistaa komennolla `poetry --version`. Tarvittaessa asennus onnistuu esimerkiksi [Ohte-kurssin](https://ohjelmistotekniikka-hy.github.io/python/viikko2#asennus)- ohjeella 

Ennen sovelluksen käynnistämistä, suorita komentoriviltä sovelluksen juurihakemistossa seuraavat komennot:

1. Asenna sovelluksen tarvitsemat riippuvuudet komennolla:
```bash
poetry install
```

2. Käynnistä sovellus komennoilla:

```bash
poetry run invoke start
```

## Yksikkötestaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```
Testikattavuusraportin luonti suoritetaan komennolla:

 ```bash
poetry run invoke coverage
```
Komennon jälkeen raportti löytyy htmlcov-hakemistosta nimellä index.html.

