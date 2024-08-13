# Write your MySQL query statement below
select u.name, t.balance
from (select account, sum(amount) as balance
     from transactions
     group by account) t
     join Users u on t.account = u.account
where t.balance > 10000;
     