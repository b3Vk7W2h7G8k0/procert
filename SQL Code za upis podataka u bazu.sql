---Insert/Upis podataka u bazu ProbnaBaza1

use ProbnaBaza1
go

insert into Naruđbe (Redni_broj_naruđbe,Redni_broj_korisnika,Redni_broj_računa)
values (1,1,1)

insert into Naruđbe (Redni_broj_naruđbe,Redni_broj_korisnika,Redni_broj_računa)
values (2,2,2)

insert into Naruđbe (Redni_broj_naruđbe,Redni_broj_korisnika,Redni_broj_računa)
values (3,3,3)

insert into Naruđbe (Redni_broj_naruđbe,Redni_broj_korisnika,Redni_broj_računa)
values (4,4,4)

insert into Naruđbe (Redni_broj_naruđbe,Redni_broj_korisnika,Redni_broj_računa)
values (5,5,5)

go

insert into Kreditne_kartice (Broj_korisnika,Tip_kartice,Broj_debitne_kartice,CSC_broj,Banka,IBAN,Vrsta_računa,Rok_valjanosti)
values (1, ' VISA ', 3489661700045832 , 923, 'Zagrabačka banka d.o.o', 'HR3915000016346895526' , 'Tekući kunski račun ' , '2028-05-26')

insert into Kreditne_kartice (Broj_korisnika,Tip_kartice,Broj_debitne_kartice,CSC_broj,Banka,IBAN,Vrsta_računa,Rok_valjanosti)
values (2, ' MasterCard ', 7741903351140521 , 328, 'Privredna Banka Zagreb d.o.o', 'HR6214000013162918813' , 'Devizni račun ' , '2025-07-29')

insert into Kreditne_kartice (Broj_korisnika,Tip_kartice,Broj_debitne_kartice,CSC_broj,Banka,IBAN,Vrsta_računa,Rok_valjanosti)
values (3, ' Diners ', 4401621198130592 , 816, 'Erste banka d.d', 'HR3385000091172843019' , 'Devizni račun ' , '2027-08-20')

insert into Kreditne_kartice (Broj_korisnika,Tip_kartice,Broj_debitne_kartice,CSC_broj,Banka,IBAN,Vrsta_računa,Rok_valjanosti)
values (4, ' Maestro ', 2122803391448157 , 788, 'Zagrabačka banka d.o.o', 'HR6719000091533268701' , 'Tekući kunski račun ' , '2023-03-23')

insert into Kreditne_kartice (Broj_korisnika,Tip_kartice,Broj_debitne_kartice,CSC_broj,Banka,IBAN,Vrsta_računa,Rok_valjanosti)
values (5, ' Amercan Express ', 1179054633034951 , 292, 'Erste banka d.d', 'HR3412000091557322693' , 'Devizni račun ' , '2024-06-05')

go


insert into Računi (Redni_broj_računa,Vrsta_računa,Naziv_artikla,Cijena_artikla,Stavke,Sveukupno_za_platiti,Datum_i_vrijeme_izdavanja,Adresa,Broj_operatera)
values (1, 'R1', 'SmartHub', '49,99 €' , '1 komad', '52,85 €', '2021-01-08 13:45:33', 'Radnička cesta 16a Zagreb', 1)

insert into Računi (Redni_broj_računa,Vrsta_računa,Naziv_artikla,Cijena_artikla,Stavke,Sveukupno_za_platiti,Datum_i_vrijeme_izdavanja,Adresa,Broj_operatera)
values (2, 'Standardni', 'Motion Sensor', '24,99€' , '1 komad', '26,85 € €', '2021-01-03 12:45:33', 'Radnička cesta 16a Zagreb', 2)

insert into Računi (Redni_broj_računa,Vrsta_računa,Naziv_artikla,Cijena_artikla,Stavke,Sveukupno_za_platiti,Datum_i_vrijeme_izdavanja,Adresa,Broj_operatera)
values (3, 'R1', 'Wireless Camera', '99,99 €' , '1 komad', '102,31 €', '2021-01-02 10:45:33', 'Radnička cesta 16a Zagreb', 3)

insert into Računi (Redni_broj_računa,Vrsta_računa,Naziv_artikla,Cijena_artikla,Stavke,Sveukupno_za_platiti,Datum_i_vrijeme_izdavanja,Adresa,Broj_operatera)
values (4, 'R1', 'Smoke Sensor', '19,99 €' , '1 komad', '21,85 €', '2021-01-07 09:45:33', 'Radnička cesta 16a Zagreb', 4)

