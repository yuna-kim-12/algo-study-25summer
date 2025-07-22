-- 코드를 입력하세요
# 첫 코드
# SELECT p.PRODUCT_CODE, SUM(p.PRICE * s.SALES_AMOUNT) OVER (PARTITION BY PRODUCT_CODE) AS SALES
# FROM PRODUCT p, OFFLINE_SALE s
# WHERE p.PRODUCT_ID = s.PRODUCT_ID
# GROUP BY PRODUCT_CODE

SELECT p.PRODUCT_CODE, SUM(p.PRICE * s.SALES_AMOUNT) AS SALES
FROM PRODUCT p, OFFLINE_SALE s
WHERE p.PRODUCT_ID = s.PRODUCT_ID
GROUP BY p.PRODUCT_CODE
ORDER BY SALES DESC, p.PRODUCT_CODE ASC;

# partition 함수와 GROUP BY 함수 개념 정리
# GROUP BY 사용:
# 그룹별 요약 정보만 필요할 때
# "상품코드별 총 매출액만 보고 싶다"
# 행이 줄어듦 (요약)

# PARTITION BY 사용:
# 개별 행 정보 + 그룹 통계를 함께 보고 싶을 때
# "각 판매 내역과 함께 해당 상품의 전체 매출액도 보고 싶다"
# 순위 매기기 (ROW_NUMBER(), RANK() 등)
# 행이 그대로 (개별 + 통계)