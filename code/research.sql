select
(SElECT avg(counts) from (SELECT count(*) counts FROM github.issue group by repository_id) as avg_issues) as avg_issues,
(SElECT avg(commits) from (SELECT count(*) commits FROM github.commit group by repository_id) as avg_commits) as avg_commits,
(SELECT std(issues) from (SELECT count(*) as issues FROM github.issue group by repository_id) as std_issues) as std_issues,
(SELECT std(commits) from (SELECT count(*) as commits FROM github.commit group by repository_id) as std_commit) as std_commits
