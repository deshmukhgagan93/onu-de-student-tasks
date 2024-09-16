-- Checking if all majors are included in majors dbt model
WITH expected_majors AS (
    SELECT 'Physics' AS major
    UNION ALL SELECT 'Electrical Engineering'
    UNION ALL SELECT 'Civil Engineering'
    UNION ALL SELECT 'Information Systems'
    UNION ALL SELECT 'Software Engineering'
    UNION ALL SELECT 'Biomedical Engineering'
    UNION ALL SELECT 'Computer Science'
    UNION ALL SELECT 'Aerospace Engineering'
    UNION ALL SELECT 'Environmental Engineering'
    UNION ALL SELECT 'Chemical Engineering'
    UNION ALL SELECT 'Industrial Engineering'
    UNION ALL SELECT 'Mechanical Engineering'
    UNION ALL SELECT 'Computer Engineering'
    UNION ALL SELECT 'Biochemistry'
    UNION ALL SELECT 'Statistics'
    UNION ALL SELECT 'Mathematics'
),
existing_majors AS (
    SELECT DISTINCT major
    FROM {{ ref('majors') }}
)
SELECT
    em.major
FROM
    expected_majors em
LEFT JOIN
    existing_majors ex
ON
    em.major = ex.major
WHERE
    ex.major IS NULL
