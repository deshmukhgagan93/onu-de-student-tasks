-- Transform the 'students' model so it is at the 'major' granularity.
select 
    major,                           -- Grouping by 'major'
    count(student_id) as total_students,      -- Counting the number of students in each major
    avg(extract(year from age(birthday))) as avg_student_age,  -- Average age of students in each major
    count(case when gender = 'Male' then 1 end) as total_male_students,  -- Count of male students in each major
    count(case when gender = 'Female' then 1 end) as total_female_students  -- Count of female students in each major
from
    {{ ref('students') }} 
group by 
    major
order by 
    major
