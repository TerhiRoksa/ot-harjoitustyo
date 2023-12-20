
 # Arkkitehtuurikuvaus

## Rakenne


Ohjelman koodi on jaettu neljään pakkaukseen eli hakemistoon. Ui:ssa on käyttöliittymän koodi, servicessä sovelluslogiikka, operators sisältää ohjelman tietokohteet ja repositories tietojen tallennuksen.

Käyttöliittymä koostuu kahdesta näkymästä. Kirjautumisnäkymä avautuu ensin. Siinä voi rekisteröidä uuden käyttäjän ja kirjautua sisään. Päänäkymä avautuu onnistuneen kirjautumisen jälkeen. Molemmat ovat omia luokkiaan.

Tietojen tallennus tehdään tietokantaan.

```mermaid
 classDiagram
    ui --> services
    services --> operators
    services --> repositories
    repositories --> operators
```

## Toiminnallisuudet

Käyttäjä voi rekisteröidä itselleen käyttäjätunnuksen antamalla sovellukseen käyttäjätunnuksen ja salasanan. Käyttäjä voi kirjautua sovellukseen kirjoittamalla käyttätunnuksen ja salasanan ja painamalla Kirjaudu-painiketta. Onnistuneen kirjautumisen jälkeen kirjautumisnäkymä sulketuu ja päänäkymä avatuu. 

Päänäkymässä käyttäjä voi hakea tallentamansa ruoat näkyviin tietokannasta painamalla Näytä-painiketta. Käyttäjä voi tallentaa uusia ruokatietoja antamalla ruoan nimen ja kalorimäärän ja painamalla Lisää ruokatieto-painiketta. Ruokatiedon lisäys tuo näkyviin käyttäjälle tallennetun kokonaiskalorimäärän. Käyttäjä voi tyhjentää tallentamansa ruokatiedot painamalla Tyhjennä tallennetut ruokatiedot-painiketta. Käyttäjä voi kirjautua ulos sovelluksesta painamalla Kirjaudu ulos-painiketta. Uloskirjautumisessa päänäkymä sulkeutuu ja kirjautumisnäkymä avautuu uudelleen.

## Sekvenssikaavio

```mermaid
sequenceDiagram
  participant User
  participant Ui
  participant database
  
  User ->> +Ui: click "Lisää ruoka" button
  Ui ->> +database: add_food(user_id, food_name)
  Ui ->> +database: get_user_foods(user_id=1)
  database ->> +Ui: foods
  Ui ->> +User: food_list_text
```
