-- ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 정렬해 주세요.
-- join해서 parent_item_id가 null 인 값을 찾고, 그 아이템 명을 출력
SELECT II.ITEM_ID, II.ITEM_NAME
FROM ITEM_INFO II
JOIN ITEM_TREE IT ON II.ITEM_ID = IT.ITEM_ID
WHERE IT.PARENT_ITEM_ID IS NULL
ORDER BY II.ITEM_ID;