insert into Računi (Redni_broj_računa,Vrsta_računa,Naziv_artikla,Cijena_artikla,Stavke,Sveukupno_za_platiti,Datum_i_vrijeme_izdavanja,Adresa,Broj_operatera)
values (5, 'R1', 'Water Leak Sensor', '14,99 €' , '1 komad', '16,25 €', '2021-01-19 14:45:33', 'Radnička cesta 16a Zagreb', 5)

go

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (3663, '20% popusta na konačni trošak ne može se koristiti zajedno s drugim kodovima', 1)

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (4815, '15% popusta na konačni trošak ne može se koristiti zajedno s drugim kodovima', 2)

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (9076, '10% popusta na konačni trošak ne može se koristiti zajedno s drugim kodovima', 3)

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (2617, '5% popusta na konačni trošak ne može se koristiti zajedno s drugim kodovima', 4)

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (5832, '20,00 € Off od sveukupnog iznosa može se koristiti sa drugim kodovima', 5)

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (4617, '13% popusta na konačni trošak za 3 komada Motion Sensor', 6)

insert into Kodovi_za_promocije (Kodovi,Promocija,Broj_promocije_za_artikle)
values (0531, '12% popusta za Smoke Sensor može se koristit sa kodom 5832', 7)

go


insert into Dobavljači (Naziv_dobavljača,Adresa,Broj_dobavljača,Email,Kontakt)
values ('Citrus d.o.o', 'Slavonska avenija 6b 10000 Zagreb', 1 , 'citrus@yahoo.com', '00385923147713')

insert into Dobavljači (Naziv_dobavljača,Adresa,Broj_dobavljača,Email,Kontakt)
values ('MEX-dostava d.o.o', 'Slavonska avenija 11 10000 Zagreb', 2 , 'MEX@gmail.com', '00385915046132')

insert into Dobavljači (Naziv_dobavljača,Adresa,Broj_dobavljača,Email,Kontakt)
values ('Snytax-it d.o.o', 'Radnička 62 10000 Zagreb', 3 , 'Syntax@aol.com', '00385994317721')

insert into Dobavljači (Naziv_dobavljača,Adresa,Broj_dobavljača,Email,Kontakt)
values ('PCguide d.o.o', 'Vukovarska 61b 10000 Zagreb', 4, 'PC@gmail.com', '00385985413325')

insert into Dobavljači (Naziv_dobavljača,Adresa,Broj_dobavljača,Email,Kontakt)
values ('nEit d.o.o', 'Ilica 60a 10000 Zagreb', 5 , 'neit@gmail.com.com', '00385918120919')

go



insert into Skladište (Naziv_predmeta_artikla,Na_zalihi,Trenutno_na_skladištu,Dobavljač_broj,FK_DobavljačiID)
values ('SmartHub', 1 , '1000 komada', 1, 1)

insert into Skladište (Naziv_predmeta_artikla,Na_zalihi,Trenutno_na_skladištu,Dobavljač_broj,FK_DobavljačiID)
values ('Motion Sensor', 1 , '1000 komada', 2, 2)

insert into Skladište (Naziv_predmeta_artikla,Na_zalihi,Trenutno_na_skladištu,Dobavljač_broj,FK_DobavljačiID)
values ('Wireless Camera', 1 , '1000 komada', 3, 3)

insert into Skladište (Naziv_predmeta_artikla,Na_zalihi,Trenutno_na_skladištu,Dobavljač_broj,FK_DobavljačiID)
values ('Smoke Snesor', 1 , '1000 komada', 4, 4)

insert into Skladište (Naziv_predmeta_artikla,Na_zalihi,Trenutno_na_skladištu,Dobavljač_broj,FK_DobavljačiID)
values ('Water Leak Sensor', 1  , '1000 komada', 5, 5)

go




insert into Cijenik (Cijena_proizvoda_za_50_komada,Cijena_proizvoda_za_100_komada,Cijena_proizvoda_za_500_komada,Popust_na_količinu_proizvoda_od_50_komada,Popust_na_količinu_proizvoda_od_100_komada,Popust_na_količinu_proizvoda_od_500_komada,Popust_na_količinu_proizvoda_od_1000_komada)
values ('SmartHub 50 komada izonsi 2,499.5 €',
        'SmartHub 100 komada iznosi 4,999 €',
		'SmartHub 500 komada iznosi 24,995 €',
		'SmartHub na 50 komada 3% iznosi 2,424.5 €',
		'SmartHub na 100 komada 5% iznosi 4,749.5 €',
		'SmartHub na 500 komada 10% iznosi 22,495.5 €',
		'SmartHub na 1000 komada 15% iznosi 42,491.5 €'
		)




