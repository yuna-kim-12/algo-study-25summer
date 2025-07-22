-- 코드를 입력하세요
# 데이터 확인용 코드
# SELECT * FROM FIRST_HALF;
# SELECT * FROM ICECREAM_INFO;


# 맛과 성분타입이 일치되지 않아 a.FLAVOR = i.FLAVOR 추가로 해결
# - 올바른 조인 조건이 성립되지 않아 카테시안 곱이 발생함
SELECT DISTINCT a.FLAVOR
FROM FIRST_HALF a, ICECREAM_INFO i
WHERE a.FLAVOR = i.FLAVOR AND a.TOTAL_ORDER > 3000 AND i.INGREDIENT_TYPE ='fruit_based'
ORDER BY a.TOTAL_ORDER DESC;