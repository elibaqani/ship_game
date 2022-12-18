from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resource_rc

class page2(object):
    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.dor = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(266, 278)
        MainWindow.setStyleSheet("background-color: rgb(66, 179, 255);\n"
                                 "background-color: rgb(44, 83, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player11 = QtWidgets.QLineEdit(self.centralwidget)
        self.player11.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.player11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "position:absolute;")
        self.player11.setObjectName("player1")
        self.player22 = QtWidgets.QLineEdit(self.centralwidget)
        self.player22.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.player22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.player22.setObjectName("lineEdit2")
        self.durbazi = QtWidgets.QLineEdit(self.centralwidget)
        self.durbazi.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.durbazi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.durbazi.setObjectName("durbazi")
        self.label_player1 = QtWidgets.QLabel(self.centralwidget)
        self.label_player1.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label_player1.setStyleSheet("background-color: rgb(67, 214, 255);")
        self.label_player1.setObjectName("label_player1")
        self.label_player2 = QtWidgets.QLabel(self.centralwidget)
        self.label_player2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.label_player2.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.label_player2.setObjectName("label_player2")
        self.label_durbazi = QtWidgets.QLabel(self.centralwidget)
        self.label_durbazi.setGeometry(QtCore.QRect(40, 120, 71, 20))
        self.label_durbazi.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                         "background-color: rgb(170, 85, 0);")
        self.label_durbazi.setObjectName("label_durbazi")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(90, 180, 81, 23))
        self.ok.setStyleSheet("background-color: rgb(0, 255, 127);\n"
                              "background-color: rgb(0, 170, 0);")
        self.ok.setObjectName("ok")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ok.clicked.connect(self.open_window)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_window(self):
        self.p1=self.player11.text()
        self.p2=self.player22.text()
        self.dor = self.durbazi.text()

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.p1, self.p2 , self.dor)
        self.ui.setupUi(self.window)
        app.processEvents()
        MainWindow.hide()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_player1.setText(_translate("MainWindow", "name player1"))
        self.label_player2.setText(_translate("MainWindow", "name palyer2"))
        self.label_durbazi.setText(_translate("MainWindow", "tedad dur bazi"))
        self.ok.setText(_translate("MainWindow", "ok"))


