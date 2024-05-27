create table fakhrutdinovvt.test_table2 (
a Int,
b String,
c Enum('f' = 1, 's' = 2) ) ENGINE = MergeTree() order by a;


insert into fakhrutdinovvt.test_table2
select
    floor(randUniform(5, 100)) AS a,
    randomPrintableASCII(randUniform(5, 25)) AS b,
    floor(randUniform(1, 3)) as c
FROM numbers(10000);

SELECT a, b, c
FROM fakhrutdinovvt.test_table2
where b ILIKE '%ab%' and a > 6;

SELECT count(*)
FROM fakhrutdinovvt.test_table2;