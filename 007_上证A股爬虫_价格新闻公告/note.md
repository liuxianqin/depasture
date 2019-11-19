# 选取网页的原则

不要纠结于某个网站，多找信息源

MOOC第几次开课每一次都会重新录制视频吗？  不是的。

user@carbon:~$ ps aux | grep python3
root       986  0.0  0.2  40852 19116 ?        Ss   20:35   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root      1278  0.0  0.2 119756 22224 ?        Ssl  20:35   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
user      2715  1.1  0.7 210376 56764 tty2     Sl+  20:36   0:09 /usr/bin/python3 completion.py
user      5347  0.3  0.2  30160 23588 tty2     S+   20:46   0:00 /usr/bin/python3 lib/python/jedi/evaluate/compiled/subprocess/__main__.py lib/python 3.7.3
user      6165  0.0  0.0   6332  2416 pts/2    S+   20:50   0:00 grep --color=auto python3
user@carbon:~$ ps aux | grep main.py
user      6234  0.0  0.0   6336  2472 pts/2    S+   20:50   0:00 grep --color=auto main.py
user@carbon:~$ kill 6234
bash: kill: (6234) - No such process
user@carbon:~$ ps aux | grep main.py
user      6242  0.0  0.0   6336   908 pts/2    S+   20:50   0:00 grep --color=auto main.py
user@carbon:~$ kill 623^?42
bash: kill: 62342: arguments must be process or job IDs
user@carbon:~$ ps aux | grep main.py
user      6248  0.0  0.0   6336  2552 pts/2    S+   20:50   0:00 grep --color=auto main.py
user@carbon:~$ 

这个进程一直在变 杀不掉
