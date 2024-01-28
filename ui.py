import customtkinter
import threading
import yaml

import task

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("account")
        self.add("mod")
        # add widgets on tabs
        # self.label = customtkinter.CTkLabel(master=self.tab("account"))
        # self.label.grid(row=0, column=0, padx=20, pady=10)

class UI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # 設定 UI 外觀和主題
        customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.loaded_data = task.getLoadData()

        # 設置主視窗
        self.geometry("550x650")
        self.grid_columnconfigure((0, 1), weight=1)
        self.title("QwQ_Bot")
        self.iconbitmap('OwO_image.ico')

        #tab
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=(20,10), sticky="ewsn")

        # Use CTkButton instead of tkinter Button
        self.textbox_width = 250
        
        self.button_start = customtkinter.CTkButton(self, text="Start", command=self.buttonStart)
        self.button_start.grid(row=1, column=0, padx=20, pady=10, sticky="ewsn", columnspan=2)

        # tab account
        self.label_chrome_path = customtkinter.CTkLabel(self.tab_view.tab('account'), text='chrome_path', anchor="w")
        self.label_chrome_path.grid(row=0, column=0, padx=20, pady=(10,5), sticky="ew")
        self.label_email = customtkinter.CTkLabel(self.tab_view.tab('account'), text='email', anchor="w")
        self.label_email.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        self.label_password = customtkinter.CTkLabel(self.tab_view.tab('account'), text='password', anchor="w")
        self.label_password.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        self.label_name = customtkinter.CTkLabel(self.tab_view.tab('account'), text='name', anchor="w")
        self.label_name.grid(row=3, column=0, padx=20, pady=5, sticky="ew")
        self.label_name_at = customtkinter.CTkLabel(self.tab_view.tab('account'), text='name_at', anchor="w")
        self.label_name_at.grid(row=4, column=0, padx=20, pady=5, sticky="ew")
        self.label_url = customtkinter.CTkLabel(self.tab_view.tab('account'), text='url', anchor="w")
        self.label_url.grid(row=5, column=0, padx=20, pady=5, sticky="ew")
        self.label_urlcommon = customtkinter.CTkLabel(self.tab_view.tab('account'), text='urlcommon(beepboop)', anchor="w")
        self.label_urlcommon.grid(row=6, column=0, padx=20, pady=5, sticky="ew")
        self.label_urlspam = customtkinter.CTkLabel(self.tab_view.tab('account'), text='urlspam', anchor="w")
        self.label_urlspam.grid(row=7, column=0, padx=20, pady=5, sticky="ew")
        self.label_loop = customtkinter.CTkLabel(self.tab_view.tab('account'), text='loop', anchor="w")
        self.label_loop.grid(row=8, column=0, padx=20, pady=5, sticky="ew")
        self.label_token = customtkinter.CTkLabel(self.tab_view.tab('account'), text='token', anchor="w")
        self.label_token.grid(row=9, column=0, padx=20, pady=5, sticky="ew")

        self.tb_chrome_path = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_chrome_path.insert('0.0', self.loaded_data['account']['chrome_path'])
        self.tb_chrome_path.grid(row=0, column=1, padx=20, pady=(10,5), sticky="ew")
        self.tb_email = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_email.grid(row=1, column=1, padx=20, pady=5, sticky="ew")
        self.tb_email.insert('0.0', self.loaded_data['account']['email'])
        self.tb_password = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_password.grid(row=2, column=1, padx=20, pady=5, sticky="ew")
        self.tb_password.insert('0.0', self.loaded_data['account']['password'])
        self.tb_name = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_name.grid(row=3, column=1, padx=20, pady=5, sticky="ew")
        self.tb_name.insert('0.0', self.loaded_data['account']['name'])
        self.tb_name_at = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_name_at.grid(row=4, column=1, padx=20, pady=5, sticky="ew")
        self.tb_name_at.insert('0.0', self.loaded_data['account']['name_at'])
        self.tb_url = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_url.grid(row=5, column=1, padx=20, pady=5, sticky="ew")
        self.tb_url.insert('0.0', self.loaded_data['account']['url'])
        self.tb_urlcommon = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_urlcommon.grid(row=6, column=1, padx=20, pady=5, sticky="ew")
        self.tb_urlcommon.insert('0.0', self.loaded_data['account']['urlcommon'])
        self.tb_urlspam = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_urlspam.grid(row=7, column=1, padx=20, pady=5, sticky="ew")
        self.tb_urlspam.insert('0.0', self.loaded_data['account']['urlspam'])
        self.tb_loop = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_loop.grid(row=8, column=1, padx=20, pady=5, sticky="ew")
        self.tb_loop.insert('0.0', self.loaded_data['account']['loop'])
        self.tb_token = customtkinter.CTkTextbox(self.tab_view.tab('account'), height=10, width=self.textbox_width)
        self.tb_token.grid(row=9, column=1, padx=20, pady=5, sticky="ew")
        self.tb_token.insert('0.0', self.loaded_data['account']['token'])

        self.button_save_account = customtkinter.CTkButton(self.tab_view.tab('account'), text="Save", command=self.saveAccount)
        self.button_save_account.grid(row=10, column=0, padx=20, pady=20, sticky="ew")
        self.label_save_account_success_text = customtkinter.CTkLabel(self.tab_view.tab('account'), text='', anchor="w")
        self.label_save_account_success_text.grid(row=10, column=1, padx=20, pady=5, sticky="ew")
        # .config(text=new_text)

        # tab prob
        self.label_prob = []
        self.tb_prob = []
        for i, mod in enumerate(self.loaded_data['mod']):
            command = mod['command']
            prob = mod['prob']
            label = customtkinter.CTkLabel(self.tab_view.tab('mod'), text=command, anchor="w")
            label.grid(row=i, column=0, padx=20, pady=(10,5), sticky="ew")
            self.label_prob.append(label)
            tb = customtkinter.CTkTextbox(self.tab_view.tab('mod'), height=10, width=self.textbox_width)
            tb.insert('0.0', prob)
            tb.grid(row=i, column=1, padx=20, pady=(10,5), sticky="ew")
            self.tb_prob.append(tb)

        self.button_save_mod = customtkinter.CTkButton(self.tab_view.tab('mod'), text="Save", command=self.saveMod)
        self.button_save_mod.grid(row=len(self.loaded_data['mod']), column=0, padx=20, pady=20, sticky="ew")
        self.label_save_mod_success_text = customtkinter.CTkLabel(self.tab_view.tab('mod'), text='', anchor="w")
        self.label_save_mod_success_text.grid(row=len(self.loaded_data['mod']), column=1, padx=20, pady=5, sticky="ew")

    def saveMod(self):
        for i in range(len(self.label_prob)):
            self.loaded_data['mod'][i]['prob'] = self.tb_prob[i].get("0.0", customtkinter.END).strip()
        if task.saveLoadData(self.loaded_data):
            self.label_save_mod_success_text.configure(text='Save success!!')

    def saveAccount(self):
        self.loaded_data['account']['chrome_path'] = self.tb_chrome_path.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['email'] = self.tb_email.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['password'] = self.tb_password.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['name'] = self.tb_name.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['name_at'] = self.tb_name_at.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['url'] = self.tb_url.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['urlcommon'] = self.tb_urlcommon.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['urlspam'] = self.tb_urlspam.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['loop'] = self.tb_loop.get("0.0", customtkinter.END).strip()
        self.loaded_data['account']['token'] = self.tb_token.get("0.0", customtkinter.END).strip()
        if task.saveLoadData(self.loaded_data):
            self.label_save_account_success_text.configure(text='Save success!!')

    def buttonStart(self):
        print("Start!")
        task_thread = threading.Thread(target=task.dc_task)
        task_thread.start()

if __name__ == "__main__":
    # 在單獨的文件中執行時，創建 UI 並啟動主迴圈
    ui = UI()
    ui.mainloop()