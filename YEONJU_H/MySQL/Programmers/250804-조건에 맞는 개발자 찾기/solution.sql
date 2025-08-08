-- 코드를 작성해주세요
# Python(256)이나 C# 스킬(1024)을 가진 개발자의 정보(ID, 이메일, 이름, 성을 조회)를 조회
SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS d, SKILLCODES s
# WHERE (SKILL_CODE & 256 = 256) OR (SKILL_CODE & 1024 = 1024) : 하드코딩 했더니 테케 1개 빼고 다틀림
WHERE s.NAME IN ('Python', 'C#') AND (d.SKILL_CODE & s.CODE = s.CODE)
ORDER BY ID;