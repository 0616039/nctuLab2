# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
> ![螢幕擷取畫面 (129).png](https://github.com/nctucn/lab2-0616039/blob/master/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(129).png)  


---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail

### iPerf Commands
h4 iperf -s -u -i 1 > ./out/result &
h2 iperf -c 10.0.0.4 -u –i 1

### Tasks


1. **Environment Setup**  
   1.先進入putty，登入我的學號，再用root登入  
   2.先clone進去我的Network_Topology  
   3.輸入 sudo mn 發現有error，於是要先打sudo service openvswitch-switch start，再打sudo mn才會成功  
2. **Example of Mininet**  
   1.先進入我的src資料夾，然後打 sudo chmod +x example.py轉成可執行的模式，再打 sudo ./example.py執行檔案  
   2.然後如果再打一次 sudo ./example.py會產生error，因為已經執行過一次，於是要打 sudo mn -c，把東西先清乾淨  
3. **Topology Generator**  
   1.先把自己的學號除以三，得到1，所以是用topo1.png  
    ![topo1.png](https://github.com/nctucn/lab2-0616039/blob/master/src/topo/topo1.png)  
   2.修改一些example.py裡面的內容，打出可以建立topo1.png的程式碼  
   3.再程式碼中加上dumpNodeConnections(net.hosts)和dumpNodeConnections(net.switches)可以顯示host跟switch之間的連結  
   3.在最上面加上from mininet.cli import CLI，然後在後面加上CLI(net)，再把stop的部分刪掉  
   4.輸入h1 ping h2便可以看到h1跟h2的連接  
4. **Measurement**  
   1.輸入h4 iperf -s -u -i 1 > ./out/result &跟h2 iperf -c 10.0.0.4 -u –i 1  
   2.
---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> 

* [0616039](https://github.com/0616039)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
