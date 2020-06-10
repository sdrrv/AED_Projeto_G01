from invoke import task
import re

@task
def test(c):
    c.run("coverage run -m unittest discover")

@task(test)
def cov(c):
    c.run("coverage report")
    #c.run("coverage html")

@task
def merge(c,branch):
    c.run("git checkout master")
    c.run("git pull")
    c.run("git checkout "+branch)
    c.run("git merge master")
    c.run("git checkout "+branch)
    c.run("git push")
@task
def push(c,branch):
    sure= input("Are you sure you want to push to master?(y/n): ")
    if sure=="y":
        c.run("git checkout "+branch)
        c.run("git push")
        c.run("git checkout master")
        c.run("git merge "+branch)
        c.run("git push")
        c.run("git checkout "+branch)
    else:
        exit()
