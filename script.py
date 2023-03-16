from PyQt5 import QtWidgets, uic
import sqlite3
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem,QApplication,QPushButton
from tkinter import messagebox
from random import randint
import total
db=sqlite3.connect('data.db')
cr=db.cursor()
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the UI files
        self.login=uic.loadUi('login.ui')
        self.cree=uic.loadUi('cree.ui')
        self.dashboard=uic.loadUi('dashboard.ui')
        self.users=uic.loadUi('users.ui')
        self.sim=uic.loadUi('sim.ui')
        self.add=uic.loadUi('BUYSIM.ui')
        self.wifi=uic.loadUi('wifi.ui')
        self.buy_wifi=uic.loadUi('BUYWIFI.ui')
        self.diagnostic=uic.loadUi('diagnostic.ui')
        self.call=uic.loadUi('call.ui')
        self.bwu=uic.loadUi('BWU.ui')
        self.bsu=uic.loadUi('BSU.ui')
        self.scall=uic.loadUi('scall.ui')
        self.mois=1
        self.to_pay_mois=3
        self.users.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.wifi.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.sim.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.users.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.wifi.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.sim.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.users.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.wifi.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.diagnostic.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.diagnostic.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.diagnostic.tableWidget_2.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.diagnostic.tableWidget_2.verticalHeader().setStyleSheet("QHeaderView::section {background-color: transparent;}")
        self.wifi.tableWidget.setShowGrid(False)
        self.diagnostic.tableWidget_2.setShowGrid(False)
        self.diagnostic.tableWidget.setShowGrid(False)
        self.users.tableWidget.setShowGrid(False)
        self.sim.tableWidget.setShowGrid(False)
        self.stack = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Add the pages to the stacked widget
        self.stack.addWidget(self.login)
        self.stack.addWidget(self.cree)
        self.stack.addWidget(self.dashboard)#1
        self.stack.addWidget(self.users)#2
        self.stack.addWidget(self.sim)#3
        self.stack.addWidget(self.add)#4
        self.stack.addWidget(self.wifi)#5
        self.stack.addWidget(self.buy_wifi)#6
        self.stack.addWidget(self.diagnostic)#7
        self.stack.addWidget(self.call)#9
        self.stack.addWidget(self.bwu)#10
        self.stack.addWidget(self.bsu)#11
        self.stack.addWidget(self.scall)
    def switch_page(self,x):
        self.stack.setCurrentIndex(x)
    def show_data_in_dashboard(self):
        online=0
        local=0
        online_local=0
        cr.execute(f"select abonnemnt from clients ")
        result=cr.fetchall()
        for i in range(len(result)):
            x=str(result[i][0])
            if x.startswith('O'):
                online+=1
            elif x.startswith('L'):
                local+=1
            elif x.startswith('T'):
                online_local+=1
        cr.execute("select * from sim")
        sim=cr.fetchall()
        cr.execute("select * from disponible")
        dispo=cr.fetchall()
        cr.execute("select * from sim where type='O'")
        o=cr.fetchall()
        cr.execute("select * from sim where type='L'")
        l=cr.fetchall()
        self.sim.label_29.setText(str(len(sim)))
        self.sim.label_31.setText(str(len(dispo)))
        self.sim.label_34.setText(str(len(o)))
        self.sim.label_33.setText(str(len(l)))
        self.add.label_29.setText(str(len(sim)))
        self.add.label_31.setText(str(len(dispo)))
        self.add.label_34.setText(str(len(o)))
        self.add.label_33.setText(str(len(l)))
        self.users.label_29.setText(str(local))
        self.users.label_31.setText(str(online))
        self.users.label_33.setText(str(online_local))
        self.dashboard.label_29.setText(str(local))
        self.dashboard.label_64.setText(str(online))
        self.dashboard.label_33.setText(str(online_local))
        self.dashboard.label_38.setText(str(len(sim)))
        self.dashboard.label_37.setText(str(len(dispo)))
        self.dashboard.label_36.setText(str(len(o)))
        self.dashboard.label_34.setText(str(len(l)))
        cr.execute("select * from routers where installation='AVEC INSTALATION'")
        avec=cr.fetchall()
        cr.execute("select * from routers where installation='SANS INSTALLATION'")
        sans=cr.fetchall()
        cr.execute("select * from wifi where type='O'")
        ow=cr.fetchall()
        cr.execute("select * from wifi where type='L'")
        lw=cr.fetchall()
        cr.execute("select price from payment_wifi")
        wifi_pric=cr.fetchall()
    
        sum_wifi_price=0
        for i in range(len(wifi_pric)):
            sum_wifi_price+=wifi_pric[i][0]
        cr.execute("select frais from wifi")
        frais=cr.fetchall()
        for i in range(len(frais)):
            sum_wifi_price+=frais[i][0]
        wifi_pric=cr.fetchall()
        self.wifi.label_29.setText(str(len(avec)))
        self.dashboard.label_45.setText(str(len(avec)))
        self.dashboard.label_44.setText(str(len(sans)))
        self.wifi.label_31.setText(str(len(sans)))
        self.wifi.label_34.setText(str(len(ow)))
        self.dashboard.label_43.setText(str(len(ow)))
        self.wifi.label_33.setText(str(len(lw)))
        self.dashboard.label_42.setText(str(len(lw)))
        self.buy_wifi.label_29.setText(str(len(avec)))
        self.buy_wifi.label_31.setText(str(len(sans)))
        self.buy_wifi.label_34.setText(str(len(ow)))
        self.buy_wifi.label_33.setText(str(len(lw)))
        self.dashboard.label_18.setText(f"{sum_wifi_price} DH")
        self.buy_wifi.label_13.setText(f"{sum_wifi_price} DH")
        self.wifi.label_13.setText(f"{sum_wifi_price} DH")
        cr.execute("select * from payment_wifi where price='0'")
        dont=cr.fetchall()
        self.diagnostic.label_29.setText(f"{str(len(dont))}")
        self.dashboard.label_50.setText(f"{str(len(dont))}")
        cr.execute("select call from sim ")
        call=cr.fetchall()
        cr.execute("select sms from sim ")
        sms=cr.fetchall()
        cr.execute("select data from sim ")
        data=cr.fetchall()
        cr.execute("select solde from sim ")
        solde=cr.fetchall()
        sum_call=0
        sum_sms=0
        sum_data=0
        sum_solde=0
        for i in range(len(call)):
            sum_call+=call[i][0]
            sum_sms+=sms[i][0]
            sum_data+=data[i][0]
            sum_solde+=solde[i][0]
        self.diagnostic.label_32.setText(f"{str(sum_call)}")
        self.dashboard.label_51.setText(f"{str(sum_call)}")
        self.diagnostic.label_34.setText(f"{str(sum_sms)}")
        self.dashboard.label_49.setText(f"{str(sum_sms)}")
        self.diagnostic.label_35.setText(f"{str(sum_data)}")
        self.dashboard.label_57.setText(f"{str(sum_data)}")
        self.diagnostic.label_32.setText(f"{str(sum_call)}")
        self.diagnostic.label_41.setText(f"{str(sum_solde)}")
        self.dashboard.label_48.setText(f"{str(sum_solde)}")
        cr.execute(f"select price from sim_payment")
        price_sim=cr.fetchall()
        sum_price_sim=0
        for i in range(len(price_sim)):
                sum_price_sim+=price_sim[i][0]
        self.dashboard.label_15.setText(f"{sum_price_sim} DH")
        self.sim.label_13.setText(f"{sum_price_sim} DH")
        self.add.label_13.setText(f"{sum_price_sim} DH")
    def show_data_in_tabel(self):
        cr.execute("SELECT c.*,sum(price) from clients c left join sim_payment s on c.cin=s.id GROUP BY c.cin")
        client=cr.fetchall()
        cr.execute(f"select * from sim")
        sim=cr.fetchall()
        for i in range(len(client)):
            self.users.tableWidget.setRowCount(i+1)
            for j in range(len(client[0])):
             item=QTableWidgetItem(str(client[i][j]))
             self.users.tableWidget.setItem(i,j, item)
        for i in range(len(sim)):
            self.sim.tableWidget.setRowCount(i+1)
            for j in range(1,len(sim[0])):
             item=QTableWidgetItem(str(sim[i][j]))
             self.sim.tableWidget.setItem(i,j-1, item)
        cr.execute(f"select * from clients where abonnemnt='OS' or abonnemnt='LS' or abonnemnt='TWS' or abonnemnt='OWS' or abonnemnt='LWS'  ")
        client=cr.fetchall()
        for i in range(len(client)):
            for j in range(len(client[0])):
             item=QTableWidgetItem(str(client[i][j]))
             self.sim.tableWidget.setItem(i,j+6, item)
        cr.execute("select * from wifi")
        wifi=cr.fetchall()
        cr.execute("select * from clients where abonnemnt='OW' or abonnemnt='LW' or abonnemnt='TWS' or abonnemnt='OWS' or abonnemnt='LWS' ")
        client_wifi=cr.fetchall()
        for i in range(len(wifi)):
            self.wifi.tableWidget.setRowCount(i+1)
            for j in range(1,len(wifi[0])):
             item=QTableWidgetItem(str(wifi[i][j]))
             self.wifi.tableWidget.setItem(i,j-1, item)
        for i in range(len(client_wifi)):
            for j in range(len(client_wifi[0])):
             item=QTableWidgetItem(str(client_wifi[i][j]))
             self.wifi.tableWidget.setItem(i,j+6, item)
        cr.execute("select * from payment_wifi")
        pay=cr.fetchall()
        cr.execute("select * from sim")
        sims=cr.fetchall()
        for i in range(len(sims)):
            self.diagnostic.tableWidget_2.setRowCount(i+1)
            for j in range(1,len(sims[0])):
             item=QTableWidgetItem(str(sims[i][j]))
             self.diagnostic.tableWidget_2.setItem(i,j-1, item)
        for i in range(len(pay)):
            self.diagnostic.tableWidget.setRowCount(i+1)
            for j in range(len(pay[0])):
             item=QTableWidgetItem(str(pay[i][j]))
             self.diagnostic.tableWidget.setItem(i,j, item)
    def search_in_client_tables(self):
        cr.execute(f"select * from clients where cin ='{self.users.plainTextEdit.toPlainText()}'")
        result=cr.fetchall()
        if result!=[]:
         for i in range(len(result)):
            self.users.tableWidget.setRowCount(i+1)
            for j in range(len(result[0])):
             item=QTableWidgetItem(str(result[i][j]))
             self.users.tableWidget.setItem(i,j, item)
        else:
            messagebox.showerror("","CIN not foundid")
    def search_in_sim_table(self):
        cr.execute(f"select * from clients where cin='{self.sim.plainTextEdit.toPlainText()}' ")
        cliento=cr.fetchall()
        cr.execute(f"select * from sim where numero='{self.sim.plainTextEdit.toPlainText()}' ")
        simo=cr.fetchall()
        if cliento!=[] and simo==[]:
            cr.execute(f"select * from sim where cin='{self.sim.plainTextEdit.toPlainText()}' ")
            sim=cr.fetchall()
            for i in range(len(sim)):
             self.sim.tableWidget.setRowCount(i+1)
             for j in range(1,len(sim[0])):
              item=QTableWidgetItem(str(sim[i][j]))
              self.sim.tableWidget.setItem(i,j-1, item)
            for i in range(len(cliento)):
             for j in range(len(cliento[0])):
              item=QTableWidgetItem(str(cliento[i][j]))
              self.sim.tableWidget.setItem(i,j+6, item)
        elif cliento==[] and simo!=[]:
            cr.execute(f"select cin from sim where numero='{self.sim.plainTextEdit.toPlainText()}'")
            cin=cr.fetchone()
            cr.execute(f"select * from clients where cin='{cin[0]}' ")
            data=cr.fetchall()
            for i in range(len(simo)):
             self.sim.tableWidget.setRowCount(i+1)
             for j in range(1,len(simo[0])):
              item=QTableWidgetItem(str(simo[i][j]))
              self.sim.tableWidget.setItem(i,j-1, item)
            for i in range(len(data)):
             for j in range(len(data[0])):
              item=QTableWidgetItem(str(data[i][j]))
              self.sim.tableWidget.setItem(i,j+6, item)
        elif cliento==[] and simo==[]:
            messagebox.showerror("","sim user not foundid")
    def generete_numbers(self):
        number=generate_fen.plainTextEdit.toPlainText()
        if all([generate_fen.plainTextEdit.toPlainText()]) and number.isdigit() :
         if int(generate_fen.plainTextEdit.toPlainText())>0:
          for i in range(int(generate_fen.plainTextEdit.toPlainText())):
           random=randint(00000000,99999999)
           number=f"06{random}"
           cr.execute(f"select numero from sim where numero='{number}'")
           result=cr.fetchone()
           while result!=None:
            random=randint(000000000,999999999)
            number=f"06{random}"
            cr.execute(f"select numero from sim where numero='{number}'")
            result=cr.fetchone()
           cr.execute(f"insert into disponible values('{number}')")
           db.commit()
          messagebox.showinfo("",f"{generate_fen.plainTextEdit.toPlainText()} generated")
         elif int(generate_fen.plainTextEdit.toPlainText())<=0 :
            messagebox.showerror("","number error")
        else: 
            messagebox.showerror("","number error")
        self.show_data_in_dashboard()
    def add_sim(self):
        cr.execute("select numero from disponible ")
        numero=cr.fetchone()
        if all([self.add.plainTextEdit.toPlainText(),self.add.plainTextEdit_2.toPlainText(),self.add.plainTextEdit_3.toPlainText(),self.add.plainTextEdit_4.toPlainText(),self.add.plainTextEdit_5.toPlainText()]):
            cr.execute(f"select cin from sim where cin='{self.add.plainTextEdit_5.toPlainText()}'")
            if cr.fetchone()==None:
             cr.execute("select *from disponible")
             result=cr.fetchall()
             if len(result)>0:
              cr.execute(f"select abonnemnt from clients where cin='{self.add.plainTextEdit_5.toPlainText()}'")
              result=cr.fetchone()
              if result==None:
               cr.execute(f"insert into clients values('{self.add.plainTextEdit_5.toPlainText()}','{self.add.plainTextEdit.toPlainText()}','{self.add.plainTextEdit_2.toPlainText()}','{self.add.plainTextEdit_3.toPlainText()}','LS','{self.add.plainTextEdit_4.toPlainText()}') ")
               
               cr.execute(f"delete  from disponible where numero='{numero[0]}' ")
               cr.execute(f"insert into sim values('{self.add.plainTextEdit_5.toPlainText()}','{numero[0]}','L','0','0','0','0')")
               db.commit()
               self.show_data_in_dashboard()
               self.show_data_in_tabel()
               window.add.plainTextEdit.clear()
               window.add.plainTextEdit_2.clear()
               window.add.plainTextEdit_3.clear()
               window.add.plainTextEdit_4.clear()
               window.add.plainTextEdit_5.clear()
               messagebox.showinfo("",f"le numero de client est {numero[0]}")
              elif   result[0]=='LW'  :
                cr.execute(f"update clients  SET abonnemnt='LWS' where cin='{self.add.plainTextEdit_5.toPlainText()}' ")
                cr.execute(f"insert into sim values('{self.add.plainTextEdit_5.toPlainText()}','{numero[0]}','L','0','0','0','0')")
                db.commit()
                window.add.plainTextEdit.clear()
                window.add.plainTextEdit_2.clear()
                window.add.plainTextEdit_3.clear()
                window.add.plainTextEdit_4.clear()
                window.add.plainTextEdit_5.clear()
                messagebox.showinfo("",f"le numero de client est {numero[0]}")
                self.show_data_in_dashboard()
                self.show_data_in_tabel()
              elif result[0]=='OW':
                cr.execute(f"update clients  SET abonnemnt='TWS' where cin='{self.add.plainTextEdit_5.toPlainText()}' ")
                cr.execute(f"insert into sim values('{self.add.plainTextEdit_5.toPlainText()}','{numero[0]}','L','0','0','0','0')")
                db.commit()
                window.add.plainTextEdit.clear()
                window.add.plainTextEdit_2.clear()
                window.add.plainTextEdit_3.clear()
                window.add.plainTextEdit_4.clear()
                window.add.plainTextEdit_5.clear()
                messagebox.showinfo("",f"le numero de client est {numero[0]}")
                self.show_data_in_dashboard()
                self.show_data_in_tabel()

             else:
                messagebox.showerror("","please generate numbers")
            else:
                messagebox.showinfo("","a deja une carte sim")

        else:
            messagebox.showinfo("","completer les donnes")
    def generate_routers(self):
        number=generate_ROU.plainTextEdit.toPlainText()
        if all([generate_ROU.plainTextEdit.toPlainText()]) and number.isdigit() :
         if int(generate_ROU.plainTextEdit.toPlainText())>0:
            for i in range(int(number)):
                id=randint(0000,9999)
                cr.execute(f"select id from routers where id='{id}'")
                if cr.fetchone()!=None:
                    while cr.fetchone()!=None:
                        id=randint(0000,9999)
                        cr.execute(f"select id from routers where id='{id}'")
                cr.execute(f"insert into routers values('{id}','{generate_ROU.comboBox.currentText()}')")
                db.commit()
                self.show_data_in_dashboard()
                self.show_data_in_tabel()
            messagebox.showinfo("",f"{number} add succsefully")
         else:
            messagebox.showerror("","number error")
        else:
            messagebox.showerror("","number error")
    def check_price(self):
        number=self.buy_wifi.plainTextEdit_6.toPlainText()
        if all([self.buy_wifi.plainTextEdit_6.toPlainText()]):
             if number.isdigit() and int(number)>0:
                    if self.buy_wifi.comboBox.currentText()=='AVEC INSTALATION':
                        self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                    else:
                        self.buy_wifi.label_17.setText(f"le prix de premiere mois et le materile est :{(int(number)*10)+100} et le prix des autres mois est {(int(number)*10)}")
             else:
                messagebox.showerror("","number error")
                self.buy_wifi.label_17.setText(f"")
        else:
            messagebox.showerror("","number error")
            self.buy_wifi.label_17.setText(f"")
    def wifi_buy(self):
        number=self.buy_wifi.plainTextEdit_6.toPlainText()
        cr.execute(f"select installation from routers where installation='{self.buy_wifi.comboBox.currentText()}' ")
        router=cr.fetchone()
        if all([self.buy_wifi.plainTextEdit.toPlainText(),self.buy_wifi.plainTextEdit_2.toPlainText(),self.buy_wifi.plainTextEdit_3.toPlainText(),self.buy_wifi.plainTextEdit_4.toPlainText(),self.buy_wifi.plainTextEdit_5.toPlainText(),self.buy_wifi.plainTextEdit_6.toPlainText()]):
            if number.isdigit() and int(number)>0:
             cr.execute(f"select cin from wifi where cin='{self.buy_wifi.plainTextEdit_5.toPlainText()}'")
             if cr.fetchone()==None:
                if router!=None:
                 cr.execute(f"select abonnemnt from clients where cin='{self.buy_wifi.plainTextEdit_5.toPlainText()}'")
                 result=cr.fetchone()
                 if result==None:
                    if self.buy_wifi.comboBox.currentText()=='AVEC INSTALATION':
                     cr.execute(f"insert into clients values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{self.buy_wifi.plainTextEdit.toPlainText()}','{self.buy_wifi.plainTextEdit_2.toPlainText()}','{self.buy_wifi.plainTextEdit_3.toPlainText()}','LW','{self.buy_wifi.plainTextEdit_4.  toPlainText()}')")
                     self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                     cr.execute("select id from routers where installation='AVEC INSTALATION' ")
                     id=cr.fetchone()
                     cr.execute(f"insert into wifi values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{id[0]}','L','{self.buy_wifi.plainTextEdit_6.toPlainText()}','AVEC INSTALATION','{(int(number))*10}','{250}')")
                     cr.execute(f"insert into payment_wifi values('{id[0]}','{self.mois}','{int((number))*10}')")
                     cr.execute(f"delete from routers where id='{id[0]}' ")
                     db.commit()
                     messagebox.showinfo("","opeartion sucessufuly")
                     self.show_data_in_dashboard()
                     self.show_data_in_tabel()
                    elif self.buy_wifi.comboBox.currentText()=='SANS INSTALLATION':
                     cr.execute(f"insert into clients values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{self.buy_wifi.plainTextEdit.toPlainText()}','{self.buy_wifi.plainTextEdit_2.toPlainText()}','{self.buy_wifi.plainTextEdit_3.toPlainText()}','LW','{self.buy_wifi.plainTextEdit_4.  toPlainText()}')")
                     self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+100} et le prix des autres mois est {(int(number)*10)}")
                     cr.execute("select id from routers where installation='SANS INSTALLATION' ")
                     id=cr.fetchone()
                     cr.execute(f"insert into wifi values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{id[0]}','L','{self.buy_wifi.plainTextEdit_6.toPlainText()}','SANS INSTALLATION','{(int(number))*10}','{100}')")
                     cr.execute(f"insert into payment_wifi values('{id[0]}','{self.mois}','{int((number))*10}')")
                     cr.execute(f"delete from routers where id='{id[0]}' ")
                     db.commit()
                     messagebox.showinfo("","opeartion sucessufuly")
                     self.show_data_in_dashboard()
                     self.show_data_in_tabel()
                 else:
                    if self.buy_wifi.comboBox.currentText()=='AVEC INSTALATION':
                     if result[0]=='OS':
                      cr.execute(f"update clients set abonnemnt='TWS' where cin='{self.buy_wifi.plainTextEdit_5.toPlainText()}'")
                      self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='AVEC INSTALATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{id[0]}','L','{self.buy_wifi.plainTextEdit_6.toPlainText()}','AVEC INSTALATION','{(int(number))*10}','250')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{self.mois}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      self.show_data_in_dashboard()
                      self.show_data_in_tabel()
                     elif result[0]=='LS' :
                      cr.execute(f"update clients set abonnemnt='LWS' where  cin='{self.buy_wifi.plainTextEdit_5.toPlainText()}'")
                      self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='AVEC INSTALATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{id[0]}','L','{self.buy_wifi.plainTextEdit_6.toPlainText()}','AVEC INSTALATION','{(int(number))*10}','250')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{self.mois}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      self.show_data_in_dashboard()
                      self.show_data_in_tabel()
                    elif self.buy_wifi.comboBox.currentText()=='SANS INSTALLATION':
                     if result[0]=='OS':
                      cr.execute(f"update clients set abonnemnt='TWS' where  cin='{self.buy_wifi.plainTextEdit_5.toPlainText()}'")
                      self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='SANS INSTALLATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{id[0]}','L','{self.buy_wifi.plainTextEdit_5.toPlainText()}','SANS INSTALLATION','{(int(number))*10+150}','{(int(number))*10}')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{self.mois}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      self.show_data_in_dashboard()
                      self.show_data_in_tabel()
                     elif result[0]=='LS':
                      cr.execute(f"update clients set abonnemnt='LWS' where  cin='{self.buy_wifi.plainTextEdit_5.toPlainText()}'")
                      self.buy_wifi.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='SANS INSTALLATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{self.buy_wifi.plainTextEdit_5.toPlainText()}','{id[0]}','L','{self.buy_wifi.plainTextEdit_5.toPlainText()}','SANS INSTALLATION','{(int(number))*10+150}','{(int(number))*10}')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{self.mois}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      self.show_data_in_dashboard()
                      self.show_data_in_tabel()
                else:
                    messagebox.showerror("","router indisponible")
             else:
                messagebox.showerror("","l'utilisteur a dejaa un wifi")
            else:
                messagebox.showerror("","number error")
        else:
            messagebox.showerror("","complete information")
    def search_in_wifi_table(self):
        cr.execute(f"select * from clients where cin='{self.wifi.plainTextEdit.toPlainText()}' ")
        client_wifi=cr.fetchall()
        cr.execute(f"select * from wifi where id='{self.wifi.plainTextEdit.toPlainText()}' ")
        wifio=cr.fetchall()
        if client_wifi!=[] and wifio==[]:
            cr.execute(f"select * from wifi where cin='{self.wifi.plainTextEdit.toPlainText()}' ")
            wifi=cr.fetchall()
            for i in range(len(wifi)):
             self.wifi.tableWidget.setRowCount(i+1)
             for j in range(1,len(wifi[0])):
              item=QTableWidgetItem(str(wifi[i][j]))
              self.wifi.tableWidget.setItem(i,j-1, item)
            for i in range(len(client_wifi)):
             for j in range(len(client_wifi[0])):
              item=QTableWidgetItem(str(client_wifi[i][j]))
              self.wifi.tableWidget.setItem(i,j+6, item)
        elif client_wifi==[] and wifio!=[]:
            cr.execute(f"select cin from wifi where id='{self.wifi.plainTextEdit.toPlainText()}'")
            cin=cr.fetchone()
            cr.execute(f"select * from clients where cin='{cin[0]}' ")
            data=cr.fetchall()
            for i in range(len(wifio)):
             self.wifi.tableWidget.setRowCount(i+1)
             for j in range(1,len(wifio[0])):
              item=QTableWidgetItem(str(wifio[i][j]))
              self.wifi.tableWidget.setItem(i,j-1, item)
            for i in range(len(data)):
             for j in range(len(data[0])):
              item=QTableWidgetItem(str(data[i][j]))
              self.wifi.tableWidget.setItem(i,j+6, item)
        elif client_wifi==[] and wifio==[]:
            messagebox.showerror("","wifi user not foundid")
    def meessage_wifi_pay(self):
        cr.execute(f"select id from payment_wifi where price='0'")
        ids=cr.fetchall()
        if ids!=[]:
         for i in range(len(ids)):
            cr.execute(f"select mois from payment_wifi  where id ='{ids[i][0]}' and price='0'")
            mois=cr.fetchall()

            cr.execute(f"insert into message values('{ids[i][0]}','il faut payer {len(mois)} mois')")

            db.commit()
         messagebox.showwarning("","les message sont envoye")
        else:
            messagebox.showwarning("","tous les utilisateur sont paye le wifi")
