# 현 대장균의 유전형질을 부모의 형질을 모두 가지고 있는지 체크하면 된다.
# 처음에 틀렸던 이유가 a.GENOTYPE & b.GENOTYPE = b.GENOTYPE 이 조건을 틀려서였음 => SQL에서 & 연산을 활용하면 굳이 이진법 변환 연산 불필요하다.
# 또한, GENOTYPE 자체가 해당 이진수 자리의 형질이 있냐없냐를 의미하므로, 연쇄적으로 역행하며 부모 형질을 체크할 필요 없다.
SELECT a.ID, a.GENOTYPE, b.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA a, ECOLI_DATA b
WHERE a.PARENT_ID = b.ID AND a.PARENT_ID IS NOT NULL AND a.GENOTYPE & b.GENOTYPE = b.GENOTYPE
ORDER BY a.ID;