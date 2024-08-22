#coding=GBK
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tm
import os
import platform
import cpuinfo as cpu
import psutil as ps
import socket
import uuid
import wmi
import subprocess as sp

def RestartPrinterServer():
    restart_printer_server_cmd_file="restartprintserver.cmd"
    result = os.popen(restart_printer_server_cmd_file).read()
    isSuccess(result)

def RestartExplorer():
    restart_explorer_cmd_file="restartexplorer.cmd"
    sp.Popen(restart_explorer_cmd_file)

def BlockUDisk():
    cmd_file = "blockudisk.cmd"
    result = os.popen(cmd_file).read()
    isSuccess(result)    

def UnblockUDisk():
    delete_registry_cmd_file="unblockudisk.cmd"
    result = os.popen(delete_registry_cmd_file).read()
    isSuccess(result) 

def OpenTaichoFile():
    pass

def ViewComputerInfo():
    computer_info_window=tk.Toplevel()
    computer_info_window.title("电脑信息浏览")
    computer_info_window.geometry("430x330")
    comp_info_label = tk.LabelFrame(computer_info_window,text="电 脑 信 息")
    cpu_label=tk.Label(comp_info_label,text="CPU:  ")
    os_label=tk.Label(comp_info_label,text="操作系统:  ")
    ram_label=tk.Label(comp_info_label,text="运行内存:  ")
    disk_label=tk.Label(comp_info_label,text="硬盘内存:  ")
    disk_seriesnumber_label=tk.Label(comp_info_label,text="硬盘序列号:  ")
    board_seriesnumber_label=tk.Label(comp_info_label,text="主板序列号:  ")
    ip_label=tk.Label(comp_info_label,text="IP:  ")
    mac_label=tk.Label(comp_info_label,text="物理地址:  ")
    
    # 获取CPU型号
    cpu_label.grid(row=0,column=0,ipady=5)
    cpu_result=cpu.get_cpu_info().get("brand_raw","未知型号")
    cpu_label_result = tk.Label(comp_info_label,text=cpu_result)
    cpu_label_result.grid(row=0,column=1,ipady=5)
    # 获取操作系统信息
    os_label.grid(row=1,column=0,ipady=5)
    os_version=platform.platform()
    os_version_result = tk.Label(comp_info_label,text=os_version)
    os_version_result.grid(row=1,column=1,ipady=5)
    # 获取运行内存
    ram_label.grid(row=2,column=0,ipady=5)
    ram_info=ps.virtual_memory().total/(1024**3)
    ram_info_result = tk.Label(comp_info_label,text=str(format(ram_info,'.0f'))+" GB")
    ram_info_result.grid(row=2,column=1,ipady=5)
    # 获取硬盘内存
    disk_label.grid(row=3,column=0,ipady=5)
    disk_info=ps.disk_usage('/').total/(1024**3)
    disk_info_result = tk.Label(comp_info_label,text=str(format(disk_info,'.0f'))+" GB")
    disk_info_result.grid(row=3,column=1,ipady=5)
    # 获取硬盘序列号
    disk_seriesnumber_label.grid(row=4,column=0,ipady=5)
    wmi_driver=wmi.WMI()
    disk_seriesnumber_values=[]
    for disk_seriesnumber_value in wmi_driver.Win32_DiskDrive():
        disk_seriesnumber_values.append(disk_seriesnumber_value.SerialNumber)
    for index in range(len(disk_seriesnumber_values)):
        disk_label=tk.Label(comp_info_label,text=disk_seriesnumber_values[index])
        disk_label.grid(row=4,column=index+1,ipady=5)
    # 获取主板序列号
    board_seriesnumber_label.grid(row=5,column=0,ipady=5)
    board_serialnumber_values=wmi_driver.Win32_BaseBoard()
    for serial_number in board_serialnumber_values:
        if serial_number:
            board_serialnumber_value_label=tk.Label(comp_info_label,text=serial_number.SerialNumber)
            board_serialnumber_value_label.grid(row=5,column=1,ipady=5)
    # 获取IP地址
    ip_label.grid(row=6,column=0,ipady=5)
    ip_address=socket.gethostbyname(socket.gethostname())
    ip_address_result = tk.Label(comp_info_label,text=ip_address)
    ip_address_result.grid(row=6,column=1,ipady=5)
    # 获取MAC地址
    mac_label.grid(row=7,column=0,ipady=5)
    mac=uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    upper_mac="-".join([mac[e:e+2] for e in range(0,11,2)])
    mac_address_result=tk.Label(comp_info_label,text=upper_mac)
    mac_address_result.grid(row=7,column=1,ipady=5)
    # 加载标签框架
    comp_info_label.pack(padx=15,pady=15,ipadx=550,ipady=550)


def PauseUpdate():
    pause_update_cmd_file="pauseupdate.cmd"
    result = os.popen(pause_update_cmd_file).read()
    isSuccess(result)

def showWindow():
    root_window = tk.Tk()
    root_window.title("整合工具")
    root_window.geometry("600x300")
    restart_server_button = tk.Button(root_window,text="重 启 打 印 服 务",height=2,width=20,command=RestartPrinterServer)
    restart_server_button.grid(row=0,column=0,padx=20,pady=5)
    restart_explorer_button = tk.Button(root_window,text="重 启 任 务 栏",height=2,width=20,command=RestartExplorer)
    restart_explorer_button.grid(row=0,column=1,padx=20)
    block_u_disk = tk.Button(root_window,text="封 禁 U 口",height=2,width=20,command=BlockUDisk)
    block_u_disk.grid(row=0,column=2,padx=20)
    unblock_u_disk = tk.Button(root_window,text="解 封 U 口",height=2,width=20,command=UnblockUDisk)
    unblock_u_disk.grid(row=1,column=0,padx=20,pady=5)
    taicho_file_open = tk.Button(root_window,text="打 开 台 账",height=2,width=20,command=OpenTaichoFile)
    taicho_file_open.grid(row=1,column=1,padx=20)
    view_computer_info = tk.Button(root_window,text="查 看 电 脑 信 息",height=2,width=20,command=ViewComputerInfo)
    view_computer_info.grid(row=1,column=2,padx=20)
    pause_windows_update = tk.Button(root_window,text="暂 停 更 新 至 2999 年",height=2,width=20,command=PauseUpdate)
    pause_windows_update.grid(row=2,column=0,padx=20,pady=5)
    root_window.mainloop()

def isSuccess(result_ref):
    if result_ref.count("success") > 0:
        tm.showinfo("信息","执行成功!") 
    else:
        tm.showerror("错误","程序运行出错！")

if __name__=="__main__":
    showWindow()
    
