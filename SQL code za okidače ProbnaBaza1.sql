---Kreiranje okidača za ProbnaBaza1


use ProbnaBaza1
go

create trigger [dbo].[OkidačInsert]
on	[dbo].[Korisnici]
after insert
as
    begin
	      print 'Unos upisan'
    end

GO

ALTER TABLE [dbo].[Korisnici] ENABLE TRIGGER [OkidačInsert]
GO

create trigger [dbo].[OkidačUpdate]
on [dbo].[Korisnici]
after update
as
    begin
	      print 'Unos ažuiran'
	end
GO

ALTER TABLE [dbo].[Korisnici] ENABLE TRIGGER [OkidačUpdate]
GO


create trigger [dbo].[OkidačDelete]
on [dbo].[Korisnici]
after delete
as
    begin 
	      print 'Unos obrisan'

	end
GO

ALTER TABLE [dbo].[Korisnici] ENABLE TRIGGER [OkidačDelete]
GO
