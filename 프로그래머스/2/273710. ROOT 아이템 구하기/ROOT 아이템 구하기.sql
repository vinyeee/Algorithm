-- 코드를 작성해주세요

select item_info.item_id, item_info.item_name 
from item_info item_info join item_tree item_tree
on item_info.item_id = item_tree.item_id
where item_tree.parent_item_id is null;