def check_price():
        number=window.bwu.plainTextEdit_6.toPlainText()
        if all([window.bwu.plainTextEdit_6.toPlainText()]):
             if number.isdigit() and int(number)>0:
                    if window.bwu.comboBox.currentText()=='AVEC INSTALATION':
                        window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                    else:
                        window.bwu.label_17.setText(f"le prix de premiere mois et le materile est :{(int(number)*10)+100} et le prix des autres mois est {(int(number)*10)}")
def show_data():
        window.call.tableWidget.setRowCount(0)
        window.call.tableWidget_2.setRowCount(0)
        window.bwu.plainTextEdit.setReadOnly(False)
        window.bwu.plainTextEdit_2.setReadOnly(False)
        window.bwu.plainTextEdit_3.setReadOnly(False)
        window.bsu.plainTextEdit.setReadOnly(False)
        window.bsu.plainTextEdit_2.setReadOnly(False)
        window.bsu.plainTextEdit_3.setReadOnly(False)
        getUser=window.login.plainTextEdit.toPlainText()
        getPass=window.login.plainTextEdit_2.toPlainText()
        window.call.label_21.setText(f"{getUser}")
        window.bsu.label_21.setText(f"{getUser}")
        window.bwu.label_21.setText(f"{getUser}")
        cr.execute(f"select cin from users where email='{getUser}'")
        cin=cr.fetchone()
        window.bwu.plainTextEdit_5.clear()
        window.bwu.plainTextEdit_4.clear()
        window.bsu.plainTextEdit_4.clear()
        window.bsu.plainTextEdit_5.clear()
        window.bwu.plainTextEdit_5.insertPlainText(cin[0])
        window.bsu.plainTextEdit_5.insertPlainText(cin[0])
        window.bwu.plainTextEdit_4.insertPlainText(getUser)
        window.bsu.plainTextEdit_4.insertPlainText(getUser)
        cr.execute(f"select id from wifi where cin='{cin[0]}'")
        id=cr.fetchone()
        if id!=None:
         cr.execute(f"select * from payment_wifi where price='0' and id='{id[0]}'")
         dont=cr.fetchall()
         window.call.label_50.setText(f"{str(len(dont))}")
         window.bwu.label_50.setText(f"{str(len(dont))}")
        else:
            window.call.label_50.setText(f"you dont have wifi")
            window.bwu.label_50.setText(f"you dont have wifi")
            window.bsu.label_50.setText(f"you dont have wifi")
        cr.execute(f"select numero from sim where cin='{cin[0]}'  ")
        num=cr.fetchone()
        if num:
           window.call.label_22.setText(num[0])
           window.bsu.label_22.setText(num[0])
           window.bwu.label_24.setText(num[0])
        else:
           window.bwu.label_24.setText("no number")
           window.call.label_22.setText("no number")
           window.bsu.label_22.setText("no number")
        cr.execute(f"select call from sim where cin='{cin[0]}' ")
        call=cr.fetchall()
        if call!=[]:
         cr.execute(f"select sms from sim where cin='{cin[0]}' ")
         sms=cr.fetchall()
         cr.execute(f"select data from sim where cin='{cin[0]}' ")
         data=cr.fetchall()
         cr.execute(f"select solde from sim where cin='{cin[0]}' ")
         solde=cr.fetchall()
         sum_call=0
         sum_sms=0
         sum_data=0
         sum_solde=0
         for i in range(len(call)):
            sum_call+=call[i][0]
            sum_sms+=sms[i][0]
            sum_data+=data[i][0]
            sum_solde+=solde[i][0]
         window.call.label_51.setText(f"{str(sum_call)}")
         window.call.label_49.setText(f"{str(sum_sms)}")
         window.call.label_57.setText(f"{str(sum_data)}")
         window.call.label_48.setText(f"{str(sum_solde)}")
         window.bwu.label_51.setText(f"{str(sum_call)}")
         window.bwu.label_49.setText(f"{str(sum_sms)}")
         window.bwu.label_57.setText(f"{str(sum_data)}")
         window.bwu.label_49.setText(f"{str(sum_solde)}")
         window.bsu.label_51.setText(f"{str(sum_call)}")
         window.bsu.label_49.setText(f"{str(sum_sms)}")
         window.bsu.label_57.setText(f"{str(sum_data)}")
         window.bsu.label_49.setText(f"{str(sum_solde)}")
        else:
         window.call.label_51.setText(f"no sim")
         window.call.label_49.setText(f"no sim")
         window.call.label_57.setText(f"no sim")
         window.call.label_48.setText(f"no sim")
         window.bwu.label_51.setText(f"no sim")
         window.bwu.label_53.setText(f"no sim")
         window.bwu.label_57.setText(f"no sim")
         window.bwu.label_49.setText(f"no sim")
         window.bsu.label_51.setText(f"no sim")
         window.bsu.label_49.setText(f"no sim")
         window.bsu.label_57.setText(f"no sim")
         window.bsu.label_48.setText(f"no sim")
        cr.execute(f"select cin from users where email='{window.login.plainTextEdit.toPlainText()}'")
        current_cin=cr.fetchone()
        cr.execute(f"select numero from sim where cin='{current_cin[0]}'")
        numero=cr.fetchone()
        if numero!=None:
         cr.execute(f"select * from call_user where too='{numero[0]}'")
         calls=cr.fetchall()
         for i in range(len(calls)):
            window.call.tableWidget.setRowCount(i+1)
            for j in range(1,len(calls[0])):
             item=QTableWidgetItem(str(calls[i][j]))
             window.call.tableWidget.setItem(i,j-1, item)
         cr.execute(f"select * from message_user where too='{numero[0]}'")
         messages=cr.fetchall()
         for i in range(len(messages)):
            window.call.tableWidget_2.setRowCount(i+1)
            for j in range(1,len(messages[0])):
             item=QTableWidgetItem(str(messages[i][j]))
             window.call.tableWidget_2.setItem(i,j-1, item)
        cr.execute(f"select nom ,prenom, adresse from clients where cin='{cin[0]}'  ")
        npa=cr.fetchone()
        if npa:
           window.bwu.plainTextEdit.setReadOnly(True)
           window.bwu.plainTextEdit_2.setReadOnly(True)
           window.bwu.plainTextEdit_3.setReadOnly(True)
           window.bsu.plainTextEdit.setReadOnly(True)
           window.bsu.plainTextEdit_2.setReadOnly(True)
           window.bsu.plainTextEdit_3.setReadOnly(True)
           window.bsu.plainTextEdit.clear()
           window.bsu.plainTextEdit_2.clear()
           window.bsu.plainTextEdit_3.clear()
           window.bwu.plainTextEdit.clear()
           window.bwu.plainTextEdit_2.clear()
           window.bwu.plainTextEdit_3.clear()
           window.bsu.plainTextEdit.insertPlainText(npa[0])
           window.bsu.plainTextEdit_2.insertPlainText(npa[1])
           window.bsu.plainTextEdit_3.insertPlainText(npa[0])
           window.bwu.plainTextEdit.insertPlainText(npa[0])
           window.bwu.plainTextEdit_2.insertPlainText(npa[1])
           window.bwu.plainTextEdit_3.insertPlainText(npa[0])
           
