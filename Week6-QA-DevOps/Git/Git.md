# Git & GitHub Hands-on

## Prerequisites

- AWS Account
- GitHub Account
- PuTTY
- PuTTYgen
- Internet Connection

---

# Task 1 - Launch EC2 Instance

- Launch Amazon Linux 2023 EC2
- Instance Type: t2.micro
- Create Key Pair (.ppk)
- Allow SSH (22)

Screenshot:
- EC2 Running

---

# Task 2 - Connect EC2 using PuTTY

Host Name

```text
ec2-user@<Public-IP>
```

Private Key

```text
git-key.ppk
```

Screenshot:
- PuTTY Connected

---

# Task 3 - Update Server

```bash
sudo yum update -y
```

Screenshot:
- Update Completed

---

# Task 4 - Install Git

```bash
sudo yum install git -y
```

Verify

```bash
git --version
```

Screenshot:
- Git Version

---

# Task 5 - Configure Git

```bash
git config --global user.name "Your Name"

git config --global user.email "yourmail@gmail.com"
```

Verify

```bash
git config --list
```

Screenshot:
- Git Config

---

# Task 6 - Create GitHub Repository

Repository Name

```text
git-practice
```

Visibility

```text
Public
```

Do NOT initialize README.

Screenshot:
- Repository Created

---

# Task 7 - Generate Personal Access Token

GitHub

Settings

Developer Settings

Personal Access Tokens

Tokens (Classic)

Generate Token

Scopes

```text
repo
workflow
```

Copy Token

---

# Task 8 - Clone Repository

```bash
git clone https://github.com/<username>/git-practice.git
```

Go inside

```bash
cd git-practice
```

Screenshot:
- Repository Cloned

---

# Task 9 - Create Files

```bash
touch README.md

mkdir Screenshots

echo "# Git Practice" > README.md
```

Verify

```bash
ls
```

Screenshot

---

# Task 10 - Git Status

```bash
git status
```

Screenshot

---

# Task 11 - Stage Files

```bash
git add .
```

Verify

```bash
git status
```

Screenshot

---

# Task 12 - Commit

```bash
git commit -m "Initial Commit"
```

Screenshot

---

# Task 13 - Push

```bash
git push origin main
```

Username

```text
GitHub Username
```

Password

```text
Personal Access Token
```

Screenshot

---

# Task 14 - Pull

```bash
git pull origin main
```

Screenshot

---

# Task 15 - Branch

Create

```bash
git checkout -b feature/login
```

Verify

```bash
git branch
```

Screenshot

---

# Task 16 - Add New File

```bash
echo "Login Page" > login.html
```

```bash
git add .
```

```bash
git commit -m "Added Login Page"
```

```bash
git push origin feature/login
```

Screenshot

---

# Task 17 - Merge

Switch

```bash
git checkout main
```

Merge

```bash
git merge feature/login
```

Push

```bash
git push
```

Screenshot

---

# Task 18 - Merge Conflict

Create Branch

```bash
git checkout -b branch1
```

Edit README

Commit

```bash
git add .
git commit -m "Branch1"
```

Switch

```bash
git checkout main
```

Create Another Branch

```bash
git checkout -b branch2
```

Edit Same Line

Commit

```bash
git add .
git commit -m "Branch2"
```

Merge

```bash
git checkout main
```

```bash
git merge branch1
```

```bash
git merge branch2
```

Resolve Conflict

```bash
git add .
```

```bash
git commit -m "Resolved Merge Conflict"
```

Screenshot

---

# Task 19 - Git Log

```bash
git log
```

Compact

```bash
git log --oneline
```

Graph

```bash
git log --graph --all
```

Screenshot

---

# Task 20 - Git Diff

```bash
git diff
```

Screenshot

---

# Task 21 - Tags

Create

```bash
git tag v1.0
```

List

```bash
git tag
```

Push

```bash
git push origin v1.0
```

Screenshot

---

# Task 22 - Stash

Modify File

```bash
git stash
```

List

```bash
git stash list
```

Apply

```bash
git stash apply
```

Delete

```bash
git stash drop
```

Screenshot

---

# Task 23 - .gitignore

Create

```bash
touch .gitignore
```

Edit

```text
*.log

node_modules/

__pycache__/

.env
```

Commit

```bash
git add .

git commit -m ".gitignore added"

git push
```

Screenshot

---

# Task 24 - Clone Existing Repository

```bash
cd ~

git clone https://github.com/<username>/git-practice.git
```

Screenshot

---

# Task 25 - Delete Repository

GitHub

Settings

Danger Zone

Delete Repository

Screenshot

---

# Common Commands

```bash
git init

git clone

git status

git add .

git commit -m ""

git push

git pull

git branch

git checkout

git checkout -b

git merge

git log

git diff

git stash

git tag

git remote -v

git config --list
```