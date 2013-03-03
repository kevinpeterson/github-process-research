from plotter import Histograph

committers_query = '''select count(distinct committer) from github.commit c group by repository_id'''
committers_histogram = Histograph(committers_query, "Committers", "Repositories", (1,25))
committers_histogram.plot("committers_histogram")

issue_reporters_query = '''select count(distinct creator) from github.issue group by repository_id'''
issue_reporters_histogram = Histograph(issue_reporters_query, "Issue Reporters", "Repositories")
issue_reporters_histogram.plot("issue_reporters_histogram")