---Okidači za bazu podataka 


---Okidači za unos podataka u bazu


use ProbnaBaza2
go


create trigger MojOkidač_Klijenti_Unos
on Klijenti
after insert
as
    select Ime_klijenta,Prezime_klijenta,Interni_id_klijenta
	from inserted


go


create trigger Unos
on Klijenti
after insert
as
if exists (select Ime_klijenta,Prezime_klijenta,Interni_id_klijenta from inserted) 
  
     begin

	       print 'Klijent uspiješno upisan u bazu podataka'
     end
go





---Okidači za ažuiranje podataka u bazi

create trigger MojOkidač_Klijenti_Ažuiranje
on Klijenti
after update
as
    select Ime_klijenta,Prezime_klijenta,Interni_id_klijenta
	from inserted


go



create trigger Ažuiranje
on Klijenti
after update
as
if exists (select Ime_klijenta,Prezime_klijenta,Interni_id_klijenta from inserted ) 
  
     begin

	       print 'Klijent uspiješno ažuiran u bazi podataka'
     end
go






---Okidači za brisanje podataka u bazi


create trigger MojOkidač_Klijenti_Brisanje
on Klijenti
after delete
as
    select Ime_klijenta,Prezime_klijenta,Interni_id_klijenta
	from deleted


go


create trigger Brisanje
on Klijenti
after delete
as
if exists (select Ime_klijenta,Prezime_klijenta,Interni_id_klijenta from deleted) 
  
     begin

	       print 'Klijent uspiješno obrisan iz baze podataka'
     end
go


