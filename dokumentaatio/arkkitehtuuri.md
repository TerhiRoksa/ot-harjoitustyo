
 # Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne ei ole vielä lopullinen. Mm database jakaantuu ja siirtyy toiseen pakkaukseen.

Ohjelman koodi on jaettu neljään pakkaukseen eli hakemistoon. Ui:ssa on käyttöliittymän koodi, servicessä sovelluslogiikka, operators sisältää ohjelman tietokohteet ja repositories 

Käyttöliittymä koostuu kahdesta näkymästä. Kirjautumisnäkymä avautuu ensin. siinä voi rekisteröidä uuden käyttäjä ja kirjautua sisään. Päänäkymä avautuu onnistuneen kirjautumisen jälkeen. Molemmat ovat omia luokkia.

Tietojen tallennus tehdään tietokantaan.

```mermaid
 classDiagram
    ui --> services
    services --> operators
    services --> repositories
    repositories --> operators
```

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
