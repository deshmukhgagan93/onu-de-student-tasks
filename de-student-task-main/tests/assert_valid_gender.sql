-- This test checks if the gender of students is Male or Female. Is there a better way to write this test?
SELECT
    gender
FROM
    students
WHERE
    gender NOT IN ('Male', 'Female')
LIMIT 1

