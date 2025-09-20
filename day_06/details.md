# Peer Review Assignment: GitHub Workflow

## Overview

In this assignment, you will work in **pairs** to review each other’s lab work. The goal is to give constructive feedback, suggest improvements, and learn from one another’s code. All interactions will be done using **Git and GitHub**.

---

## Steps

### 1. Pair Up
- Each student should be assigned a partner.
- Decide who will **review first** and who will **receive feedback**.

~~---~~

### 2. Fork / Clone Your Partner’s Repository
1. Go to your partner’s GitHub repository.
2. **Fork** it to your own GitHub account **OR** clone it locally:
```bash
git clone https://github.com/partner-username/repo-name.git
cd repo-name
```
3. If you forked the repo, add the original repo as a remote for easier syncing:
```bash
git remote add upstream https://github.com/partner-username/repo-name.git
git fetch upstream
```

### 3. Create a New Branch for Feedback

* Always make a new branch when making changes or suggestions.
```bash
git checkout -b feedback-changes
```
* Make your changes, add comments, or improve the code.
* Commit your changes with clear messages:

```bash
git add .
git commit -m "Add suggestions for lab improvements"
```

### 4. Push and Create a Pull Request
* Push your branch to your own fork (or your partner’s repo if they allow collaboration):

```bash
git push origin feedback-changes
```

* On GitHub, create a Pull Request (PR) from feedback-changes into your partner’s main branch.
* Use the PR description to summarize your suggestions:
    * What works well
    * What could be improved
    * Specific lines or functions that could be enhanced

---

### Review and Discuss
* Your partner will review the PR and respond to comments.
* Make sure to discuss your suggestions, either through GitHub comments or in class.
* The person who receives feedback can merge approved changes into their main branch if they want.

### Tips for Effective Peer Review
* Be specific with suggestions: point out exact lines or sections.
* Focus on code clarity, organization, and correctness.
* Offer alternative solutions or approaches rather than just pointing out errors.
* Keep your tone professional and supportive.

### Submission
* After both rounds of peer review, ensure your main branch is up-to-date with merged suggestions.
* Your final repository should reflect any approved changes made during peer review.
*Notify the instructor once both rounds are complete.