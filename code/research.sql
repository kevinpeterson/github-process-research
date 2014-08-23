##############################################################
# research.sql
#
# SQL analytical queries used to analyze data from the data gathering process.
#
# License: MIT 2014 Kevin Peterson
##############################################################
select 
    'Issues' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        issue
    group by repository_id) as issues 
union select 
    'Commits' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        commit
    group by repository_id) as commits 
union select 
    'Closed Issues' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        issue issues
    where
        issues.close_date is not null
    group by repository_id) as closed_issues 
union select 
    'Open Issues' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(*) counts
    from
        issue issues
    where
        issues.close_date is null
    group by repository_id) as open_issues 
union select 
    'Issue Close Time' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        avg(DATEDIFF(close_date, open_date)) as counts
    from
        issue issues
    where
        issues.close_date is not null
    group by repository_id) issues 
union select 
    'Issue Reporters' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(distinct creator) as counts
    from
        issue
    group by repository_id) as distinct_issue_creators 
union select 
    'Committers' as var, avg(counts), min(counts), max(counts), std(counts)
from
    (select 
        count(distinct committer) as counts
    from
        commit
    group by repository_id) as distinct_committers

