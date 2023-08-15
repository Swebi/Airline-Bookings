import customtkinter
import tkinter as tk
from tkinter import ttk

import tkintermapview

import mysql.connector as sqlcon

from tkinter import messagebox
from PIL import ImageTk,Image

import time

# Importing the geodesic module from the library

from geopy.distance import geodesic
from geopy.geocoders import Nominatim


global username


def paymentwin():
    app = customtkinter.CTkToplevel()
    app.geometry("1920x1080")
    app.title("Airline Bookings")
    app.configure(fg_color="#272f32")

    bg = customtkinter.CTkImage(dark_image=Image.open("grad10.jpg"), size=(1920, 1080))
    bglabel = customtkinter.CTkLabel(master=app, text="", image=bg)
    bglabel.place(relx=0, rely=0)

    headinglabel = customtkinter.CTkLabel(master=app, text="Fly+ Bookings", fg_color='black', width=1920, height=90,
                                          font=("Impact", 70))  # width=1000,corner_radius=25,fg_color='darkblue',
    headinglabel.pack(padx=0, pady=0)

    pay_frame = customtkinter.CTkFrame(master=app, width=800, height=570, fg_color="transparent",
                                          border_width=10,
                                          border_color="black")  # ,border_width=2,border_color="black"
    pay_frame.pack(padx=20, pady=150)
    pay_frame.pack_propagate(False)

    paylabel = customtkinter.CTkLabel(master=pay_frame, text="Thank You For \n Booking With Fly+", fg_color='transparent',

                                         font=("Impact", 80))  # width = 1000,,corner_radius=25,fg_color='darkblue',
    paylabel.pack(padx=0, pady=40)

    blanklabel = customtkinter.CTkLabel(master=pay_frame, text="", fg_color='transparent',
                                        height=20)  # width = 1000,,corner_radius=25,fg_color='darkblue',font=("Comfortaa",30)
    blanklabel.pack(padx=0, pady=15)

    exitbutton = customtkinter.CTkButton(master=pay_frame, text="Exit", text_color="black", width=400, height=80,
                                       border_width=0, corner_radius=8,
                                          fg_color="#8bbad0", hover_color="#3d525c", font=("Comfortaa", 40, "bold"),
                                          command=app.destroy)
    exitbutton.pack(padx=0, pady=15)




