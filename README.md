## The GitHub Open Source Development Process

### Abstract
Open Source Software (OSS) has produced many successful projects. The development process by which these projects are produced is generally unstructured compared to commercial software -- but a definite pattern does arrive, and is no less a pattern. GitHub, a popular OSS code hosting website, and Git, the site's Source Code Management (SCM) tool of choice, may have the potential to fundamentally change ths process.
By analyzing a subset of GitHub repositories, this report will show how GitHub has influenced some very intrinsic aspects of traditional OSS develoment, such as developer hierarchies and issue close velicity. We find that many of the traditional aspects of OSS development remain, such most project developlment is done by a small group of core developers. Others assumptions about project hierarchy, such as a large number of Issue Reporters compared to Committers, seems unsupported by the data.

### Project Structure
The project is divided into two sections. The first section is a collection of [Python and SQL code](code/) used to gather and analyze GitHub repository data. The second section is the [LaTeX-based manuscript](paper/) where the results are presented and discussed. The resulting manuscript is also available as a [PDF download](http://kevinp.me/github-process-research/github-process-research.pdf).

### Reproduce the Experiment
___First___ make sure to familiarize yourself with the [code](code/) and [LaTeX](paper/) sections, noting all prerequisites and software installation/configuration needed.

####  Steps to Reproduce
##### 1. Gather Data
From the ```code/``` directory, execute:

    python research.py
__Note:__ This may take several hours, depending on desired sample size

##### 2. Analyze the Results

When complete, generate the data summary analytics table by executing:

    python get_summary_data.py > ../paper/summary_statistics.tex
Finally, generate the data plots by executing:

    python plots.py
This will generate images and output them to the ```paper/images/``` directory.

##### 3. Build the Manuscript
Now, all necessary tables and images should be generated. The next step is to generate the manuscript. From the ```paper/``` directory, execute:

    ./publish.sh

If you've contributed novel research to the manuscript, don't forget to add your name! You can do this by adding another author on the top of ```main.tex```.
