# laba_3
Лабораторная работа по базам данных №3

Описание проекта:

Проект реализован на двух типах данных: tiny и big - размером 115 МБ и 697 МБ соответвенно. В двух папках, соответствующих данным типам, находятся 5 py файлов, в каждом из которых реализованы 4 sql запроса для конкретной библиотеки, указанной в названии файла.

SQL запросы:

    1. SELECT VendorID, count(*) FROM trips GROUP BY 1;
    2. SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;
    3. SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;
    4. SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;

Впечатления от библиотек:

В целом, у библиотек: sqlite3, DuckDB, psycopg2, SQLAlchemy схожий синтаксис, но со своими нюансами. Синтаксис sqlite3 показался самым простым из них, у DuckDB синтаксис индентичный sqlite3. С psycopg2 изначально возникли трудности, так как я не знала, что надо указывать public при обращении к таблице, а при обращении к столбцам заключать их в двойные кавычки, но достаточно один раз создать запрос в самом pgadmin и проблема решается. У Pandas совершенно другой синтаксис, и самый сложный, наверное, поэтому в начале работы с этой библиотекой возникли трудности. Сами запросы Pandas выполняет относительно быстро, но при каждом запуске он считывает scv файл по новой, из-за чего приходится долго ждать.

По времени работы, для первых трех запросов самым медленным оказался sqlite3, а для четвертого - SQLAlchemy. Самый быстрый на всех запросах был DuckDB, так как он выполняет запросы путём векторизации (ориентированной на столбцы), в то время как другие СУБД (SQLite, PostgreSQL и другие) обрабатывают каждую строку последовательно.

Графики:

1) Для маленьких данных

![image](https://github.com/rolik00/laba_3/assets/148611487/dede7e0b-38da-4045-8f73-a6908604787e)
![image](https://github.com/rolik00/laba_3/assets/148611487/c5bf8ad0-7475-4583-9aab-35b74b9c262e)

2) Для больших данных

![image](https://github.com/rolik00/laba_3/assets/148611487/c5fdc1f1-0ecb-407e-8c45-11173e1e98f2)
![image](https://github.com/rolik00/laba_3/assets/148611487/fad3e2bb-01e7-4a40-93cb-76cc4de61d01)
