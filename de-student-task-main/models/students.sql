-- Just selects the raw 'student_data' seed data.
select 
    student_id,
    name,
    age,
    gender,
    major,
    minor,
    year_of_university,
    test_score_math,
    test_score_science,
    test_score_english,
    birthday,
    city_of_birth,
    state_of_birth
from 
    {{ ref('student_data') }}
