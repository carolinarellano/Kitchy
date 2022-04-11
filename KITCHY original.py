from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
from validador import signup
import json
import os
import tkinter.font as tkFont
import ast
import csv
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.figure import Figure

window = tk.Tk()
window.title('Kitchy')
window.iconbitmap("Kitchy.jpeg")
window.geometry('1100x600')
window.config(background='navajo white', padx=50, pady=50)

img = Image.open("Kitchy2.jpeg")
img = img.resize((300, 178), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img)
label_photo = Label(image=test, background='sandy brown')
label_photo.grid(row=0, column=2)

lista_ingredientes = []
lista_procedimiento = []
cuentas = {}

def recuperar_usuarios():
        with open('usuarios.csv', 'r') as file:
                reader = csv.reader(file, delimiter=',', quotechar='"')
                for row in reader:
                        if not row:
                                continue

                        user = row[0]
                        password = row[1]
                        cuentas[user] = password

def guardar_info_usuarios():
        with open('usuarios.csv', 'w') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"')

                for user in cuentas:
                        password = cuentas[user]
                        writer.writerow([user, password])

recuperar_usuarios()

def iniciar_sesion(usuario, password):
        if usuario not in cuentas or cuentas[usuario] != password:
                return False # no se inicio sesion
                
        else:
                return True                

