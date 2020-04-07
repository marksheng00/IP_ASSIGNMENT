from random import *
import datetime
import sys

# Global variable for count up coin 20200307
usercoin = 0
aicoin = 0


# Setting of each values
class actor(object):
    # warrior & tanker's HP, EXP, LV setting is same
    def __init__(self, H_P=100, EXP=0, R_L=1):
        self.H_P = H_P
        self.EXP = EXP
        self.R_L = R_L

    def warrior(self):
        self.A_P = randint(20, 25)
        if self.A_P > 15:
            self.D_P = randint(1, 3)
        else:
            self.D_P = randint(4, 6)
        return self.A_P, self.D_P

    def tanker(self):
        self.A_P = randint(8, 12)
        if self.A_P > 7:
            self.D_P = randint(6, 8)
        else:
            self.D_P = randint(8, 10)
        return self.A_P, self.D_P


class gameset(actor):
    # 1. Ask User's name. 2. Ask Number of Unit. 3. Ask Job of unit -> job_list[]. 4. Ask Unit's name. -> unitname[]
    # Unit list setting : [0] : name | [1] : HP | [2] : AP | [3] : DP | [4] : EXP | [5] : LV | [6] : Job (W/T)
    def __init__(self, name, num_unit, unitname, job_list):
        # name = input("Enter your name"), num_unit = int(input("How many units do you want?"))
        self.username = name
        self.num_unit = num_unit
        self.unitname = unitname
        self.job_list = job_list

    # Create user's team & unit
    def user_team_list(self):
        userunit = []

        for x in range(self.num_unit):
            if self.job_list[x] == 1:
                self.W_A_P, self.W_D_P = actor.warrior(self)
                userunit.append([self.unitname[x], 100, self.W_A_P, self.W_D_P, 0, 1, "W"])
            else:
                self.T_A_P, self.T_D_P = actor.tanker(self)
                userunit.append([self.unitname[x], 100, self.T_A_P, self.T_D_P, 0, 1, "T"])
        return userunit

    # Create AI's team & unit
    def ai_team_list(self):
        aiunit = []
        tankerCU = 0

        for x in range(self.num_unit):
            # To prevent all the units are tanker
            if x + 1 == self.num_unit and tankerCU / self.num_unit >= 0.5:
                wap, wdp = actor.warrior(self)
                aiunit.append(['AI' + str(randint(0, 9)) + str(randint(0, 9)), 100, wap, wdp, 0, 1, "W"])
            else:
                job = randint(1, 2)
                if job == 1:
                    wap, wdp = actor.warrior(self)
                    aiunit.append(['AI' + str(randint(0, 9)) + str(randint(0, 9)), 100, wap, wdp, 0, 1, "W"])

                else:
                    tap, tdp = actor.tanker(self)
                    aiunit.append(['AI' + str(randint(0, 9)) + str(randint(0, 9)), 100, tap, tdp, 0, 1, "T"])
                    tankerCU += 1
        return aiunit


# gameset 3, 4 (get unitname, joblist)
def unitSetting_list(numberOfUnit):
    unitname = []
    job_list = []
    for i in range(numberOfUnit):
        question_line()
        name = input("What's the name of unit {}? : ".format(i + 1))
        unitname.append(name)
        while True:
            question_line()
            job = int(input("What's the position of the unit? 1. Warrior 2. Tanker (Enter 1 or 2) : "))
            if job == 1 or job == 2:
                break
            else:
                message_line()
                print("Choose 1 or 2")
        job_list.append(job)
    return unitname, job_list


def statsUp(unit, num):
    if unit[num][6] == "W":
        unit[num][2] += 10  # Warrior atk up
        unit[num][3] += 7  # Warrior def up
    else:
        unit[num][2] += 3  # Tanker atk up
        unit[num][3] += 5  # Tanker def up


# recorder
def write(turn, notturn, attacker, target, damage):
    with open('data.txt', 'a')as d:
        d.write(str(turn[attacker][0]) + ' ' + 'attack' + ' ' + str(notturn[target][0]) + ' ' + str(damage) + ' ' + str(
            datetime.datetime.now()) + '\n')


# Using coin function 20200307
def useCoin(turncoin, turnlist, turn):
    if turncoin >= 100:
        if turn == "U":
            question_line()
            unitselect = int(input('Choose your unit to use coin : ')) - 1
            x = unitselect
            while x >= len(turnlist):
                print("(Write the proper value in number!)")
                question_line()
                unitselect = int(input('Choose your unit to use coin : ')) - 1
                x = unitselect

            dowhat = int(input("1. HP up, 2. ATK up, 3. DEF up : "))
        else:
            unitselect = randint(0, len(turnlist) - 1)
            dowhat = randint(1, 3)

        if dowhat == 1:
            turnlist[unitselect][1] += 20
            print("{}'s HP 20 UP!".format(turnlist[unitselect][0]))
        elif dowhat == 2:
            turnlist[unitselect][2] += 10
            print("{}'s ATK 10 UP!".format(turnlist[unitselect][0]))
        else:
            turnlist[unitselect][3] += 10
            print("{}'s DEF 10 UP!".format(turnlist[unitselect][0]))
        print_line()


