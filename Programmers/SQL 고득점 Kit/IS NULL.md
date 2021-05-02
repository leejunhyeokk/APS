## IS NULL

### 이름이 없는 동물의 아이디

```sql
select ANIMAL_ID 
from ANIMAL_INS 
where NAME IS NULL
```



### 이름이 있는 동물의 아이디

```sql
select ANIMAL_ID
from ANIMAL_INS
where NAME IS NOT NULL;
```



### NULL 처리하기

```sql
select ANIMAL_TYPE, IFNULL(NAME,'No name'), SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID;
```



