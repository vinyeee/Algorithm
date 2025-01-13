-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, 
    case 
        when freezer_yn is null then 'N'
        else freezer_yn
    end as freezer_yn
from FOOD_WAREHOUSE
where warehouse_name Like '%경기%'
order by warehouse_id