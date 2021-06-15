from tkinter import *
import math, random, os
import Database
import Model
from tkinter import messagebox



class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "grey"
        title = Label(self.root, text="BILL PAYMENT  ", bd=15, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # ================Variables==========================
        # =========
        # =======Cosemetics==========================
        self.db=Database.DBconnect()




        self.Burger = IntVar()
        self.Pizza = IntVar()
        self.French_fries = IntVar()
        self.Chicken_chilly = IntVar()
        self.Chowein = IntVar()
        self.Selroti = IntVar()

        self.customer_name=StringVar()
        self.phone_number=StringVar()

        # ================Grocery==========================

        self.DalBhat = IntVar()
        self.Newari_khaja = IntVar()
        self.Thakali_food = IntVar()
        self.Fish_curry= IntVar()
        self.Fried_rice = IntVar()
        self.Momo = IntVar()

        # ================Cold Drinks==========================

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ================Total Product Price & Tax variables==========================

        self.list1_price = StringVar()
        self.list2_price = StringVar()
        self.cold_drink_price = StringVar()

        self.list1_tax = StringVar()
        self.list2_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ================Cutomers==================================

        self.c_name = StringVar()
        self.c_phon = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)

        self.bill_no.set(str(x))



        # =============Customer Details Frame
        F1 = LabelFrame(self.root, bd=8, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,

                                                                                pady=5,
                                                                                                             padx=10)


        cphn_lbl = Label(F1, text="Contact No", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,


            pady=5   ,                                                                  padx=10)

        sav_btn=Button(F1,text="Save",bg=bg_color, fg="White", font=("times new roman", 18, "bold"),command=self.save_btn).grid(
            row=0, column=5, padx=20, pady=5)









        # ==================list1 Frame==========

        F2 = LabelFrame(self.root, bd=8, text="list1", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text="Burger", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.Burger, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Pizza", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10, textvariable=self.Pizza, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Fcae_w_lbl = Label(F2, text="French Fries", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10, textvariable=self.French_fries, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Chicken chilly", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10, textvariable=self.Chicken_chilly, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Chowein", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.Chowein, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_lbl = Label(F2, text="Selroti", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=10, textvariable=self.Selroti, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================list2 Frame==========

        F3 = LabelFrame(self.root, bd=8, text="list2", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="DalBhat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.DalBhat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Newari khaja", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.Newari_khaja, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Thakali food", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.Thakali_food, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Fish curry", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.Fish_curry, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Fried rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.Fried_rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Momo", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.Momo, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================Cold Drink Frame==========

        F4 = LabelFrame(self.root, bd=8, text="Cold Drinks", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F4.place(x=675, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coca Cola", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)





         #=======================
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)

        bill_title = Label(F5, text="BILL AREA", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ==============Button Frame=============

        F6 = LabelFrame(self.root, bd=8, text="BILL MENU", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total list1 Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.list1_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total list2 Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.list2_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="list1 Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.list1_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="list2 Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.list2_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=740, width=590, height=102)

        total_btn = Button(btn_F, text="Total", bg="cadetblue", fg="white", pady=15, bd=4, width=10,command=self.total,
                           font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", bg="cadetblue", fg="white", pady=15,command=self.bill_area,
                           bd=4, width=10, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", pady=15, bd=4,command=self.clear_data,
                           width=10, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", pady=15, bd=4,
                          width=10, font="arial 14 bold").grid(row=0, column=3, padx=4, pady=5)
    def exit(self):
        self.add()
        self.root.destroy()

        self.welcome_bill()

    def total(self):
            self.c_s_p = self.Burger.get() * 80
            self.c_fc_p = self.Pizza.get() * 300
            self.c_fw_p = self.French_fries.get() * 150
            self.c_hs_p = self.Chicken_chilly.get() * 180
            self.c_hg_p = self.Chowein.get() * 140
            self.c_bl_p = self.Selroti.get() * 100
            self.total_cosemetic_price = float(
                self.c_s_p +
                self.c_fc_p +
                self.c_fw_p +
                self.c_hs_p +
                self.c_hg_p +
                self.c_bl_p
            )
            self.list1_price.set("Rs. " + str(self.total_cosemetic_price))
            self.c_tax = round((self.total_cosemetic_price * 0.05), 2)
            self.list1_tax.set("Rs. " + str(self.c_tax))

            self.g_r_p = self.DalBhat.get() * 250
            self.g_f_p = self.Newari_khaja.get() * 200
            self.g_d_p = self.Thakali_food.get() * 300
            self.g_w_p = self.Fish_curry.get() * 180
            self.g_s_p = self.Fried_rice.get() * 150
            self.g_t_p = self.Momo.get() * 180

            self.total_grocery_price = float(
                self.g_r_p +
                self.g_f_p +
                self.g_d_p +
                self.g_w_p +
                self.g_s_p +
                self.g_t_p
            )
            self.list2_price.set("Rs. " + str(self.total_grocery_price))
            self.g_tax = round((self.total_grocery_price * 0.1), 2)
            self.list2_tax.set("Rs. " + str(self.g_tax))

            self.d_m_p = self.maza.get() * 60
            self.d_c_p = self.cock.get() * 60
            self.d_f_p = self.frooti.get() * 50
            self.d_t_p = self.thumbsup.get() * 45
            self.d_l_p = self.limca.get() * 40
            self.d_s_p = self.sprite.get() * 60
            self.total_drinks_price = float(
                self.d_m_p +
                self.d_c_p +
                self.d_f_p +
                self.d_t_p +
                self.d_l_p +
                self.d_s_p
            )
            self.cold_drink_price.set("Rs. " + str(self.total_drinks_price))
            self.d_tax = round((self.total_drinks_price * 0.05), 2)
            self.cold_drink_tax.set("Rs. " + str(self.d_tax))

            self.Total_bill = float(
                self.total_cosemetic_price +
                self.total_grocery_price +
                self.total_drinks_price +
                self.c_tax +
                self.g_tax +
                self.d_tax
            )

    def clear_data(self):
        op = messagebox.askyesno("Clearing...", "Do You Really Want to Clear All data")
        if op > 0:
            # ================Cosemetics==========================

            self.Burger.set("")
            self.Pizza.set("")
            self.French_fries.set("")
            self.Chicken_chilly.set("")
            self.Chowein.set("")
            self.Selroti.set("")

            # ================Grocery==========================

            self.DalBhat.set("")
            self.Newari_khaja.set("")
            self.Thakali_food.set("")
            self.Fish_curry.set("")
            self.Fried_rice.set("")
            self.Momo.set("")

            # ================Cold Drinks==========================

            self.maza.set("")
            self.cock.set("")
            self.frooti.set("")
            self.thumbsup.set("")
            self.limca.set("")
            self.sprite.set("")

            # ================Total Product Price & Tax variables==========================

            self.list1_price.set("")
            self.list2_price.set("")
            self.cold_drink_price.set("")

            self.list1_tax.set("")
            self.list2_tax.set("")
            self.cold_drink_tax.set("")

            # ================Cutomers==================================

            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)

            self.bill_no.set(str(x))


            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do You Really Want to Exit")
        if op > 0:
            self.root.destroy()


    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome to online food service \n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n ====================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n ====================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.list1_price.get() == "Rs. 0.0" and self.list2_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # ========Cosemetics==========
            if self.Burger.get() != 0:
                self.txtarea.insert(END, f"\n Burger\t\t{self.Burger.get()}\t\t{self.c_s_p}")

            if self.Pizza.get() != 0:
                self.txtarea.insert(END, f"\n Pizza\t\t{self.Pizza.get()}\t\t{self.c_fc_p}")

            if self.French_fries.get() != 0:
                self.txtarea.insert(END, f"\n French fries\t\t{self.French_fries.get()}\t\t{self.c_fw_p}")

            if self.Chicken_chilly.get() != 0:
                self.txtarea.insert(END, f"\n Chiken chilly\t\t{self.Chicken_chilly.get()}\t\t{self.c_hs_p}")

            if self.Chowein.get() != 0:
                self.txtarea.insert(END, f"\n Chowein\t\t{self.Chowein.get()}\t\t{self.c_hg_p}")

            if self.Selroti.get() != 0:
                self.txtarea.insert(END, f"\n Selroti\t\t{self.Selroti.get()}\t\t{self.c_bl_p}")

            # ========Grocery==========
            if self.DalBhat.get() != 0:
                self.txtarea.insert(END, f"\n DalBhat\t\t{self.DalBhat.get()}\t\t{self.g_r_p}")

            if self.Newari_khaja.get() != 0:
                self.txtarea.insert(END, f"\n Newari Khaja\t\t{self.Newari_khaja.get()}\t\t{self.g_f_p}")

            if self.Thakali_food.get() != 0:
                self.txtarea.insert(END, f"\n Thakali food\t\t{self.Thakali_food.get()}\t\t{self.g_d_p}")

            if self.Fish_curry.get() != 0:
                self.txtarea.insert(END, f"\n Fish curry\t\t{self.Fish_curry.get()}\t\t{self.g_w_p}")

            if self.Fried_rice.get() != 0:
                self.txtarea.insert(END, f"\n Fried rice\t\t{self.Fried_rice.get()}\t\t{self.g_s_p}")

            if self.Momo.get() != 0:
                self.txtarea.insert(END, f"\n Momo\t\t{self.Momo.get()}\t\t{self.g_t_p}")

            # ========Cold Drinks==========
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")

            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.cock.get()}\t\t{self.d_c_p}")

            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, f"\n ------------------------------------")
            if self.list1_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n list1 Tax\t\t{self.list1_tax.get()}")
            if self.list2_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n list2 Tax\t\t{self.list2_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n ------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Saving Bill.....", "please save the bill and pay money to our deliver")

        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saving.....",
                                f"{self.c_name.get()} Your Bill No : {self.bill_no.get()}  Successfully Saved please see the Bills folder on bill directory to see your Bills")
        else:
            return

    def save_btn(self):
        cname=self.c_name.get()
        pho=self.c_phon.get()

        u=Model.nishan(cname,pho)
        query = "insert into customer(customer_name,phone) values(%s,%s)"
        values = (
            u.get_customer_name(),u.get_phone())

        self.db.insert(query,values)
        messagebox.showinfo('Success', 'successfully saved data')


root=Tk()
Bill_App(root)
root.mainloop()


