## SUM, MAX, MIN

###  최댓값 구하기

```sql
select DATETIME 
from ANIMAL_INS 
order by DATETIME desc 
limit 1;
```



### 최솟값 구하기

```sql
SELECT DATETIME 
from ANIMAL_INS 
order by DATETIME    
limit 1;
```



### 동물 수 구하기

```sql
select count(ANIMAL_ID) 
from ANIMAL_INS;
```



### 중복 제거하기

```sql
SELECT count(distinct NAME) 
from ANIMAL_INS 
where NAME IS NOT NULL;
```