def damage_EXP(turn, notturn, attacker, target):
    # Damage & EXP calculating
    damage = int(turn[attacker][2] - randint(5, 10) - notturn[target][3])
    # attacker +EXP
    turn[attacker][4] += turn[attacker][2]
    # target -HP, +EXP
    if damage > 0:
        message_line()
        print("Damage is {}".format(damage))
        print_line()
        notturn[target][1] -= damage
        write(turn, notturn, attacker, target, damage)
        if damage < 10:
            notturn[target][4] += damage
        else:
            notturn[target][4] += int(damage * 1.2)
    else:
        message_line()
        print("MISS!")
        print_line()
        notturn[target][4] += int(abs(damage * 1.5))

    # attacker level up
    while len(turn) > 0 and turn[attacker][4] >= 100:
        turn[attacker][4] -= 100
        message_line()
        print("{}'s level up! {}->{}".format(turn[attacker][0], turn[attacker][5], turn[attacker][5] + 1))
        turn[attacker][5] += 1
        statsUp(turn, attacker)
    # target Faint / Level Up
    if notturn[target][1] <= 0:
        del notturn[target]
    else:
        while len(notturn) > 0 and notturn[target][4] >= 100:
            notturn[target][4] -= 100
            message_line()
            print("{}'s level up! {}->{}".format(notturn[target][0], notturn[target][5], notturn[target][5] + 1))
            notturn[target][5] += 1
            statsUp(notturn, target)
    return damage # This is for checking coin up


# User attack
def uattack(userunit, aiunit):
    global aicoin
    try:
        i = len(userunit)
        # Choose attacker
        while True:
            try:
                # nameset = Used for displaying remaining unit's name
                nameset = ""
                numUp = 1
                for x in range(i):
                    nameset += str(numUp) + "." + userunit[x][0] + " "
                    numUp += 1
                question_line()
                attacker = int(input("Choose the attacker " + nameset + ": ")) - 1
                message_line()
                print('{0} is been chosen as attacker'.format(userunit[attacker][0]))
                break

            except IndexError:
                print('Choose between 1 and {}'.format(i))
            except ValueError:
                print('Only number is acceptable. choose between 1 and {}'.format(i))
        # Choose target
        l = len(aiunit)
        while True:
            try:
                nameset = ""
                numUp = 1

                for x in range(l):
                    nameset += str(numUp) + "." + aiunit[x][0] + " "
                    numUp += 1
                question_line()
                target = int(input("Choose the target " + nameset + ": ")) - 1
                message_line()
                print('{0} is been chosen as target'.format(aiunit[target][0]))
                break

            except IndexError:
                question_line()
                print('Choose between 1 and {}'.format(l))
            except ValueError:
                question_line()
                print('Only number is acceptable. chose between 1 and {}'.format(l))

        # damage, exp and coin up 20200307
        if damage_EXP(userunit, aiunit, attacker, target) >= 10:
            aicoin += 20
    finally:
        pass


# AI attack
def aiattack(aiunit, userunit):
    global usercoin
    try:
        userDP = userunit[0][3]
        target = 0
        aiAP = aiunit[0][2]
        attacker = 0
        # Selecting the target unit that has the lowest DP
        for x in range(len(userunit)):
            if userDP > userunit[x][3]:
                userDP = userunit[x][3]
                target = x

        # Selecting the attacker unit that has the highest AP
        for x in range(len(aiunit)):
            if aiAP < aiunit[x][2]:
                aiAP = aiunit[x][2]
                attacker = x
        message_line()
        print('{0} is been chosen as attacker'.format(aiunit[attacker][0]))
        print('{0} is been chosen as target'.format(userunit[target][0]))

        # damage, exp and coin up 20200307
        if damage_EXP(aiunit, userunit, attacker, target) >= 10:
            usercoin += 20
    finally:
        pass


def print_line():
    print("-----------------------------------------------------------------------------------------------------------")


def message_line():
    print("<<MESSAGE>>  ", end="")


def question_line():
    print("?QUESTION?  ", end="")


def rewrite_list(list, vname):
    count = 1
    for i in list:
        name = " name :" + str(i[0])
        HP = " HP :" + str(i[1])
        AP = " AP :" + str(i[2])
        DP = " DP :" + str(i[3])
        EXP = " EXP :" + str(i[4])
        LV = " LV :" + str(i[5])
        actor = "AI   " + str(count) + ""
        if vname == "u_list":
            actor = "USER " + str(count)

        print(actor + name + HP + AP + DP + EXP + LV)
        print_line()
        count += 1


def main_game_loop():
    global aicoin, usercoin
    while True:
        uattack(u_list, ai_list)
        if len(ai_list) == 0:
            print("u win, ai lose")
            return (u_list, ai_list)
            break
        # AI Use coin 20200307
        else:
            useCoin(aicoin, ai_list, "A")
            if aicoin >= 100:
                aicoin -= 100
        rewrite_list(u_list, 'u_list')
        rewrite_list(ai_list, 'ai_list')
        print("User coin :", usercoin)
        print("AI coin :", aicoin)

        aiattack(ai_list, u_list)
        if len(u_list) == 0:
            print("ai win, u lose")
            return (u_list, ai_list)
            break
        # User Use coin 20200307
        else:
            useCoin(usercoin, u_list, "U")
            if usercoin >= 100:
                usercoin -= 100
        rewrite_list(u_list, 'u_list')
        rewrite_list(ai_list, 'ai_list')
        print("User coin :", usercoin)
        print("AI coin :", aicoin)


if __name__ == '__main__':
    # create user list
    question_line()
    username = input("Enter your name : ")
    while True:
        try:
            question_line()
            num_list = int(input('Enter the number of unit : '))
            break
        except:
            question_line()
            print("Enter only number")
    unit_name, job_list = unitSetting_list(num_list)
    # launch main loop of game
    user = gameset(username, num_list, unit_name, job_list)
    u_list = user.user_team_list()
    ai_list = user.ai_team_list()
    main_game_loop()