-- 코드를 입력하세요
-- 네비게이션 옵션이 포함된 자동차리스트를 출력
-- 자동차 ID 를 기준으로 내림차순 

SELECT *
from car_rental_company_car
where options like '%네비게이션%'
order by car_id desc