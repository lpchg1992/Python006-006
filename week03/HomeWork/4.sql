-- inner join
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
-- 结果应该是：(1, table1_table2)

-- left join
-- 结果应该是：Table1 符合条件的记录以及Table2符合条件的记录，和，Table1所有记录。Table2不符合条件的部分，虚拟表中显示NULL

-- right join
-- 结果应该是：Table2 符合条件的记录以及Table1符合条件的记录，和，Table2所有记录。Table1不符合条件的部分，虚拟表中显示NULL
