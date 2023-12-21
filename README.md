# Painonhallintasovellus
Tämän sovelluksen tarkoitus on auttaa painonhallinnassa. Sovelluksessa voi pitää 
kirjaa syömisistään eli tallentaa ruokia ja laskea kalorimääriä.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Releases](https://github.com/TerhiRoksa/ot-harjoitustyo/releases)

[Käyttöohje](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)

## Ohjelman komentoja

Ohjelman käynnistys:
poetry run invoke start

Testaus:
poetry run invoke test

Testikattavuusraportti:
poetry run invoke coverage-report
Raportti muodostuu htmlcov-hakemistoon.

Pylint tarkitus:
poetry run invoke lint
