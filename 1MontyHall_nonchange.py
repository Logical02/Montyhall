# coding=EUC-KR

import random

success = 0
fail = 0

print("������ �ٲܱ�� �ȹٲܱ��?(y/n)")
mode = input(">> ")
if mode != "y" and mode != "n":
    while True:
        mode = input("y �Ǵ� n���θ� �ٽ� �Է����ּ���\n>> ")
        if mode == "y" or mode == "n":
            break

print("�� ȸ �ݺ��� ������ �˷��ּ���\n")
repeat = input(">> ")
if repeat.isdigit() == False:
      while True:
        repeat = input("\n�ڿ����θ� �ٽ� �Է��ϼ���.\n>> ")
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
    print("\n" + "������ �ٲپ��� ��")
if mode == "n":
    print("\n" + "������ �ٲ��� �ʾ��� ��")

print( str(repeat) + "ȸ �õ� ��" + str(success) + "ȸ ���߾����ϴ�.")
print("Ȯ��: " + str(int(success)/int(repeat)))


