-- This test checks if the age of students is between 18 and 35. Is there a better way to write this test? 
SELECT
    age
FROM
    {{ ref('students') }}
WHERE
    age < 18 OR age > 35
LIMIT 1
