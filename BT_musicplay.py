import subprocess
from random import *

Music_List = []


def iter_Music(var):
    global Music_List
    for i in range(0, 5):
        #        print(Music_List)
        #        print("Count: ",i)
        #        print("val: ",var)
        if var + i >= 5:
            Ans = var + i - 4
        else:
            Ans = var + i
        sum = randint(0, 4)
        subprocess.call(["afplay", "Users\박천욱\PycharmProjects\EverydayCoding\afplay" + str(Ans * 4 - sum) + ".wav"])

        Flag = int(input("If you like Music, Typing 1\nWant to hear next, typing 0\n"))

        if Flag == 1:
            Music_List.append(Ans)
            if len(Music_List) == 3: return
            iter_Music(Ans)
            if len(Music_List) == 3: return

    Music_List.pop()
    return


iter_Music(1)

print(Music_List)