from tkinter import * 
from tkinter import ttk 
from tkinter.messagebox import showinfo, askyesno, showerror
import os
import wget 
import shutil
from zipfile import ZipFile

print("Проверка обновлений, происходит консольная проверка")

url_down = "https://raw.githubusercontent.com/alfantasy/calcphysics/main/update.ini"
if wget.download(url_down, './update.ini'):
    print("Я СКАЧАЛ!")
print("\n")

if os.path.isfile('./version.ini'):
    version = open('version.ini', 'r')

if os.path.isfile('./update.ini'):
    update = open('update.ini', 'r')
try: 
    if os.path.isfile('./update.ini'):
        update_value = update.read()
        print(update_value)
    if os.path.isfile('./version.ini'):
        version_value = version.read()
        print(version_value)
finally:
    update.close()    
    os.remove("./update.ini")

update_window = Tk()
update_window.title("CalcPhysics - Updater")

def update_command():
    try: 
        if int(update_value) > int(version_value):
            print("\n" + str(update_value))
            if os.path.isdir('./image'):
                shutil.rmtree('image')
            else: 
                print("Директория изображений отсутствует. Загружаем...")
            if os.path.isfile('./physics.py'):
                os.remove('./physics.py')
            else:
                print('Мастер отсутствует. Устанавливаем программу!\n')
            try:
                if os.path.isfile('./version.ini'):
                    os.remove("./version.ini")
                else:
                    print('Обновляю файл версии!')    
            except PermissionError:
                print("Обновление текстового файла невозможно.")        
            url_main = "https://github.com/alfantasy/calcphysics/archive/refs/heads/main.zip"
            wget.download(url_main)
            arc = 'calcphysics-main.zip'
            with ZipFile(arc,'r') as zip_file:
                zip_file.extractall()
                folder_from = './calcphysics-main'
                folder_to = ''
                for f in os.listdir(folder_from):
                    if os.path.isfile(os.path.join(folder_from, f)):
                        shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
                    if os.path.isdir(os.path.join(folder_from, f)):
                        shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))
            os.remove("calcphysics-main.zip")       
            os.remove("./update.ini") 
            shutil.rmtree('calcphysics-main')
            showinfo(title="CalcPhysics - Updater", message="Обновление закончено. Программа обновления закрывается.")
            update_window.destroy()
        else: 
            if os.path.isdir('./image'):
                shutil.rmtree('image')
            else: 
                print("Директория изображений отсутствует. Загружаем...")
            if os.path.isfile('./physics.py'):
                os.remove('./physics.py')
            else:
                print('Мастер отсутствует. Устанавливаем программу!\n')
            try:
                if os.path.isfile('./version.ini'):
                    os.remove("./version.ini")
                else:
                    print('Обновляю файл версии!')    
            except PermissionError:
                print("Обновление текстового файла невозможно.")        
            url_main = "https://github.com/alfantasy/calcphysics/archive/refs/heads/main.zip"
            wget.download(url_main)
            arc = 'calcphysics-main.zip'
            with ZipFile(arc,'r') as zip_file:
                zip_file.extractall()
                folder_from = './calcphysics-main'
                folder_to = ''
                for f in os.listdir(folder_from):
                    if os.path.isfile(os.path.join(folder_from, f)):
                        shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
                    if os.path.isdir(os.path.join(folder_from, f)):
                        shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))
            os.remove("calcphysics-main.zip")       
            os.remove("./update.ini") 
            shutil.rmtree('calcphysics-main')
            showinfo(title="CalcPhysics - Installer", message="Установка закончена. Программа установки закрывается.")
            update_window.destroy()
    except NameError: 
        print("Файл, именуемый как version.ini отсутствует в папке назначения.")
        print("Исходя из этого планирую установку всего пакета.")
        if os.path.isdir('./image'):
            shutil.rmtree('image')
        else: 
            print("Директория изображений отсутствует. Загружаем...")
        if os.path.isfile('./physics.py'):
            os.remove('./physics.py')
        else:
            print('Мастер отсутствует. Устанавливаем программу!\n')
        if os.path.isfile('./version.ini'):
            os.remove("./version.ini")
        else:
            print('Обновляю файл версии!')    
        url_main = "https://github.com/alfantasy/calcphysics/archive/refs/heads/main.zip"
        wget.download(url_main)
        arc = 'calcphysics-main.zip'
        with ZipFile(arc,'r') as zip_file:
            zip_file.extractall()
            folder_from = './calcphysics-main'
            folder_to = ''
            for f in os.listdir(folder_from):
                if os.path.isfile(os.path.join(folder_from, f)):
                    shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
                if os.path.isdir(os.path.join(folder_from, f)):
                    shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))
        os.remove("calcphysics-main.zip")       
        os.remove("./update.ini") 
        shutil.rmtree('calcphysics-main')
        showinfo(title="CalcPhysics - Installer", message="Установка закончена. Программа установки закрывается.")
        update_window.destroy()


