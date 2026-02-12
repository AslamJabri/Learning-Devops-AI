What is GitHub Actions?
    It is a workflow automation service by github.We can store code on github and we can create the workflow in github action for automation.
    It is a CI/CD process for automating app development and deployment.
    In CI code changes are automatically built tested and merged with existing code
    In cd After integration , new ap or package versions are published automatically.
    It also help with automating code reviews and issue management etc.

What is git?
    It is a free version control system where we manage source code changes. which allow us to create snapshots (commits), work on alternative code versions (branches) and move between branches and commits (checkout).
    With git you can easily roll back to older code snapshots or develop new features without breaking the production code.

What is Github?
    A cloud Git repository and services provider. We can push pull to repos and make it public or private for management and more. It also helps in code management and collabrative development via issues, projects (pull requests and more).

first thing after installing the git is to set the global username and email
    git config --global user.name "Your Name"
    git config --global user.email "yourname@example.com"
    git config --list "This will give you the list of the repo"
    
git stores all the config 
    (directory) ~/.gitconfig

## Commands

git init - for initilizing the local git 
git add . - this will stage the files for next commit
git commit -m - this will create a commit that includes all staged changes it also takes a message which we can add with commit
git status - will give you the status of staged files and ready to commit
git log  - this will give all the logs
(HEAD -> main) - the main is the branch and which state is currently loaded thats where the HEAD will be pointing on the commit.
git checkout <commit-id> - This will take us to the old version of the project
git checkout main - this will get back to the latest commit.
git revert <id> - revert changes of commit by creating a new commit. It wont delete the previous commit but adds new commit.
git reset --hard <id> - when we want to delete the commit we use this command.We will lose all the changes happend in that commit. Use it with care.

git branch <branch name> - creating the branch
git merge <branch name>> - merge the branch
git branch - will view all the branches
git checkout <branchname> - move to another branch
git branch -D <branch name> - delete the branch
git checkout -b <branchname> - create and get into that branch

git merge <branch name> - this will merge with the branch