-- 코드를 입력하세요
SELECT FLAVOR 
from first_half-- 상반기 주문 정보를 담은 테이블
order by total_order desc , shipment_id;