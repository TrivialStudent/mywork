# Git/GitHub Intro for Student Pairs (SSH Setup)

This guide will walk you through the Git/GitHub workflow for working with a partner on a project.  

***You already have:***

* A GitHub account  
* SSH keys set up  
* Git installed on your computer  

---

## Lesson 1: Repository Setup

1. One partner creates a **new repository** on GitHub website. 
 
   1. Name it (for example `cool-project`)  
   2. Initialize with a `README.md`  
   3. Leave it public 

2. Add the other partner as a collaborator:  
   *Settings → Collaborators → Add*  

3. Copy the **SSH clone link**.

---

## Lesson 2: Clone the Repo (SSH)

Each partner gets the repo on their computer:

```bash
git clone git@github.com:username/cool-project.git
cd cool-project
```

## Lesson 3: Git Basics

- Check what is going on

```bash
git status    # Check what is going on with your changes you've worked on
```

- Stage Files(Tell Git what to save from your changes)

```bash
git add src/modules/file_name.py # Stage a specific file
git add .                        # Stage all changes from root directory
```
- Commit Files (make a snapshot)

```bash
git commit -m 'Explain changes in this comment'
```

## Lesson 4: Branching

To avoid breaking each other's work, use branches

- Create a new branch and switch to it in working directory

```bash
git checkout -b yourname-feature # yourname-feature is example name for branch
```
- View list of branches available

```bash
git branch
```
- Switch between branches

```bash
git checkout main
git checkout yourname-feature
```
- To do your first push to a new branch

```bash
git push -u origin yourname-feature
```

## Lesson 5: Moving Changes Between Local and Github

-  Get the latest changes from Github

```bash
git pull origin main  # Grab all changes from main branch repo (Partner's changes)
```

- Send your commits to github

```bash
git push origin branch-name # Push working branch up to github for PR
```

## Lesson 6: Pull Requests
Log into https://github.com

1. When finished with branch work and branch has been pushed click `New Pull Request`
2. Base Branch = `main`, compare branch = `yourname-feature`
3. Your partner reviews and approves of any changes by revising yourname-feature branch
4. Merge into `main` branch  

---

# Student Workflow

### Clone the repo once  

```bash
git clone git@github.com:username/cool-project.git
cd cool-project
```

### Each day or feature workflow

1. Grab any recent changes from `main`
```bash
git checkout main
git pull origin main
```

2. Make a branch for your task

```bash
git checkout -b yourname-task
```
3. Do your coding, then stage and commit your changes:

```bash
git add .
git commit -m "Describe your changes"
```

4. Push your branch

```bash
git push -u origin yourname-task
```

5. Open a Pull Request on GitHub and have your partner review it
   - Merge to main only after review
  
6. Switch back to main and pull latest changes to make sure main branch is up to date

```bash
git checkout main
git pull origin main
```