def mapwin():





    app = customtkinter.CTkToplevel()
    app.geometry("1920x1080")
    app.title("Airline Bookings")
    app.configure(fg_color="#272f32")

    bg = customtkinter.CTkImage(dark_image=Image.open("grad14.jpg"), size=(1920, 1080))
    bglabel = customtkinter.CTkLabel(master=app, text="", image=bg)
    bglabel.place(relx=0, rely=0)

    headinglabel = customtkinter.CTkLabel(master=app, text="Fly+ Bookings", fg_color='black', width=1920, height=90,
                                          font=("Impact", 70))  # width=1000,corner_radius=25,fg_color='darkblue',
    headinglabel.pack(padx=0, pady=0)

    detail_frame = customtkinter.CTkFrame(master=app, width=1000, height=900, fg_color="#272f32", border_width=10,
                                          border_color="black")  # ,border_width=2,border_color="black"
    detail_frame.pack(padx=50, pady=50, side = tk.LEFT)
    detail_frame.pack_propagate(False) #to make sure it doesn't get resized

    data_frame = customtkinter.CTkFrame(master=app, width=800, height=1200, fg_color="#272f32", border_width=10,
                                          border_color="black")  # ,border_width=2,border_color="black"
    data_frame.pack(padx=120, pady=150, side=tk.LEFT)
    data_frame.pack_propagate(False)  # to make sure it doesn't get resized


    customerid = tk.StringVar()
    departuredate = tk.StringVar()
    departurelocationvar = tk.StringVar()
    arrivallocationvar = tk.StringVar()
    seatclassvar = tk.StringVar()
    seatmealvar = tk.StringVar()
    airlinevar = tk.StringVar()

    def update_label(event):
        event = print()
        arrivallocationvalue = arrivallocationvar.get()
        departurelocationvalue=departurelocationvar.get()


        geolocator = Nominatim(user_agent="MyApp")
        arrivalvalue = (geolocator.geocode(arrivallocationvalue).latitude, geolocator.geocode(arrivallocationvalue).longitude)
        departurevalue = (geolocator.geocode(departurelocationvalue).latitude, geolocator.geocode(departurelocationvalue).longitude)

        distancebet = round(geodesic(arrivalvalue, departurevalue).km)
        cost = round(distancebet * 4)

        distance_lbl.configure(text=distancebet)
        fare.configure(text=cost)

        price=cost

        if seatclassvar.get()=="First":
            price=price+cost*1
        elif seatclassvar.get()=="Business":
            price=price+cost*0.5
        else:
            price=cost

        if seatmealvar.get()=="Non-Vegetarian":
            price+=500
        elif seatmealvar.get()=="Vegetarian":
            price+=300
        else:
            price+=0



        price_lbl.configure(text=price)

        map_widget.delete_all_marker()

        map_widget.set_address(arrivallocationvalue,text=str(arrivallocationvalue),marker=True)
        map_widget.set_zoom(10)



    def add_function():
        if departuredate.get() == "":
            messagebox.showerror("Error!", "Please fill all the fields!")
        else:
            mycon = sqlcon.connect(host="localhost", user="root", password="suhayb", database="flight")
            cursor1 = mycon.cursor()
            cursor1.execute("INSERT INTO bookhist VALUES (%s, %s, %s, %s,%s, %s, %s , %s, %s, %s)",
                            (username.get(),departuredate.get(),departurelocationvar.get(),arrivallocationvar.get(),airlinevar.get(),
                             distance_lbl.cget("text"),fare.cget("text")
                            ,seatclassvar.get(),seatmealvar.get(),price_lbl.cget("text"))) #%s is placeholder cget is to get label value

            paymentwin()
            app.destroy()
            mycon.commit()
            mycon.close()


    #===== ENTRY ======= ||

    userid_lbl = customtkinter.CTkLabel(master=detail_frame, text="Username", fg_color='transparent',
                                         font=("Impact",35 ))
    userid_lbl.grid(row=0, column=0, padx=40, pady=40)

    user_lbl = customtkinter.CTkLabel(master=detail_frame, text=username.get(), fg_color='transparent',
                                         font=("Impact",40 ))
    user_lbl.grid(row=0, column=1, padx=40, pady=40)


    date_lbl = customtkinter.CTkLabel(master=detail_frame, text="Date (YYYY-MM-DD)", fg_color='transparent',
                                         font=("Impact",30 ))
    date_lbl.grid(row=1, column=0, padx=20, pady=10)

    date_ent = customtkinter.CTkEntry(master=detail_frame, font=("Comfortaa", 25),
                                           textvariable=departuredate,
                                           width=350, height=40, border_width=2, corner_radius=10)
    date_ent.grid(row=1, column=1, padx=40, pady=10)




    departurelocation_lbl = customtkinter.CTkLabel(master=detail_frame, text="Departure", fg_color='transparent',
                                         font=("Impact",40 ))
    departurelocation_lbl.grid(row=2, column=0, padx=10, pady=10)

    departurecities = ["Chennai","Mumbai","Bangalore","Delhi","Pune",
                       "Kolkata", "Ahmedabad", "Hyderabad",
                       "Jaipur", "Lucknow ", "Kanpur", "Coimbatore", "Kochi", "Port Blair", "Shimla"]

    departurelocation = customtkinter.CTkComboBox(detail_frame,values=departurecities,width=350, height=40,
                                                  dropdown_font =("Comfortaa", 20),
                                                  font =("Comfortaa", 25),variable=departurelocationvar,
                                                  command = update_label
                                                  )
    departurelocation.bind("<<ComboboxSelected>>", update_label)

    departurelocation.grid(row=2, column=1, padx=10, pady=10)




    arrivallocation_lbl = customtkinter.CTkLabel(master=detail_frame, text="Arrival", fg_color='transparent',
                                         font=("Impact",40 ))
    arrivallocation_lbl.grid(row=3, column=0, padx=10, pady=10)

    arrivallocation = customtkinter.CTkComboBox(detail_frame,values=departurecities,width=350, height=40,
                                                  font =("Comfortaa", 25),dropdown_font =("Comfortaa", 20)
                                                ,variable=arrivallocationvar,command = update_label)
    arrivallocation.bind("<<ComboboxSelected>>", update_label)

    arrivallocation.grid(row=3, column=1, padx=10, pady=10)




    airline_lbl = customtkinter.CTkLabel(master=detail_frame, text="Airline", fg_color='transparent',
                                                 font=("Impact", 40))
    airline_lbl.grid(row=4, column=0, padx=10, pady=10)

    airlinechoice = ["Air India", "Indigo", "Vistara", "SpiceJet", "GoAir", "Akasa Air"]

    airline = customtkinter.CTkComboBox(detail_frame, values=airlinechoice, width=350, height=40,
                                                font=("Comfortaa", 25),dropdown_font =("Comfortaa", 25),
                                        variable=airlinevar,command = update_label)
    airline.bind("<<ComboboxSelected>>", update_label)

    airline.grid(row=4, column=1, padx=2, pady=2)




    distancehead_lbl = customtkinter.CTkLabel(master=detail_frame, text="Distance", fg_color='transparent',
                                                 font=("Impact", 40))
    distancehead_lbl.grid(row=5, column=0, padx=10, pady=10)

    distance_lbl = customtkinter.CTkLabel(master=detail_frame, text="", fg_color='transparent',
                                                 font=("Impact", 40))
    distance_lbl.grid(row=5, column=1, padx=10, pady=10)




    farehead_lbl = customtkinter.CTkLabel(master=detail_frame, text="Fare", fg_color='transparent',
                                              font=("Impact", 40))
    farehead_lbl.grid(row=6, column=0, padx=10, pady=10)

    fare = customtkinter.CTkLabel(master=detail_frame, text="", fg_color='transparent',
                                          font=("Impact", 40))
    fare.grid(row=6, column=1, padx=10, pady=10)




    classhead_lbl = customtkinter.CTkLabel(master=detail_frame, text="Class", fg_color='transparent',
                                          font=("Impact", 40))
    classhead_lbl.grid(row=7, column=0, padx=10, pady=10)

    classflight = ["Economy", "Business", "First"]

    seatclass = customtkinter.CTkComboBox(detail_frame, values=classflight, width=350, height=40,
                                        font=("Comfortaa", 25),dropdown_font =("Comfortaa", 25), variable=seatclassvar
                                          ,command = update_label)
    seatclass.bind("<<ComboboxSelected>>", update_label)

    seatclass.grid(row=7, column=1, padx=2, pady=2)




    mealhead_lbl = customtkinter.CTkLabel(master=detail_frame, text="Meal", fg_color='transparent',
                                          font=("Impact", 40))
    mealhead_lbl.grid(row=8, column=0, padx=10, pady=10)

    mealflight = ["Non-Vegetarian", "Vegetarian", "None"]

    seatmeal = customtkinter.CTkComboBox(detail_frame, values=mealflight, width=350, height=40,
                                        font=("Comfortaa", 25),dropdown_font =("Comfortaa", 25), variable=seatmealvar,
                                         command = update_label)
    seatmeal.bind("<<ComboboxSelected>>", update_label)

    seatmeal.grid(row=8, column=1, padx=2, pady=2)





    pricehead_lbl = customtkinter.CTkLabel(master=detail_frame, text="Price", fg_color='transparent',
                                              font=("Impact", 40))
    pricehead_lbl.grid(row=9, column=0, padx=10, pady=10)

    price_lbl = customtkinter.CTkLabel(master=detail_frame, text="", fg_color='transparent',
                                          font=("Impact", 40))

    price_lbl.grid(row=9, column=1, padx=10, pady=40)







    map_widget = tkintermapview.TkinterMapView(data_frame, width=700, height=450, corner_radius= 20)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                    max_zoom=22)  # google normal



    '''map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                    max_zoom=22)  # google satellite'''

    map_widget.set_address("Chennai Airport",text = "Chennai Airport",marker = True)
    map_widget.set_zoom(14)

    map_widget.place(x=50,y=50)




    paybutton = customtkinter.CTkButton(master=data_frame, text="Pay", text_color="black", width=200, height=50,
                                          border_width=0, corner_radius=8,
                                          fg_color="#8bbad0", hover_color="#3d525c", font=("Comfortaa", 23, "bold"),
                                          command=add_function) #add_function

    paybutton.place(x = 300, y =530)

