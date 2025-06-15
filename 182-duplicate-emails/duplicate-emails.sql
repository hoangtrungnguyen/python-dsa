# Write your MySQL query statement below
select distinct(p.email) as "Email" from Person p where (select count(1) from Person p2 where p2.email = p.email ) > 1