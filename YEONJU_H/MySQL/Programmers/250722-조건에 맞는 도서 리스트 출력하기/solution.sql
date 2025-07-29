-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021 AND CATEGORY = '인문';

-- YEAR(PUBLISHED_DATE) = 2021은 함수를 사용해서 인덱스를 타지 못할 수 있고 한다. (성능저하) 따라서, 아래 방법을 더 추천
-- PUBLISHED_DATE >= '2021-01-01' AND PUBLISHED_DATE < '2022-01-01'
-- # 성능 차이 예시:
-- 100만 건 테이블에서
-- 함수 사용: 100만 건 모두 스캔 (Full Table Scan)
-- 범위 조건: 2021년 데이터만 스캔 (Index Range Scan)