def bookinghistorywin():

    app = customtkinter.CTkToplevel()
    app.geometry("1920x1080")
    app.title("Airline Bookings")
    app.configure(fg_color="#272f32")

    bg = customtkinter.CTkImage(dark_image=Image.open("grad12.jpg"), size=(1920, 1080))
    bglabel = customtkinter.CTkLabel(master=app, text="", image=bg)
    bglabel.place(relx=0, rely=0)

    headinglabel = customtkinter.CTkLabel(master=app, text="Fly+ Bookings", fg_color='black', width=1920, height=90,
                                          font=("Impact", 70))  # width=1000,corner_radius=25,fg_color='darkblue',
    headinglabel.pack(padx=0, pady=0)


    main_frame = customtkinter.CTkFrame(master=app, width=900, height=900, fg_color="transparent", border_width=10,
                                          border_color="black")  # ,border_width=2,border_color="black"
    main_frame.pack(padx=0, pady=150)
    main_frame.pack_propagate(False)

    y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

    customer_table = ttk.Treeview(main_frame, columns=("customerid", "departuredate", "departure", "arrival", "airline",
                                                       "distance", "fare", "seat", "meal", "price"),
                                  yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)  # Tkinter TreeView Table

    customer_table.heading("customerid", text="CustomerID")
    customer_table.heading("departuredate", text="Departure Date")
    customer_table.heading("departure", text="Departure")
    customer_table.heading("arrival", text="Arrival")
    customer_table.heading("airline", text="Airline")
    customer_table.heading("distance", text="Distance")
    customer_table.heading("fare", text="Fare")
    customer_table.heading("seat", text="Seat")
    customer_table.heading("meal", text="Meal")
    customer_table.heading("price", text="Price")

    customer_table['show'] = 'headings'
    customer_table.column("customerid", width=100)
    customer_table.column("departuredate", width=100)
    customer_table.column("departure", width=100)
    customer_table.column("arrival", width=100)
    customer_table.column("airline", width=100)
    customer_table.column("distance", width=70)
    customer_table.column("fare", width=80)
    customer_table.column("seat", width=100)
    customer_table.column("meal", width=100)
    customer_table.column("price", width=100)


    def fetch_data():
        mycon = sqlcon.connect(host="localhost", user="root", password="suhayb", database="flight")
        uservar = username.get()
        cursor1 = mycon.cursor()
        cursor1.execute("SELECT * FROM bookhist where customerid = %s",(uservar,))
        rows = cursor1.fetchall()
        if len(rows) != 0:
            customer_table.delete(*customer_table.get_children())  # treeview children
            for row in rows:
                customer_table.insert('', tk.END, values=row)
                mycon.commit()
        mycon.close()

    fetch_data()

    y_scroll.config(command=customer_table.yview)
    x_scroll.config(command=customer_table.xview)
    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
    customer_table.pack(fill=tk.BOTH,expand=True)


