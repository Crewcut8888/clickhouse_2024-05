--check table
SELECT
	id,
	country,
	description,
	designation,
	points,
	price,
	province,
	region_1,
	region_2,
	variety,
	winery,
	taster_name,
	taster_twitter_handle,
	title,
	Column15,
	Column16,
	Column17,
	Column18
FROM
	fakhrutdinovvt.hw2;

optimize table fakhrutdinovvt.hw2;

--filter country and price
SELECT
	id,
	country,
	description,
	designation,
	points,
	price,
	province,
	region_1,
	region_2,
	variety,
	winery,
	taster_name,
	taster_twitter_handle,
	title,
	Column15,
	Column16,
	Column17,
	Column18
FROM
	fakhrutdinovvt.hw2
where
	length(country) > 0
	and not isnull(price);

--max price by country
SELECT
	country,
	max(price)	as	maxprice
FROM
	fakhrutdinovvt.hw2
where
	length(country) > 0
	and not isnull(price)
group by country;

--top-10 country by price of wine
SELECT
	country,
	max(price)	as	maxprice
FROM
	fakhrutdinovvt.hw2
where
	length(country) > 0
	and not isnull(price)
group by country
order by maxprice desc
limit 10;

--определить как высокая цена коррелирует с оценкой дегустатора (насколько дорогие вина хорошие) - 0.6232670000744933 determination coef
with main as 
(SELECT
	variety,
	avg(price)	as	maxprice,
	avg(toInt32OrZero(points))	as	pointsnum
FROM
	fakhrutdinovvt.hw2
where
	length(country) > 0
	and not isnull(price)
	and length(variety) > 0
group by variety
order by maxprice desc
)
select
corr(maxprice, pointsnum) as det_coef
from main
where pointsnum > 0
;

--учесть в выборке также регион производства - 0.5069291718966205 determination coef
with main as 
(SELECT
	province,
	variety,
	avg(price)	as	maxprice,
	avg(toInt32OrZero(points))	as	pointsnum
FROM
	fakhrutdinovvt.hw2
where
	length(country) > 0
	and not isnull(price)
	and length(variety) > 0
group by
	variety,
	province
order by maxprice desc
)
select
corr(maxprice, pointsnum) as det_coef
from main
where pointsnum > 0
;