insert into Cijenik (Cijena_proizvoda_za_50_komada,Cijena_proizvoda_za_100_komada,Cijena_proizvoda_za_500_komada,Popust_na_količinu_proizvoda_od_50_komada,Popust_na_količinu_proizvoda_od_100_komada,Popust_na_količinu_proizvoda_od_500_komada,Popust_na_količinu_proizvoda_od_1000_komada)
values ( 
        'Motion Sensor 50 komada izonsi 1,249.5 €',
        'Motion Sensor 100 komada iznosi 2,499 €',
		'Motion Sensor 500 komada iznosi 12,495 €',
		'Motion Sensor 50 komada 3% iznosi 1,212 €',
		'Motion Sensor 100 komada 5% iznosi 2,374 €',
		'Motion Sensor 500 komada 10% iznosi 11,245.5 €',
		'Motion Sensor 1000 komada 15% iznosi 21,241.5 €'
		)



insert into Cijenik (Cijena_proizvoda_za_50_komada,Cijena_proizvoda_za_100_komada,Cijena_proizvoda_za_500_komada,Popust_na_količinu_proizvoda_od_50_komada,Popust_na_količinu_proizvoda_od_100_komada,Popust_na_količinu_proizvoda_od_500_komada,Popust_na_količinu_proizvoda_od_1000_komada)
values ('Wireless Camera 50 komada izonsi 4,995.5 €',
        'Wireless Camera 100 komada iznosi 9,999 €',
		'Wireless Camera 500 komada iznosi 49,995 €',
		'Wireless Camera na 50 komada 3% iznosi 4,849.5 €',
		'Wireless Camera na 100 komada 5% iznosi 9,499.05 €',
		'Wireless Camera na 500 komada 10% iznosi 49,995 €',
		'Wireless Camera na 1000 komada 15% iznosi 99,900 €'
		)



insert into Cijenik (Cijena_proizvoda_za_50_komada,Cijena_proizvoda_za_100_komada,Cijena_proizvoda_za_500_komada,Popust_na_količinu_proizvoda_od_50_komada,Popust_na_količinu_proizvoda_od_100_komada,Popust_na_količinu_proizvoda_od_500_komada,Popust_na_količinu_proizvoda_od_1000_komada)
values ('Smoke Sensor 50 komada izonsi 999,5 €',
        'Smoke Sensor 100 komada iznosi 1,999 €',
		'Smoke Sensor 500 komada iznosi 9,995 €',
		'Smoke Sensor na 50 komada 3% iznosi 969.5 €',
		'Smoke Snesor na 100 komada 5% iznosi 1,899.05 €',
		'Smoke Sensor na 500 komada 10% iznosi 8,995.5 €',
		'Smoke Sensor na 1000 komada 15% iznosi 16,991.5 €'
		)




insert into Cijenik (Cijena_proizvoda_za_50_komada,Cijena_proizvoda_za_100_komada,Cijena_proizvoda_za_500_komada,Popust_na_količinu_proizvoda_od_50_komada,Popust_na_količinu_proizvoda_od_100_komada,Popust_na_količinu_proizvoda_od_500_komada,Popust_na_količinu_proizvoda_od_1000_komada)
values ('WaterleakSensor 50 komada izonsi 749.5 €',
        'WaterleakSensor 100 komada iznosi 1,499 €',
		'WaterleakSensor 500 komada iznosi 7,495 €',
		'WaterleakSensor na 50 komada 3% iznosi 727 €',
		'WaterleakSensor na 100 komada 5% iznosi 1424.05€',
		'WaterleakSensor na 500 komada 10% iznosi 6745.5€',
		'WaterleakSensor na 1000 komada 15% iznosi 12741.5€'
		)


go

insert into Predmeti_artikli (Naziv_predmeta_artikla,Opis_predmeta,Rok_valjanosti,Garancija,Cijena_po_komadu,Broj_promocije,Količina,Sveukupno,Dodaj_u_košaricu,FK_Predmeti_artikli,FK_SkladišteID)
values ('SmartHub', 'Pametno čvorište za USB', '2030-01-01 00:00:00', '2 godine', '49,99 €', 2 , 1, 'Za platiti 49.99 €', 1,1,1)