def pagina_inicial():

        def login_window():
                login_w_frame = Frame(window)
                login_w_frame.grid(row=0, column=0)
                login_w_frame.config(width=1000, height=1000, bg='navajo white', bd= '24', relief='flat')
                login_w = Frame(login_w_frame)
                login_w.grid(row=0, column=0)
                login_w.config(width=900, height=250, bg='navajo white', bd= '24', relief='flat')
                tittle = Label(login_w, text="Entra a Kitchy!", font='Helvetica, 16', bg='navajo white').grid(column=1, row=2)
                log_user = Label(login_w, text="Ingresa tu usuario: ", font='Helvetica, 13', bg='navajo white').grid(column=0, row=4)
                entry_user = Entry(login_w, width=20)
                entry_user.grid(column=1, row=4)
                log_pass = Label(login_w, text="Ingresa tu password: ", font='Helvetica, 13', bg='navajo white').grid(column=0, row=8)
                entry_pass = Entry(login_w, width=20, show='*')
                entry_pass.grid(column=1, row=8)

                submit_button = Button(login_w, text="Log-In", font='Helvetica, 13', bg='dark salmon', fg='black', command= lambda: iniciar_sesion(entry_user.get(), entry_pass.get()))
                submit_button.grid(column=1, row=12)
                back_button = Button(login_w, text= "Back", font='Helvetica, 13', bg='dark salmon', fg='black', command= lambda: [login_w.destroy(), login_w_frame.destroy()])
                back_button.grid(column=0, row=13)

                def iniciar_sesion(usuario, password):
                        if usuario not in cuentas or cuentas[usuario] != password:
                                estatus_user = tk.StringVar()
                                estatus_user.set('')
                                estatus_user.set('Log-in no valido')
                                usuario_noencontrado = Label(login_w ,textvariable=estatus_user, font= 'Helvetica, 11', bg='navajo white', fg= 'indian red')
                                usuario_noencontrado.grid(row=9, column=1)
                                return False # no se inicio sesion
                                
                        buscar_ingresar_menu()
                        return True                
        
        def close_window():
                window.destroy()

        def signup_window():
                frame_signup = Frame(window)
                frame_signup.grid(column=0, row=0)
                frame_signup.config(width=1100, height=1000, background='navajo white', bd= '24', relief='flat')
                sign_up_w = Frame(frame_signup)
                sign_up_w.config(width=1000, height=1000)
                sign_up_w.grid(column=0, row=0)
                sign_up_w.config(background='navajo white', bd= '24', relief='flat')

                tittle = Label(sign_up_w, text="Registrate y disfruta de Kitchy!", font='Helvetica, 16', bg='navajo white').grid(column=1, row=2)
                l_user = Label(sign_up_w, text ="Nuevo usuario: ", font='Helvetica, 13', bg='navajo white').grid(column=0, row=4)
                username_entry = Entry(sign_up_w, width=20)
                username_entry.grid(column=1, row=4)
                l_user_conf = Label(sign_up_w, text ="Confirmar usuario: ", font='Helvetica, 13', bg='navajo white').grid(column=0, row=6)
                username_entry_valid = Entry(sign_up_w, width=20)
                username_entry_valid.grid(column=1, row=6)
                l_pass = Label(sign_up_w, text ="Nueva password: ", font='Helvetica, 13', bg='navajo white').grid(column=0, row=8)
                entry_pass = Entry(sign_up_w, width=20, show='*')
                entry_pass.grid(column=1, row=8)
                l_pass_conf = Label(sign_up_w, text ="Confirmar password: ", font='Helvetica, 13', bg='navajo white').grid(column=0, row=10)
                entry_pass_conf = Entry(sign_up_w, width=20, show='*')
                entry_pass_conf.grid(column=1, row=10)
                submit_button = Button(sign_up_w, text= "Submit", font='Helvetica, 13', bg='dark salmon', fg='black', command=lambda: [signup(username_entry.get(), username_entry_valid.get(), entry_pass.get(), entry_pass_conf.get()), validador(username_entry.get(), username_entry_valid.get(), entry_pass.get(), entry_pass_conf.get())])
                submit_button.grid(column=1, row=12)
                back_button = Button(sign_up_w, text= "Back", font='Helvetica, 13',bg='dark salmon', fg='black', command= lambda: [sign_up_w.destroy(), frame_signup.destroy()])
                back_button.grid(column=0, row=13)

                def crear_cuenta(usuario, contrasena):
                                cuentas[usuario] = contrasena

                def validador(username, user_confirmation, password, password_confirmation):
                        from validador import signup
                        estatus_user = tk.StringVar()
                        estatus_user.set('')
                        estatus_user_label = Label(sign_up_w,textvariable=estatus_user, fg= 'indian red', font='Helvetica, 11')
                        estatus_user_label.grid(column=1, row=13)
                        estatus_password = tk.StringVar()
                        estatus_password.set('')
                        estatus_password_label = Label(sign_up_w, textvariable=estatus_password, fg= 'indian red', font='Helvetica, 11')
                        estatus_password_label.grid(column=1, row=14)

                        if username != user_confirmation:
                                estatus_user.set('Los usuarios no coinciden')
                        elif username == '':
                                estatus_user.set('Usuario no válido')

                        else:
                                signup(username_entry.get(), username_entry_valid.get(), entry_pass.get(), entry_pass_conf.get())
                                crear_cuenta(username_entry.get(), entry_pass.get())
                                sign_up_w.destroy()
                                frame_signup.destroy()
                                buscar_ingresar_menu()

                        if password != password_confirmation:
                                estatus_password.set('Los passwords no coinciden')
                        elif password == '':
                                estatus_password.set('Password no válido')
                        else:
                                signup(username_entry.get(), username_entry_valid.get(), entry_pass.get(), entry_pass_conf.get())
                                crear_cuenta(username_entry.get(), entry_pass.get())
                                sign_up_w.destroy()
                                frame_signup.destroy()
                                buscar_ingresar_menu()

        inicio_frame = Frame(window)
        inicio_frame.config(background='navajo white', bd= '12', relief='flat')
        inicio_frame.grid(column=0, row=0)
        inicio = Frame(inicio_frame)
        inicio_frame.config(background='navajo white', bd= '12', relief='flat')
        inicio_frame.grid(column=0, row=0)
        
        HOME_label = Label(inicio_frame, text='Bienvenid@ a Kitchy', font='Helvetica, 16', bg='navajo white', fg='black')
        log_in_label = Label(inicio_frame, text= 'Tienes una cuenta de Kitchy? Ingresa', font='Helvetica, 13', bg='navajo white', fg='black')
        log_in_button = Button(inicio_frame, text='Log-in', bg='sandy brown', fg='black', font='Helvetica, 13', command=login_window)
        exit_label = Label(inicio_frame, text= 'Click para salir', font='Helvetica, 13', bg='navajo white', fg='black')
        exit_button= Button(inicio_frame, text='Salir', bg='sandy brown', fg='black', font='Helvetica, 13', command= lambda: [close_window(), guardar_info_usuarios()])
        exit_label.grid(column=1, row=8), exit_button.grid(column=1, row=9)
        sign_up_label = Label(inicio_frame, text= 'Es tu primer vez en Kitchy? Registrate', font='Helvetica, 13', bg='navajo white', fg='black')
        sign_up_button = Button(inicio_frame, text='Sign-up', bg='sandy brown', fg='black', font='Helvetica, 13', command=signup_window)

        HOME_label.grid(column=1, row=1), sign_up_label.grid(column=1, row=2), sign_up_button.grid(column=1, row=3), log_in_label.grid(column=1, row=4), 
        log_in_button.grid(column=1, row=5), exit_label.grid(column=1, row=8), exit_button.grid(column=1, row=9)

                              
        def ingreso_recetas():
                menu_frame = Frame(window)
                menu_frame.config(background='navajo white', bd= '20', relief='flat')
                menu_frame.config(width=800, height=1000)
                menu_frame.grid(row=0, column=0)
        
                window_menu = Frame(menu_frame)
                window_menu.grid(row=0, column=0)
                window_menu.config(width=800, height=1000, bd= '30', relief= 'flat')
                window_menu.config(background='navajowhite')
                tittle = Label(window_menu, text='Selecciona las caracteristicas de tu receta', font='Helvetica, 13',bg='navajo white').grid(row=0, column=0)
                window_menu.combo = ttk.Combobox(window_menu)
                labelTop = tk.Label(window_menu,
                                text = "Tipo de dieta", bg='navajo white', font='Helvetica, 11')
                labelTop.grid(row=1, column=0)
                tipode_dieta = ttk.Combobox(window_menu,values=["(seleccionar)","Vegana", "Vegetariana", 
                                        "Dietetica"])
                tipode_dieta.config(font='Helvetica, 11')
                tipode_dieta.grid(row=1, column=1)
                tipode_dieta.current(0)
                window_menu.combo = ttk.Combobox(window_menu)
                labelTop = tk.Label(window_menu,
                                text = "Hora de comida", bg='navajo white', font='Helvetica, 11')
                labelTop.grid(row=3, column=0)
                horade_comida = ttk.Combobox(window_menu,values=["(seleccionar)","Desayuno", "Comida", 
                                        "Cena"])
                horade_comida.config(font='Helvetica, 11')
                horade_comida.grid(row=3, column=1)
                horade_comida.current(0)
                window_menu.combo = ttk.Combobox(window_menu)
                labelTop = tk.Label(window_menu,
                                text = "Tipo de comida", bg='navajo white', font='Helvetica, 11')
                labelTop.grid(row=5, column=0)
                tipode_comida = ttk.Combobox(window_menu,values=["(seleccionar)","Dulce", "Salado"])
                tipode_comida.config(font='Helvetica, 11')
                tipode_comida.grid(row=5, column=1)
                tipode_comida.current(0)
                
                def validador_categorias(dieta, hora, tipo):
                        estatus_seleccion = tk.StringVar()
                        estatus_seleccion.set('')
                        if tipode_dieta.get() == '(seleccionar)' and horade_comida.get() == '(seleccionar)' and tipode_comida.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=2, column=1)
                                hora_novalida = Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                hora_novalida.grid(row=4, column=1)
                                tipo_novalido= Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                tipo_novalido.grid(row=6, column=1)
                                
                        else:
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                dieta_no_valida.grid(row=2, column=1)
                                hora_novalida = Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                hora_novalida.grid(row=4, column=1)
                                tipo_novalido= Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                tipo_novalido.grid(row=6, column=1)
                                
                                        
                        if tipode_dieta.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=2, column=1)
                        else:
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')

                        if horade_comida.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=4, column=1)
                        else: 
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                hora_novalida = Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                hora_novalida.grid(row=4, column=1)

                        if tipode_comida.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=6, column=1)
                        else:
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                dieta_no_valida.grid(row=6, column=1)

                        if tipode_dieta.get() != '(seleccionar)' and horade_comida.get() != '(seleccionar)' and tipode_comida.get() != '(seleccionar)':
                                CrearReceta(filtro(tipode_dieta.get(), horade_comida.get(), tipode_comida.get()))

                def filtro(dieta, hora, tipo):
                        
                        if tipode_dieta.get() == "Vegana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_Cena_Dulce.txt'

                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegetariana_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegetariana_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegetariana_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_Cena_Dulce.txt'


                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_Cena_Dulce.txt'
                        return f

                
                        
                #agregar imagen al menú de crear receta
                # agregar validador a un comando
                def CrearReceta(a):

                        def Ingredientes(ventana,valor):
                                global lista_ingredientes
                                lista_ingredientes.append(valor)
                                listbox_ing=tk.Listbox(ventana)
                                listbox_ing.place(x=2,y=150, height=300)
                                listbox_ing.insert(tk.END,*lista_ingredientes)


                        def Procedimiento(ventana,valor, validador):
                                global lista_procedimiento
                                lista_procedimiento.append(valor)
                                listbox_proc=tk.Listbox(ventana)
                                listbox_proc.place(x=450,y=150, height=300, width=400)
                                listbox_proc.insert(tk.END,*lista_procedimiento)


                        def AgregarReceta(a,ventana,c,d,e,f,g):
                                global lista_ingredientes
                                global lista_procedimiento
                        
                                receta = {}

                                receta['Nombre de Receta'] = e
                                receta['Lista de Ingredientes'] = a
                                receta['Procedimiento'] = d
                                receta['Cantidad'] = f
                                receta['Dificultad'] = g

                                recetas_file = c
                                if os.path.isfile(recetas_file):
                                        f = open(recetas_file, 'a')
                                else:
                                        f = open(recetas_file, 'w')
                                json_str = json.dumps(receta)
                                f.write('\n')
                                f.write(json_str)

                                if recetas_file=='Recetas_Vegana_Desayuno_Salado.txt':
                                        u = open('Recetas_Vegana_Desayuno_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegana_No_especificar_Salado.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Desayuno_Salado.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Desayuno_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))
                                
                                if recetas_file=='Recetas_Vegana_Desayuno_Dulce.txt':
                                        u = open('Recetas_Vegana_Desayuno_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegana_No_especificar_Dulce.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Desayuno_Dulce.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Desayuno_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))
                                        
                                if recetas_file=='Recetas_Vegana_Comida_Salado.txt':
                                        u = open('Recetas_Vegana_Comida_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegana_No_especificar_Salado.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Comida_Salado.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Comida_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))
                                
                                if recetas_file=='Recetas_Vegana_Comida_Dulce.txt':
                                        u = open('Recetas_Vegana_Comida_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegana_No_especificar_Dulce.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Comida_Dulce.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Comida_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))
                                        
                                if recetas_file=='Recetas_Vegana_Cena_Salado.txt':
                                        u = open('Recetas_Vegana_Cena_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegana_No_especificar_Salado.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Cena_Salado.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Cena_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))
                                
                                if recetas_file=='Recetas_Vegana_Cena_Dulce.txt':
                                        u = open('Recetas_Vegana_Cena_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegana_No_especificar_Dulce.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Cena_Dulce.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Cena_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Vegetariana_Desayuno_Salado.txt':
                                        u = open('Recetas_Vegetariana_Desayuno_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegetariana_No_especificar_Salado.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegetariana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Desayuno_Salado.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Desayuno_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Vegetariana_Desayuno_Dulce.txt':
                                        u = open('Recetas_Vegetariana_Desayuno_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegetariana_No_especificar_Dulce.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegetariana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Desayuno_Dulce.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Desayuno_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))
                                        
                                if recetas_file=='Recetas_Vegetariana_Comida_Salado.txt':
                                        u = open('Recetas_Vegetariana_Comida_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegetariana_No_especificar_Salado.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegetariana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Comida_Salado.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Comida_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Vegetariana_Comida_Dulce.txt':
                                        u = open('Recetas_Vegetariana_Comida_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegetariana_No_especificar_Dulce.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegetariana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Comida_Dulce.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Comida_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Vegetariana_Cena_Salado.txt':
                                        u = open('Recetas_Vegetariana_Cena_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegetariana_No_especificar_Salado.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegetariana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Cena_Salado.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Cena_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Vegetariana_Cena_Dulce.txt':
                                        u = open('Recetas_Vegetariana_Cena_No_especificar.txt', 'a')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Vegetariana_No_especificar_Dulce.txt', 'a')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Vegetariana_No_especificar_No_especificar.txt', 'a')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Cena_Dulce.txt', 'a')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Cena_No_especificar.txt', 'a')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'a')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'a')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Dietetica_Desayuno_Salado.txt':
                                        u = open('Recetas_Dietetica_Desayuno_No_especificar.txt', 'w')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Dietetica_No_especificar_Salado.txt', 'w')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Dietetica_No_especificar_No_especificar.txt', 'w')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Desayuno_Salado.txt', 'w')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Desayuno_No_especificar.txt', 'w')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'w')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'w')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Dietetica_Desayuno_Dulce.txt':
                                        u = open('Recetas_Dietetica_Desayuno_No_especificar.txt', 'w')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Dietetica_No_especificar_Dulce.txt', 'w')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Dietetica_No_especificar_No_especificar.txt', 'w')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Desayuno_Dulce.txt', 'w')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Desayuno_No_especificar.txt', 'w')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'w')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'w')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Dietetica_Comida_Salado.txt':
                                        u = open('Recetas_Dietetica_Comida_No_especificar.txt', 'w')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Dietetica_No_especificar_Salado.txt', 'w')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Dietetica_No_especificar_No_especificar.txt', 'w')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Comida_Salado.txt', 'w')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Comida_No_especificar.txt', 'w')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'w')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'w')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Dietetica_Comida_Dulce.txt':
                                        u = open('Recetas_Dietetica_Comida_No_especificar.txt', 'w')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Dietetica_No_especificar_Dulce.txt', 'w')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Dietetica_No_especificar_No_especificar.txt', 'w')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Comida_Dulce.txt', 'w')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Comida_No_especificar.txt', 'w')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'w')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'w')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Dietetica_Cena_Salado.txt':
                                        u = open('Recetas_Dietetica_Comida_No_especificar.txt', 'w')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Dietetica_No_especificar_Salado.txt', 'w')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Dietetica_No_especificar_No_especificar.txt', 'w')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Cena_Salado.txt', 'w')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Cena_No_especificar.txt', 'w')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Salado.txt', 'w')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'w')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                                if recetas_file=='Recetas_Dietetica_Cena_Dulce.txt':
                                        u = open('Recetas_Dietetica_Cena_No_especificar.txt', 'w')
                                        u.write('\n')
                                        u.write(json.dumps(receta))
                                        v = open('Recetas_Dietetica_No_especificar_Dulce.txt', 'w')
                                        v.write('\n')
                                        v.write(json.dumps(receta))
                                        w = open('Recetas_Dietetica_No_especificar_No_especificar.txt', 'w')
                                        w.write('\n')
                                        w.write(json.dumps(receta))
                                        x = open('Recetas_SinRestriccion_Cena_Dulce.txt', 'w')
                                        x.write('\n')
                                        x.write(json.dumps(receta))
                                        p = open('Recetas_SinRestriccion_Cena_No_especificar.txt', 'w')
                                        p.write('\n')
                                        p.write(json.dumps(receta))
                                        y = open('Recetas_SinRestriccion_No_especificar_Dulce.txt', 'w')
                                        y.write('\n')
                                        y.write(json.dumps(receta))
                                        z = open('Recetas_SinRestriccion_No_especificar_No_especificar.txt', 'w')
                                        z.write('\n')
                                        z.write(json.dumps(receta))

                        def Ingredientes(ventana,valor):
                                global lista_ingredientes
                                listbox_ing=tk.Listbox(ventana)
                                listbox_ing.place(x=2,y=150, height=300)
                                lista_ingredientes.append(valor)
                                listbox_ing.insert(tk.END,*lista_ingredientes) 
                                        

                        def Procedimiento(ventana,valor):
                                global lista_procedimiento
                                lista_procedimiento.append(valor)
                                listbox_proc=tk.Listbox(ventana)
                                listbox_proc.place(x=450,y=150, height=300, width=400)
                                listbox_proc.insert(tk.END,*lista_procedimiento)

                        
                        global lista_ingredientes
                        global lista_procedimiento
                        CrearReceta = Frame(window)
                        CrearReceta.config(bg="navajo white", bd=11, relief='flat')
                        CrearReceta.place(x=50,y=0, width=1000,height=500)
                        Label(CrearReceta,text="Ingrese Nombre de la Receta", font='Helvetica, 12', bg="floral white").place(x=0,y=0)
                        nombre_receta = Entry(CrearReceta)
                        nombre_receta.place(x=220,y=0)

                        def validador_nombre():
                                if nombre_receta.get() == '':
                                        estatus_seleccion = tk.StringVar()
                                        estatus_seleccion.set('')
                                        nombre=Label(CrearReceta ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                        estatus_seleccion.set('Ingresa un nombre de receta válido')
                                        nombre.place(x=220, y=50)
                                else:
                                        estatus_seleccion = tk.StringVar()
                                        estatus_seleccion.set('')
                                        nombre=Label(CrearReceta ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                        estatus_seleccion.set('                                            ')
                                        nombre.place(x=220, y=50)

                        Label(CrearReceta,text="Porciones", font='Helvetica, 12', bg="floral white").place(x=570,y=0)
                        cantidad = ttk.Spinbox(CrearReceta,from_=1, to=10,increment=1)
                        cantidad.place(x=650,y=0,width=50)
                        Label(CrearReceta,text="Dificultad %", font='Helvetica, 12', bg="floral white").place(x=570,y=25)
                        dificultad = ttk.Spinbox(CrearReceta,from_=0, to=100,increment=10)
                        dificultad.place(x=650,y=25,width=50)

                        def validador_cantidad():
                                if cantidad.get() == '':
                                        estatus_seleccion = tk.StringVar()
                                        estatus_seleccion.set('')
                                        porciones=Label(CrearReceta ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                        estatus_seleccion.set('Ingresa una porción válida')
                                        porciones.place(x=650,y=50)
                                else: 
                                        estatus_seleccion = tk.StringVar()
                                        estatus_seleccion.set('')
                                        porciones=Label(CrearReceta ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                        estatus_seleccion.set('                                             ')
                                        porciones.place(x=150, y=210)

                        def validador_receta_nombre_cantidad():
                                validador_nombre()
                                validador_cantidad()
                                AgregarReceta(lista_ingredientes,CrearReceta,a,lista_procedimiento,nombre_receta.get(),cantidad.get(),dificultad.get()), visualizar_receta(a)

                        Label(CrearReceta,text="Ingrese los ingredientes de su receta", font='Helvetica, 12', bg="floral white").place(x=0,y=75)
                        entry_ing = Entry(CrearReceta)
                        entry_ing.place(x=0,y=105, width=100)
                        boton_ing = Button(CrearReceta,text="añadir",command = lambda:[Ingredientes(CrearReceta,entry_ing.get())])
                        boton_ing.place(x=105,y=105,width=50)
                        Label(CrearReceta,text="Ingrese el procedimiento de su receta", font='Helvetica, 12', bg="floral white").place(x=450,y=75)
                        entry_proc = Entry(CrearReceta)
                        entry_proc.place(x=450,y=105, width=200)

                        def visualizar_receta(a):
                                visualizacion= Frame(CrearReceta)
                                visualizacion.config(height=500, width=1200, bg='navajo white', relief='flat', bd=1)
                                visualizacion.place(x=0,y=0)
                                PantallaFinal = Frame(visualizacion)
                                PantallaFinal.config(height=500, width=1200, bg='navajo white')
                                PantallaFinal.grid(row=0, column=0)
                                boton_hecho = Button(text='Okay', command= lambda: [PantallaFinal.destroy(), visualizacion.destroy(), boton_back.destroy(), CrearReceta.destroy(), boton_hecho.destroy(), menu_frame.destroy()])
                                boton_back = Button(text='Back', command= lambda: [PantallaFinal.destroy(), visualizacion.destroy(), boton_hecho.destroy()])
                                boton_hecho.place(x=450,y=400)
                                boton_hecho.place(x=550,y=400)
                                fontStyle = tkFont.Font(family="Lucida Grande", size=20)

                                recetas_file = a
                                f = open(recetas_file, 'r')
                                numero_recetas = f.readlines()
                                a = ast.literal_eval(numero_recetas[len(numero_recetas)-1])

                                vy = 100
                                uy = 100

                                Label(PantallaFinal, text = "Receta: ", font='Helvetica, 11').place(x=0,y=0)
                                Label(PantallaFinal, text = a['Nombre de Receta'], font='Helvetica, 11', bg='navajo white').place(x=60,y=0)
                                print(a['Nombre de Receta'])
                                Label(PantallaFinal, text = "Cantidad de la porción: ", font='Helvetica, 11').place(x=0,y=25)
                                Label(PantallaFinal, text = a['Cantidad'], font='Helvetica, 11').place(x=155,y=25)
                                Label(PantallaFinal, text = "Ingredientes", font=fontStyle).place(x=0,y=60)
                                for i in range(len(a['Lista de Ingredientes'])):
                                        Label(PantallaFinal,text= a['Lista de Ingredientes'][i], font='Helvetica, 11').place(x=0,y=vy)
                                        vy += 20
                                Label(PantallaFinal, text = 'Procedimiento', font=fontStyle) .place(x=400,y=60)   
                                for i in range(len(a['Procedimiento'])):
                                        Label(PantallaFinal, text = i+1, font='Helvetica, 11').place(x=400,y=uy)
                                        Label(PantallaFinal, text= a['Procedimiento'][i], font='Helvetica, 12').place(x=420,y=uy)
                                        uy += 20           

                        boton_proc= Button(CrearReceta,text="añadir", font='Helvetica, 11', command = lambda:[Procedimiento(CrearReceta,entry_proc.get())])
                        boton_proc.place(x=655,y=105,width=50)
                        boton_submit = Button(CrearReceta,text="Submit", font='Helvetica, 11',command=lambda:[validador_receta_nombre_cantidad()])
                        boton_submit.place(x=300,y=400)
                        boton_back = Button(CrearReceta, text='Back', font='Helvetica, 11', command=lambda: CrearReceta.destroy())
                        boton_back.place(x=150,y=400)    

                button_select = Button(window_menu, text="Continuar", bg='dark salmon', fg='black', font='Helvetica, 11', command=lambda: [validador_categorias(tipode_dieta.get(), horade_comida.get(), tipode_comida.get())])
                button_select.grid(row=9, column=1)
                back_button = Button(window_menu, text= "Back", font='Helvetica, 11',bg='dark salmon', fg='black', command= lambda: [window_menu.destroy(), menu_frame.destroy()])
                back_button.grid(row=9, column=0)

        def perfil_general():
                Perfil = Frame(window,width=800,height=900,bg="navajo white", bd='80')
                Perfil.grid(row=0, column=0)
                frame1=Frame(Perfil,width=800,height=900,bg="navajo white")
                frame1.grid(row=0,column=0)
                Label(frame1, text= 'Bienvenido a tu perfil', font='Helvetica, 18',bg='navajo white').grid(row=0, column=0)
        
                ModificarPerfil = Frame(Perfil,width=800,height=900,bg="navajo white", bd='11')
                ModificarPerfil.grid(row=1, column=0)
                frame2=Frame(ModificarPerfil,width=1800,height=900,bg="navajo white", bd='3')
                frame2.grid(row=0, column=0)
                LabelPerfil = Label(frame2, bg= 'navajo white')
                LabelPerfil.grid(row=0, column=0)

                def Modificar_Perfil():
                        def cambio_contrasena(usuario, contrasena_actual, contrasena_nueva, confirmar):
                                if not iniciar_sesion(usuario, contrasena_actual):
                                        Label(frame2, text= "Contrasena actual es incorrecta, no puede cambiar el password", fg='indian red').grid(row=6, column=0)
                                else:            
                                        cuentas[usuario] = contrasena_nueva

                        LabelUsuario = Label(frame2, text=' Usuario:')
                        LabelUsuario.grid(row=2, column=0)
                        EntryUsuario = Entry(frame2, width=50)
                        EntryUsuario.grid(row=2, column=1)
                        LabelPassActual = Label(frame2, text='Contraseña actual')
                        LabelPassActual.grid(row=3, column=0)
                        EntryPassActual = Entry(frame2, width=50)
                        EntryPassActual.grid(row=3, column=1)
                        LabelPassNuevo = Label(frame2, text='Contraseña nueva')
                        LabelPassNuevo.grid(row=4, column=0)
                        EntryPassNuevo = Entry(frame2, width=50)
                        EntryPassNuevo.grid(row=4, column=1)
                        LabelPassNuevoConf = Label(frame2, text='Confirmar contraseña nueva')
                        LabelPassNuevoConf.grid(row=5, column=0)
                        EntryPassNuevoConf = Entry(frame2, width=50)
                        EntryPassNuevoConf.grid(row=5, column=1)
                        EjecutarBoton = Button(frame2, text= 'Aceptar cambio', bg= 'salmon', command= lambda: [cambio_contrasena(EntryUsuario.get(), EntryPassActual.get(), EntryPassNuevo.get(), EntryPassNuevoConf.get()), frame2.destroy(), Perfil.destroy()])
                        EjecutarBoton.grid(row=7, column=1)

                LabelAviso = Label(frame1, text= "No puedes modificar tu contraseña si tu usuario es nuevo")
                LabelAviso.grid(row=1, column=0)
                Boton2 = Button(frame1,text="Modificar Contraseña", bg='tomato', command= lambda: Modificar_Perfil())
                Boton2.grid(row=2, column=0)
                Boton3 = Button(frame1, text= 'Back', bg='tomato', command= lambda: [frame1.destroy(), Perfil.destroy()])
                Boton3.grid(row=3, column=1)


        def buscar_recetas():
                def filtro2(dieta, hora, tipo):
                        if tipode_dieta.get() == "Vegana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "No especificar":
                                f ='Recetas_Vegana_Desayuno_No_especificar.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Comida" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegana_Comida_No_especificar.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_Cena_Dulce.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "Cena" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegana_Cena_No_especificar.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegana_No_especificar_Salado.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegana_No_especificar_Dulce.txt'
                        elif tipode_dieta.get() == "Vegana" and horade_comida.get() == "No especificar" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegana_No_especificar_No_especificar.txt'

                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegetariana_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegetariana_Desayuno_No_especificar.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegetariana_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Comida" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegetariana_Comida_No_especificar.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Vegetariana_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_Cena_Dulce.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "Cena" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegetariana_Cena_No_especificar.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "No especificar" and tipode_comida.get() =="Salado":
                                f = 'Recetas_Vegetariana_No_especificar_Salado.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Vegetariana_No_especificar_Dulce.txt'
                        elif tipode_dieta.get() == "Vegetariana" and horade_comida.get() == "No especificar" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Vegetariana_No_especificar_No_especificar.txt'

                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Dietetica_Desayuno_No_especificar.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Comida" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Dietetica_Comida_No_especificar.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_Cena_Dulce.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "Cena" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Dietetica_Cena_No_especificar.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Salado":
                                f = 'Recetas_Dietetica_No_especificar_Salado.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_Dietetica_No_especificar_Dulce.txt'
                        elif tipode_dieta.get() == "Dietetica" and horade_comida.get() == "No especificar" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_Dietetica_No_especificar_No_especificar.txt'

                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Salado":
                                f = 'Recetas_SinRestriccion_Desayuno_Salado.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_SinRestriccion_Desayuno_Dulce.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Desayuno" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_SinRestriccion_Desayuno_No_especificar.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Comida" and tipode_comida.get() == "Salado":
                                f = 'Recetas_SinRestriccion_Comida_Salado.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Comida" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_SinRestriccion_Comida_Dulce.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Comida" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_SinRestriccion_Comida_No_especificar.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Cena" and tipode_comida.get() == "Salado":
                                f = 'Recetas_SinRestriccion_Cena_Salado.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Cena" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_SinRestriccion_Cena_Dulce.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "Cena" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_SinRestriccion_Cena_No_especificar.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Salado":
                                f = 'Recetas_SinRestriccion_No_especificar_Salado.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "No especificar" and tipode_comida.get() == "Dulce":
                                f = 'Recetas_SinRestriccion_No_especificar_Dulce.txt'
                        elif tipode_dieta.get() == "Sin Restriccion" and horade_comida.get() == "No especificar" and tipode_comida.get() == "No especificar":
                                f = 'Recetas_SinRestriccion_No_especificar_No_especificar.txt'
                        return f

                menu_frame = Frame(window)
                menu_frame.config(background='navajo white', bd= '39', relief='flat')
                menu_frame.config(width=10000, height=1000)
                menu_frame.grid(row=0, column=0)
                window_menu = Frame(menu_frame)
                window_menu.grid(row=0, column=0)
                window_menu.config(width=10000, height=1500, bd= '40', relief= 'flat')
                window_menu.config(background='navajo white')
                tittle = Label(window_menu, text='¿Qué tipo de receta buscas?', font='Helvetica, 13',bg='navajo white').grid(row=0, column=0)
                window_menu.combo = ttk.Combobox(window_menu)
                labelTop = tk.Label(window_menu,
                                text = "Tipo de dieta", bg='navajo white', font='Helvetica, 11')
                labelTop.grid(row=1, column=0)
                tipode_dieta = ttk.Combobox(window_menu,values=["(seleccionar)","Vegana", "Vegetariana", 
                                        "Dietetica","Sin restriccion"])
                tipode_dieta.config(font='Helvetica, 11')
                tipode_dieta.grid(row=1, column=1)
                tipode_dieta.current(0)
                window_menu.combo = ttk.Combobox(window_menu)
                labelTop = tk.Label(window_menu,
                                text = "Hora de comida", bg='navajo white', font='Helvetica, 11')
                labelTop.grid(row=3, column=0)
                horade_comida = ttk.Combobox(window_menu,values=["(seleccionar)","Desayuno", "Comida", 
                                        "Cena", "No especificar"])
                horade_comida.config(font='Helvetica, 11')
                horade_comida.grid(row=3, column=1)
                horade_comida.current(0)
                window_menu.combo = ttk.Combobox(window_menu)
                labelTop = tk.Label(window_menu,
                                text = "Tipo de comida", bg='navajo white', font='Helvetica, 11')
                labelTop.grid(row=5, column=0)
                tipode_comida = ttk.Combobox(window_menu,values=["(seleccionar)","Dulce", "Salado", "No especificar"])
                tipode_comida.config(font='Helvetica, 11')
                tipode_comida.grid(row=5, column=1)
                tipode_comida.current(0)

                def validador_categorias(dieta, hora, tipo):
                        estatus_seleccion = tk.StringVar()
                        estatus_seleccion.set('')
                        if tipode_dieta.get() == '(seleccionar)' and horade_comida.get() == '(seleccionar)' and tipode_comida.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=2, column=1)
                                hora_novalida = Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                hora_novalida.grid(row=4, column=1)
                                tipo_novalido= Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                tipo_novalido.grid(row=6, column=1)
                                
                        else:
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                dieta_no_valida.grid(row=2, column=1)
                                hora_novalida = Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                hora_novalida.grid(row=4, column=1)
                                tipo_novalido= Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                tipo_novalido.grid(row=6, column=1)
                                
                                        
                        if tipode_dieta.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=2, column=1)
                        else:
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')

                        if horade_comida.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=4, column=1)
                        else: 
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                hora_novalida = Label(window_menu, textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                hora_novalida.grid(row=4, column=1)

                        if tipode_comida.get() == '(seleccionar)':
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('Categoría no válida, selecciona una categoría')
                                dieta_no_valida.grid(row=6, column=1)
                        else:
                                estatus_seleccion = tk.StringVar()
                                estatus_seleccion.set('')
                                dieta_no_valida=Label(window_menu ,textvariable= estatus_seleccion, fg= 'indian red', bg='navajo white', font='Helvetica, 10')
                                estatus_seleccion.set('                                                                  ')
                                dieta_no_valida.grid(row=6, column=1)
                
                def formato(recetas_file,count):
                        
                        formato = Frame(window,width=1200,height=900,bg="navajo white")
                        formato.place(x=0,y=0)
                        
                        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
                        
                        f = open(recetas_file, 'r')
                        numero_recetas = f.readlines()
                        a = ast.literal_eval(numero_recetas[count])
                        
                        vy = 90
                        uy = 90
                        
                        Label(formato, text = "Receta: ").place(x=0,y=0)
                        Label(formato, text = a['Nombre de Receta']).place(x=50,y=0)
                        Label(formato, text = "Cantidad de la porción: ").place(x=0,y=25)
                        Label(formato, text = a['Cantidad']).place(x=145,y=25)
                        Label(formato, text = "Ingredientes", font=fontStyle).place(x=0,y=55)
                        for i in range(len(a['Lista de Ingredientes'])):
                                Label(formato,text= a['Lista de Ingredientes'][i]).place(x=0,y=vy)
                                vy += 25
                        Label(formato, text = 'Procedimiento', font=fontStyle).place(x=400,y=55)
                        Button(formato, text='Volver', command=lambda: [formato.destroy()]).place(x=700, y=10)
                        #Button(formato, text='Regresar al menu principal', command= lambda: [window_menu.destroy(), menu_frame.destroy()]).place(x=700, y=300)
                        for i in range(len(a['Procedimiento'])):
                                Label(formato, text = i+1).place(x=400,y=uy)
                                Label(formato, text= a['Procedimiento'][i]).place(x=420,y=uy)
                                uy += 25

                        
                        fig = Figure( figsize=(20, 9), dpi=80 )
                        
                        x = a['Dificultad']
                        y=100-int(x)
                        Dificultad = [x,y]
                        nombres = [x+"%",""]
                        colores = ["pink","grey"]
                        plt.pie(Dificultad,autopct="%0.1f %%",colors=colores)
                        plt.axis("equal")
                        plt.show()
                        
                lista_recetas = []
                def RecetaEspecifica(file,recetas):
                        f = open(file, 'r')
                        numero_recetas = f.readlines()
                        count = 0
                        for i in range(len(numero_recetas)):
                                a = ast.literal_eval(numero_recetas[i])
                                if recetas in a['Nombre de Receta']:
                                        formato(file,count)
                                else:
                                        count += 1

                                

                def AbrirRecetas(file,b,c,d):
                        global botones_lista
                        AbrirRecetas = Frame(window,width=1200,height=900,bg="navajo white")
                        AbrirRecetas.place(x=0,y=0)
                        
                        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
                        
                        Label(AbrirRecetas, text = 'Recetas con filtros:', font=fontStyle, bg='navajo white').place(x=0,y=0)
                        Label(AbrirRecetas, text = 'Tipo de Dieta:', bg='navajo white').place(x=0,y=30)
                        Label(AbrirRecetas, text= b).place(x=110,y=30)
                        Label(AbrirRecetas, text = 'Hora de Comida:', bg='navajo white').place(x=0,y=50)
                        Label(AbrirRecetas, text= c).place(x=110,y=50)
                        Label(AbrirRecetas, text = 'Tipo de Comida:', bg='navajo white').place(x=0,y=70)
                        Label(AbrirRecetas, text= d).place(x=110,y=70)
                        Label(AbrirRecetas, text = 'Seleccione Receta que deseas cocinar', font=fontStyle, bg='navajo white').place(x=0,y=100)
                        
                        f = open(file, 'r')
                        numero_recetas = f.readlines()
                        for i in range(len(numero_recetas)):
                                a = ast.literal_eval(numero_recetas[i])
                                lista_recetas.append(a['Nombre de Receta'])
                        recetas = ttk.Combobox(AbrirRecetas,values=lista_recetas)
                        recetas.place(x=0,y=140)
                        seleccionar = Button(AbrirRecetas,text = 'Seleccionar',command = lambda:[RecetaEspecifica(file,recetas.get())])
                        seleccionar.place(x=0,y=180)
                        back_back = Button(AbrirRecetas,text = 'Regresar al menu',command = lambda: [AbrirRecetas.destroy(), window_menu.destroy(), menu_frame.destroy()])
                        back_back.place(x=0,y=280)

                button_select = Button(window_menu, text="Continuar", bg='dark salmon', fg='black', font='Helvetica, 11', command=lambda: [validador_categorias(tipode_dieta.get(), horade_comida.get(), tipode_comida.get()), AbrirRecetas(filtro2(tipode_dieta.get(),horade_comida.get(),tipode_comida.get()),tipode_dieta.get(),horade_comida.get(),tipode_comida.get())])
                button_select.grid(row=9, column=1)
                back_button = Button(window_menu, text= "Back", font='Helvetica, 11',bg='dark salmon', fg='black', command= lambda: [window_menu.destroy(), menu_frame.destroy()])
                back_button.grid(row=9, column=0)

        def buscar_ingresar_menu():
                menu_frame = Frame(window)
                menu_frame.config(background='navajo white', bd= '40', relief='flat', width=1000, height=250)
                menu_frame.grid(row=0, column=0)
                buscar_ingresar = Frame(menu_frame)
                buscar_ingresar.grid(row=0, column=0)
                buscar_ingresar.config(width=1000, height=250)
                buscar_ingresar.config(background='navajo white', bd= '10', relief='flat')
                accion = Label(buscar_ingresar, text='¿Que deseas hacer?', font='Helvetica, 16', fg='indian red', bg='navajo white').grid(row=0, column=0)
                ingresar_label = Label(buscar_ingresar, text='                ', font='Helvetica, 13', fg='saddle brown', bg='navajo white').grid(row=1, column=1)
                ingresar= Button(buscar_ingresar, text='Nueva receta', font='Helvetica, 10', bg= 'dark salmon', fg='black', command=lambda: ingreso_recetas())
                ingresar.grid(row=2, column=1)
                buscar_label = Label(buscar_ingresar, text='             ', font='Helvetica, 13', fg='saddle brown', bg='navajo white').grid(row=3, column=1)
                buscar= Button(buscar_ingresar, text='Buscar receta', font='Helvetica, 10', bg= 'dark salmon', fg='black', command=buscar_recetas)
                buscar.grid(row=4, column=1)
                modificar_perfil = Label(buscar_ingresar, text='                 ', font='Helvetica, 13', fg='saddle brown', bg='navajo white').grid(row=5, column=1)
                perfil = Button(buscar_ingresar, text='Perfil', font='Helvetica, 10', bg= 'dark salmon', fg='black', command=perfil_general)
                perfil.grid(row=13, column=1)
                back_button = Button(buscar_ingresar, text= "Back", font='Helvetica, 10',bg='dark salmon', fg='black', command= lambda: [buscar_ingresar.destroy(), menu_frame.destroy()])
                back_button.grid(column=0, row=13)        
        
        #admin = Button(inicio_frame, text='ADMIN', bg='sandy brown', fg='black', font='Helvetica, 13', command=buscar_ingresar_menu).grid(row= 14, column= 2)

pagina_inicial()

        
window.mainloop()
guardar_info_usuarios()
