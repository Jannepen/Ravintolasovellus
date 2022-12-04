# Ravintolasovellus

Sovelluksessa on tietoa alueen ravintoloista. Ravintoloille voi antaa arvosteluja ja muiden arvosteluja on mahdollista lukea. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen toiminnallisuuksia:

* Käyttäjä voi kirjautua sisään ja ulos tai luoda uuden tunnuksen.
* Käyttäjä näkee listan ravintoloista, joita klikkaamalla näytetään lisätietoa ravintolasta.
* Ravintoloita sisältävä lista on mahdollista järjestää eri tavoin, esim. parhaiten arvostellut.
* Käyttäjä voi antaa ravintolalle arvostelun, sekä lukea muiden arvosteluita.
* Käyttäjä voi etsiä ravintoloita avainsanan avulla.
* Ylläpitäjä voi lisätä sekä poistaa ravintoloita, sekä muokata ravintoloiden tietoja.
* Ylläpitäjä voi poistaa käyttäjien tekemiä arvosteluita.
* Ylläpitäjä voi luoda ryhmiä (esim. pizzeriat), johon kuuluu ravintoloita. Yksi ravintola voi kuulua useampaan ryhmään.
* Käyttäjä voi selata ryhmiä ja niihin kuuluvia ravintoloita.

## Sovelluksen tilanne (4.12.2022)

Sovellus ei vielä ole testattavissa tuotantopalvelimella, vaikka fly.io on alustettu versionhallintaan. Alla on ohjeet sovelluksen testaamiseen omalla koneella. 

Sovelluksessa on nyt mahdollista lisätä, poistaa sekä arvostella ravintoloita. Lisätyt ravintolat näkyvät ravintolat-sivulla, ja ravintolaa painamalla pääsee kyseisen ravintolan sivulle, jossa näkyy tietoa ravintolasta sekä ravintolalle kirjoitetut arvostelut. Sovellukseen on myös mahdollista luoda käyttäjä ja kirjautua sisään/ulos, mutta sovelluksen käyttäminen onnistuu vielä ilman käyttäjän luomista.

Seuraavia toiminnallisuuksia/kehityksen kohteita:

* Sovelluksen toimintojen käyttäminen vaatii kirjautumisen sisään käyttäjänä tai ylläpitäjänä.
* Ravintololle voi lisätä aukioloajat
* Mahdollisuus etsiä ravintoloita nimen perusteella.
* Ulkoasun parantaminen.
* Sovelluksen vieminen tuotantopalvelimelle.

### Sovelluksen testaaminen

1. Kloonaa sovellus omalle koneelle   
   `git clone https://github.com/Jannepen/Ravintolasovellus.git`
   
2. Mene sovelluksen repositorioon ja käynnistä pythonin virtuaaliympäristö komennoilla   
   `python3 -m venv venv`   
   `source venv/bin/activate`
3. Lataa tarvittavat riippuvuudet komennolla   
   `pip install -r requirements.txt`
4. Luo tiedosto .env ja alusta ympäristömuuttujat   
   `DATABASE_URL=postgresql:///user`   
   `SECRET_KEY=your_key`
5. Alusta tietokannat   
   `psql < schema.sql`
6. Käynnistä sovellus   
   `flask run`
   
### Käyttöohje

Sovelluksen toiminnallisuuksia:
1. Ravintolan lisääminen tapahtuu menemällä lisäämissivulle, antamalla nimi sekä painamalla "Lisää ravintola"
2. Ravintoloita voi poistaa menemällä poistamissivulle, ja valitsemalla poistettava ravintola
3. Painamalla "Selaa ravintoloita" pääsee sivulle, jossa on lista olemassa olevista ravintoloista. Mikäli ravintoloita ei ole lisätty, sivu näyttää tyhjältä. Painamalla ravintolaa pääsee ravintolan omalle sivulle.
4. Ravintolat-sivulla voi myös painaa "Järjestä arvosanan mukaan", jolloin ylhäällä ovat parhaiten arvostellut ravintolat
5. Sovellukseen voi myös tehdä käyttäjän ja kirjautua sisään/ulos, mutta muiden toimintojen kannalta se ei ole pakollista.
