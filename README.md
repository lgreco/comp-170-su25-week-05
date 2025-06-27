
# COMP 170 SU25 WEEK 05

This assignment has **THREE** parts: a **midterm review part,** a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.


## MIDTERM REVIEW

*Ungrading* is an assessment technique that measures learning and professional development. Learning is assessed by how you learn from your mistakes. Professional development is assessed by your overall engagement with the course.

Looking at the first five assignments, discuss how you learned from any mistakes you made. Repeating mistakes is a sign that your learning needs to be improved. If you have repeated mistakes, discuss how you learning will be improved in the second half of the course. Typical mistakes for this discussion include:
* code that doesn't execute (even in one assignment);
* lack of comments;
* Missed assignments (even when due to not committing/synchronizing your CodeSpaces);

Looking at your course engagement over the first six weeks, discuss how you've managed so far. The ideal standard is that you treat the course as a job that you like, that you wish to keep, and in which you aspire to grow and be promoted. Factors to consider include:
* Timeliness -- joining the class meeting on time
* Consistency -- not missing classes (except for university-justified absences)
* Participation -- asking questions, answering questions
* Proactiveness -- each out to the instructor with any difficulties you encounter, in a way that allows a timely resolution
* Initiative -- trying additiona problems from the book and discussing them with the instructor; learning something new, like writing your reflections in MarkDown.
* Commitment: studying/working on the course for ~3 hours per hour class-hour, i.e., 9 hours per week in addition to coming to class.

Your discussion for the above should be in the form of a well-written essay, 200-300 words. You may include it in your week05 assignemnt as `midterm_review.md`.


## Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.

## Code

This assignment has TBD tasks. Write your code in file `week05.py`. The file comes with a bit of testing code. Do not modify the testing code. Write your methods *above* the testing code. If your methods are correct, running the testing code will show that you passed the tests. In addition to correct logic, your methods must have **one and only one** return statement each. Useful comments are required.


### Find the longest word
Write a method with header
```python
def longest_word(words: list[str]) -> str:
```
that returns the longest word (that is the longest string) in list `words`.


### Find the shortest word
Write a method with header
```python
def shortest_word(words: list[str]) -> str:
```
that returns the shortest word (that is the longest string) in list `words`.


### Find odd words
Write a method with header
```python
def odd_words(words: list[str]) -> list[str]:
```
that returns a list with all the strings in list `words` whose length is an odd number.


### Find average words
Write a method with header
```python
def average_words(words: list[str]) -> list[str]:
```
that returns a list with all the strings in `words` whose length is $\pm 1$ from the average length of all strings in `words`.


### Find an intersection
Write a method with header
```python
def intersect(foo: list[str], bar: list[str]) -> bool:
```
that returns `True` if lists `foo` and `bar` have at least one element in common, anf `False` otherwise. 

## Reflect

Review the posted [solutions from the previous assignment](./solutions_week04.py). Compare the posted solutions with your solutions. Notice the differences between your code and the solutions code and describe them. Trivial differences like the names of variables are not that important.

### Frequent mistakes expected at this point

* **Code has no comments** to demonstrate mastery of the program.

* **Code does not produce correct outputs** because it was not tested after completed.

* **Code uses excessive logic** which may be the sign of AI-generated programs.

* **Code does not include type hints (annotations).** This is also typical with solutions found online or are AI-generated.


### Read more about:

* [Type hints in Python](https://docs.python.org/3/library/typing.html); also useful [cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#functions)
* [f-strings in Python](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
* [lists in Python](https://docs.python.org/3/tutorial/datastructures.html). Also chapters 7.1 and 7.2 of the textbook.
* [the for statement](https://docs.python.org/3/reference/compound_stmts.html#for) and [for loop over a list in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements). Also chapter 2.3 and 7.1 of the textbook.
