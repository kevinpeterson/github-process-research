select 
    'Issues' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        github.issue
    group by repository_id) as issues 
union select 
    'Commits' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        github.commit
    group by repository_id) as commits 
union select 
    'Closed Issues' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        github.issue issues
    where
        issues.close_date is not null
    group by repository_id) as closed_issues 
union select 
    'Open Issues' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        github.issue issues
    where
        issues.close_date is null
    group by repository_id) as open_issues 
union select 
    'Average Issue Close Time Per Project' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        avg(DATEDIFF(close_date, open_date)) as counts
    from
        github.issue issues
    where
        issues.close_date is not null
    group by repository_id) issues 
union select 
    'Issue Creators' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(distinct creator) as counts
    from
        github.issue
    group by repository_id) as distinct_issue_creators 
union select 
    'Committers' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(distinct committer) as counts
    from
        github.commit
    group by repository_id) as distinct_committers

