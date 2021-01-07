-- inner join
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
-- 结果应该是：(1, table1_table2)

-- left join
-- 结果应该是：((1, table1_table2), (2, table1))

-- right join
-- 结果应该是：((1, table1_table2), (3, table2))