insert into Predmeti_artikli (Naziv_predmeta_artikla,Opis_predmeta,Rok_valjanosti,Garancija,Cijena_po_komadu,Broj_promocije,Količina,Sveukupno,Dodaj_u_košaricu,FK_Predmeti_artikli,FK_SkladišteID)
values ('Motion Sensor', 'Senzor pokreta', '2030-01-01 00:00:00', '2 godine', '24,99 €', 3 , 1, 'Za platiti 24,99 €', 2,2,2)


insert into Predmeti_artikli (Naziv_predmeta_artikla,Opis_predmeta,Rok_valjanosti,Garancija,Cijena_po_komadu,Broj_promocije,Količina,Sveukupno,Dodaj_u_košaricu,FK_Predmeti_artikli,FK_SkladišteID)
values ('Wireless Camera', 'Bežična kamera', '2030-01-01 00:00:00', '2 godine', '99.99 €', 4 , 1, 'Za platiti 99.99 €', 3,3,3)


insert into Predmeti_artikli (Naziv_predmeta_artikla,Opis_predmeta,Rok_valjanosti,Garancija,Cijena_po_komadu,Broj_promocije,Količina,Sveukupno,Dodaj_u_košaricu,FK_Predmeti_artikli,FK_SkladišteID)
values ('Smoke Sensor', 'Detektor dima', '2030-01-01 00:00:00', '2 godine', '19,99 €', 5 , 1, 'Za platiti 19,99 €', 4,4,4)


insert into Predmeti_artikli (Naziv_predmeta_artikla,Opis_predmeta,Rok_valjanosti,Garancija,Cijena_po_komadu,Broj_promocije,Količina,Sveukupno,Dodaj_u_košaricu,FK_Predmeti_artikli,FK_SkladišteID)
values ('Water Leak Sensor', 'Vodoprpusni senzor', '2030-01-01 00:00:00', '2 godine', '14,99€', 6, 1, 'Za platiti 14,99 €', 5,5,5)

go

insert into Košarica (Artikli,Količina,Izbriši_iz_košarice,Promocije_artikla,Izbriši_promocije_artikla,Broj_promocije_artikla,Dostava,Broj_naruđbe,Za_platiti,FK_Predmeti_artikliID)
values ('SmartHub', '1', '0','1','0', '1', 'Besplatna dostava', '1', '52,91 €', 1)


insert into Košarica (Artikli,Količina,Izbriši_iz_košarice,Promocije_artikla,Izbriši_promocije_artikla,Broj_promocije_artikla,Dostava,Broj_naruđbe,Za_platiti,FK_Predmeti_artikliID)
values ('Motion Sensor', '1', '0','2','0', '1', 'Dostava 3 €', '1', '27,82 €', 2)


insert into Košarica (Artikli,Količina,Izbriši_iz_košarice,Promocije_artikla,Izbriši_promocije_artikla,Broj_promocije_artikla,Dostava,Broj_naruđbe,Za_platiti,FK_Predmeti_artikliID)
values ('Wireless Camera', '1', '0','3','0', '1', 'Besplatna dostava', '1', '102,65 €', 3)


insert into Košarica (Artikli,Količina,Izbriši_iz_košarice,Promocije_artikla,Izbriši_promocije_artikla,Broj_promocije_artikla,Dostava,Broj_naruđbe,Za_platiti,FK_Predmeti_artikliID)
values ('Smoke Senosor', '1', '0','4','0', '1', 'Dostava 3 €', '1', '23,06 €', 4)


insert into Košarica (Artikli,Količina,Izbriši_iz_košarice,Promocije_artikla,Izbriši_promocije_artikla,Broj_promocije_artikla,Dostava,Broj_naruđbe,Za_platiti,FK_Predmeti_artikliID)
values ('Water Leak Senosr', '1', '0','5','0', '1', 'Dostava 3 €', '1', '18,65 €', 5)

go

set identity_insert Promocije On


insert into Promocije (IDPromocije,Broj_promocije,Opis_deklaracija_promocije,Pogodnosti,PromocijeID,Košarica1ID)
values (1,1, 'Promocija vezano za kod 0531 sa kodom 5832', 'SmartHub',1,1)


