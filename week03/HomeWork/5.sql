-- 查询官方文档，了解索引
-- 增加索引：
ALTER TABLE userinfo ADD INDEX (user_id, user_name);
-- 增加索引后的查询：
SELECT * FROM userinfo;
-- 时间：0.127s, 0.135s,0.136s,0.151s,0.154s,0.125s,0.129s,0.136s.0.26s

-- 删除索引：
ALTER TABLE userinfo DROP INDEX user_id;
ALTER TABLE userinfo DROP INDEX user_name;
-- 删除索引后查询：
SELECT * FROM userinfo;
-- 时间：0.171s, 0.403s, 0.144s, 0.151s, 0.159s, 0.157s, 0.137s

-- 反复尝试多次发现没有明显变化。
-- 可能需要当数据量大的时候，同时，索引作为WHERE语句条件的时候才能提升速度。
-- 索引的本质也是一张表，增加索引会降低数据改变的时间。