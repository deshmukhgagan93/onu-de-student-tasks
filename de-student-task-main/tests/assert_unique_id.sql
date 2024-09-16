-- Test to check if student ids are unique 
SELECT
    student_id
FROM
    {{ ref('students') }}
GROUP BY
    student_id
HAVING
    COUNT(*) > 1
LIMIT 1
