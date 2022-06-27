---Pogledi za ProbnaBaza1

use ProbnaBaza1
go


create view vwKorisnik_Kreditna_kartica
with encryption
as
      select k.Ime , k.Prezime, kk.Broj_debitne_kartice,kk.Tip_kartice,kk.Vrsta_računa
	  from Korisnici k
	  inner join Kreditne_kartice kk on k.FK_Korisnik_kreditne_karticeID = kk.IDKreditne_kartice
	  where kk.Broj_debitne_kartice is not null
	  and kk.Tip_kartice is not null

go





select * from vwKorisnik_Kreditna_kartica

drop view vwKorisnik_Kreditna_kartica


create view vwKorisnici_računi
with encryption
as
      select k.Ime,k.Prezime , r.Redni_broj_računa , r.Datum_i_vrijeme_izdavanja
	  from Korisnici k
	  inner join Računi r on k.FK_RačunID = r.IDRačun
	  where r.Redni_broj_računa is not null 
	  and r.Datum_i_vrijeme_izdavanja is not null

go






select * from vwKorisnici_računi



create view vwKorisnici_naruđbe
with encryption
as 

         select k.Ime,k.Prezime , k.Korisnik_broj , n.Redni_broj_korisnika , n.Redni_broj_naruđbe
		 from Korisnici k
		 inner join Naruđbe n on k.FK_Naruđbe1ID = n.IDNaruđbe
		 where n.Redni_broj_korisnika is not null

go





select * from vwKorisnici_naruđbe