def buy_wifi_func():
        number=window.bwu.plainTextEdit_6.toPlainText()
        cr.execute(f"select installation from routers where installation='{window.bwu.comboBox.currentText()}' ")
        router=cr.fetchone()
        if all([window.bwu.plainTextEdit.toPlainText(),window.bwu.plainTextEdit_2.toPlainText(),window.bwu.plainTextEdit_3.toPlainText(),window.bwu.plainTextEdit_4.toPlainText(),window.bwu.plainTextEdit_5.toPlainText(),window.bwu.plainTextEdit_6.toPlainText()]):
            if number.isdigit() and int(number)>0:
             cr.execute(f"select cin from wifi where cin='{window.bwu.plainTextEdit_5.toPlainText()}'")
             if cr.fetchone()==None:
                if router!=None:
                 cr.execute(f"select abonnemnt from clients where cin='{window.bwu.plainTextEdit_5.toPlainText()}'")
                 result=cr.fetchone()
                 if result==None:
                    if window.bwu.comboBox.currentText()=='AVEC INSTALATION':
                     cr.execute(f"insert into clients values('{window.bwu.plainTextEdit_5.toPlainText()}','{window.bwu.plainTextEdit.toPlainText()}','{window.bwu.plainTextEdit_2.toPlainText()}','{window.bwu.plainTextEdit_3.toPlainText()}','OW','{window.bwu.plainTextEdit_4.  toPlainText()}')")
                     window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                     cr.execute("select id from routers where installation='AVEC INSTALATION' ")
                     id=cr.fetchone()
                     cr.execute(f"insert into wifi values('{window.bwu.plainTextEdit_5.toPlainText()}','{id[0]}','O','{window.bwu.plainTextEdit_6.toPlainText()}','AVEC INSTALATION','{(int(number))*10}','{250}')")
                     cr.execute(f"insert into payment_wifi values('{id[0]}','{1}','{int((number))*10}')")
                     cr.execute(f"delete from routers where id='{id[0]}' ")
                     db.commit()
                     messagebox.showinfo("","opeartion sucessufuly")
                     window.show_data_in_dashboard()
                     window.show_data_in_tabel()
                     show_data()
                     window.bwu.plainTextEdit.clear()
                     window.bwu.plainTextEdit_2.clear()
                     window.bwu.plainTextEdit_3.clear()
                     window.bwu.plainTextEdit_4.clear()
                     window.bwu.plainTextEdit_5.clear()
                     window.bwu.plainTextEdit_6.clear()
                     window.switch_page(9)
                    elif window.bwu.comboBox.currentText()=='SANS INSTALLATION':
                     cr.execute(f"insert into clients values('{window.bwu.plainTextEdit_5.toPlainText()}','{window.bwu.plainTextEdit.toPlainText()}','{window.bwu.plainTextEdit_2.toPlainText()}','{window.bwu.plainTextEdit_3.toPlainText()}','OW','{window.bwu.plainTextEdit_4.  toPlainText()}')")
                     window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+100} et le prix des autres mois est {(int(number)*10)}")
                     cr.execute("select id from routers where installation='SANS INSTALLATION' ")
                     id=cr.fetchone()
                     cr.execute(f"insert into wifi values('{window.bwu.plainTextEdit_5.toPlainText()}','{id[0]}','O','{window.bwu.plainTextEdit_6.toPlainText()}','SANS INSTALLATION','{(int(number))*10}','{100}')")
                     cr.execute(f"insert into payment_wifi values('{id[0]}','{1}','{int((number))*10}')")
                     cr.execute(f"delete from routers where id='{id[0]}' ")
                     db.commit()
                     messagebox.showinfo("","opeartion sucessufuly")
                     window.show_data_in_dashboard()
                     window.show_data_in_tabel()
                     show_data()
                     window.bwu.plainTextEdit.clear()
                     window.bwu.plainTextEdit_2.clear()
                     window.bwu.plainTextEdit_3.clear()
                     window.bwu.plainTextEdit_4.clear()
                     window.bwu.plainTextEdit_5.clear()
                     window.bwu.plainTextEdit_6.clear()
                     window.switch_page(9)
                 else:
                    if window.bwu.comboBox.currentText()=='AVEC INSTALATION':
                     if result[0]=='OS':
                      cr.execute(f"update clients set abonnemnt='OWS' where  cin='{window.bwu.plainTextEdit_5.toPlainText()}'")
                      window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='AVEC INSTALATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{window.bwu.plainTextEdit_5.toPlainText()}','{id[0]}','O','{window.bwu.plainTextEdit_6.toPlainText()}','AVEC INSTALATION','{(int(number))*10}','250')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{1}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      window.show_data_in_dashboard()
                      window.show_data_in_tabel()
                      show_data()
                      window.bwu.plainTextEdit.clear()
                      window.bwu.plainTextEdit_2.clear()
                      window.bwu.plainTextEdit_3.clear()
                      window.bwu.plainTextEdit_4.clear()
                      window.bwu.plainTextEdit_5.clear()
                      window.bwu.plainTextEdit_6.clear()
                      window.switch_page(9)
                     elif result[0]=='LS':
                      cr.execute(f"update clients set abonnemnt='TWS' where  cin='{window.bwu.plainTextEdit_5.toPlainText()}'")
                      window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='AVEC INSTALATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{window.bwu.plainTextEdit_5.toPlainText()}','{id[0]}','O','{window.bwu.plainTextEdit_6.toPlainText()}','AVEC INSTALATION','{(int(number))*10}','250')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{1}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      window.show_data_in_dashboard()
                      window.show_data_in_tabel()
                      show_data()
                      window.bwu.plainTextEdit.clear()
                      window.bwu.plainTextEdit_2.clear()
                      window.bwu.plainTextEdit_3.clear()
                      window.bwu.plainTextEdit_4.clear()
                      window.bwu.plainTextEdit_5.clear()
                      window.bwu.plainTextEdit_6.clear()
                      window.switch_page(9)
                    elif window.bwu.comboBox.currentText()=='SANS INSTALLATION':
                     if result[0]=='OS':
                      cr.execute(f"update clients set abonnemnt='OWS' where  cin='{window.bwu.plainTextEdit_5.toPlainText()}'")
                      window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='SANS INSTALLATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{window.bwu.plainTextEdit_5.toPlainText()}','{id[0]}','O','{window.bwu.plainTextEdit_5.toPlainText()}','SANS INSTALLATION','{(int(number))*10+150}','{(int(number))*10}')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{1}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      window.show_data_in_dashboard()
                      window.show_data_in_tabel()
                      show_data()
                      window.bwu.plainTextEdit.clear()
                      window.bwu.plainTextEdit_2.clear()
                      window.bwu.plainTextEdit_3.clear()
                      window.bwu.plainTextEdit_4.clear()
                      window.bwu.plainTextEdit_5.clear()
                      window.bwu.plainTextEdit_6.clear()
                      window.switch_page(9)
                     elif result[0]=='LS':
                      cr.execute(f"update clients set abonnemnt='TWS' where  cin='{window.bwu.plainTextEdit_5.toPlainText()}'")
                      window.bwu.label_17.setText(f"le prix de premiere mois et l'installation est :{(int(number)*10)+250} et le prix des autres mois est {(int(number)*10)}")
                      cr.execute("select id from routers where installation='SANS INSTALLATION' ")
                      id=cr.fetchone()
                      cr.execute(f"insert into wifi values('{window.bwu.plainTextEdit_5.toPlainText()}','{id[0]}','O','{window.bwu.plainTextEdit_5.toPlainText()}','SANS INSTALLATION','{(int(number))*10+150}','{(int(number))*10}')")
                      cr.execute(f"insert into payment_wifi values('{id[0]}','{1}','{int((number))*10}')")
                      cr.execute(f"delete from routers where id='{id[0]}' ")
                      db.commit()
                      messagebox.showinfo("","opeartion sucessufuly")
                      window.show_data_in_dashboard()
                      window.show_data_in_tabel()
                      show_data()
                      window.bwu.plainTextEdit.clear()
                      window.bwu.plainTextEdit_2.clear()
                      window.bwu.plainTextEdit_3.clear()
                      window.bwu.plainTextEdit_4.clear()
                      window.bwu.plainTextEdit_5.clear()
                      window.bwu.plainTextEdit_6.clear()
                      window.switch_page(9)
                else:
                    messagebox.showerror("","router indisponible")
             else:
                messagebox.showerror("","l'utilisteur a dejaa un wifi")
            else:
                messagebox.showerror("","number error")
        else:
            messagebox.showerror("","complete information")
            window.show_data_in_dashboard()
            window.show_data_in_tabel()
