# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RC_car.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(833, 772)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 831, 721))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gb_log = QGroupBox(self.tab)
        self.gb_log.setObjectName(u"gb_log")
        self.gb_log.setGeometry(QRect(10, 530, 801, 161))
        self.tb_log = QTextBrowser(self.gb_log)
        self.tb_log.setObjectName(u"tb_log")
        self.tb_log.setGeometry(QRect(15, 20, 771, 131))
        self.gb_car_status = QGroupBox(self.tab)
        self.gb_car_status.setObjectName(u"gb_car_status")
        self.gb_car_status.setGeometry(QRect(10, 10, 211, 391))
        self.lb_model = QLabel(self.gb_car_status)
        self.lb_model.setObjectName(u"lb_model")
        self.lb_model.setGeometry(QRect(30, 30, 64, 15))
        self.lb_status = QLabel(self.gb_car_status)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setGeometry(QRect(30, 150, 64, 15))
        self.lb_model_param = QLabel(self.gb_car_status)
        self.lb_model_param.setObjectName(u"lb_model_param")
        self.lb_model_param.setGeometry(QRect(100, 30, 91, 16))
        self.lb_status_param = QLabel(self.gb_car_status)
        self.lb_status_param.setObjectName(u"lb_status_param")
        self.lb_status_param.setGeometry(QRect(100, 150, 91, 16))
        self.lb_speed = QLabel(self.gb_car_status)
        self.lb_speed.setObjectName(u"lb_speed")
        self.lb_speed.setGeometry(QRect(30, 180, 64, 15))
        self.lb_speed_param = QLabel(self.gb_car_status)
        self.lb_speed_param.setObjectName(u"lb_speed_param")
        self.lb_speed_param.setGeometry(QRect(100, 180, 91, 16))
        self.lb_gate = QLabel(self.gb_car_status)
        self.lb_gate.setObjectName(u"lb_gate")
        self.lb_gate.setGeometry(QRect(30, 210, 64, 15))
        self.lb_gate_param = QLabel(self.gb_car_status)
        self.lb_gate_param.setObjectName(u"lb_gate_param")
        self.lb_gate_param.setGeometry(QRect(100, 210, 91, 16))
        self.lb_motor = QLabel(self.gb_car_status)
        self.lb_motor.setObjectName(u"lb_motor")
        self.lb_motor.setGeometry(QRect(30, 90, 64, 15))
        self.lb_socket = QLabel(self.gb_car_status)
        self.lb_socket.setObjectName(u"lb_socket")
        self.lb_socket.setGeometry(QRect(30, 120, 64, 15))
        self.lb_motor_param = QLabel(self.gb_car_status)
        self.lb_motor_param.setObjectName(u"lb_motor_param")
        self.lb_motor_param.setGeometry(QRect(100, 90, 91, 16))
        self.lb_socket_param = QLabel(self.gb_car_status)
        self.lb_socket_param.setObjectName(u"lb_socket_param")
        self.lb_socket_param.setGeometry(QRect(100, 120, 91, 16))
        self.lb_rgb = QLabel(self.gb_car_status)
        self.lb_rgb.setObjectName(u"lb_rgb")
        self.lb_rgb.setGeometry(QRect(30, 240, 131, 16))
        self.lb_rgb_param = QLabel(self.gb_car_status)
        self.lb_rgb_param.setObjectName(u"lb_rgb_param")
        self.lb_rgb_param.setGeometry(QRect(30, 270, 121, 16))
        self.lb_car_no = QLabel(self.gb_car_status)
        self.lb_car_no.setObjectName(u"lb_car_no")
        self.lb_car_no.setGeometry(QRect(30, 60, 64, 15))
        self.lb_car_no_param = QLabel(self.gb_car_status)
        self.lb_car_no_param.setObjectName(u"lb_car_no_param")
        self.lb_car_no_param.setGeometry(QRect(100, 60, 64, 15))
        self.gb_setting = QGroupBox(self.tab)
        self.gb_setting.setObjectName(u"gb_setting")
        self.gb_setting.setGeometry(QRect(240, 10, 241, 391))
        self.lb_ip = QLabel(self.gb_setting)
        self.lb_ip.setObjectName(u"lb_ip")
        self.lb_ip.setGeometry(QRect(20, 40, 61, 16))
        self.lb_ip_2 = QLabel(self.gb_setting)
        self.lb_ip_2.setObjectName(u"lb_ip_2")
        self.lb_ip_2.setGeometry(QRect(20, 80, 61, 16))
        self.le_ip = QLineEdit(self.gb_setting)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setGeometry(QRect(80, 30, 141, 31))
        self.le_port = QLineEdit(self.gb_setting)
        self.le_port.setObjectName(u"le_port")
        self.le_port.setGeometry(QRect(80, 70, 141, 31))
        self.lb_gate1 = QLabel(self.gb_setting)
        self.lb_gate1.setObjectName(u"lb_gate1")
        self.lb_gate1.setGeometry(QRect(10, 120, 64, 15))
        self.lb_gate2 = QLabel(self.gb_setting)
        self.lb_gate2.setObjectName(u"lb_gate2")
        self.lb_gate2.setGeometry(QRect(10, 160, 64, 15))
        self.lb_gate3 = QLabel(self.gb_setting)
        self.lb_gate3.setObjectName(u"lb_gate3")
        self.lb_gate3.setGeometry(QRect(10, 200, 64, 15))
        self.lb_gate4 = QLabel(self.gb_setting)
        self.lb_gate4.setObjectName(u"lb_gate4")
        self.lb_gate4.setGeometry(QRect(10, 240, 64, 15))
        self.le_gate1 = QLineEdit(self.gb_setting)
        self.le_gate1.setObjectName(u"le_gate1")
        self.le_gate1.setGeometry(QRect(80, 110, 141, 31))
        self.le_gate2 = QLineEdit(self.gb_setting)
        self.le_gate2.setObjectName(u"le_gate2")
        self.le_gate2.setGeometry(QRect(80, 150, 141, 31))
        self.le_gate3 = QLineEdit(self.gb_setting)
        self.le_gate3.setObjectName(u"le_gate3")
        self.le_gate3.setGeometry(QRect(80, 190, 141, 31))
        self.le_gate4 = QLineEdit(self.gb_setting)
        self.le_gate4.setObjectName(u"le_gate4")
        self.le_gate4.setGeometry(QRect(80, 230, 141, 31))
        self.gb_event = QGroupBox(self.tab)
        self.gb_event.setObjectName(u"gb_event")
        self.gb_event.setGeometry(QRect(490, 10, 311, 81))
        self.btn_motor_connect = QPushButton(self.gb_event)
        self.btn_motor_connect.setObjectName(u"btn_motor_connect")
        self.btn_motor_connect.setGeometry(QRect(10, 30, 141, 41))
        self.btn_motor_disconnect = QPushButton(self.gb_event)
        self.btn_motor_disconnect.setObjectName(u"btn_motor_disconnect")
        self.btn_motor_disconnect.setGeometry(QRect(160, 30, 141, 41))
        self.gb_send_data = QGroupBox(self.tab)
        self.gb_send_data.setObjectName(u"gb_send_data")
        self.gb_send_data.setGeometry(QRect(410, 410, 401, 111))
        self.tb_send_data = QTextBrowser(self.gb_send_data)
        self.tb_send_data.setObjectName(u"tb_send_data")
        self.tb_send_data.setGeometry(QRect(10, 30, 381, 71))
        self.gb_recv_data = QGroupBox(self.tab)
        self.gb_recv_data.setObjectName(u"gb_recv_data")
        self.gb_recv_data.setGeometry(QRect(10, 410, 381, 111))
        self.tb_recv_data = QTextBrowser(self.gb_recv_data)
        self.tb_recv_data.setObjectName(u"tb_recv_data")
        self.tb_recv_data.setGeometry(QRect(10, 30, 361, 71))
        self.gb_signal = QGroupBox(self.tab)
        self.gb_signal.setObjectName(u"gb_signal")
        self.gb_signal.setGeometry(QRect(490, 180, 311, 91))
        self.btn_ready = QPushButton(self.gb_signal)
        self.btn_ready.setObjectName(u"btn_ready")
        self.btn_ready.setGeometry(QRect(10, 30, 91, 41))
        self.btn_finish = QPushButton(self.gb_signal)
        self.btn_finish.setObjectName(u"btn_finish")
        self.btn_finish.setGeometry(QRect(210, 30, 91, 41))
        self.btn_start = QPushButton(self.gb_signal)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(110, 30, 91, 41))
        self.gb_function = QGroupBox(self.tab)
        self.gb_function.setObjectName(u"gb_function")
        self.gb_function.setGeometry(QRect(490, 270, 311, 131))
        self.btn_color_matching = QPushButton(self.gb_function)
        self.btn_color_matching.setObjectName(u"btn_color_matching")
        self.btn_color_matching.setGeometry(QRect(160, 30, 141, 41))
        self.lb_gate_2 = QLabel(self.gb_function)
        self.lb_gate_2.setObjectName(u"lb_gate_2")
        self.lb_gate_2.setGeometry(QRect(10, 40, 51, 16))
        self.sb_gate = QSpinBox(self.gb_function)
        self.sb_gate.setObjectName(u"sb_gate")
        self.sb_gate.setGeometry(QRect(70, 40, 71, 22))
        self.sb_gate.setMinimum(1)
        self.sb_gate.setMaximum(4)
        self.lb_color_count = QLabel(self.gb_function)
        self.lb_color_count.setObjectName(u"lb_color_count")
        self.lb_color_count.setGeometry(QRect(10, 90, 51, 16))
        self.lb_color_offset = QLabel(self.gb_function)
        self.lb_color_offset.setObjectName(u"lb_color_offset")
        self.lb_color_offset.setGeometry(QRect(160, 90, 61, 16))
        self.sb_color_count = QSpinBox(self.gb_function)
        self.sb_color_count.setObjectName(u"sb_color_count")
        self.sb_color_count.setGeometry(QRect(70, 90, 71, 22))
        self.sb_color_count.setMinimum(10)
        self.sb_color_count.setMaximum(300)
        self.sb_color_count.setValue(100)
        self.sb_color_offset = QSpinBox(self.gb_function)
        self.sb_color_offset.setObjectName(u"sb_color_offset")
        self.sb_color_offset.setGeometry(QRect(230, 90, 71, 22))
        self.sb_color_offset.setMinimum(0)
        self.sb_color_offset.setMaximum(1000)
        self.sb_color_offset.setValue(100)
        self.sb_color_offset.setDisplayIntegerBase(10)
        self.gb_socket = QGroupBox(self.tab)
        self.gb_socket.setObjectName(u"gb_socket")
        self.gb_socket.setGeometry(QRect(490, 100, 311, 81))
        self.btn_socket_connect = QPushButton(self.gb_socket)
        self.btn_socket_connect.setObjectName(u"btn_socket_connect")
        self.btn_socket_connect.setGeometry(QRect(10, 30, 141, 41))
        self.btn_socket_disconnect = QPushButton(self.gb_socket)
        self.btn_socket_disconnect.setObjectName(u"btn_socket_disconnect")
        self.btn_socket_disconnect.setGeometry(QRect(160, 30, 141, 41))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gb_handle = QGroupBox(self.tab_2)
        self.gb_handle.setObjectName(u"gb_handle")
        self.gb_handle.setGeometry(QRect(430, 180, 381, 141))
        self.lb_handle_left = QLabel(self.gb_handle)
        self.lb_handle_left.setObjectName(u"lb_handle_left")
        self.lb_handle_left.setGeometry(QRect(20, 30, 61, 16))
        self.le_handle_left = QLineEdit(self.gb_handle)
        self.le_handle_left.setObjectName(u"le_handle_left")
        self.le_handle_left.setGeometry(QRect(120, 30, 111, 21))
        self.le_handle_center = QLineEdit(self.gb_handle)
        self.le_handle_center.setObjectName(u"le_handle_center")
        self.le_handle_center.setGeometry(QRect(120, 60, 111, 21))
        self.lb_handle_center = QLabel(self.gb_handle)
        self.lb_handle_center.setObjectName(u"lb_handle_center")
        self.lb_handle_center.setGeometry(QRect(20, 60, 61, 16))
        self.le_handle_right = QLineEdit(self.gb_handle)
        self.le_handle_right.setObjectName(u"le_handle_right")
        self.le_handle_right.setGeometry(QRect(120, 90, 111, 21))
        self.lb_handle_right = QLabel(self.gb_handle)
        self.lb_handle_right.setObjectName(u"lb_handle_right")
        self.lb_handle_right.setGeometry(QRect(20, 90, 61, 16))
        self.btn_handle_save = QPushButton(self.gb_handle)
        self.btn_handle_save.setObjectName(u"btn_handle_save")
        self.btn_handle_save.setGeometry(QRect(250, 30, 111, 81))
        self.gb_dc_motor_pin_setting = QGroupBox(self.tab_2)
        self.gb_dc_motor_pin_setting.setObjectName(u"gb_dc_motor_pin_setting")
        self.gb_dc_motor_pin_setting.setGeometry(QRect(20, 20, 381, 141))
        self.lb_dc_enable = QLabel(self.gb_dc_motor_pin_setting)
        self.lb_dc_enable.setObjectName(u"lb_dc_enable")
        self.lb_dc_enable.setGeometry(QRect(20, 30, 101, 16))
        self.lb_dc_input1 = QLabel(self.gb_dc_motor_pin_setting)
        self.lb_dc_input1.setObjectName(u"lb_dc_input1")
        self.lb_dc_input1.setGeometry(QRect(20, 60, 101, 16))
        self.lb_dc_input2 = QLabel(self.gb_dc_motor_pin_setting)
        self.lb_dc_input2.setObjectName(u"lb_dc_input2")
        self.lb_dc_input2.setGeometry(QRect(20, 90, 101, 16))
        self.le_dc_enable = QLineEdit(self.gb_dc_motor_pin_setting)
        self.le_dc_enable.setObjectName(u"le_dc_enable")
        self.le_dc_enable.setGeometry(QRect(120, 30, 111, 21))
        self.le_dc_input1 = QLineEdit(self.gb_dc_motor_pin_setting)
        self.le_dc_input1.setObjectName(u"le_dc_input1")
        self.le_dc_input1.setGeometry(QRect(120, 60, 111, 21))
        self.le_dc_input2 = QLineEdit(self.gb_dc_motor_pin_setting)
        self.le_dc_input2.setObjectName(u"le_dc_input2")
        self.le_dc_input2.setGeometry(QRect(120, 90, 111, 21))
        self.btn_dc_motor_pin_setting_save = QPushButton(self.gb_dc_motor_pin_setting)
        self.btn_dc_motor_pin_setting_save.setObjectName(u"btn_dc_motor_pin_setting_save")
        self.btn_dc_motor_pin_setting_save.setGeometry(QRect(250, 30, 111, 81))
        self.gb_servo_motor_pin_setting = QGroupBox(self.tab_2)
        self.gb_servo_motor_pin_setting.setObjectName(u"gb_servo_motor_pin_setting")
        self.gb_servo_motor_pin_setting.setGeometry(QRect(430, 20, 381, 141))
        self.lb_servo_pin = QLabel(self.gb_servo_motor_pin_setting)
        self.lb_servo_pin.setObjectName(u"lb_servo_pin")
        self.lb_servo_pin.setGeometry(QRect(20, 30, 101, 16))
        self.le_servo_pin = QLineEdit(self.gb_servo_motor_pin_setting)
        self.le_servo_pin.setObjectName(u"le_servo_pin")
        self.le_servo_pin.setGeometry(QRect(120, 30, 111, 21))
        self.btn_servo_motor_pin_setting_save = QPushButton(self.gb_servo_motor_pin_setting)
        self.btn_servo_motor_pin_setting_save.setObjectName(u"btn_servo_motor_pin_setting_save")
        self.btn_servo_motor_pin_setting_save.setGeometry(QRect(250, 30, 111, 81))
        self.gb_speed = QGroupBox(self.tab_2)
        self.gb_speed.setObjectName(u"gb_speed")
        self.gb_speed.setGeometry(QRect(20, 180, 381, 141))
        self.lb_speed_limit_speed = QLabel(self.gb_speed)
        self.lb_speed_limit_speed.setObjectName(u"lb_speed_limit_speed")
        self.lb_speed_limit_speed.setGeometry(QRect(10, 30, 61, 16))
        self.le_speed_limit_speed = QLineEdit(self.gb_speed)
        self.le_speed_limit_speed.setObjectName(u"le_speed_limit_speed")
        self.le_speed_limit_speed.setGeometry(QRect(120, 30, 111, 21))
        self.le_speed_limit_boost_limit = QLineEdit(self.gb_speed)
        self.le_speed_limit_boost_limit.setObjectName(u"le_speed_limit_boost_limit")
        self.le_speed_limit_boost_limit.setGeometry(QRect(120, 60, 111, 21))
        self.lb_speed_limit_boost_speed = QLabel(self.gb_speed)
        self.lb_speed_limit_boost_speed.setObjectName(u"lb_speed_limit_boost_speed")
        self.lb_speed_limit_boost_speed.setGeometry(QRect(10, 60, 111, 16))
        self.btn_speed_limit_save = QPushButton(self.gb_speed)
        self.btn_speed_limit_save.setObjectName(u"btn_speed_limit_save")
        self.btn_speed_limit_save.setGeometry(QRect(250, 30, 111, 81))
        self.gb_color_sensor_pin_setting = QGroupBox(self.tab_2)
        self.gb_color_sensor_pin_setting.setObjectName(u"gb_color_sensor_pin_setting")
        self.gb_color_sensor_pin_setting.setGeometry(QRect(20, 340, 381, 141))
        self.lb_color_s2 = QLabel(self.gb_color_sensor_pin_setting)
        self.lb_color_s2.setObjectName(u"lb_color_s2")
        self.lb_color_s2.setGeometry(QRect(20, 30, 101, 16))
        self.lb_color_s3 = QLabel(self.gb_color_sensor_pin_setting)
        self.lb_color_s3.setObjectName(u"lb_color_s3")
        self.lb_color_s3.setGeometry(QRect(20, 60, 101, 16))
        self.lb_color_signal = QLabel(self.gb_color_sensor_pin_setting)
        self.lb_color_signal.setObjectName(u"lb_color_signal")
        self.lb_color_signal.setGeometry(QRect(20, 90, 101, 16))
        self.le_color_s2 = QLineEdit(self.gb_color_sensor_pin_setting)
        self.le_color_s2.setObjectName(u"le_color_s2")
        self.le_color_s2.setGeometry(QRect(120, 30, 111, 21))
        self.le_color_s3 = QLineEdit(self.gb_color_sensor_pin_setting)
        self.le_color_s3.setObjectName(u"le_color_s3")
        self.le_color_s3.setGeometry(QRect(120, 60, 111, 21))
        self.le_color_signal = QLineEdit(self.gb_color_sensor_pin_setting)
        self.le_color_signal.setObjectName(u"le_color_signal")
        self.le_color_signal.setGeometry(QRect(120, 90, 111, 21))
        self.btn_color_sensor_pin_setting_save = QPushButton(self.gb_color_sensor_pin_setting)
        self.btn_color_sensor_pin_setting_save.setObjectName(u"btn_color_sensor_pin_setting_save")
        self.btn_color_sensor_pin_setting_save.setGeometry(QRect(250, 30, 111, 81))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 833, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_ready.clicked.connect(MainWindow.readySignal)
        self.btn_socket_connect.clicked.connect(MainWindow.socketConnect)
        self.btn_motor_connect.clicked.connect(MainWindow.motorConnect)
        self.btn_socket_disconnect.clicked.connect(MainWindow.socketDisconnect)
        self.btn_motor_disconnect.clicked.connect(MainWindow.motorDisconnect)
        self.btn_finish.clicked.connect(MainWindow.finishSignal)
        self.btn_color_matching.clicked.connect(MainWindow.colorMatching)
        self.btn_start.clicked.connect(MainWindow.startSignal)
        self.btn_handle_save.clicked.connect(MainWindow.handleSave)
        self.btn_dc_motor_pin_setting_save.clicked.connect(MainWindow.dcMotorPinSettingSave)
        self.btn_servo_motor_pin_setting_save.clicked.connect(MainWindow.servoMotorPinSettingSave)
        self.btn_speed_limit_save.clicked.connect(MainWindow.speedLimitSave)
        self.btn_color_sensor_pin_setting_save.clicked.connect(MainWindow.colorSensorPinSetting)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gb_log.setTitle(QCoreApplication.translate("MainWindow", u"log", None))
        self.gb_car_status.setTitle(QCoreApplication.translate("MainWindow", u"Car Status", None))
        self.lb_model.setText(QCoreApplication.translate("MainWindow", u"Model :", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.lb_model_param.setText(QCoreApplication.translate("MainWindow", u"AX_231", None))
        self.lb_status_param.setText(QCoreApplication.translate("MainWindow", u"Preparing", None))
        self.lb_speed.setText(QCoreApplication.translate("MainWindow", u"Speed :", None))
        self.lb_speed_param.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lb_gate.setText(QCoreApplication.translate("MainWindow", u"Gate :", None))
        self.lb_gate_param.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_motor.setText(QCoreApplication.translate("MainWindow", u"Motor :", None))
        self.lb_socket.setText(QCoreApplication.translate("MainWindow", u"Socket :", None))
        self.lb_motor_param.setText(QCoreApplication.translate("MainWindow", u"Not Setting", None))
        self.lb_socket_param.setText(QCoreApplication.translate("MainWindow", u"Not Connect", None))
        self.lb_rgb.setText(QCoreApplication.translate("MainWindow", u"Red, Green, Blue :", None))
        self.lb_rgb_param.setText(QCoreApplication.translate("MainWindow", u"100, 100, 100", None))
        self.lb_car_no.setText(QCoreApplication.translate("MainWindow", u"Car No :", None))
        self.lb_car_no_param.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gb_setting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.lb_ip.setText(QCoreApplication.translate("MainWindow", u"IP :", None))
        self.lb_ip_2.setText(QCoreApplication.translate("MainWindow", u"Port :", None))
        self.lb_gate1.setText(QCoreApplication.translate("MainWindow", u"Gate 1 :", None))
        self.lb_gate2.setText(QCoreApplication.translate("MainWindow", u"Gate 2 :", None))
        self.lb_gate3.setText(QCoreApplication.translate("MainWindow", u"Gate 3 :", None))
        self.lb_gate4.setText(QCoreApplication.translate("MainWindow", u"Gate 4 :", None))
        self.gb_event.setTitle(QCoreApplication.translate("MainWindow", u"Motor/Sensor", None))
        self.btn_motor_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_motor_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.gb_send_data.setTitle(QCoreApplication.translate("MainWindow", u"Send Data", None))
        self.gb_recv_data.setTitle(QCoreApplication.translate("MainWindow", u"Recv Data", None))
        self.gb_signal.setTitle(QCoreApplication.translate("MainWindow", u"Signal", None))
        self.btn_ready.setText(QCoreApplication.translate("MainWindow", u"READY", None))
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.gb_function.setTitle(QCoreApplication.translate("MainWindow", u"Function", None))
        self.btn_color_matching.setText(QCoreApplication.translate("MainWindow", u"Color Matching", None))
        self.lb_gate_2.setText(QCoreApplication.translate("MainWindow", u"Gate :", None))
        self.lb_color_count.setText(QCoreApplication.translate("MainWindow", u"Count:", None))
        self.lb_color_offset.setText(QCoreApplication.translate("MainWindow", u"Offset :", None))
        self.gb_socket.setTitle(QCoreApplication.translate("MainWindow", u"Socket", None))
        self.btn_socket_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_socket_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.gb_handle.setTitle(QCoreApplication.translate("MainWindow", u"Handle", None))
        self.lb_handle_left.setText(QCoreApplication.translate("MainWindow", u"Left :", None))
        self.lb_handle_center.setText(QCoreApplication.translate("MainWindow", u"Center :", None))
        self.lb_handle_right.setText(QCoreApplication.translate("MainWindow", u"Right :", None))
        self.btn_handle_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.gb_dc_motor_pin_setting.setTitle(QCoreApplication.translate("MainWindow", u"DC Motor Pin Setting", None))
        self.lb_dc_enable.setText(QCoreApplication.translate("MainWindow", u"DC Enable :", None))
        self.lb_dc_input1.setText(QCoreApplication.translate("MainWindow", u"DC input1 :", None))
        self.lb_dc_input2.setText(QCoreApplication.translate("MainWindow", u"DC input2 :", None))
        self.btn_dc_motor_pin_setting_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.gb_servo_motor_pin_setting.setTitle(QCoreApplication.translate("MainWindow", u"Servo Motor Pin Setting", None))
        self.lb_servo_pin.setText(QCoreApplication.translate("MainWindow", u"Servo Pin :", None))
        self.btn_servo_motor_pin_setting_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.gb_speed.setTitle(QCoreApplication.translate("MainWindow", u"Speed Limit", None))
        self.lb_speed_limit_speed.setText(QCoreApplication.translate("MainWindow", u"Speed :", None))
        self.lb_speed_limit_boost_speed.setText(QCoreApplication.translate("MainWindow", u"Boost Speed :", None))
        self.btn_speed_limit_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.gb_color_sensor_pin_setting.setTitle(QCoreApplication.translate("MainWindow", u"Color Sensor Pin Setting", None))
        self.lb_color_s2.setText(QCoreApplication.translate("MainWindow", u"Color S2 :", None))
        self.lb_color_s3.setText(QCoreApplication.translate("MainWindow", u"Color S3 :", None))
        self.lb_color_signal.setText(QCoreApplication.translate("MainWindow", u"Color Signal :", None))
        self.btn_color_sensor_pin_setting_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Motor", None))
    # retranslateUi
