-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서
-- 완료된 중고 거래의 총금액이 70만 원 이상인 사람의
-- 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성
-- 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.


SELECT u.user_id, u.nickname, sum(price) as total_sales
from USED_GOODS_BOARD b
join USED_GOODS_USER u on b.WRITER_ID = u.user_id
where status = 'DONE'
group by u.user_id, u.nickname
having sum(price) >= 700000
order by total_sales;