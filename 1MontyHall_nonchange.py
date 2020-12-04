# coding=EUC-KR

import random

success = 0
fail = 0

print("선택을 바꿀까요 안바꿀까요?(y/n)")
mode = input(">> ")
if mode != "y" and mode != "n":
    while True:
        mode = input("y 또는 n으로만 다시 입력해주세요\n>> ")
        if mode == "y" or mode == "n":
            break

print("몇 회 반복할 것인지 알려주세요\n")
repeat = input(">> ")
if repeat.isdigit() == False:
      while True:
        repeat = input("\n자연수로만 다시 입력하세요.\n>> ")
        if repeat.isdigit() == True:
            break

if mode == "n":


    for i in range(int(repeat)):
        goatlist = [1,2,3]
        chance = [1,2,3]
        car = random.randrange(1,4)
        selected = random.randrange(1,4)
        if selected == car:
            print("True")
            success = success + 1
        elif selected != car:
            print("False")
            fail = fail + 1
        else:
            print("error")

if mode == "y":
    for i in range(int(repeat)):
        goatlist = [1,2,3]
        chance = [1,2,3]
        car = random.randrange(1,4)
        selected = random.randrange(1,4)
        if car == selected:
            goatlist.remove(int(car))
        else:
            goatlist.remove(int(car))
            goatlist.remove(int(selected))
        show = random.choice(goatlist)
        chance.remove(int(show))
        chance.remove(int(selected))
        selected = random.choice(chance)
        if selected == car:
            print("True")
            success = success + 1
        elif selected != car:
            print("False")
            fail = fail + 1
        else:
            print("error")


if mode == "y":
    print("\n" + "선택을 바꾸었을 때")
if mode == "n":
    print("\n" + "선택을 바꾸지 않았을 때")

print( str(repeat) + "회 시도 중" + str(success) + "회 맞추었습니다.")
print("확률: " + str(int(success)/int(repeat)))


