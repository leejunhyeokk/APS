## GROUP BY

### 고양이와 개는 몇 마리 있을까

```sql
select ANIMAL_TYPE, count(ANIMAL_TYPE)
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE;
```



### 동명 동물 수 찾기

```sql
select NAME, count(NAME)
from ANIMAL_INS
group by NAME
having count(NAME) > 1
order by NAME;
```



### 입양 시각 구하기(1)

```
select hour(DATETIME) as hour, count(DATETIME)
from ANIMAL_OUTS
group by hour
having hour > 8 and hour < 20
order by hour;
```

