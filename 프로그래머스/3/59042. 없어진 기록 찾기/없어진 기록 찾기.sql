-- 코드를 입력하세요
SELECT aout.animal_id, aout.name
from animal_ins ain 
right join animal_outs aout
on ain.animal_id = aout.animal_id
where aout.datetime is not null and ain.datetime is null
order by animal_id;
