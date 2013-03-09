from plotter import Histograph, ScatterPlot, PieChart

committers_query = '''select count(distinct committer) from commit c group by repository_id'''
committers_histogram = Histograph(committers_query, "Committers", "Repositories", (1,25))
committers_histogram.plot("committers_histogram")

committers_percentage_query = '''
select 
	cast(cast( (count(*) / commits.cnt ) as decimal(2,2)) * 100 as unsigned integer)
from
    (select 
        count(*) as cnt, c1.repository_id
    from
        commit c1
    group by c1.repository_id) commits
        inner join
    commit c1 ON c1.repository_id = commits.repository_id
group by c1.repository_id , c1.committer
'''
committers_percentage_histogram = Histograph(committers_percentage_query, "% Of Project Commits", "Committers")
committers_percentage_histogram.plot("committers_percentage_histogram")

issue_reporters_query = '''select count(distinct creator) from issue group by repository_id'''
issue_reporters_histogram = Histograph(issue_reporters_query, "Issue Reporters", "Repositories", (1,40))
issue_reporters_histogram.plot("issue_reporters_histogram")

issue_close_time_query = '''
select cast(avg(datediff(close_date, open_date)) as unsigned) FROM issue issues 
where issues.close_date is not null 
group by repository_id
'''
issue_close_time_histogram = Histograph(issue_close_time_query, "Average Issue Close Time (Days)", "Repositories", (0,140))
issue_close_time_histogram.plot("issue_close_time_histogram")

watcher_forks_scatterplot_query = '''select watchers, forks from repository'''
watcher_forks_scatterplot = ScatterPlot(watcher_forks_scatterplot_query, "Watchers", "Forks", (0,1000), (0,150))
print watcher_forks_scatterplot.plot("watcher_forks_scatterplot")

issue_reporters_committers_query = '''
select 
    issues.reporters_count, commits.committers_count
from
    (select 
        repository_id, count(distinct committer) as committers_count
    from
        commit
    group by repository_id) commits
        inner join
    (select 
        repository_id, count(distinct creator) as reporters_count
    FROM
        issue
    group by repository_id) issues ON issues.repository_id = commits.repository_id
'''
issue_reporters_committers_scatterplot = ScatterPlot(issue_reporters_committers_query, "Committers", "Issue Reoprters", (0,140), (0,140))
print issue_reporters_committers_scatterplot.plot("issue_reporters_committers_scatterplot")

issue_close_time_forks_query = '''
select 
    cast(issues.close_time as unsigned), repository.forks
from
    repository repository
        inner join
    (select 
        avg(DATEDIFF(close_date, open_date)) as close_time,
            repository_id
    from
        issue issue
    where
        issue.close_date is not null
    group by repository_id) issues ON repository.id = issues.repository_id
group by repository_id
'''
issue_close_time_forks_scatterplot = ScatterPlot(issue_close_time_forks_query, "Close Time", "Forks", (0,200), (0,200))
print issue_close_time_forks_scatterplot.plot("issue_close_time_forks_scatterplot")



committers_percentage_pie_chart = PieChart(committers_percentage_query)
committers_percentage_pie_chart.plot("committers_percentage_pie_chart")

