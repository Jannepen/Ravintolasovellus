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

## Sovellukseen toteutetut toiminnallisuudet:

* Käyttäjätunnuksen tekeminen ja sisään sekä uloskirjautuminen
* Ravintoloiden lisääminen
* Ravintoloiden poistaminen
* Ravintoloiden selaaminen (mahdollisuus järjestää ravintolat arvosanan perusteella)
* Arvostelujen kirjoittaminen
* Ravintolan aukioloaikojen lisääminen
* Ravintolan lisääminen ryhmään (yhteen tai useampaan)
* Ravintolan tietojen lukeminen (arvosana, muiden arvostelut, aukioloajat, ryhmät)

## Sovelluksen testaaminen

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
   
### Puutteita/parannusehdotuksia

* Sovelluksen kaikki käyttäjät ovat samanarvoisia, olisi voinut tehdä ylläpitäjiä joilla erikoisoikeuksia.
* Ulkoasun tekeminen jäi hyvin puutteelliseksi.
* Mahdollisuus etsiä ravintoloita nimen perusteella.
* Ryhmät -toiminnallisuus jäi aika alkuvaiheeseen.
