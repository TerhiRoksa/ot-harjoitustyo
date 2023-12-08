# Ohjelmistotekniikka, harjoitustyö
Harjoitustyöni tulee olemaan **Painonhallintasovellus**. Sillä voi pitää 
kirjaa *syömisistään*, tallentaa ruokia ja laskea kalorimääriä.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/TerhiRoksa/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Releases](https://github.com/TerhiRoksa/ot-harjoitustyo/releases)


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
