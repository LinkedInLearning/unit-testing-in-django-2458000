# Unit Testing in Django
This is the repository for the LinkedIn Learning course Unit Testing in Django. The full course is available from [LinkedIn Learning][lil-course-url].

![Unit Testing in Django][lil-thumbnail-url] 

Tests are at the heart of modern software development, and testing is a skill that should be as basic as building the applications. In this course, Leticia Portella uses an untested Django application to teach you about the tools and good practices of writing tests. Learn about Pytest, one of the most known and complete testing frameworks in Python. Explore how you can use Pytest to test a Django application, from building your first unit tests to learning how to think about what makes a good test. Review several tests you can run with Pytest and Django, including testing a GET endpoint and testing behavior when a user is authenticated. Walk through the layers of security that Pytest adds to protect you from accidents. Find out how being lazy while writing tests can be leveraged to write better tests faster. Finally, discover how to quickly create instances and use tools to avoid rewriting code. This is the ideal course to follow Leticia’s first course, Django Essential Training.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

Leticia Portella 
                            
Software Engineer

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/leticia-portella).

[lil-course-url]: https://www.linkedin.com/learning/unit-testing-in-django
[lil-thumbnail-url]: https://cdn.lynda.com/course/2458000/2458000-1657572268933-16x9.jpg
