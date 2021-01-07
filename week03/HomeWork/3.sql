SELECT DISTINCT player_id, player_name, count(*) as num 
FROM player JOIN team ON player.team_id = team.team_id 
WHERE height > 1.80 
GROUP BY player.team_id 
HAVING num > 2 
ORDER BY num DESC 
LIMIT 2

-- Step1：FROM JOIN ON：player + team通过筛选生成新的虚拟表；
-- Step2：WHERE ： 进一步筛选形成虚拟表；
-- Step3：GROUP BY 执行分组操作
-- Step4：HAVING 进行筛选，生成虚拟表
-- Step5：SELECT 从上一个虚拟表中进行不重复字段查询
-- Step6：ORDER 对查询结果进行降序排序
-- Step7：LIMIT 取2条查询结果