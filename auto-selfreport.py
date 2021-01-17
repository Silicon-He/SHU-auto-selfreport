# -*- coding = utf-8 -*-
# @Author:Silicon He
# @Time:2020/11/12 10:03
# @File:demo11.12.py
# @Software:PyCharm

from selenium import webdriver
import tkinter as tk
import os, time
import tkinter.messagebox
from bs4 import BeautifulSoup
from threading import Timer


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    with open('login_info.txt', 'r+') as f:
        name_info = f.readlines()
        for i in name_info:
            if usr_name in i:
                tkinter.messagebox.showinfo('warning', '账号已存在')
                return None

        f.write('\n' + usr_name + '*')
        for s in usr_pwd:
            temp = str(ord(s) - 20)
            f.write(temp + '*')
        tkinter.messagebox.showinfo('success', '账号添加成功')
        f.close()



def read_usr_info():
    name, password, temp = [], [], []
    with open('login_info.txt', 'r+',encoding='utf-8') as f:
        info = list(f.readlines())
        driver_path = info[0]
        for data in info[1:]:
            if data != '\n':
                data = data.split('*')
                name.append(data[0])
                temp = ''
                for n in data[1:-1]:
                    temp = temp + (str(chr(int(n) + 20)))
                password.append(temp)
        f.close()
    return name, password,driver_path


def submit():
    username_list, password_list,driver_path = read_usr_info()

    dic = dict(zip(username_list, password_list))

    for username in dic.keys():

        chromedriver = driver_path.strip()

        os.environ['webdriver.Chrome.driver'] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        try:
            driver.get('https://selfreport.shu.edu.cn/')
        except:
            tkinter.messagebox.showinfo('warning', '请连接校园网')
        driver.refresh()
        title = driver.title

        if title == '上海大学统一身份认证':
            time.sleep(1)
            login(username, dic[username], driver)
            if username[:2] == '10':
                position_flag = 1
            else:
                position_flag = 0
            found_not_report(driver,position_flag)
            driver.close()

    shotdown()


def login(username, password, driver):
    driver.find_element_by_id('username').click()
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(username)
    time.sleep(1)
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(1)
    driver.find_element_by_id('submit').click()
    print('账号%s登录成功' % username)
    time.sleep(1)


def found_not_report(driver,position_flag):
    if position_flag == 0:
        driver.get('https://selfreport.shu.edu.cn/XueSFX/HalfdayReport_History.aspx')
    else:
        driver.get('https://selfreport.shu.edu.cn/ReportHistory.aspx')

    source = driver.page_source
    bs_html = BeautifulSoup(source, 'lxml')

    localtime = time.localtime(time.time())
    new_time = list(localtime)
    print("现在时间为 :%d年%d月%d日%d时%d分" % (new_time[0], new_time[1], new_time[2], new_time[3], new_time[4]))
    cnt = 1
    if position_flag == 0:
        for item in bs_html.find_all("a"):

            link = str(item.get("href"))

            if new_time[3] < 20 and cnt == 1:
                cnt += 1
                continue

            if 'View' not in link and 'XueSFX' in link:
                tar_link = 'https://selfreport.shu.edu.cn' + link
                print(tar_link)
                time.sleep(0.5)
                driver.get(tar_link)
                report(driver,position_flag)


    if position_flag == 1:
        link = 'https://selfreport.shu.edu.cn/DayReport.aspx?day={}-{}-{}'.format(new_time[0], new_time[1], new_time[2])
        print(link)
        driver.get(link)
        report(driver, position_flag)


def report(driver,position_flag):
    # driver.find_element_by_id('lbReport').click()
    # time.sleep(1)
    if position_flag == 0:
        time.sleep(1)
        driver.find_element_by_id("p1_ChengNuo-inputEl-icon").click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_0-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('p1_TiWen-inputEl').send_keys('36.5')
        time.sleep(0.5)
        driver.find_element_by_id('fineui_6-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_12-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_14-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_18-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_20-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_27-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('p1_ctl00_btnSubmit').click()
        time.sleep(1)
        driver.find_element_by_id('fineui_37').click()

    else:
        driver.find_element_by_id("p1_ChengNuo-inputEl-icon").click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_0-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_6-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_21-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_23-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_27-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_29-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_31-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_36-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('fineui_37-inputEl-icon').click()
        time.sleep(0.5)
        driver.find_element_by_id('p1_ctl00_btnSubmit').click()
        time.sleep(1)
        driver.find_element_by_id('fineui_42').click()


def shotdown():
    flag = v1.get()
    if flag == 1:
        os.system('shutdown -s -t 60')
    else:
        pass


def delay():
    flag1 = v2.get()
    flag2 = v3.get()
    localtime = time.localtime(time.time())
    new_time = list(localtime)
    print("现在时间为 :%d年%d月%d日%d时%d分" % (new_time[0], new_time[1], new_time[2], new_time[3], new_time[4]))

    if flag1 == 1 and flag2 == 0:
        n = int(time_delay_num.get())
        print('%d分钟后打卡' % n)
        t = Timer(n * 60, submit)
        t.start()
    elif flag2 == 1:
        localtime = time.localtime(time.time())
        new_time = list(localtime)
        delay_time = ((24 - new_time[3]) * 60 - new_time[4] + 2)
        print('%d分钟后打卡(00:02)' % delay_time)
        t = Timer(delay_time * 60, submit)
        t.start()
    else:
        submit()


def about():
    tkinter.messagebox.showinfo('关于', '作者:Silicon He')



if __name__ == '__main__':
    window = tk.Tk()

    window.title('每日一报助手')
    window.geometry('500x580')


    menubutton = tk.Menubutton(window, text='帮助', relief="raised")
    filemenu = tk.Menu(menubutton, tearoff=False)
    filemenu.add_checkbutton(label="关于", command=about, selectcolor="yellow")
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=window.quit)
    menubutton.config(menu=filemenu)
    menubutton.place(x=10, y=360)


    canvas = tk.Canvas(window, width=440, height=350, bg='green')
    image_file = tk.PhotoImage(file='gui_img.gif')
    image = canvas.create_image(200, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    tk.Label(window, text='欢迎使用每日一报助手~ \n 若无法打开网页请连接校园网', font=('Arial', 16)).pack()


    var = tk.StringVar()
    tk.Label(window, text='账号:', font=('Arial', 14)).place(x=50, y=440)
    tk.Label(window, text='密码:', font=('Arial', 14)).place(x=50, y=480)


    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14), width=16)
    entry_usr_name.place(x=100, y=440)
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*', width=16)
    entry_usr_pwd.place(x=100, y=480)


    time_delay_num = tk.Spinbox(from_=0, to=300, width=4)
    time_delay_num.place(x=435, y=473)


    btn_login = tk.Button(window, text='添加账号', command=usr_login)
    btn_login.place(x=100, y=510)
    btn_login = tk.Button(window, text='开始每日一报', command=delay)
    btn_login.place(x=200, y=510)


    v1, v2, v3 = tk.IntVar(), tk.IntVar(), tk.IntVar()
    shot_down_flag = tk.Checkbutton(window, text="打卡完60s后关机", variable=v1,onvalue=1, offvalue=0)
    shot_down_flag.place(x=300, y=440)

    delay_flag = tk.Checkbutton(window, text="是否延时打卡(min)", variable=v2,onvalue=1, offvalue=0)
    delay_flag.place(x=300, y=470)

    zero_submit = tk.Checkbutton(window, text="是否过零点自动打卡", variable=v3,onvalue=1, offvalue=0)
    zero_submit.place(x=300, y=500)

    window.mainloop()