insert into Promocije (IDPromocije,Broj_promocije,Opis_deklaracija_promocije,Pogodnosti,PromocijeID,Košarica1ID)
values (2,2, 'Promocija vezano za kod 4617 nemože se koristiti ni sa kojim drugim kodom', 'Motion Sensor' , 2 ,2)


insert into Promocije (IDPromocije,Broj_promocije,Opis_deklaracija_promocije,Pogodnosti,PromocijeID,Košarica1ID)
values (3,3, 'Promocija vezano za kod 5832 može se koristiti ni sa drugim kodom', 'Wireless Camera' , 3 ,3)


insert into Promocije (IDPromocije,Broj_promocije,Opis_deklaracija_promocije,Pogodnosti,PromocijeID,Košarica1ID)
values (4,4, 'Promocija vezano za kod 531 može se koristiti ni sa kodom 5832', 'Smoke Sensor' , 4 ,4)


insert into Promocije (IDPromocije,Broj_promocije,Opis_deklaracija_promocije,Pogodnosti,PromocijeID,Košarica1ID)
values (5,5, 'Promocija vezano za kod 5832 20,00€ off može se koristiti sa drugim kodovima', 'Water Leak Sensor' , 5 ,5)


set identity_insert Promocije Off


go


insert into Korisnici (Ime,
                       Prezime,
					   OIB,
					   Adresa,
					   Email,
					   Mobitel,
					   Fiksna_linija,
					   Korisnik_broj,
					   FK_Korisnik_kreditne_karticeID,
					   FK_KošaricaID,
					   FK_Naruđbe1ID,
					   FK_RačunID
					   )

values ('Darko', 
        'Meršin', 
		 43221806173 , 
		'Škorpikova 14a 10000 Zagreb', 
		'd.mer@gmail.com', 
		'00385917114501', 
		'003851814-232',
		'1',
		 1,
		 1,
		 1,
		 1
		)


insert into Korisnici (Ime,
                       Prezime,
					   OIB,
					   Adresa,
					   Email,
					   Mobitel,
					   Fiksna_linija,
					   Korisnik_broj,
					   FK_Korisnik_kreditne_karticeID,
					   FK_KošaricaID,
					   FK_Naruđbe1ID,
					   FK_RačunID
					   )

values ('Melita', 
        'Melly', 
		 31257738011 , 
		'Ulica grada Vukovara 32a 10000 Zagreb', 
		'melly@gmail.com', 
		'00385919813325', 
		'003851814-914',
		'2',
		 2,
		 2,
		 2,
		 2
		)




insert into Korisnici (Ime,
                       Prezime,
					   OIB,
					   Adresa,
					   Email,
					   Mobitel,
					   Fiksna_linija,
					   Korisnik_broj,
					   FK_Korisnik_kreditne_karticeID,
					   FK_KošaricaID,
					   FK_Naruđbe1ID,
					   FK_RačunID
					   )

values ('Davor', 
        'Smreka', 
		 71322608123 , 
		'Ilica 1 10000 Zagreb', 
		'smreka@aol.com', 
		'00385918143392', 
		'003851313-525',
		'3',
		 3,
		 3,
		 3,
		 3
		)





insert into Korisnici (Ime,
                       Prezime,
					   OIB,
					   Adresa,
					   Email,
					   Mobitel,
					   Fiksna_linija,
					   Korisnik_broj,
					   FK_Korisnik_kreditne_karticeID,
					   FK_KošaricaID,
					   FK_Naruđbe1ID,
					   FK_RačunID
					   )

values ('Martina', 
        'Maušec', 
		 74561330921 , 
		'Kvaternikov trg 33c 10000 Zagreb', 
		'm.mausecr@gmail.com', 
		'00385914139904', 
		'003851514-685',
		'4',
		 4,
		 4,
		 4,
		 4
		)






insert into Korisnici (Ime,
                       Prezime,
					   OIB,
					   Adresa,
					   Email,
					   Mobitel,
					   Fiksna_linija,
					   Korisnik_broj,
					   FK_Korisnik_kreditne_karticeID,
					   FK_KošaricaID,
					   FK_Naruđbe1ID,
					   FK_RačunID
					   )

values ('Antonio', 
        'Kajs', 
		 77133408551 , 
		'Jarun 16a 10000 Zagreb', 
		'a.kajs@gmail.com', 
		'00385913124083', 
		'003851420-240',
		'5',
		 5,
		 5,
		 5,
		 5
		)
