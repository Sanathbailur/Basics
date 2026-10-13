print(" hi hello")
n = 5 
i =0
while i < n:
    print(i)
    i += 1
    
'''
Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics
$ git init
Initialized empty Git repository in C:/Users/HP/Desktop/gitandgithub/basics/.git/

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git config user.name "sanath"

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git config user.email "sanathpbailur@gmail.com"

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        f1.py
        f2.py

nothing added to commit but untracked files present (use "git add" to track)

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git add .

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   f1.py
        new file:   f2.py


Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git commit f1.py -m "add f1.py in master"
[master (root-commit) 2443ffb] add f1.py in master
 1 file changed, 6 insertions(+)
 create mode 100644 f1.py

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   f2.py


Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git commit f2.py -m " add f2.py in master
> 
> git commit f2.py -m " add f2.py in master"
> ^C

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git commit f2.py -m  "add f2.py in master"
[master 31802a4] add f2.py in master
 1 file changed, 4 insertions(+)
 create mode 100644 f2.py

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git status
On branch master
nothing to commit, working tree clean

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git log
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master
(END)
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master
(END)
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master
(END)
commit 31802a4ae55278d7e925833405ea6e838a4b5f41 (HEAD -> master)
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:33:47 2026 +0530

    add f2.py in master

commit 2443ffbc5a0f9e4f1b806684d7a189f0dc97129c
Author: sanath <sanathpbailur@gmail.com>
Date:   Mon Oct 12 17:31:37 2026 +0530

    add f1.py in master

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git remote add origin https://github.com/Sanathbailur/Basics.git

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git remote -v
origin  https://github.com/Sanathbailur/Basics.git (fetch)
origin  https://github.com/Sanathbailur/Basics.git (push)

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ git push origin master 
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 565 bytes | 188.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Sanathbailur/Basics.git
 * [new branch]      master -> master

Sanath@LAPTOP-AN5L2RG2 UCRT64 ~/Desktop/gitandgithub/basics (master)
$ '''
