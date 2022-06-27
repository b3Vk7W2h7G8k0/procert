---Indeksi za ProbnaBaza1

use ProbnaBaza1
go


create clustered index indeksIme
on Korisnici (Ime asc)

select * from Korisnici



create nonclustered index indeksKreditne_Kartice
on Kreditne_kartice (IDKreditne_Kartice asc)


select * from Kreditne_kartice

drop index Kreditne_kartice.indeksKreditne_Kartice


create nonclustered index indeksNaruđbe
on Naruđbe(IDNaruđbe asc)



select * from Naruđbe


create nonclustered index indeksRačuni
on Računi(IDRačun asc)

