---Kreiranje pogleda za bazu podataka Intralot_Adria 09.04.2021 Petak 20:11:00h

---Kreiranje pogleda za krajnju jednostavniju upotrebu

use ProbnaBaza2
go


create view vwKlijenti_sa_pocetnim_slovom_imena_M
with encryption
as

               select k.Ime_klijenta, k.Prezime_klijenta
               from Klijenti k
			   where k.Ime_klijenta like 'M%'
			   group by k.Ime_klijenta,k.Prezime_klijenta
              

go

select * from vwKlijenti_sa_pocetnim_slovom_imena_M   ---Ovom naredbom pozivamo pogled bez da moramo pisati dotični upit

create view vmKlijenti_iz_određenog_mjesta
with encryption
as

         select m.Naziv_mjesta,k.Ime_klijenta,k.Prezime_klijenta,k.MjestoID
         from Mjesto m
         inner join Klijenti k on k.MjestoID = m.IDMjesto
         where MjestoID > 0


go


select * from vmKlijenti_iz_određenog_mjesta     ---Ovom naredbom pozivamo pogled bez da moramo pisati dotični upit


create view vmEvidencija_o_bivšim_klijentima
with encryption 
as

             select ev.Ime_Prezime_klijenta,ev.Status_klijenta
			 from Evidencija_o_bivšim_klijentima ev
			 where ev.Status_klijenta is not null

go


select * from vmEvidencija_o_bivšim_klijentima     ---Ovom naredbom pozivamo pogled bez da moramo pisati dotični upit


create view vmMjesta_i_županije
with encryption
as

        select ž.Naziv_županije,ž.Broj_županije,m.Poštanski_broj,ž.Lokacija_županije,m.ŽupanijaID
		from Županija ž
		inner join Mjesto m on m.ŽupanijaID = ž.IDŽupanija
		where m.ŽupanijaID is not null

go


select * from vmMjesta_i_županije  ---Ovom naredbom pozivamo pogled bez da moramo pisati dotični upit


---Kreirao: Saša Pozder