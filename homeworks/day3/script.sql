SELECT x, y, deltaX, deltaY, clientTimeStamp, button, target
FROM `default`.mouse_movements;

optimize table `default`.mouse_movements;

--посчитать количество всех движений мыши
SELECT count(*)
FROM `default`.mouse_movements;
--посчитать кол-во движений мыши, попадающих в диапазон x < 1000 AND y < 1000 и сгруппировать по target
SELECT target, count(*)
FROM `default`.mouse_movements
where x < 1000 AND y < 1000
group by target;
--найти наиболее большие движения мыши (можно посчитать с помощью дельт: plus(abs(deltaX), abs(deltaY))
SELECT plus(abs(deltaX), abs(deltaY)) as mov , *
FROM `default`.mouse_movements
order by mov desc;