def send_msg():
        if all([window.call.plainTextEdit_6.toPlainText(),window.call.plainTextEdit_7.toPlainText()]):
            cr.execute(f"select cin from users where email='{window.login.plainTextEdit.toPlainText()}'")
            current_cin=cr.fetchone()
            cr.execute(f"select numero from sim where cin='{current_cin[0]}'")
            numero=cr.fetchone()
            cr.execute(f"select sms from sim where cin='{current_cin[0]}'")
            sms=cr.fetchone()
            cr.execute(f"select numero from sim where numero='{window.call.plainTextEdit_7.toPlainText()}'")
            recive_number=cr.fetchone()
            if numero!=None:
                if recive_number!=None:
                    if sms[0]>0:
                        cr.execute(f"insert into message_user values('{recive_number[0]}','{numero[0]}','{window.call.plainTextEdit_6.toPlainText()}')")
                        cr.execute(f"update sim set sms='{sms[0]-1}' where cin='{current_cin[0]}'")
                        show_data()
                        window.show_data_in_dashboard()
                        window.show_data_in_tabel()
                        db.commit()
                        messagebox.showinfo("","le message est bien envoye")
                        window.call.plainTextEdit_7.clear()
                        window.call.plainTextEdit_6.clear()
                    else:
                        messagebox.showerror("","recharger votre solde sms")
                else:
                    messagebox.showerror("","le number de recepteur est faux")
            else:
                messagebox.showwarning("","acheter une carte sim")
        else:
            messagebox.showerror("","completer les donnes")
