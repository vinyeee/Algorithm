-- 코드를 입력하세요
-- 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty 인 동물의
-- 아이디, 이름, 성별 , 중성화 여부

SELECT animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id