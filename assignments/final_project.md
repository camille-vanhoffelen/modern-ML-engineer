# Final Project

In this final project, you will put into practice everything you have learned so far in this course. You will experimentally develop solutions to a machine learning task. The project is structured like a real data science project, and consists of two parts:

- a python notebook experimental report
- a live presentation

## Experimental Report

**Credits: 30%**
**Due: 10/07/2020 at noon**

This is a report like those data scientists make to share their experimental progress. It tests your ability to design, carry out, and communicate machine learning experiments.

### Tasks 

**_links to the datasets will be added asap_**

Pick **one** task to investigate in your final project:

**Task A**
This is a classification task. Predict if a person's income is greater than 50k $, using tabular data.
label: `income`
[dataset url](https://introduction-to-machine-learning-ilia-university.s3.eu-west-2.amazonaws.com/final_project/census_income.csv)

**Task B**
This is a regression task. Predict a person's medical insurance costs, using tabular data.
label: `charges`
[dataset url](https://introduction-to-machine-learning-ilia-university.s3.eu-west-2.amazonaws.com/final_project/medical_insurance.csv)

**Task C**
This is a classification task. Predict pneumonia, using chest x-ray images.
label: `normal` vs `pneumonia`
[dataset url](https://introduction-to-machine-learning-ilia-university.s3.eu-west-2.amazonaws.com/final_project/chest_xray.tar.gz)

Feel free to choose your own dataset + task, as long as it wasn't used in the course before. Please consult me before doing so, to check if the choice is a good fit for this project size.

### Format

The report is a runnable python notebook, intended for a local jupyter server, or Google colab. It has both code and text cells ([here's](https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb) a refresher on notebook formatting). The notebook should be organized in five sections:

**Introduction:**

- Describe the task you're trying to solve, and the goal of the experiments.
- List the prerequesites and special installation instructions for the notebook. Please use `pipenv` as package manager, and list all required dependencies in a `Pipfile`.  
_e.g: Google colab GPU required, special libraries added to the Pipfile, ..._

**Data exploration:**

- Explore the dataset
- Communicate key insights
- Relate these observations to the main task

**Data munging:**

- Outline, explain, and justify the data cleaning and preprocessing steps  
_e.g: feature selection, variable manipulation, removing data points, feature scaling methods, formatting ..._
- Preprocess the dataset to turn it into machine learning consummable features & labels

**Experiments:**

The experiments should aim to compare candidates which tackle the main task. At least some of these candidates must be machine learning algorithms.

- Outline, explain, and justify the experimental protocol. The experimental protocol should describe the steps which compare solution candidates. It can be broken down in one or several "rounds", and should roughly mirror your actual experimental investigations.  
_e.g of a 3 round experimental outline: To solve this regression task, we compared linear regression, random forests, and neural network models. We then picked the most promising model, and searched for its optimal hyperparameters. Finally, we studied the effect of training dataset size on the accuracy of the best candidate._
- Carry out the experimental protocol by training and evaluating candidates.


**Analysis & Discussion:**

- Analyse the results. The results must be compared quantitatively and qualitatively. Data visualization is key to communicate these findings. Describe the main patterns, but also formulate hypotheses on _how_, and _why_. Even better, find quantitative or experimental ways to validate these hypotheses.
- Discuss ways in which this work could be continued. What questions are left unanswered? How would you further improve the accuracy or performance of the model(s)?
- Discuss the ethical significance of this task in its greater context. What would be the positive and/or negative impacts of these machine learning solutions, if they were integrated in a product?  
_e.g: possible effects on society, environment, health, privacy, economy..._

**Conclusion:**

- Summarize what the experiments set out to achieve, and the report's key findings.

### Grading Scheme

**Experimental design (10 points)**

- Is the data exploration effective and insightful?
- Is the dataset preprocessed correctly?
- Are the machine learning algorithms a good fit for this task?
- Do the design choices show a thorough understanding of the techniques used?
- How complex & ambitious are the experiments?
- How creative are the experiments?

**Code quality (10 points)**

- Does the notebook run without errors? 
- Does the Pipfile contain all the notebook dependencies?
- Are the correct libraries and apis used?
- Is the code clean and legible?
- Is the code fast?

**Analysis (10 points)**

- Does the data exploration section show good data literacy?
- Are experimental design choices explained and justified?
- Are the results effectively communicated?
- Does the analysis go beyond a simple quantitative comparison?
- Does the discussion place this research in its greater context, and comment on its implications?
- Does the discussion propose future research directions?
- Does the report form a coherent investigation from start to finish?

**Project size**

Three and a half weeks isn't enough to get published in [NeurIPS](https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems) or win a [Kaggle](https://www.kaggle.com/) competition. However, the experiments are expected to compare _at least_ three solutions, and the analysis should go beyond surface comparison of the results. 

A good project can choose to focus more on the experiments or the analysis. What will be rewarded is putting analytical efforts into creating interesting insights, and showing a good understanding and mastery of machine learning techniques.

### Submission

Notebooks and their Pipfile should be sent by email. If a custom task was chosen, please also provide a link to the dataset.

### Late Submissions

Please be punctual. Submissions up to 24h late will see their grade penalized by 20%. Submissions more than 24 hours late will not be accepted.

### Plagiarism

Plagiarim is **not acceptable**, and the notebooks will be checked for it. Visiting forums/blogs/documentation for inspiration or to learn new techniques is strongly encouraged. Discussing with classmates can also boost creativity, or help debug code. However, it is not acceptable to copy-paste an entire analysis or experimental protocol for your dataset or a similar task. There is a big practical and ethical difference between inspiration and plagiarism, so please make sure that the code, the results, and the analysis are your own :).

### Pro-tips

**Time management**

Please start this project early, and spread the workload. Machine learning experiments take time to design, time to run, time to debug, and time to analyze. A good report will require polishing and will be difficult to rush a single week-end. 

**Redaction**

The way you carry out the experiments is up to you: you could do everything in python scripts and then migrate to a notebook, or you could write the final report including text cells step by step from the start.

I recommend a compromise however: first coding/debugging your experiments inside a notebook within the sections listed in "Format" above, and once everything runs smooth, turning to the detailed analysis and elaborating on the text cells. This prevents you from having to migrate all your code, but still gives you coding speed and flexibility. Working this way is one of the reasons data scientists love python notebooks!

**Inspiration**

- [Stackoverflow](https://stackoverflow.com/) is an eternal life-savior for debugging code
- [Kaggle kernels](https://www.kaggle.com/notebooks) are examples of data science reports. Please keep in mind that not all of them are good, or follow the criteria of this project.
- There are many insightful and helpful blog posts about data science, but also many misleading and outdated ones. Please stay aware of their ratings/comments/support and publishing date.


## Presentation

**Credits: 30%**
**Due: week of 13/07**

**_More details will be added asap_**


This is a short presentation like those data scientists are expected to make to summarize their experimental results. It tests the ability of the student to communicate, synthesize, and discuss machine learning experiments.