def send_call():
        if all([window.call.plainTextEdit_4.toPlainText(),window.call.plainTextEdit_5.toPlainText()]):
            cr.execute(f"select cin from users where email='{window.login.plainTextEdit.toPlainText()}'")
            current_cin=cr.fetchone()
            cr.execute(f"select numero from sim where cin='{current_cin[0]}'")
            numero=cr.fetchone()
            cr.execute(f"select call from sim where cin='{current_cin[0]}'")
            call=cr.fetchone()
            cr.execute(f"select numero from sim where numero='{window.call.plainTextEdit_4.toPlainText()}'")
            recive_number=cr.fetchone()
            if numero!=None:
                if recive_number!=None:
                    if call[0]-int(window.call.plainTextEdit_5.toPlainText())>0 or call[0]-int(window.call.plainTextEdit_5.toPlainText())==0 :
                        cr.execute(f"insert into call_user values('{recive_number[0]}','{numero[0]}','{window.call.plainTextEdit_5.toPlainText()}')")
                        cr.execute(f"update sim set call='{call[0]-int(window.call.plainTextEdit_5.toPlainText())}' where cin='{current_cin[0]}'")
                        
                        show_data()
                        window.show_data_in_dashboard()
                        window.show_data_in_tabel()
                        db.commit()
                        messagebox.showinfo("","l'appele est bien effectue")
                        window.call.plainTextEdit_4.clear()
                        window.call.plainTextEdit_5.clear()
                    else:
                        messagebox.showerror("","recharger votre solde call")
                else:
                    messagebox.showerror("","le number de recepteur est faux")
            else:
                messagebox.showwarning("","acheter une carte sim")
        else:
            messagebox.showerror("","completer les donnes")