def serviceswin():
    app = customtkinter.CTkToplevel()
    app.geometry("1920x1080")
    app.title("Airline Bookings")
    app.configure(fg_color="#106677")

    bg = customtkinter.CTkImage(dark_image=Image.open("grad8.jpg"), size=(1920, 1080))
    bglabel = customtkinter.CTkLabel(master=app, text="", image=bg)
    bglabel.place(relx=0, rely=0)

    headinglabel = customtkinter.CTkLabel(master=app, text="Fly+ Bookings", fg_color='black', width=1920, height=90,
                                          font=("Impact", 70))  # width=1000,corner_radius=25,fg_color='darkblue',
    headinglabel.pack(padx=0, pady=0)

    services_frame = customtkinter.CTkFrame(master=app, width=800, height=570,fg_color="transparent",border_width=10,border_color="black") #,border_width=2,border_color="black"
    services_frame.pack(padx=20,pady=150)
    services_frame.pack_propagate(False)

    serviceslabel = customtkinter.CTkLabel(master=services_frame, text="Services", fg_color='transparent',
                                         font=("Impact", 85))  # width = 1000,,corner_radius=25,fg_color='darkblue',
    serviceslabel.pack(padx=0, pady=40)

    bookingbutton = customtkinter.CTkButton(master=services_frame, text="Bookings", text_color="white", width=500, height=120,
                                        border_width=0, corner_radius=40,
                                        fg_color="#263238", hover_color="#3d525c", font=("Comfortaa", 35, "bold"),
                                        command=mapwin)
    bookingbutton.pack(padx=0, pady=15)

    historybutton = customtkinter.CTkButton(master=services_frame, text="History",text_color="white", width=500, height=120,
                                              border_width=0, corner_radius=40,#a1caa8
                                              fg_color="#263238", hover_color="#3d525c",
                                              font=("Comfortaa", 35, "bold"), command=bookinghistorywin)
    historybutton.pack(padx=0, pady=10)

