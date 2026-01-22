"""#What are the git commands used to check the status of a repository and to stage changes for a commit?
from logging import log


git status
git add <file_name> or git add . (to stage all changes) 
#What command is used to commit staged changes with a message?
git commit -m "Your commit message here"
#How do you push committed changes to a remote repository?
git push origin <branch_name>
#How can you view the commit history of a repository?
#git log
#What command is used to create a new branch in Git?
git branch <new_branch_name>
#How do you switch to a different branch in Git?
git checkout <branch_name>
#What command is used to merge changes from one branch into another?
git merge <branch_name>
#How can you clone a remote repository to your local machine?
git clone <repository_url>
#What command is used to pull the latest changes from a remote repository?
git pull origin <branch_name>
#How do you discard changes in your working directory?
git checkout -- <file_name>
#or to discard all changes
git reset --hard
#What command is used to view the differences between your working directory and the last commit?
git diff
#How can you remove a file from the staging area?
git reset <file_name>
#or to unstage all files
git reset
#What command is used to delete a branch in Git?
git branch -d <branch_name>
#How do you rename a branch in Git?
git branch -m <old_branch_name> <new_branch_name>
#What command is used to view the remote repositories associated with your local repository?
git remote -v
#How can you fetch changes from a remote repository without merging them?
git fetch origin
#What command is used to stash changes in Git?
git stash
#How do you apply stashed changes back to your working directory?
git stash apply
#What command is used to view the list of stashed changes?
git stash list
#How can you drop a specific stash from the stash list?
git stash drop stash@{index}
#or to drop the latest stash
git stash pop
#How do you create a tag in Git?
git tag <tag_name>
#What command is used to push tags to a remote repository?
git push origin <tag_name>
#How can you view the details of a specific commit?
git show <commit_hash>
#What command is used to revert a commit in Git?
git revert <commit_hash>    
#How do you reset your repository to a previous commit?
git reset --hard <commit_hash>
#What command is used to configure your Git username and email?
git config --global user.name "Your Name"
git config --global user.email "
  
#IS THERE FUNCTION OF GIT COMMANDS IN PYTHON PROGRAMMING OR NOT
#NO THERE IS NO FUNCTION OF GIT COMMANDS IN PYTHON PROGRAMMING  """