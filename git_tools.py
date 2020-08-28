import subprocess
import time


def add():
    cmd = "git add ."
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    returnCode = process.returncode
    if returnCode != 0:
        print(" add returnCode", returnCode)
    else:
        print("----------")
        commit()

commitMessage = "单元测试exec文件"


def commit():
    global commitMessage
    commitMessage = time.strftime("%Y/%m/%d-%H:%M")
    cmd = "git commit -m  '{}'".format(commitMessage)
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    returnCode = process.returncode
    print(returnCode)
    push()


def push():
    cmd = "git push origin master"
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    returnCode = process.returncode
    if returnCode != 0:
        print("push returnCode", returnCode)
    else:
        print("push success!")

add()
