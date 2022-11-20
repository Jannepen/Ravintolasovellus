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

## Sovelluksen tilanne (20.11.2022)

Sovellus on toiminnallisuuksiltaan vielä aika alkuvaiheessa. Sovelluksessa on mahdollista lisätä ja poistaa ravintoloita, sekä tarkkailla listaa ravintoloista. Sovellus ei ole vielä testattavissa tuotannossa, mutta alla ohjeita sovelluksen käyttöön ja sen testaamiseen.

### Sovelluksen testaaminen

1. Kloonaa sovellus omalle koneelle   
   `git clone https://github.com/Jannepen/Ravintolasovellus.git`
   
2. Mene sovelluksen repositorioon ja käynnistä pythonin virtuaaliympäristö komennoilla   
   `python3 venv venv`   
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

Sovelluksen etusivulla on vaihtoehdot lisätä, poistaa tai selata ravintoloita.
1. Lisääminen tapahtuu menemällä lisäämissivulle, antamalla nimi sekä painamalla "Lisää ravintola"
2. Ravintoloita voi poistaa menemällä poistamissivulle, antamalla poistettavan ravintolan nimen ja painamalla "Poista ravintola"
3. Painamalla "Selaa ravintoloita" pääsee sivulle, jossa on lista olemassa olevista ravintoloista. Mikäli ravintoloita ei ole lisätty, sivu näyttää tyhjältä.