def buy_sim():
        cr.execute("select numero from disponible ")
        numero=cr.fetchone()
        if all([window.bsu.plainTextEdit.toPlainText(),window.bsu.plainTextEdit_2.toPlainText(),window.bsu.plainTextEdit_3.toPlainText(),window.bsu.plainTextEdit_4.toPlainText(),window.bsu.plainTextEdit_5.toPlainText()]):
            cr.execute(f"select cin from sim where cin='{window.bsu.plainTextEdit_5.toPlainText()}'")
            if cr.fetchone()==None:
             cr.execute("select *from disponible")
             result=cr.fetchall()
             if len(result)>0:
              cr.execute(f"select abonnemnt from clients where cin='{window.bsu.plainTextEdit_5.toPlainText()}'")
              result=cr.fetchone()
              if result==None:
               cr.execute(f"insert into clients values('{window.bsu.plainTextEdit_5.toPlainText()}','{window.bsu.plainTextEdit.toPlainText()}','{window.bsu.plainTextEdit_2.toPlainText()}','{window.bsu.plainTextEdit_3.toPlainText()}','LS','{window.bsu.plainTextEdit_4.toPlainText()}') ")
               
               cr.execute(f"delete  from disponible where numero='{numero[0]}' ")
               cr.execute(f"insert into sim values('{window.bsu.plainTextEdit_5.toPlainText()}','{numero[0]}','O','0','0','0','0')")
               db.commit()
               window.show_data_in_dashboard()
               window.show_data_in_tabel()
               show_data()
               messagebox.showinfo("",f"le numero de client est {numero[0]}")
               window.switch_page(9)
               window.bsu.plainTextEdit.clear()
               window.bsu.plainTextEdit_2.clear()
               window.bsu.plainTextEdit_3.clear()
               window.bsu.plainTextEdit_4.clear()
               window.bsu.plainTextEdit_5.clear()
              elif  result[0]=='LW'  :
                cr.execute(f"update clients  SET abonnemnt='TWS' where cin='{window.bsu.plainTextEdit_5.toPlainText()}' ")
                cr.execute(f"insert into sim values('{window.bsu.plainTextEdit_5.toPlainText()}','{numero[0]}','O','0','0','0','0')")
                cr.execute(f"delete  from disponible where numero='{numero[0]}' ")
                db.commit()
                window.bsu.plainTextEdit.clear()
                window.bsu.plainTextEdit_2.clear()
                window.bsu.plainTextEdit_3.clear()
                window.bsu.plainTextEdit_4.clear()
                window.bsu.plainTextEdit_5.clear()
                window.show_data_in_dashboard()
                window.show_data_in_tabel()
                show_data()
                window.switch_page(9)
                messagebox.showinfo("",f"le numero de client est {numero[0]}")
              elif result[0]=='OW':
                cr.execute(f"update clients  SET abonnemnt='OWS' where cin='{window.bsu.plainTextEdit_5.toPlainText()}' ")
                cr.execute(f"insert into sim values('{window.bsu.plainTextEdit_5.toPlainText()}','{numero[0]}','O','0','0','0','0')")
                cr.execute(f"delete  from disponible where numero='{numero[0]}' ")
                db.commit()
                messagebox.showinfo("",f"le numero de client est {numero[0]}")
                window.show_data_in_dashboard()
                window.show_data_in_tabel()
                show_data()
                window.switch_page(9)
                window.bsu.plainTextEdit.clear()
                window.bsu.plainTextEdit_2.clear()
                window.bsu.plainTextEdit_3.clear()
                window.bsu.plainTextEdit_4.clear()
                window.bsu.plainTextEdit_5.clear()
             else:
                messagebox.showerror("","NO NUMBERS NOW SOORY!")
            else:
                messagebox.showinfo("","a deja une carte sim")

        else:
            messagebox.showinfo("","completer les donnes")