class Ui_MainWindow(object):
    def __init__(self,p1,p2,dor):
        super(Ui_MainWindow,self).__init__()
        self.player1= p1
        self.player2= p2
        self.dast = int(dor)
        self.balance_player1 = 100000
        self.balance_player2 = 100000
        self.deficit1 = 0
        self.deficit2 = 0
        self.win = []
        self.ship_player_1 = 0
        self.ship_player_2 = 0
        self.fish_player_1 = 0
        self.fish_player_2 = 0
        self.all_fish = 1000000
        self.Number_fish_each_time = (5 * self.all_fish) / 100
        self.stop = False
        self.item = 0
        self.Profit1 = 0
        self.profid2 = 0
        self.number_fish_deficit_each_time = 0
        self.new = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 575)
        MainWindow.setStyleSheet("position: relative;\n"
                                 "width:429px;\n"
                                 "height:934px;\n"
                                 "\n"
                                 "background: #060028;"
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("position: relative;\n"
                                         "width:429px;\n"
                                         "height:934px;\n"
                                         "\n"
                                         "background: #060028;"
                                         )
        self.centralwidget.setObjectName("centralwidget")
        self.ship = QtWidgets.QPushButton(self.centralwidget)
        self.ship.setGeometry(QtCore.QRect(340, 200, 111, 51))
        self.ship.setStyleSheet("#ship{\n"
                                "image: url(:/image/28707-7-ship-photos.png);\n"
                                "color:rgb(255, 255, 255);\n"
                                "box-sizing: border-box;\n"
                                "position:absolute;\n"
                                "width:140px;\n"
                                "height:95px;\n"
                                "left:255px;\n"
                                "top:655px;\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                "backdrop-filter :blur(2px);\n"
                                "border-radius:21px;\n"
                                "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                "}")
        self.ship.setText("")
        self.ship.setObjectName("ship")
        self.fish = QtWidgets.QPushButton(self.centralwidget)
        self.fish.setGeometry(QtCore.QRect(340, 270, 111, 51))
        self.fish.setStyleSheet("#fish{\n"
                                "    image: url(:/image/transparent-fish-pomacanthidae-blue-fish-holacanthus-5d9caf64006eb3.1375152215705496040018.png);\n"
                                "color:rgb(255, 255, 255);\n"
                                "box-sizing: border-box;\n"
                                "position:absolute;\n"
                                "width:140px;\n"
                                "height:95px;\n"
                                "left:255px;\n"
                                "top:655px;\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                "backdrop-filter :blur(2px);\n"
                                "border-radius:21px;\n"
                                "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                "}")
        self.fish.setText("")
        self.fish.setObjectName("fish")
        self.balance = QtWidgets.QPushButton(self.centralwidget)
        self.balance.setGeometry(QtCore.QRect(340, 340, 111, 51))
        self.balance.setStyleSheet("#balance{\n"
                                   "image:url(:/image/Money-Bag-PNG-Image.png);\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "box-sizing: border-box;\n"
                                   "position:absolute;\n"
                                   "width:140px;\n"
                                   "height:95px;\n"
                                   "left:255px;\n"
                                   "top:655px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                   "backdrop-filter :blur(2px);\n"
                                   "border-radius:21px;\n"
                                   "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                   "}\n"
                                   "QPushButton::hover\n"
                                   "{\n"
                                   " background-color : lightgreen;\n"
                                   "                  }")
        self.balance.setText("")
        self.balance.setObjectName("balance")
        self.buy_ship = QtWidgets.QPushButton(self.centralwidget)
        self.buy_ship.setGeometry(QtCore.QRect(150, 200, 111, 51))
        self.buy_ship.setStyleSheet("#buy_ship{\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "box-sizing: border-box;\n"
                                    "position:absolute;\n"
                                    "width:140px;\n"
                                    "height:95px;\n"
                                    "left:255px;\n"
                                    "top:655px;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                    "backdrop-filter :blur(2px);\n"
                                    "border-radius:21px;\n"
                                    "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                    "}")
        self.buy_ship.setObjectName("buy_ship")
        self.sell_ship = QtWidgets.QPushButton(self.centralwidget)
        self.sell_ship.setGeometry(QtCore.QRect(150, 270, 111, 51))
        self.sell_ship.setStyleSheet("#sell_ship{\n"
                                     "color:rgb(255, 255, 255);\n"
                                     "box-sizing: border-box;\n"
                                     "position:absolute;\n"
                                     "width:140px;\n"
                                     "height:95px;\n"
                                     "left:255px;\n"
                                     "top:655px;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                     "backdrop-filter :blur(2px);\n"
                                     "border-radius:21px;\n"
                                     "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                     "}")
        self.sell_ship.setObjectName("sell_ship")
        self.sell_fish = QtWidgets.QPushButton(self.centralwidget)
        self.sell_fish.setGeometry(QtCore.QRect(150, 340, 111, 51))
        self.sell_fish.setStyleSheet("#sell_fish{\n"
                                     "color:rgb(255, 255, 255);\n"
                                     "box-sizing: border-box;\n"
                                     "position:absolute;\n"
                                     "width:140px;\n"
                                     "height:95px;\n"
                                     "left:255px;\n"
                                     "top:655px;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                     "backdrop-filter :blur(2px);\n"
                                     "border-radius:21px;\n"
                                     "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                     "}")
        self.sell_fish.setObjectName("sell_fish")
        self.investment = QtWidgets.QPushButton(self.centralwidget)
        self.investment.setGeometry(QtCore.QRect(320, 450, 131, 51))
        self.investment.setStyleSheet("#investment{\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "box-sizing: border-box;\n"
                                      "position:absolute;\n"
                                      "width:140px;\n"
                                      "height:95px;\n"
                                      "left:255px;\n"
                                      "top:655px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                      "backdrop-filter :blur(2px);\n"
                                      "border-radius:21px;\n"
                                      "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                      "}\n"
                                      "QPushButton::hover\n"
                                      "{\n"
                                      " background-color : lightgreen;}")
        self.investment.setObjectName("investment")
        self.fishing = QtWidgets.QPushButton(self.centralwidget)
        self.fishing.setGeometry(QtCore.QRect(150, 450, 131, 51))
        self.fishing.setStyleSheet("#fishing{\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "box-sizing: border-box;\n"
                                   "position:absolute;\n"
                                   "width:140px;\n"
                                   "height:95px;\n"
                                   "left:255px;\n"
                                   "top:655px;\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                   "backdrop-filter :blur(2px);\n"
                                   "border-radius:21px;\n"
                                   "linear-gradient:(red 10%, 30%, blue 90%);\n"
                                   "}")
        self.fishing.setObjectName("fishing")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 30, 51, 51))
        self.start.setStyleSheet("#start{\n"
                                 "image:url(:/image/start.png);\n"
                                 "color:rgb(255, 255, 255);\n"
                                 "box-sizing: border-box;\n"
                                 "position:absolute;\n"
                                 "width:140px;\n"
                                 "height:95px;\n"
                                 "left:255px;\n"
                                 "top:655px;\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                                 "backdrop-filter :blur(2px);\n"
                                 "border-radius:21px;\n"
                                 "linear-gradient:(red 10%, 30%, blue 90%)\n"
                                 "\n"
                                 "}")
        self.start.setText("")
        self.start.setObjectName("start")
        self.textbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(110, 10, 391, 161))
        self.textbox.setStyleSheet("#textbox{\n"
                                   "color:rgb(0, 0, 0);\n"
                                   "    background-color: rgb(222, 221, 255);\n"
                                   "}")
        self.textbox.setObjectName("textbox")
        self.end = QtWidgets.QPushButton(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(560, 30, 51, 51))
        self.end.setStyleSheet("#end{\n"
                               "image:url(:/image/stop.png);\n"
                               "color:rgb(255, 255, 255);\n"
                               "box-sizing: border-box;\n"
                               "position:absolute;\n"
                               "width:140px;\n"
                               "height:95px;\n"
                               "left:255px;\n"
                               "top:655px;\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 4, 40, 255), stop:1 rgba(33, 45, 83, 255));\n"
                               "backdrop-filter :blur(2px);\n"
                               "border-radius:21px;\n"
                               "linear-gradient:(red 10%, 30%, blue 90%)\n"
                               "\n"
                               "}")
        self.end.setText("")
        self.end.setObjectName("end")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        app.processEvents()
        # self.sell_ship.clicked.connect(partial(self.check,"sell_ship"))  # type: ignore
        self.start.clicked.connect(lambda: self.play("Run"))  # type: ignore
        # self.balance.clicked.connect(self.balancee) # type: ignore
        self.sell_ship.clicked.connect(lambda: self.play("Sell Ship"))  # type: ignore
        self.sell_fish.clicked.connect(lambda: self.play("Sell Fish"))  # type: ignore
        self.fishing.clicked.connect(lambda: self.play("Fishing"))  # type: ignore
        self.buy_ship.clicked.connect(lambda: self.play("Buy Ship"))  # type: ignore
        self.balance.clicked.connect(lambda: self.play("Balance"))  # type: ignore
        self.investment.clicked.connect(lambda: self.play("Investment"))  # type: ignore
        self.fish.clicked.connect(lambda: self.play("fish"))  # type: ignore
        self.ship.clicked.connect(lambda: self.play("ship"))  # type: ignore
        self.end.clicked.connect(self.payan)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def payan(self):
      exit()

    def fishh(self):
        self.textbox.setText(f"tedad mahi darya = {self.all_fish}")

    def buy_shipp(self, player):
        number = 1
        if player == self.player1:
            if self.balance_player1 >= (int(number) * 50000):
                self.balance_player1 -= (int(number) * 50000)
                self.ship_player_1 += int(number)
                self.textbox.setText(f"{player} {int(number)} ship add for you")
                self.textbox.append(f"mojodi jadide {player} = {self.balance_player1}")
                self.textbox.append(f"tedad ships {player}= {self.ship_player_1}")
            else:
                self.textbox.setText(f"{player} mojodi kafi nemibashad")
                self.textbox.append("plz enter another item")
        else:
            if self.balance_player2 >= (int(number) * 50000):
                self.balance_player2 -= (int(number) * 50000)
                self.ship_player_2 += int(number)
                self.textbox.setText(f"{player} {int(number)} ship add for you")
                self.textbox.append(f"mojodi jadide {player} = {self.balance_player2}")
                self.textbox.append(f"tedad ships {player}= {self.ship_player_2}")
            else:
                self.textbox.setText(f"{player} mojodi kafi nemibashad")
                self.textbox.append("plz enter another item")

    def balancee(self, player):
        if player == self.player1:
            self.textbox.setText(f"mojodi {player} = {self.balance_player1}")
        else:
            self.textbox.setText(f"mojodi {player} = {self.balance_player2}")

    def shipp(self, ship_player):
        self.textbox.setText(f"tedad qayeqe shoma = {ship_player}")

    def sell_shipp(self, player):
        number = 1
        if player == self.player1:
            if self.ship_player_1 >= int(number):
                self.balance_player1 += (int(number) * 40000)
                self.ship_player_1 -= int(number)
                self.textbox.setText(f"{player} {int(number)} ship subtraction from you")
                self.textbox.append(f"mojodi jadide {player} = {self.balance_player1}")
                self.textbox.append(f"tedad ships {player}= {self.ship_player_1}")

            else:
                self.textbox.setText(f"{player} shoma qayeqi baraye forosh nadarid")
                self.textbox.append("plz enter another item")
        else:
            if self.ship_player_2 >= int(number):
                self.balance_player2 += (int(number) * 40000)
                self.ship_player_2 -= int(number)
                self.textbox.setText(f"{player} {int(number)} ship subtraction from you")
                self.textbox.append(f"mojodi jadide {player} = {self.balance_player2}")
                self.textbox.append(f"tedad ships {player}= {self.ship_player_2}")
            else:
                self.textbox.setText(f"{player} shoma qayeqi baraye forosh nadarid")
                self.textbox.append("plz enter another item")

    def sell_fishh(self, player):
        if player == self.player1:
            if self.fish_player_1 > 0:
                self.balance_player1 += self.fish_player_1
                self.fish_player_1 = 0
                self.textbox.setText(f"{player} mahi shoma b nerkhe roz forokhte shod")
                self.textbox.append(f"mojodi jadide {player} = {self.balance_player1}")
            else:
                self.textbox.setText(f"{player} shoma mahi baraye forosh nadarid")
                self.textbox.append("plz enter another item")
        else:
            if self.fish_player_2 > 0:
                self.balance_player2 += self.fish_player_2
                self.fish_player_2 = 0
                self.textbox.setText(f"{player} mahi shoma b nerkhe roz forokhte shod")
                self.textbox.append(f"mojodi jadide {player} = {self.balance_player2}")
            else:
                self.textbox.setText(f"{player} shoma mahi baraye forosh nadarid")
                self.textbox.append("plz enter another item")

    def egg(self):
        if self.all_fish <= 0:
            self.all_fish = 1000
            self.all_fish += (5 * self.all_fish) / 100
        else:
           self.all_fish += (5 * self.all_fish) / 100
        self.endd()

    def Computing(self):
        self.profid1 = (10 * self.balance_player1) / 100
        self.balance_player1 += self.profid1
        self.balance_player1 -= self.deficit1
        self.profid2 = (10 * self.balance_player2) / 100
        self.balance_player2 += self.profid2
        self.balance_player2 -= self.deficit2
        self.all_fish -= self.number_fish_deficit_each_time
        self.number_fish_deficit_each_time = 0 #reset mishe majmoe mahihaye gerefte shode on dast
        self.egg()

    def akhari(self, player):
        app.processEvents()
        self.item += 1
        if self.item <= 1:
            if player == self.player1:
                self.textbox.setText(f"nobate {self.player2}")
            else:
                self.textbox.setText(f" nobate {self.player1}")
        else:
            self.new += 1
            self.textbox.setText(f"payan marhale {self.new}")
            if (self.dast - self.new) == 1:
                self.textbox.append(f"marhale akhare bazi")
            elif (self.dast - self.new) == 0:
                self.textbox.append(f"bazi tamom shod natayejo bebinid")
            else:
              self.textbox.append(f"tanha  {self.dast - self.new} marhale baqi monde polhaye khod ra b behtarin sorat afzayesh dahid")
            self.textbox.append(f"Enter any key")

    def fishingg(self, player):
        if self.all_fish > 1200:
            if player == self.player1:
                if self.ship_player_1 >= 1:
                    fish_deficit1 = self.Number_fish_each_time * self.ship_player_1
                    self.number_fish_deficit_each_time += fish_deficit1
                    self.fish_player_1 += fish_deficit1
                    self.deficit1 = (4 * self.ship_player_1) / 100
                    self.akhari(player)
                else:
                    self.textbox.setText(f"{player} shoma qayeqi vase mahigiri nadarid")
                    self.textbox.append("plz enter another item")
            else:
                if self.ship_player_2 >= 1:
                    fish_deficit2 = self.Number_fish_each_time * self.ship_player_2
                    self.number_fish_deficit_each_time += fish_deficit2
                    self.fish_player_2 += fish_deficit2
                    self.deficit2 = (4 * self.ship_player_2) / 100
                    self.akhari(player)
                else:
                    self.textbox.setText(f"{player} shoma qayeqi vase mahigiri nadarid")
                    self.textbox.append("plz enter another item")
        else:
            self.textbox.setText(f"{player} tedad mahia kam shode shoma nemitavanit mahigiri konid")

    def investmentt(self, player):
        if player == self.player1:
            if self.balance_player1 > 0:
                self.textbox.append(f"{player} polo shoma dar bank saramaye gozari shod ")
                self.textbox.append(f"nobate {self.player2}")
                self.akhari(player)
            else:
                self.textbox.setText(f"{player} shoma poli baraye sarmaye gozari nadarid")
                self.textbox.append(f"plz enter another item")
        else:
            if self.balance_player2 > 0:
                self.textbox.setText(f"{player} polo shoma dar bank sarmaye gozari shod ")
                self.textbox.append(f"nobate {self.player2}")
                self.akhari(player)
            else:
                self.textbox.setText(f"{player} shoma poli baraye sarmaye gozari nadarid")
                self.textbox.append(f"plz enter another item")

    def endd(self):
        self.win.append("|")
        self.textbox.setText(f"{self.win}")
        if len(self.win) == self.dast:
            self.balance_player1 += self.fish_player_1
            self.balance_player1 += (self.ship_player_1 * 40000)
            self.fish_player_1 =0
            self.ship_player_1 = 0

            self.balance_player2 += self.fish_player_2
            self.balance_player2 += (self.ship_player_2 * 40000)
            self.fish_player_2 = 0
            self.ship_player_2 = 0
            self.textbox.append(
                f"{self.player1}:\nbalance = {self.balance_player1} ship = {self.ship_player_1} fish = {self.fish_player_1}\n"
                f"{self.player2}:\nbalance = {self.balance_player2} ship = {self.ship_player_2} fish = {self.fish_player_2}")

        else:
            self.stop = False
            self.item = 0
            self.textbox.append(f"daste jadid {self.player1} bazi konid")

    def play(self, button_name):
        app.processEvents()
        if self.item >= 2:
            self.stop = True
        else:
            self.stop = False

        if self.stop == False:
            if self.item == 0:
                player = self.player1
            else:
                player = self.player2
            app.processEvents()
            if button_name == "Run":
                if player == self.player1:
                    self.textbox.setText(f"{self.player1} bazi konid")
                else:
                    self.textbox.setText(f"{self.player2} bazi konid")

            if button_name == "Balance":
                if player == self.player1:
                    self.balancee(self.player1)
                else:
                    self.balancee(self.player2)
            elif button_name == "ship":
                if player == self.player1:
                    self.shipp(self.ship_player_1)
                else:
                    self.shipp(self.ship_player_2)
            elif button_name == "Buy Ship":
                if player == self.player1:
                    self.buy_shipp(self.player1)
                else:
                    self.buy_shipp(self.player2)
            elif button_name == "Sell Ship":
                if player == self.player1:
                    self.sell_shipp(self.player1)
                else:
                    self.sell_shipp(self.player2)
            elif button_name == "Fishing":
                if player == self.player1:
                    self.fishingg(self.player1)
                else:
                    self.fishingg(self.player2)
            elif button_name == "Sell Fish":
                if player == self.player1:
                    self.sell_fishh(self.player1)
                else:
                    self.sell_fishh(self.player2)
            elif button_name == "Investment":
                if player == self.player1:
                    self.investmentt(self.player1)
                else:
                    self.investmentt(self.player2)
            elif button_name == "fish":
                self.fishh()
        else:
            self.Computing()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buy_ship.setText(_translate("MainWindow", "Buy Ship"))
        self.sell_ship.setText(_translate("MainWindow", "Sell Ship"))
        self.sell_fish.setText(_translate("MainWindow", "Sell Fish"))
        self.investment.setText(_translate("MainWindow", "Investment"))
        self.fishing.setText(_translate("MainWindow", "Fishing"))
        self.textbox.setHtml(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">I Was Waiting For You</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = page2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



