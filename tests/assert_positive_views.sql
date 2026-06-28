
SELECT *
FROM {{ ref('fct_messages') }}
WHERE views < 0
