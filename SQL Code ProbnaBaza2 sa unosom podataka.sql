---Izrada baze podataka --- 09.04.2021 Petak 20:08:00h

create database ProbnaBaza2
go

use ProbnaBaza2
go


create table Županija
(
IDŽupanija int primary key identity,
Naziv_županije nvarchar (300),
Lokacija_županije nvarchar (200),
Broj_županije decimal (3)
)

create table Mjesto
(
IDMjesto int primary key identity,
Naziv_mjesta nvarchar (200),
Poštanski_broj decimal (5),
ŽupanijaID int foreign key references Županija(IDŽupanija)
)


create table Klijenti
(
IDKlijenti int primary key identity,
Ime_klijenta nvarchar (100),
Prezime_klijenta nvarchar (100),
OIB decimal (11),
Adresa nvarchar (300),
Kontakt_broj nvarchar (150),
Broj_mobilnog_operatera nvarchar (150),
Interni_id_klijenta nvarchar (10),
MjestoID int foreign key references Mjesto(IDMjesto)
)




create table Evidencija_o_bivšim_klijentima
(
IDEvidecija_o_bivšim_klijentima int primary key identity,
Ime_Prezime_klijenta nvarchar (350),
Interni_id_klijenta nvarchar (10),
Status_klijenta nvarchar (300)
)


---Unos podataka u tablicu Županija


insert into Županija(Naziv_županije,Lokacija_županije,Broj_županije)
values('Zagrebačka županija', 'Sjevernozapadna Hrvatska',1)

insert into Županija(Naziv_županije,Lokacija_županije,Broj_županije)
values('Primorsko-goranska županija', 'Zapadna Hrvatska', 2)

insert into Županija(Naziv_županije,Lokacija_županije,Broj_županije)
values('Brodsko-posavska županija', 'Istočna Hrvatska',3)

insert into Županija(Naziv_županije,Lokacija_županije,Broj_županije)
values('Koprivničko-Križevačka županija', 'Sjeverna Hrvatska', 4)


---Unos podataka u tablicu Mjesto


insert into Mjesto(Naziv_mjesta,Poštanski_broj,ŽupanijaID)
values ('Zagreb' , '10000', 1)

insert into Mjesto(Naziv_mjesta,Poštanski_broj,ŽupanijaID)
values ('Rijeka' , '51000', 2)

insert into Mjesto(Naziv_mjesta,Poštanski_broj,ŽupanijaID)
values ('Slavonski Brod' , '35000', 3)

insert into Mjesto(Naziv_mjesta,Poštanski_broj,ŽupanijaID)
values ('Koprivnica' , '48000', 4)


---Unos u tablicu Klijenti

insert into Klijenti(Ime_klijenta,Prezime_klijenta,OIB,Adresa,Kontakt_broj,Broj_mobilnog_operatera,Interni_id_klijenta,MjestoID)
values ('Branko' , 'Krlec' , 51130927738 , 'Slavnoska avenija 61a,Zagreb', '+385/1/431-2201', '+385/99/312-6091', 'HR01',1)


insert into Klijenti(Ime_klijenta,Prezime_klijenta,OIB,Adresa,Kontakt_broj,Broj_mobilnog_operatera,Interni_id_klijenta,MjestoID)
values ('Marko' , 'Les' , 51189045228 , 'Radnička cesta 92c,Zagreb', '+385/1/132-5401', '+385/98/654-1231', 'HR02',1)

insert into Klijenti(Ime_klijenta,Prezime_klijenta,OIB,Adresa,Kontakt_broj,Broj_mobilnog_operatera,Interni_id_klijenta,MjestoID)
values ('Marko' , 'Lam' , 91332005671, 'Delta 5b,Rijeka', '+385/51/300-203', '+385/91/316-6092', 'HR03',2)

insert into Klijenti(Ime_klijenta,Prezime_klijenta,OIB,Adresa,Kontakt_broj,Broj_mobilnog_operatera,Interni_id_klijenta,MjestoID)
values ('Valentina' , 'Kedir' , 41300563481 , 'Ante Starčevića 16a,Slavonski Brod', '+385/35/651-133', '+385/95/701-6092', 'HR04',3)

insert into Klijenti(Ime_klijenta,Prezime_klijenta,OIB,Adresa,Kontakt_broj,Broj_mobilnog_operatera,Interni_id_klijenta,MjestoID)
values ('Martha' , 'Ked' , 90115567329 , 'Bjelovarska cesta 45,Koprivnica', '+385/48/340-111', '+385/97/689-0192', 'HR05',4)




---Unos podataka u tablicu Evidencija o bivšim zaposlenicima


insert into Evidencija_o_bivšim_klijentima(Ime_Prezime_klijenta,Interni_id_klijenta,Status_klijenta)
values('Nikola Kliš', 'HR088', 'Neaktivan')

insert into Evidencija_o_bivšim_klijentima(Ime_Prezime_klijenta,Interni_id_klijenta,Status_klijenta)
values('Melita Breš', 'HR081', 'Neaktivna')

insert into Evidencija_o_bivšim_klijentima(Ime_Prezime_klijenta,Interni_id_klijenta,Status_klijenta)
values('Martina Makeš', 'HR092', 'Neaktivna')


---Baza je čisto oglednog primjera te se nemože upotrebljavati u industrijske ili bilo kakve tehničke svrhe.
---Te iz gore navedenog razloga baza je kreirana minimalistički.
---Nisam odgovoran za integritet podataka jer su dio fikcije potrebne za ogled,niti su podaci autentične prirode.
---Zabranjeno dijeliti podatke coda u bilo koje svrhe i sa strankama treće strane.


---S poštovanjem


---Created by Saša Pozder
