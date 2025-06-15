-- Write your PostgreSQL query statement below
select p.email as "Email" from Person p group by email having count(email) > 1