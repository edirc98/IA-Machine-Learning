-- CDs Comprados el año 2010
select * from cds where cds.buy_year = 2010;

-- Quien Compro cada cd
select cds.buyer, singers.singer_name, cds.buy_year
from cds
join singers
on cds.id_singer = singers.id;

-- CDs pertenecientes a "X singer"

select * from cds
join singers 
on singers.id = cds.id_singer
where singer_name like "Frank Sinatra";

-- CDs com generos 2 x

select cds.buy_year,cds.buyer from cds_generes
join cds on cds_generes.id_cd = cds.id
join generes g on cds_generes.id_genere = g.id 
where g.genere_name like "K-Pop" or g.genere_name like "Reagge"
group by cds.id
having count(cds.id)>1;

-- CDs que estan en ingles

select * from cds 
join languages l on cds.id_language = l.id where l.language like "English";

-- Listar cantantes Italianos

select * from singers s
join nacionalities n on s.id_nacionality = n.id
where n.nacionality_name like "Italian";

-- Cantantes de las Discograficas

select singers.singer_name, discografics.discografic_name from singers
join cds on singers.id = cds.id_singer
join discografics on discografics.id = cds.id_discografic
where discografics.discografic_name like "Epic Records" or discografics.discografic_name like "Warner Music Group";


