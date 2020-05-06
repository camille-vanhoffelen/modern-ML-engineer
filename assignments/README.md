

# Assignment Guidelines

## 1. Format

For each assignment, you will be given a jupyter notebook that you are expected to **fill in** and **submit**. The notebooks will contain three types of cells:  

* instructions and background information in the form of text cells
* working code cells to set up the exercises
* empty or partial code cells you are expected to complete 

The latter will always be clearly marked with `# INSERT YOUR CODE HERE` comments. You are also encouraged to add new code or text cells, or anything that accomplishes the tasks and/or answers the questions. 

## 2. Submission

Please send the completed jupyter notebook file (`.ipynb`) as an email attachment to the teacher before the dealine.

## 3. Grading Scheme


Unless otherwise stated, each task counts for 1 point.  

For :brain: **:written questions**, 1 point will be given for a comprehensive answer, 1/2 for a partial answer, and 0 for a wrong answer.  

For :muscle: **coding tasks**, a 1/2 point will be given to code that successfully accomplishes the task, and a 1/2 point is reserved for code quality. Code quality includes using the correct methods, following api "best practices", efficiency, clarity, and comments. This does means that you may get 1/2 point for broken code, if the attempt is coherent, and commented or self-explanatory.

Where applicable, **unit tests** will be provided underneath the incomplete code cells to help you validate your work. **Warning: The unit tests are not used for grading**. The behaviour of your code will be manually assessed. Code that passes a unit test is not necessarily accomplishing the task correctly, so please check and debug your code thoroughly. However , failing the unit tests is a strong indication that you should fix your code, and passing the unit tests is a good sign that your code is working as expected.

**Bonus** tasks and questions are for an additional 1/2 point, and are not mandatory. They will be added to the score, although an assignment cannot score more than the maximal grade.

## 4. Late Submissions

### Assignments 1-4

Assignments are given on Mondays, and you have two weeks to complete them. i.e the deadline is on **Monday at midday, two weeks after the assignments are handed out**. Late assignments will be given a grade penalty of **10% per 24h**, up until the Friday of deadline week at midday, after which assignments will not be accepted.

Each student gets one late submission "joker" for the whole course. This joker allows you to hand in one of the first four assignments late without point deductions (not the final project). The joker extension is up to the Friday of the same week, at midday, after which assignments will not be accepted. Using a "joker" does not move back the deadline of the next assignment. 

### Final Project

The final project will start on the 01/06/2020, and you will be given 4 weeks to complete it.

## 5. Tips

#### Final check

When graded, the notebooks will be run cell by cell from top to bottom. Therefore it's a good idea to do a "final check" before submission, by [restarting the kernel](#Restarting-the-kernel) and running all cells in order. All unit tests should pass! 

#### Restarting the kernel

Jupyter notebooks share variables between cells. This means that outputs are dependent on the _order_ in which the cells were executed. Keep this in mind if you ever backtrack during your assigment, a unit test might be failing solely because of code run _after_ the cell in question! If in doubt, you can restart the [kernel](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html#kernel) by selecting `Kernel>Restart` in the notebook menu. This will clear all state in the notebook (but keep cell contents), and start fresh.

#### Saving your work

When programming, it is very easy to lose a change, or to accidentally break working code. Whilst jupyter notebooks support basic "undo" features, you might want to backup your assignments as you complete them. You can do this by simply copying the notebook with `File>Make a Copy...` in the menu. If you are comfortable with [git](https://git-scm.com/), you can also create a new branch, and commit your changes there. Careful if you commit to the master branch, you might have conflicts next time you pull the repository.

#### Difficulty

Assignments 1-4 test variations of what was already covered in class, and are not intended to be extremely difficult. If you are stuck, please consider revisiting one of the previous lecture notebooks!

#### Time management

This is a _hands on_ course, meaning tests and theoretical exams are replaced with coding homework and projects. Completeling these assignments requires practical skills as well as knowledge, and as such, it is a pretty bad idea to start them at the last minute. The best way to distribute the workload more evenly is to keep up to date with the lectures. It is important to watch/read the content to understand the concepts, but also to play with the notebooks to feel comfortable with the python libraries and their apis. This will ensure that you already have all the necessary competences before starting the homework.

#### Jupyter Notebook Tutorial

If you need a refresher on jupyter notebooks, check out this [tutorial notebook](https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb), or the [documentation](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).
