SELECT
    tariff,
    mfn
FROM
    tphs
WHERE
    tariff LIKE '3926%' AND mfn NOT NULL
ORDER BY
    tariff;