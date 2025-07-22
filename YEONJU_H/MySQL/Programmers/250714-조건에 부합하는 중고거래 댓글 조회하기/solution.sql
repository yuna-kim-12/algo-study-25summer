-- 코드를 입력하세요
-- 2022년 10월 작성 게시물 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일 조회 / 댓글 작성일 기준 오름차순 정렬, 같을 경우 게시글 제목 기준 오름차순

SELECT b.TITLE, r.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d')
FROM USED_GOODS_BOARD b, USED_GOODS_REPLY r
WHERE b.BOARD_ID = r.BOARD_ID AND b.CREATED_DATE >= '2022-10-01' AND b.CREATED_DATE <= '2022-10-31'
ORDER BY r.CREATED_DATE, b.TITLE ;

-- DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d')을 사용하지 않아서 틀렸었음

