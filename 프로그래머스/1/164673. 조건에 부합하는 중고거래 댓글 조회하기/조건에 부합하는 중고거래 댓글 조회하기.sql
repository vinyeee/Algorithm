-- 코드를 입력하세요
SELECT ub.title, ub.board_id, ur.reply_id, ur.writer_id, ur.contents, date_format(ur.created_date,'%Y-%m-%d') as created_date
from used_goods_board ub join used_goods_reply ur
on ub.board_id = ur.board_id
where year(ub.created_date) = 2022 and month(ub.created_date) = 10
order by ur.created_date , ub.title;