def recharge():
        getUser=window.login.plainTextEdit.toPlainText()
        cr.execute(f"select cin from users where email='{getUser}'")
        cin=cr.fetchone()
        cr.execute(f"select cin from sim where cin='{cin[0]}'")
        result=cr.fetchone()
        if result==None:
            messagebox.showerror("","achetet une carte sim")
        else:
            cr.execute(f"select solde from sim where cin='{cin[0]}'")
            solde=cr.fetchone()
            sold=solde[0]
            cr.execute(f"select sms from sim where cin='{cin[0]}'")
            sms=cr.fetchone()
            sm=sms[0]
            cr.execute(f"select call from sim where cin='{cin[0]}'")
            call=cr.fetchone()
            cal=call[0]
            cr.execute(f"select data from sim where cin='{cin[0]}'")
            data=cr.fetchone()
            dat=data[0]
            if window.call.comboBox.currentText()=='* 1':
                cr.execute(f"update sim set sms='{int(window.call.comboBox_2.currentText())*10+sm}' where cin='{cin[0]}' ")
                cr.execute(f"insert into sim_payment values('{cin[0]}','{window.call.comboBox_2.currentText()}') ")
                db.commit()
                messagebox.showinfo("",f"vous avez charger {int(window.call.comboBox_2.currentText())*10} sms")
                show_data()
                window.show_data_in_dashboard()
                window.show_data_in_tabel()
            elif  window.call.comboBox.currentText()=='*2':
                cr.execute(f"update sim set call='{int(window.call.comboBox_2.currentText()) +cal}' where cin='{cin[0]}' ")
                cr.execute(f"insert into sim_payment values('{cin[0]}','{window.call.comboBox_2.currentText()}') ")
                db.commit()
                show_data()
                window.show_data_in_dashboard()
                window.show_data_in_tabel()
                db.commit()
                messagebox.showinfo("",f"vous avez charger {int(window.call.comboBox_2.currentText())} heurs")
            elif window.call.comboBox.currentText()=='*3':
                cr.execute(f"update sim set data='{int(window.call.comboBox_2.currentText())/10 +dat}' where cin='{cin[0]}' ")
                cr.execute(f"insert into sim_payment values('{cin[0]}','{window.call.comboBox_2.currentText()}') ")
                db.commit()
                db.commit()
                show_data()
                window.show_data_in_dashboard()
                window.show_data_in_tabel()
                messagebox.showinfo("",f"vous avez charger {int(window.call.comboBox_2.currentText())/10} GB")
            elif window.call.comboBox.currentText()=='SOLDE':
                cr.execute(f"update sim set solde='{int(window.call.comboBox_2.currentText())+sold}' where cin='{cin[0]}' ")
                cr.execute(f"insert into sim_payment values('{cin[0]}','{window.call.comboBox_2.currentText()}') ")
                db.commit()
                db.commit()
                show_data()
                window.show_data_in_dashboard()
                window.show_data_in_tabel()
                messagebox.showinfo("",f"vous avez charger {int(window.call.comboBox_2.currentText())} dh")
app = QtWidgets.QApplication([])
window = MainWindow()
def check_login():
    getUser=window.login.plainTextEdit.toPlainText()
    getPass=window.login.plainTextEdit_2.toPlainText()
    cr.execute(f"SELECT role, email, pass FROM users WHERE email='{getUser}' and pass='{getPass}'")
    result = cr.fetchone()
    if result:
        if result[0]=="a":
           window.login.plainTextEdit_2.insertPlainText("")
           window.login.plainTextEdit.insertPlainText("")
           window.switch_page(2)
        else :
            window.call.plainTextEdit_4.clear()
            window.call.plainTextEdit_5.clear()
            window.call.plainTextEdit_7.clear()
            window.call.plainTextEdit_6.clear()
            window.bwu.plainTextEdit_2.clear()
            window.bwu.plainTextEdit.clear()
            window.bwu.plainTextEdit_3.clear()
            window.bwu.plainTextEdit_4.clear()
            window.bwu.plainTextEdit_5.clear()
            window.bwu.plainTextEdit_6.clear()
            window.bsu.plainTextEdit.clear()
            window.bsu.plainTextEdit_2.clear()
            window.bsu.plainTextEdit_3.clear()
            window.bsu.plainTextEdit_4.clear()
            window.bsu.plainTextEdit_5.clear()
            window.call.plainTextEdit_4.clear()
            window.call.plainTextEdit_5.clear()
            window.call.plainTextEdit_7.clear()
            window.call.plainTextEdit_6.clear()
            window.bwu.label_17.setText("")
            window.switch_page(9)
            show_data()
    else:
        messagebox.showerror("","l'email ou le mot de pass est faux ")