def login():
    import mysql.connector as sqlcon
    mycon = sqlcon.connect(host="localhost", user="root", password="suhayb", database="flight") #change your password

    cursor1 = mycon.cursor()
    cursor1.execute("SELECT*FROM userpass")
    data = cursor1.fetchmany(100)


    name = usernameentry.get()
    password = passwordentry.get()

    for row in data:
        if name=='' or password == '':
            tk.messagebox.showinfo("Login", "Incorrect Username or Password \n"
                                            "                 Try Again")
            break

        elif name in row[0] and password in row[1]:
            serviceswin()
            break


        else:
            tk.messagebox.showinfo("Login", "Incorrect Username or Password \n"
                                            "                 Try Again")
            break

def createnew():

    def createuser():
        import mysql.connector as sqlcon
        mycon = sqlcon.connect(host="localhost", user="root", password="suhayb", database="flight")

        cursor1 = mycon.cursor()
        cursor1.execute("SELECT*FROM userpass")
        data = cursor1.fetchmany(100)

        name = cusernameentry.get()
        password = cpasswordentry.get()
        valid = False

        for row in data:
            if name == '' or password == '':
                tk.messagebox.showinfo("Create", "Cannot Be Blank \n"
                                                "                 Try Again")
                valid = False
                break

            elif name in row[0] :
                tk.messagebox.showinfo("Create", "Username Exists \n"
                                                "                 Try Again")
                valid = False
                break


            else:
                valid = True


        if valid == True:
            cursor1.execute("insert into userpass values (%s,%s)",(name,password))

        mycon.commit()
        mycon.close()
        app.destroy()


    app = customtkinter.CTkToplevel()
    app.geometry("1920x1080")
    app.title("Airline Bookings")
    app.configure(fg_color="#272f32")

    bg = customtkinter.CTkImage(dark_image=Image.open("grad10.jpg"), size=(1920, 1080))
    bglabel = customtkinter.CTkLabel(master=app, text="", image=bg)
    bglabel.place(relx=0, rely=0)

    headinglabel = customtkinter.CTkLabel(master=app, text="Fly+ Bookings", fg_color='black', width=1920, height=90,
                                          font=("Impact", 70))  # width=1000,corner_radius=25,fg_color='darkblue',
    headinglabel.pack(padx=0, pady=0)

    signin_frame = customtkinter.CTkFrame(master=app, width=800, height=570, fg_color="transparent", border_width=10,
                                          border_color="black")  # ,border_width=2,border_color="black"
    signin_frame.pack(padx=20, pady=150)
    signin_frame.pack_propagate(False)

    createlabel = customtkinter.CTkLabel(master=signin_frame, text="Create User", fg_color='transparent',
                                         font=("Impact", 50))  # width = 1000,,corner_radius=25,fg_color='darkblue',
    createlabel.pack(padx=0, pady=40)

    usernamelabel = customtkinter.CTkLabel(master=signin_frame, text="Username", fg_color='transparent', font=(
    "Comfortaa", 30))  # width = 1000,,corner_radius=25,fg_color='darkblue',
    usernamelabel.pack(anchor='w', padx=75, pady=10)



    cusernameentry = customtkinter.CTkEntry(master=signin_frame, font=("Comfortaa", 25),
                                           width=650, height=40, border_width=2, corner_radius=10,
                                           )
    cusernameentry.pack(padx=50, pady=2)

    passwordlabel = customtkinter.CTkLabel(master=signin_frame, text="Password", fg_color='transparent', font=(
    "Comfortaa", 30))  # width = 1000,,corner_radius=25,fg_color='darkblue',
    passwordlabel.pack(anchor='w', padx=75, pady=10)

    cpasswordentry = customtkinter.CTkEntry(master=signin_frame, show="*", font=("Comfortaa", 25),
                                           width=650, height=40, border_width=2, corner_radius=10)
    cpasswordentry.pack(padx=50, pady=2)

    blanklabel = customtkinter.CTkLabel(master=signin_frame, text="", fg_color='transparent',
                                        height=20)  # width = 1000,,corner_radius=25,fg_color='darkblue',font=("Comfortaa",30)
    blanklabel.pack(padx=0, pady=15)

    loginbutton = customtkinter.CTkButton(master=signin_frame, text="Create", text_color="black", width=200, height=50,
                                          border_width=0, corner_radius=8,
                                          fg_color="#8bbad0", hover_color="#3d525c", font=("Comfortaa", 23, "bold"),
                                          command=createuser)
    loginbutton.pack(padx=0, pady=15)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("Airline Bookings")
