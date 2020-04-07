import tkinter as tk
import imageio
import time
import pygame
from tkinter import Tk, Label
from PIL import ImageTk, Image
from pathlib import Path
from random import *
from tkinter import messagebox
import datetime
import pyglet
import pygame
import _thread
from PIL import Image, ImageTk
import threading
#pygame.mixer.init()
#sound1 = pygame.mixer_music.load("./sound/Music  Falcon vs The TIE fighters.mp3")


class IPMAIN():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/start.mp3")
        pygame.mixer_music.play()
        self.ai_t_b = 0
        self.u_t_b = 0
        self.main_window = tk.Tk()
        self.main_window.title('PSB Battle Game')
        self.main_window.config(bg='black')
        self.main_window.geometry('480x320')
        self.canvas = tk.Canvas(self.main_window, width=480, height=320)
        self.bg = tk.PhotoImage(file='./image/bg.jpg')
        bg2 = tk.PhotoImage(file='./image/bg2.png')
        self.bg2_x = bg2.subsample(5,5)
        self.bg3 = tk.PhotoImage(file='./image/bg3.png')
        self.bg4 = tk.PhotoImage(file='./image/bg4.png')
        self.bg5 = tk.PhotoImage(file='./image/bg5.png')
        self.bg6 = tk.PhotoImage(file='image/bg6.jpg')
        self.canvas.create_image(240,160,image=self.bg)
        self.canvas.pack()
        self.label1 = tk.Label(self.main_window, text="Click to Start !",fg='white', bg='black')
        self.label1.pack()
        self.start_image = tk.PhotoImage(file='./image/start.jpg',width=500,height=200)
        self.start_image_x = self.start_image.subsample(5,5)
        self.start_button = tk.Button(self.main_window, image=self.start_image_x,bg='black',command=self.start_game_name)
        self.start_button.pack()
        self.canvas.create_window(240,130,window=self.label1)
        self.canvas.create_window(240,180,window=self.start_button)
        self.main_window.mainloop()

    def start_game_name(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/deathstar.mp3")
        pygame.mixer_music.play()
        self.main_window.geometry('1080x720')
        self.start_button.destroy()
        self.label1.destroy()
        self.canvas.destroy()
        self.canvas2 = tk.Canvas(self.main_window, width=1080, height=720, bg='black')
        self.canvas2.create_image(540, 260, image=self.bg3)
        self.canvas2.pack()
        self.label2 = tk.Label(self.main_window, text="What's your Name ?", fg='white', bg='black', height=5, width=100)
        self.label2.pack()
        self.confirm_image = tk.PhotoImage(file='./image/confirm.png', height=280, width=660)
        self.confirm_image_x = self.confirm_image.subsample(7, 7)
        self.confirm_button = tk.Button(self.main_window, image=self.confirm_image_x, bg='black',
                                        command=self.start_game_num)
        self.confirm_button.pack()
        self.name_text = tk.Entry(self.main_window)
        self.name_text.pack()
        self.canvas2.create_window(540, 505, window=self.label2)
        self.canvas2.create_window(540, 535, window=self.name_text)
        self.canvas2.create_window(540, 575, window=self.confirm_button)
        self.main_window.mainloop()


    def start_game_num(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/fighters.mp3")
        pygame.mixer_music.play()
        # return the self.name_text.get() to the corresponding function
        self.username = self.name_text.get()

        self.canvas2.destroy()
        self.name_text.destroy()
        self.label2.destroy()
        self.canvas3 = tk.Canvas(self.main_window, width=1080, height=720, bg='black')
        self.canvas3.create_image(540, 260, image=self.bg4)
        self.canvas3.pack()
        self.label3 = tk.Label(self.main_window, text="Enter the number of units that you want to employ", fg='white', bg='black', height=5, width=100)
        self.label3.pack()
        self.button3 = tk.Button(self.main_window, image=self.confirm_image_x, bg='black', command=self.start_game_uname)
        self.button3.pack()
        self.num_text = tk.Entry(self.main_window)
        self.num_text.pack()
        self.canvas3.create_window(545, 505, window=self.label3)
        self.canvas3.create_window(545, 535, window=self.num_text)
        self.canvas3.create_window(545, 575, window=self.button3)
        self.main_window.mainloop()

    def start_game_uname(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/Jump.mp3")
        pygame.mixer_music.play()
        self.canvas3.destroy()
        self.label3.destroy()
        self.button3.destroy()

        self.num_list = self.num_text.get()
        # return the num of list to the corresponding function
        print(self.num_list)
        self.canvas4 = tk.Canvas(self.main_window, width=1080, height=720, bg='black')
        self.canvas4.create_image(540, 260, image=self.bg5)
        self.canvas4.pack()

        self.label4 = tk.Label(self.main_window,text="Enter your character's name and its job (Warrior:1 / Tanker:2)", fg='white', bg='black', height=5, width=120)
        self.button4 = tk.Button(self.main_window, image=self.confirm_image_x, bg='black',command=self.battle_game)
        self.user1 = tk.Label(self.main_window,text='User1 Name')
        self.user2 = tk.Label(self.main_window, text='User2 Name')
        self.user3 = tk.Label(self.main_window, text='User3 Name')

        self.name1 = tk.Entry(self.main_window)
        self.name2 = tk.Entry(self.main_window)
        self.name3 = tk.Entry(self.main_window)

        self.job1 = tk.Entry(self.main_window)
        self.job2 = tk.Entry(self.main_window)
        self.job3 = tk.Entry(self.main_window)

        if self.num_list == "1":
            self.canvas4.create_window(470, 505, window=self.user1)
            self.canvas4.create_window(595, 505, window=self.name1)
            self.canvas4.create_window(700, 505, window=self.job1)
        if self.num_list == "2":
            self.canvas4.create_window(470, 505, window=self.user1)
            self.canvas4.create_window(595, 505, window=self.name1)
            self.canvas4.create_window(700, 505, window=self.job1)
            self.canvas4.create_window(470, 535, window=self.user2)
            self.canvas4.create_window(595, 535, window=self.name2)
            self.canvas4.create_window(700, 535, window=self.job2)
        if self.num_list == "3":
            self.canvas4.create_window(470, 505, window=self.user1)
            self.canvas4.create_window(595, 505, window=self.name1)
            self.canvas4.create_window(700, 505, window=self.job1)
            self.canvas4.create_window(470, 535, window=self.user2)
            self.canvas4.create_window(595, 535, window=self.name2)
            self.canvas4.create_window(700, 535, window=self.job2)
            self.canvas4.create_window(470, 565, window=self.user3)
            self.canvas4.create_window(595, 565, window=self.name3)
            self.canvas4.create_window(700, 565, window=self.job3)

        self.canvas4.create_window(540, 475, window=self.label4)
        self.canvas4.create_window(540, 600, window=self.button4)

        self.main_window.mainloop()


    def warrior(self):
        self.A_P = randint(20, 25)
        if self.A_P > 23:
            self.D_P = randint(1, 3)
        else:
            self.D_P = randint(4, 6)
        return self.A_P, self.D_P

    def tanker(self):
        self.A_P = randint(8, 12)
        if self.A_P > 10:
            self.D_P = randint(6, 8)
        else:
            self.D_P = randint(8, 10)
        return self.A_P, self.D_P


    def ub1(self):
        self.acttacker = 1



    def ub2(self):
        self.acttacker = 2


    def ub3(self):
        self.acttacker = 3

    def rewrite_list(self,list, vname):
        count = 1
        self.list = ""
        for i in list:
            name = " " + str(i[0])
            HP = " HP:" + str(i[1])
            AP = " AP:" + str(i[2])
            DP = " DP:" + str(i[3])
            EXP = " EXP :" + str(i[4])
            LV = " LV:" + str(i[5])
            actor = "AI  " + str(count) + ""
            if vname == "u_list":
                actor = "USER" + str(count)
            self.list += actor + name + HP + AP + DP + EXP + LV + " "
            count += 1
        print(self.list)
        return self.list


    def ab1(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/Clash.mp3")
        pygame.mixer_music.play()
        self.target = 1
        self.damage(self.acttacker,self.target)
        var = self.rewrite_list(self.aiunit,"ai_list")
        self.label5 = tk.Label(self.main_window, text=var, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 650, anchor='n', window=self.label5)
        var2 = self.rewrite_list(self.userunit,"u_list")
        self.label6 = tk.Label(self.main_window, text=var2, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 675, anchor='n', window=self.label6)
        self.win()


    def ab2(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/Clash.mp3")
        pygame.mixer_music.play()
        self.target = 2
        self.damage(self.acttacker, self.target)
        var = self.rewrite_list(self.aiunit, "ai_list")
        self.label5 = tk.Label(self.main_window, text=var, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 650, anchor='n', window=self.label5)
        var2 = self.rewrite_list(self.userunit, "u_list")
        self.label6 = tk.Label(self.main_window, text=var2, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 675, anchor='n', window=self.label6)
        self.win()


    def ab3(self):
        pygame.mixer.init()
        pygame.mixer_music.load("./sound/Clash.mp3")
        pygame.mixer_music.play()
        self.target = 3
        self.damage(self.acttacker, self.target)
        var = self.rewrite_list(self.aiunit, "ai_list")
        self.label5 = tk.Label(self.main_window, text=var, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 650, anchor='n', window=self.label5)
        var2 = self.rewrite_list(self.userunit, "u_list")
        self.label6 = tk.Label(self.main_window, text=var2, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 675, anchor='n', window=self.label6)
        self.win()

    def damage(self, attacker, target):
        attacker -= 1
        target -= 1
        # ~~~~User Attack~~~~
        # Caculating damage(User -> AI)
        AIGetdamage = int(self.userunit[attacker][2] - randint(5, 10) - self.aiunit[target][3])
        print(AIGetdamage)
        # User +EXP
        self.userunit[attacker][4] += self.userunit[attacker][2]

        # target -HP, +EXP
        if AIGetdamage > 0:
            self.aiunit[target][1] -= AIGetdamage
            if AIGetdamage < 10:
                self.aiunit[target][4] += AIGetdamage
            else:
                self.aiunit[target][4] += int(AIGetdamage * 1.2)
        else:
            self.aiunit[target][4] += int(abs(AIGetdamage * 1.5))

        # User level up
        while self.userunit[attacker][4] >= 100:
            self.userunit[attacker][4] -= 100
            self.userunit[attacker][5] += 1
            print("levelup")
            # Stats up
            if self.userunit[attacker][6] == "W":
                self.userunit[attacker][2] += 10  # Warrior atk up
                self.userunit[attacker][3] += 7  # Warrior def up
            else:
                self.userunit[attacker][2] += 3  # Tanker atk up
                self.userunit[attacker][3] += 5  # Tanker def up

        # AI Faint / Level UP
        try:
            # Faint
            for x in range(len(self.aiunit)):
                if self.aiunit[x][1] <= 0:
                    self.aiunit[x][1] = 0
                    if x == 0:
                        self.aibutton1.destroy()
                        if self.aiunit[x][7] == "O":
                            self.aiunit[x][7] = "X"

                    if x == 1:
                        self.aibutton2.destroy()
                        if self.aiunit[x][7] == "O":
                            self.aiunit[x][7] = "X"

                    if x == 2:
                        self.aibutton3.destroy()
                        if self.aiunit[x][7] == "O":
                            self.aiunit[x][7] = "X"
            # Level up
            while self.aiunit[target][7] == "O" and self.aiunit[target][4] >= 100:
                self.aiunit[target][4] -= 100
                self.aiunit[target][5] += 1
                print("levelup")
                # Stats up
                if self.aiunit[target][6] == "W":
                    self.aiunit[target][2] += 10  # Warrior atk up
                    self.aiunit[target][3] += 7  # Warrior def up
                else:
                    self.aiunit[target][2] += 3  # Tanker atk up
                    self.aiunit[target][3] += 5  # Tanker def up
        except IndexError:
            pass

        # Checking whether there is any AI unit that is alive
        aialive = 0
        for x in range(len(self.aiunit)):
            if self.aiunit[x][1] > 0:
                aialive += 1

        if aialive > 0:
            # ~~~~AI Attack~~~~
            # Selecting target, attacker
            for x in range(len(self.userunit)):
                if self.userunit[x][1] > 0:
                    userDP = self.userunit[x][3]
                    aitarget = x
                    break
            for x in range(len(self.aiunit)):
                if self.aiunit[x][1] > 0:
                    aiAP = self.aiunit[x][3]
                    aiattacker = x
                    break
            # Selecting the target unit that has the lowest DP
            for x in range(len(self.userunit)):
                if userDP > self.userunit[x][3] and self.userunit[x][1] > 0:
                    userDP = self.userunit[x][3]
                    aitarget = x

            # Selecting the attacker unit that has the highest AP
            for x in range(len(self.aiunit)):
                if aiAP < self.aiunit[x][2] and self.aiunit[x][1] > 0:
                    aiAP = self.aiunit[x][2]
                    aiattacker = x

            # Caculating damage(AI -> User)
            UserGetdamage = int(self.aiunit[aiattacker][2] - randint(5, 10) - self.userunit[aitarget][3])
            print(UserGetdamage)
            # AI +EXP
            self.aiunit[aiattacker][4] += self.userunit[aitarget][2]

            # target -HP, +EXP
            if UserGetdamage > 0:
                self.userunit[aitarget][1] -= UserGetdamage
                if UserGetdamage < 10:
                    self.userunit[aitarget][4] += UserGetdamage
                else:
                    self.userunit[aitarget][4] += int(UserGetdamage * 1.2)
            else:
                self.userunit[aitarget][4] += int(abs(UserGetdamage * 1.5))

            # AI level up
            while self.aiunit[aiattacker][4] >= 100:
                self.aiunit[aiattacker][4] -= 100
                self.aiunit[aiattacker][5] += 1
                print("levelup")
                # Stats up
                if self.aiunit[aiattacker][6] == "W":
                    self.aiunit[aiattacker][2] += 10  # Warrior atk up
                    self.aiunit[aiattacker][3] += 7  # Warrior def up
                else:
                    self.aiunit[aiattacker][2] += 3  # Tanker atk up
                    self.aiunit[aiattacker][3] += 5  # Tanker def up

            # User Faint / Level UP
            try:
                # Faint
                for i in range(len(self.userunit)):
                    if self.userunit[i][1] <= 0:
                        self.userunit[i][1] = 0
                        if i == 0:
                            self.userbutton1.destroy()
                            if self.userunit[i][7] == "O":
                                self.userunit[i][7] = "X"
                        if i == 1:
                            self.userbutton2.destroy()
                            if self.userunit[i][7] == "O":
                                self.userunit[i][7] = "X"
                        if i == 2:
                            self.userbutton3.destroy()
                            if self.userunit[i][7] == "O":
                                self.userunit[i][7] = "X"

                # Level up
                while self.userunit[aitarget][7] == "O" and self.userunit[aitarget][4] >= 100:
                    self.userunit[aitarget][4] -= 100
                    self.userunit[aitarget][5] += 1
                    print("levelup")
                    # Stats up
                    if self.userunit[aitarget][6] == "W":
                        self.userunit[aitarget][2] += 10  # Warrior atk up
                        self.userunit[aitarget][3] += 7  # Warrior def up
                    else:
                        self.userunit[aitarget][2] += 3  # Tanker atk up
                        self.userunit[aitarget][3] += 5  # Tanker def up
            except IndexError:
                pass

    def win(self):
        if len(self.userunit) == 3:
            if self.userunit[0][1] + self.userunit[1][1] + self.userunit[2][1] == 0:
                messagebox.showinfo("RESULT","AI WIN U LOSE")
                self.final_win()
        if len(self.aiunit) == 3:
            if self.aiunit[0][1] + self.aiunit[1][1] + self.aiunit[2][1] == 0:
                messagebox.showinfo("RESULT","U WIN AI LOSE")
                self.final_win()
        if len(self.userunit) == 2:
            if self.userunit[0][1] + self.userunit[1][1] == 0:
                messagebox.showinfo("RESULT","AI WIN U LOSE")
                self.final_win()
        if len(self.aiunit) == 2:
            if self.aiunit[0][1] + self.aiunit[1][1] == 0:
                messagebox.showinfo("RESULT","U WIN AI LOSE")
                self.final_win()
        if len(self.userunit) == 1:
            if self.userunit[0][1] == 0:
                messagebox.showinfo("RESULT","AI WIN U LOSE")
                self.final_win()
        if len(self.aiunit) == 1:
            if self.aiunit[0][1] == 0:
                messagebox.showinfo("RESULT","U WIN AI LOSE")
                self.final_win()


    def final_win(self):
        self.main_window.destroy()
        video_name = str(Path().absolute()) + './image/final3.mp4'
        video = imageio.get_reader(video_name)
        delay = int(1000 / video.get_meta_data()['fps'])

        def stream(label):
            try:
                image = video.get_next_data()
            except:
                video.close()
                return
            label.after(delay, lambda: stream(label))
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

        def run_viedo():
            root = Tk()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        def run_sound():
            pygame.mixer.init()
            pygame.mixer.music.load('./image/final3.wav')
            pygame.mixer.music.play()


        threads = []
        t1 = threading.Thread(target=run_sound())
        threads.append(t1)
        t2 = threading.Thread(target=run_viedo())
        threads.append(t2)

        if __name__ == '__main__':
            for t in threads:
                t.setDaemon(True)
        t.start()




    def battle_game(self):
        self.userunit = []
        # return the three name
        namelist = []
        joblist = []
        namelist.append(self.name1.get())
        namelist.append(self.name2.get())
        namelist.append(self.name3.get())
        joblist.append(self.job1.get())
        joblist.append(self.job2.get())
        joblist.append(self.job3.get())

        numunit = 0
        for x in range(len(namelist)):
            if namelist[x] != "":
                if joblist[x] == "1":
                    ap, dp = self.warrior()
                    self.userunit.append([namelist[x], 100, ap, dp, 0, 1, "W", "O"])
                elif joblist[x] == "2":
                    ap, dp = self.tanker()
                    self.userunit.append([namelist[x], 100, ap, dp, 0, 1, "T", "O"])
                else:
                    pass
                numunit += 1
        print(self.userunit)

        self.aiunit = []
        tankerCU = 0
        for x in range(numunit):
            if x + 1 == numunit and tankerCU / numunit >= 0.5:
                ap, dp = self.warrior()
                self.aiunit.append(['AI' + str(randint(0, 9)) + str(randint(0, 9)), 100, ap, dp, 0, 1, "W", "O"])
            else:
                job = randint(1, 2)
                if job == 1:
                    ap, dp = self.warrior()
                    self.aiunit.append(['AI' + str(randint(0, 9)) + str(randint(0, 9)), 100, ap, dp, 0, 1, "W", "O"])

                else:
                    ap, dp = self.tanker()
                    self.aiunit.append(['AI' + str(randint(0, 9)) + str(randint(0, 9)), 100, ap, dp, 0, 1, "T", "O"])
                    tankerCU += 1
        print(self.aiunit)

        self.label4.destroy()
        self.canvas4.destroy()
        self.button4.destroy()
        self.user1.destroy()
        self.user2.destroy()
        self.user3.destroy()
        self.name1.destroy()
        self.name2.destroy()
        self.name3.destroy()

        self.canvas5 = tk.Canvas(self.main_window, width=1080, height=720, bg='black')
        self.canvas5.create_image(540, 260, image=self.bg6)
        self.canvas5.pack()
        # here is the value should be input the all print text in console version
        var = self.rewrite_list(self.aiunit, "ai_list")
        self.label5 = tk.Label(self.main_window, text=var, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 650, anchor='n', window=self.label5)
        var2 = self.rewrite_list(self.userunit, "u_list")
        self.label6 = tk.Label(self.main_window, text=var2, fg='white', bg='black', height=1, width=150)
        self.canvas5.create_window(540, 675, anchor='n', window=self.label6)

        self.usertanker = tk.PhotoImage(file='./image/UserTanker.png')
        self.userwarrior = tk.PhotoImage(file='./image/UserWarrior.png')
        self.aitanker = tk.PhotoImage(file='./image/AITanker.png')
        self.aiwarrior = tk.PhotoImage(file='./image/AIWarriorBlue.png')

        self.choose_image = tk.PhotoImage(file='./image/choose1.png', height=308, width=656)
        self.choose_image_x = self.choose_image.subsample(8, 8)
        self.choose_button = tk.Button(self.main_window, image=self.choose_image_x, bg='black')
        self.choose_button.pack()
        self.userbutton1 = tk.Button(self.main_window,image=self.choose_image_x, bg='black', command=self.ub1)
        self.userbutton2 = tk.Button(self.main_window, image=self.choose_image_x, bg='black', command=self.ub2)
        self.userbutton3 = tk.Button(self.main_window, image=self.choose_image_x, bg='black', command=self.ub3)
        self.aibutton1 = tk.Button(self.main_window, image=self.choose_image_x, bg='black', command=self.ab1)
        self.aibutton2 = tk.Button(self.main_window, image=self.choose_image_x, bg='black', command=self.ab2)
        self.aibutton3 = tk.Button(self.main_window, image=self.choose_image_x, bg='black', command=self.ab3)


        for i in range(len(self.userunit)):
            if self.userunit[i][6] == "W" and i == 0:
                self.canvas5.create_image(300, 50, anchor='n', image=self.userwarrior)
                self.canvas5.create_window(150, 100, anchor='n', window=self.userbutton1)
            if self.userunit[i][6] == "T" and i == 0:
                self.canvas5.create_image(300, 50, anchor='n', image=self.usertanker)
                self.canvas5.create_window(150, 100, anchor='n', window=self.userbutton1)
            if self.userunit[i][6] == "W" and i == 1:
                self.canvas5.create_image(300, 250, anchor='n', image=self.userwarrior)
                self.canvas5.create_window(150, 300, anchor='n', window=self.userbutton2)
            if self.userunit[i][6] == "T" and i == 1:
                self.canvas5.create_image(300, 250, anchor='n', image=self.usertanker)
                self.canvas5.create_window(150, 300, anchor='n', window=self.userbutton2)
            if self.userunit[i][6] == "W" and i == 2:
                self.canvas5.create_image(300, 450, anchor='n', image=self.userwarrior)
                self.canvas5.create_window(150, 500, anchor='n', window=self.userbutton3)
            if self.userunit[i][6] == "T" and i == 2:
                self.canvas5.create_image(300, 450, anchor='n', image=self.usertanker)
                self.canvas5.create_window(150, 500, anchor='n', window=self.userbutton3)

        for i in range(len(self.aiunit)):
            if self.aiunit[i][6] == "W" and i == 0:
                self.canvas5.create_image(780, 50, anchor='n', image=self.aiwarrior)
                self.canvas5.create_window(930, 100, anchor='n', window=self.aibutton1)
            if self.aiunit[i][6] == "T" and i == 0:
                self.canvas5.create_image(780, 50, anchor='n', image=self.aitanker)
                self.canvas5.create_window(930, 100, anchor='n', window=self.aibutton1)
            if self.aiunit[i][6] == "W" and i == 1:
                self.canvas5.create_image(780, 250, anchor='n', image=self.aiwarrior)
                self.canvas5.create_window(930, 300, anchor='n', window=self.aibutton2)
            if self.aiunit[i][6] == "T" and i == 1:
                self.canvas5.create_image(780, 250, anchor='n', image=self.aitanker)
                self.canvas5.create_window(930, 300, anchor='n', window=self.aibutton2)
            if self.aiunit[i][6] == "W" and i == 2:
                self.canvas5.create_image(780, 450, anchor='n', image=self.aiwarrior)
                self.canvas5.create_window(930, 500, anchor='n', window=self.aibutton3)
            if self.aiunit[i][6] == "T" and i == 2:
                self.canvas5.create_image(780, 450, anchor='n', image=self.aitanker)
                self.canvas5.create_window(930, 500, anchor='n', window=self.aibutton3)

        self.main_window.mainloop
""" used for gif 
class MyLabel(tk.Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        tk.Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)
"""

ipmain = IPMAIN()