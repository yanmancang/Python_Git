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


commitMessage = "ssssss"


def commit():
    global commitMessage
    commitMessage = time.strftime("%Y/%m/%d %H:%M")
    cmd = "git commit -m  '{}'".format(commitMessage)

    # print("cmd = " + cmd)
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