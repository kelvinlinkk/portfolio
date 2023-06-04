import tkinter as tk
import subprocess
import os

def check_git_status():
    result = subprocess.run(["git", "status"], capture_output=True, text=True,shell=True)
    output = result.stdout
    text_area.delete(1.0, tk.END)
    if(output != "On branch master\nYour branch is up to date with 'origin/master'.\n\nnothing to commit, working tree clean\n"):
        text_area.insert(tk.END, output)
        subprocess.run(["git", "add","."])
    else:
        text_area.insert(tk.END, "nothting to change")
def commit_text():
    text = text_entry.get()
    subprocess.run(["git", "commit","-m",text])
    subprocess.run(["git", "push"])


# 建立主視窗
window = tk.Tk()

# 建立檢測按鈕
check_button = tk.Button(window, text="檢測Git狀態", command=check_git_status)
commit_button = tk.Button(window, text="commit & push", command=commit_text)
# 建立文字區域
text_area = tk.Text(window)
text_entry = tk.Entry(window)
# 放置元件
check_button.pack()
text_area.pack()
commit_button.pack()
text_entry.pack()

# 啟動主迴圈
window.mainloop()