def cree():
    getEmail=window.cree.plainTextEdit.toPlainText()
    getPass=window.cree.plainTextEdit_2.toPlainText()
    getRePass=window.cree.plainTextEdit_3.toPlainText()
    getCin=window.cree.plainTextEdit_4.toPlainText()
    if all([getEmail,getPass,getRePass,getCin]):
        if getPass==getRePass:
            cr.execute(f"select email from users where email='{getEmail}'")
            emailResult=cr.fetchone()
            if emailResult==None:
                cr.execute(f"select cin from users where cin='{getCin}'")
                cinResult=cr.fetchone()
                if cinResult==None:
                 cr.execute(f"insert into users values('u','{getEmail}','{getPass}','0','{getCin}')")
                 db.commit()
                 window.switch_page(0)
                 window.cree.plainTextEdit_2.clear()
                 window.cree.plainTextEdit.clear()
                 window.cree.plainTextEdit_3.clear()
                 window.cree.plainTextEdit_4.clear()
                else:
                    messagebox.showerror("","CIN already used")
            else:
                messagebox.showerror("","l'email deja utilise")
        else:
            messagebox.showerror("","le deuxieme mot de pass est faux")
    else:
        messagebox.showerror("","completer les donnes")
def switch_wifi():
   getUser=window.login.plainTextEdit.toPlainText()
   cr.execute(f"select cin from users where email='{getUser}'")
   cin=cr.fetchone()
   cr.execute(f"select cin from wifi where cin='{cin[0]}'")
   wifi=cr.fetchone()
   if wifi:
      messagebox.showerror("","you already have wifi")
      
   else:
      window.switch_page(10)
      
def switch_sim():
   getUser=window.login.plainTextEdit.toPlainText()
   cr.execute(f"select cin from users where email='{getUser}'")
   cin=cr.fetchone()
   cr.execute(f"select cin from sim where cin='{cin[0]}'")
   wifi=cr.fetchone()
   if wifi:
      messagebox.showerror("","you already have sim")
      
   else:
      window.switch_page(11)
window.call.pushButton_15.clicked.connect(lambda:recharge())
window.bsu.pushButton_13.clicked.connect(lambda:buy_sim())
window.call.pushButton_14.clicked.connect(lambda:switch_sim())
window.call.pushButton_12.clicked.connect(lambda:send_call())
window.call.pushButton_13.clicked.connect(lambda:send_msg())
window.bwu.pushButton_12.clicked.connect(lambda:buy_wifi_func())
window.call.pushButton_16.clicked.connect(lambda:switch_wifi())
window.bwu.pushButton_13.clicked.connect(lambda:check_price())
window.login.pushButton_2.clicked.connect(lambda:window.switch_page(1))
window.cree.pushButton_3.clicked.connect(lambda:window.switch_page(0))
window.dashboard.pushButton_2.clicked.connect(lambda:window.switch_page(3))
window.users.pushButton.clicked.connect(lambda:window.switch_page(2))
window.cree.pushButton_2.clicked.connect(lambda:cree())
window.users.pushButton_12.clicked.connect(lambda:window.search_in_client_tables())
window.users.pushButton_13.clicked.connect(lambda:window.show_data_in_tabel())
window.users.pushButton_3.clicked.connect(lambda:window.switch_page(4))
window.dashboard.pushButton_3.clicked.connect(lambda:window.switch_page(4))
window.sim.pushButton_2.clicked.connect(lambda:window.switch_page(3))
window.sim.pushButton.clicked.connect(lambda:window.switch_page(2))
window.login.pushButton.clicked.connect(lambda:check_login())
window.sim.pushButton_12.clicked.connect(lambda:window.search_in_sim_table())
window.sim.pushButton_13.clicked.connect(lambda:window.show_data_in_tabel())
window.users.pushButton_4.clicked.connect(lambda:window.switch_page(6))
window.dashboard.pushButton_4.clicked.connect(lambda:window.switch_page(6))
window.sim.pushButton_4.clicked.connect(lambda:window.switch_page(6))
window.wifi.pushButton.clicked.connect(lambda:window.switch_page(2))
window.wifi.pushButton_2.clicked.connect(lambda:window.switch_page(3))
window.wifi.pushButton_3.clicked.connect(lambda:window.switch_page(4))
window.show_data_in_tabel()
window.show()
generate_fen=uic.loadUi("generate.ui")
generate_ROU=uic.loadUi("gentrou.ui")
generate_fen.pushButton.clicked.connect(lambda:window.generete_numbers())
window.sim.pushButton_15.clicked.connect(lambda:generate_fen.show())
window.sim.pushButton_14.clicked.connect(lambda:window.switch_page(5))
window.add.pushButton.clicked.connect(lambda:window.switch_page(2))
window.add.pushButton_2.clicked.connect(lambda:window.switch_page(3))
window.add.pushButton_3.clicked.connect(lambda:window.switch_page(4))
window.add.pushButton_12.clicked.connect(lambda:window.add_sim())
window.wifi.pushButton_15.clicked.connect(lambda:generate_ROU.show())
generate_ROU.pushButton.clicked.connect(lambda:window.generate_routers())
window.wifi.pushButton_14.clicked.connect(lambda:window.switch_page(7))
window.buy_wifi.pushButton.clicked.connect(lambda:window.switch_page(2))
window.buy_wifi.pushButton_2.clicked.connect(lambda:window.switch_page(3))
window.buy_wifi.pushButton_3.clicked.connect(lambda:window.switch_page(4))
window.buy_wifi.pushButton_4.clicked.connect(lambda:window.switch_page(6))
window.buy_wifi.pushButton_13.clicked.connect(lambda:window.check_price())
window.buy_wifi.pushButton_12.clicked.connect(lambda:window.wifi_buy())
window.wifi.pushButton_12.clicked.connect(lambda:window.search_in_wifi_table())
window.wifi.pushButton_13.clicked.connect(lambda:window.show_data_in_tabel())
window.diagnostic.pushButton.clicked.connect(lambda:window.switch_page(2))
window.diagnostic.pushButton_2.clicked.connect(lambda:window.switch_page(3))
window.diagnostic.pushButton_3.clicked.connect(lambda:window.switch_page(4))
window.diagnostic.pushButton_4.clicked.connect(lambda:window.switch_page(6))
window.dashboard.pushButton_5.clicked.connect(lambda:window.switch_page(8))
window.sim.pushButton_5.clicked.connect(lambda:window.switch_page(8))
window.users.pushButton_5.clicked.connect(lambda:window.switch_page(8))
window.wifi.pushButton_5.clicked.connect(lambda:window.switch_page(8))
window.buy_wifi.pushButton_5.clicked.connect(lambda:window.switch_page(8))
window.add.pushButton_5.clicked.connect(lambda:window.switch_page(8))
window.diagnostic.pushButton_14.clicked.connect(lambda:window.meessage_wifi_pay())
window.dashboard.pushButton_6.clicked.connect(lambda:window.switch_page(0))
window.users.pushButton_6.clicked.connect(lambda:window.switch_page(0))
window.sim.pushButton_6.clicked.connect(lambda:window.switch_page(0))
window.add.pushButton_6.clicked.connect(lambda:window.switch_page(0))
window.wifi.pushButton_6.clicked.connect(lambda:window.switch_page(0))
window.buy_wifi.pushButton_6.clicked.connect(lambda:window.switch_page(0))
window.diagnostic.pushButton_6.clicked.connect(lambda:window.switch_page(0))
def clear_login():
   window.switch_page(0)
   window.login.plainTextEdit.clear()
   window.login.plainTextEdit_2.clear()
window.call.pushButton_6.clicked.connect(lambda:clear_login())
window.bsu.pushButton_6.clicked.connect(lambda:window.switch_page(9))
window.bwu.pushButton_6.clicked.connect(lambda:window.switch_page(9))
window.add.pushButton_4.clicked.connect(lambda:window.switch_page(6))
window.show_data_in_dashboard()
app.exec_()