app.configure(fg_color="#263238")


bg = customtkinter.CTkImage(dark_image=Image.open("grad10.jpg"),size=(1920,1080))
bglabel = customtkinter.CTkLabel(master=app,text = "",image=bg)
bglabel.place(relx=0,rely=0)

headinglabel = customtkinter.CTkLabel(master=app,text = "Fly+ Bookings",fg_color='black',width =1920,height= 90,font=("Impact",70)) #width=1000,corner_radius=25,fg_color='darkblue',
headinglabel.pack(padx=0,pady=0)





signin_frame = customtkinter.CTkFrame(master=app, width=800, height=570,fg_color="transparent",border_width=10,border_color="black") #,border_width=2,border_color="black"
signin_frame.pack(padx=20,pady=150)
signin_frame.pack_propagate(False)


signinlabel = customtkinter.CTkLabel(master=signin_frame,text = "Sign In",fg_color='transparent',font=("Impact",50)) #width = 1000,,corner_radius=25,fg_color='darkblue',
signinlabel.pack(padx=0,pady=40)

usernamelabel = customtkinter.CTkLabel(master=signin_frame,text = "Username",fg_color='transparent',font=("Comfortaa",30)) #width = 1000,,corner_radius=25,fg_color='darkblue',
usernamelabel.pack(anchor='w',padx=75,pady=10)

username = tk.StringVar()

usernameentry = customtkinter.CTkEntry(master=signin_frame, placeholder_text="Username",font=("Comfortaa",25),
                                       width=650,height=40,border_width=2,corner_radius=10,textvariable=username)
usernameentry.pack(padx=50,pady=2)

passwordlabel = customtkinter.CTkLabel(master=signin_frame,text = "Password",fg_color='transparent',font=("Comfortaa",30)) #width = 1000,,corner_radius=25,fg_color='darkblue',
passwordlabel.pack(anchor='w',padx=75,pady=10)

passwordentry = customtkinter.CTkEntry(master=signin_frame, show="*",font=("Comfortaa",25),
                                       width=650,height=40,border_width=2,corner_radius=10)
passwordentry.pack(padx=50,pady=2)

blanklabel = customtkinter.CTkLabel(master=signin_frame,text = "",fg_color='transparent',height=20) #width = 1000,,corner_radius=25,fg_color='darkblue',font=("Comfortaa",30)
blanklabel.pack(padx=0,pady=15)

loginbutton = customtkinter.CTkButton(master=signin_frame, text="Login",text_color="black",width=200,height=50,border_width=0,corner_radius=8,
                                      fg_color="#8bbad0",hover_color="#3d525c",font=("Comfortaa",23,"bold"),command=login)
loginbutton.pack(padx=0, pady=15)

createnewbutton = customtkinter.CTkButton(master=signin_frame, text="Create New",width=200,height=35,border_width=0,corner_radius=8,
                                          fg_color="transparent",hover_color="#3f545e",font=("Comfortaa",18,"bold"),command=createnew)
createnewbutton.pack(padx=0, pady=0)





app.mainloop()