def check_update():
    if os.path.isfile("./version.ini") and os.path.isfile('./physics.py'): 
        if int(update_value) > int(version_value):
            if os.path.isfile('./physics.py'): 
                check_update_res = askyesno(title="CalcPhysics - Updater", message="Вышло новое обновление! Обновить?")
            else: 
                check_update_res = askyesno(title="CalcPhysics - Installer", message="Программа не установлена. Установить?")
            if check_update_res: update_command() 
            else: 
                result = Label(update_window,text="Вы отказались от обновления/установки программы!")
                result.pack(anchor=NW)
                result.after(10000,result.destroy)
                showinfo("CalcPhysics - Updater", "Программа обновления закрывается связи с отказом в обновлении/установки.")
                update_window.after(5000,update_window.destroy())
        else: 
            showinfo("CalcPhysics - Updater", "Обновление отсутствует! Программа установки автоматически закрывается.") 
            update_window.destroy()
    elif not os.path.isfile('./version.ini') and os.path.isfile('./physics.py'):
        check_version_res = askyesno(title="CalcPhysics - Installer", message="Файл версии программы отсутствует. Установить?")
        if check_version_res: 
            url_version = "https://raw.githubusercontent.com/alfantasy/calcphysics/main/version.ini"
            wget.download(url_version)
            showinfo("CalcPhysics - Installer", "Файл версии скачен. Закрываю программу установки.")
            update_window.after(5000,update_window.destroy())
        else: 
            result = Label(update_window,text="Вы отказались от установки некоторых файлов программы!")
            result.pack(anchor=NW)
            result.after(10000,result.destroy)
            showinfo("CalcPhysics - Updater", "Программа обновления закрывается связи с отказом в обновлении/установки.")
            update_window.after(5000,update_window.destroy())     
    else:
        check_update_res = askyesno(title="CalcPhysics - Installer", message="Программа не установлена. Установить?")
        if check_update_res: update_command() 
        else: 
            result = Label(update_window,text="Вы отказались от обновления/установки программы!")
            result.pack(anchor=NW)
            result.after(10000,result.destroy)
            showinfo("CalcPhysics - Updater", "Программа обновления закрывается связи с отказом в обновлении/установки.")
            update_window.after(5000,update_window.destroy())            
        

def check_setup():
    if os.path.isfile("./version.ini") and os.path.isfile('./physics.py'):
        showerror("CalcPhysics - Updater", "Программа уже установлена.")
    else: 
        check_setup_res = askyesno(title="CalcPhysics - Installer", message="Уверены в установке программы?")
        if check_setup_res: update_command()
        else: 
            result = Label(update_window,text="Вы отказались от установки.")
            result.pack(anchor=NW)
            result.after(10000,result.destroy)
            showinfo("CalcPhysics - Updater", "Программа обновления закрывается связи с отказом в установке.")
            update_window.after(5000,update_window.destroy())

try: 
    if int(update_value) > int(version_value):
        update_button = ttk.Button(update_window,text="Проверка обновления",command=check_update).pack(anchor=NW)
except NameError:
    print("Программа не установлена, либо отсутствуют файлы. Проверяю! ")
    if os.path.isfile("./version.ini") and os.path.isfile('./physics.py'): 
        update_button = ttk.Button(update_window,text="Проверка обновления",command=check_update).pack(anchor=NW)
    elif not os.path.isfile("./version.ini") or not os.path.isfile('./physics.py'):
        print("Программа возможно не установлена.")
        if os.path.isfile('./physics.py') and not os.path.isfile("./version.ini"):
            print("Отрицаю. Программа установлена, нет файла версии. Продолжать можно.")
            update_button = ttk.Button(update_window,text="Проверка обновления",command=check_update).pack(anchor=NW)
download_button = ttk.Button(update_window,text="Установка программы",command=check_setup).pack(anchor=NW)

update_window.mainloop()