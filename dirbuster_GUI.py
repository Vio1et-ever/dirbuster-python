import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from dirbuster_logic import async_dirbuster
import asyncio

filetype = []
list1=['php', 'txt', 'asp', 'aspx', 'jsp']
v = []


def run_dirbuster():
    output_text.delete(1.0, tk.END)  # 清空输出区域
    url = url_entry.get()
    wordlist = wordlist_entry.get()
    filetypes = filetype
    savefile = savefile_entry.get()
    asyncio.run(async_dirbuster(url, wordlist, filetypes, savefile, output_text))

# 选择fuzz文件
def select_wordlist():
    filename = filedialog.askopenfilename()
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, filename)

# 选择扫描文件类型
def select_filetype(item):
    filetype.append(item)

# 全选
def selectall():
  for index,item in enumerate(list1):
    v[index].set(item)
    filetype.append(item)

root = tk.Tk()
root.title("Dirbuster GUI")
root.geometry('600x500')

tk.Label(root, text="URL:").grid(row=0, column=0)
url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1)

tk.Label(root, text="Wordlist:").grid(row=1, column=0)
wordlist_entry = tk.Entry(root)
wordlist_entry.grid(row=1, column=1)
wordlist_button = tk.Button(root, text="Browse...", command=select_wordlist)
wordlist_button.grid(row=1, column=2)

tk.Label(root, text="File Types (comma-separated):").grid(row=2, column=0)
filetypes_entry = tk.Frame(root,pady=10,padx=15)
filetypes_entry.grid(row=2, column=1)
opt=tk.IntVar()
ttk.Radiobutton(filetypes_entry,text='全选',variable=opt,value=1,command=selectall).grid(row=0,column=0,sticky='w')
#设置勾选框，每四个换行
for index,item in enumerate(list1):
  v.append(tk.StringVar())
  ttk.Checkbutton(filetypes_entry,text=item,variable=v[-1],onvalue=item,offvalue='',command=lambda item=item:select_filetype(item)).grid(row=index//4+1,column=index%4,sticky='w')

tk.Label(root, text="Save Results To (optional):").grid(row=3, column=0)
savefile_entry = tk.Entry(root)
savefile_entry.grid(row=3, column=1)

start_button = tk.Button(root, text="Start Dirbuster", command=run_dirbuster)
start_button.grid(row=4, column=1)

output_text = scrolledtext.ScrolledText(root, height=10)
output_text.grid(row=5, column=0, columnspan=3)

root.mainloop()