---Izrada baze podataka za IntraLot_Adria ---Petak 09.04.2021 u 19:39:00 h 

create database ProbnaBaza1  ---1(prvi korak)---stvaramo bazu podataka.
go

use ProbnaBaza1    ---2(drugi korak)---pokrečemo korištenje baze podataka.
go


create table Korisnici     ---3(treći korak)---kreiramo redom sve tablice u codu.Ovdje se radi o tablici Korisnici
(
Ime nvarchar (50),
Prezime nvarchar (50),
OIB decimal (11) not null,
Adresa nvarchar (500),
Email nvarchar (100),
Mobitel nvarchar (100),
Fiksna_linija nvarchar (100),
Korisnik_broj decimal (38) ,
)


---14(četrnaesti korak)dodajemo i kreiramo strane kljućeve navedene ispod u komentarima.


/*
alter table Korisnici
add FK_Korisnik_kreditne_karticeID int foreign key references Kreditne_kartice(IDKreditne_kartice)


alter table Korisnici
add FK_Naruđbe1ID  int foreign key references Naruđbe(IDNaruđbe)

alter table Korisnici
add FK_KošaricaID int foreign key references Košarica(IDKošarica)

alter table Korisnici
add FK_RačunID int foreign key references Računi(IDRačun)

*/



create table Kreditne_kartice  ---4(četvrti korak) kreiramo tablicu Kreditne_kartice
(
IDKreditne_kartice int CONSTRAINT PK_Kreditne_kartice primary key identity,
Broj_korisnika decimal (38) not null,
Tip_kartice nvarchar (100) not null,
Broj_debitne_kartice decimal (16) not null,
CSC_broj decimal (3) not null,
Banka nvarchar (100) not null,
IBAN nvarchar (21) not null,
Vrsta_računa nvarchar (150) not null,
Rok_valjanosti date not null,
)




create table Naruđbe  ---5(peti korak) kreiramo tablicu Naruđbe
(
IDNaruđbe int CONSTRAINT PK_IDNaruđbe primary key identity,
Redni_broj_naruđbe decimal (38),
Redni_broj_korisnika decimal (38) ,
Redni_broj_računa decimal (38),
)






create table Košarica   ---6(šesti korak) kreiramo tablicu Košarica
(
IDKošarica int CONSTRAINT PK_Košarica primary key identity ,
Artikli nvarchar (300) ,
Količina nvarchar (500),
Izbriši_iz_košarice nvarchar (500),
Promocije_artikla nvarchar (500),
Izbriši_promocije_artikla nvarchar (500) ,
Broj_promocije_artikla decimal (38) ,
Dostava nvarchar (100),
Broj_naruđbe decimal (38) ,
Za_platiti nvarchar (350),
)



---15(petnaesti korak)dodajemo i kreiramo strani kljuć,dolje naveden u komentarima.

/*
alter table Košarica
add FK_Predmeti_artikliID int foreign key references Predmeti_artikli(IDPredmeti_artikli)
*/





create table Računi   ---7(sedmi korak)kreiramo tablicu Računi.
(
IDRačun int CONSTRAINT PK_Račun primary key identity,
Redni_broj_računa decimal (38),
Vrsta_računa nvarchar (250) ,
Naziv_artikla nvarchar (300),
Cijena_artikla nvarchar (300) ,
Stavke nvarchar (500),
Sveukupno_za_platiti nvarchar (500),
Datum_i_vrijeme_izdavanja datetime ,
Adresa nvarchar (350),
Broj_operatera decimal (20),
)






create table Predmeti_artikli    ---8(osmi korak)kreiramo tablicu Predmeti_artikli.
(
IDPredmeti_artikli int primary key identity,
Naziv_predmeta_artikla nvarchar (200) ,
Opis_predmeta nvarchar (350) ,
Rok_valjanosti datetime ,
Garancija nvarchar (300) ,
Cijena_po_komadu nvarchar (300) ,
Broj_promocije decimal (38) ,
Količina decimal (38) ,
Sveukupno nvarchar (350) ,
Dodaj_u_košaricu bit ,
)


---16(šesnaesti korak)dodajemo i kreiramo strane kljućeve koji navedni u komentarima.

/*
alter table Predmeti_artikli
add FK_Predmeti_artikli int foreign key references Cijenik(IDCijenik)

alter table Predmeti_artikli
add FK_SkladišteID int foreign key references Skladište(IDSkladište)

*/


create table Cijenik ---9(deveti korak)kreiramo tablicu Cijenik.
(
IDCijenik int CONSTRAINT PK_Cijenik primary key identity ,
Cijena_proizvoda_za_50_komada nvarchar (350) ,
Cijena_proizvoda_za_100_komada nvarchar (350) ,
Cijena_proizvoda_za_500_komada nvarchar (350) ,
Popust_na_količinu_proizvoda_od_50_komada nvarchar (50) ,
Popust_na_količinu_proizvoda_od_100_komada nvarchar (50) ,
Popust_na_količinu_proizvoda_od_500_komada nvarchar (50) ,
Popust_na_količinu_proizvoda_od_1000_komada nvarchar (50) ,
)




create table Dobavljači  ---10(deseti korak)kreiramo tablicu Dobavljači.
(
IDDobavljači int CONSTRAINT PK_Dobavljači primary key identity ,
Naziv_dobavljača nvarchar (300) ,
Adresa nvarchar (500) ,
Broj_dobavljača decimal (38) ,
Email nvarchar (100) ,
Kontakt nvarchar (200) ,
)




create table Skladište ---11(jedanaesti korak) kreiramo tablicu Skladište.
(
IDSkladište int primary key identity,
Naziv_predmeta_artikla nvarchar (300) ,
Na_zalihi bit ,
Trenutno_na_skladištu nvarchar (350) ,
Dobavljač_broj decimal (38),
)



---17(sedamnaesti korak)dodajemo i kreiramo strani kljuć u dolje navedenom komentaru.

/*
alter table Skladište
add FK_DobavljačiID int foreign key references Dobavljači(IDDobavljači)
*/


create table Promocije  ---12(dvanaesti korak) kreiramo tablicu Promocije.
(
IDPromocije int CONSTRAINT PK_Promocije primary key identity ,
Broj_promocije decimal (38) ,
Opis_deklaracija_promocije nvarchar (500) ,
Pogodnosti nvarchar (300) ,
)



---18(osamnaesti korak)dodajemo i kreiramo dolje navedene strane kljućeve.

/*
alter table Promocije
add PromocijeID int foreign key references Kodovi_za_promocije(IDKodovi_za_promocije)

alter table Promocije
add Košarica1ID int foreign key references Košarica(IDKošarica)
*/





create table Kodovi_za_promocije ---13(trinaesti korak)kreiramo tablicu Kodovi_za_promocije.
(
IDKodovi_za_promocije int CONSTRAINT PK_Kodovi_za_promocije primary key identity,
Kodovi decimal (38) ,
Promocija nvarchar (500) ,
Broj_promocije_za_artikle decimal (38) ,
)


---Autor: Saša Pozder


---Napomena: Cijela baza podataka kao i njen sadržaj jest striktno za potrebe testiranja(ogledni primjer),podaci koji će biti navedeni u
---bazi nisu stvarni i relevantni.Te za iste nemogu ni na koji način pravno odgovarati.
---Te bih vas zamolio da dotičnu bazu nekoristite u krajnjoj produkciji iz razloga što nije prilagođena potrebama poduzeća i
---testirana u radnim uvijetima.Hvala vam na razumijevanju te vam želim ugodan ostatak dana.

---S poštovanjem


---  Saša Pozder