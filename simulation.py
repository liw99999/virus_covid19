# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(1581, 818)
        mainWindow.setStyleSheet("background-color: rgb(133, 133, 133);\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1300, 30, 171, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1480, 30, 146, 431))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPersonCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelPersonCount.setObjectName("labelPersonCount")
        self.verticalLayout_2.addWidget(self.labelPersonCount)
        self.labelNormalPersonCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelNormalPersonCount.setObjectName("labelNormalPersonCount")
        self.verticalLayout_2.addWidget(self.labelNormalPersonCount)
        self.labelLatencyPersonCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelLatencyPersonCount.setObjectName("labelLatencyPersonCount")
        self.verticalLayout_2.addWidget(self.labelLatencyPersonCount)
        self.labelConfirmedPersonCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelConfirmedPersonCount.setObjectName("labelConfirmedPersonCount")
        self.verticalLayout_2.addWidget(self.labelConfirmedPersonCount)
        self.labelFreezePersonCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelFreezePersonCount.setObjectName("labelFreezePersonCount")
        self.verticalLayout_2.addWidget(self.labelFreezePersonCount)
        self.labelDeathPersonCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelDeathPersonCount.setObjectName("labelDeathPersonCount")
        self.verticalLayout_2.addWidget(self.labelDeathPersonCount)
        self.labelFreeBedCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelFreeBedCount.setObjectName("labelFreeBedCount")
        self.verticalLayout_2.addWidget(self.labelFreeBedCount)
        self.labelNeedBedCount = QtWidgets.QLabel(self.layoutWidget1)
        self.labelNeedBedCount.setObjectName("labelNeedBedCount")
        self.verticalLayout_2.addWidget(self.labelNeedBedCount)
        self.labelCurrentTime = QtWidgets.QLabel(self.layoutWidget1)
        self.labelCurrentTime.setObjectName("labelCurrentTime")
        self.verticalLayout_2.addWidget(self.labelCurrentTime)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1480, 560, 218, 301))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelBedCount = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelBedCount.setObjectName("labelBedCount")
        self.verticalLayout_6.addWidget(self.labelBedCount)
        self.labelAverageFlowIntention = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelAverageFlowIntention.setObjectName("labelAverageFlowIntention")
        self.verticalLayout_6.addWidget(self.labelAverageFlowIntention)
        self.labelBroadRate = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelBroadRate.setObjectName("labelBroadRate")
        self.verticalLayout_6.addWidget(self.labelBroadRate)
        self.labelLatency = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelLatency.setObjectName("labelLatency")
        self.verticalLayout_6.addWidget(self.labelLatency)
        self.labelReceiveTime = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelReceiveTime.setObjectName("labelReceiveTime")
        self.verticalLayout_6.addWidget(self.labelReceiveTime)
        self.labelSafeDistance = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelSafeDistance.setObjectName("labelSafeDistance")
        self.verticalLayout_6.addWidget(self.labelSafeDistance)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(1250, 560, 218, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "病毒传播仿真器"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">城市总人数：</span></p></body></html>"))
        self.label_2.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">健康者人数：</span></p></body></html>"))
        self.label_3.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">潜伏期人数：</span></p></body></html>"))
        self.label_4.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">发病者人数：</span></p></body></html>"))
        self.label_5.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">已隔离人数：</span></p></body></html>"))
        self.label_6.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">已死亡人数：</span></p></body></html>"))
        self.label_7.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">空余病床：</span></p></body></html>"))
        self.label_8.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">急需病床：</span></p></body></html>"))
        self.label_9.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">当前时间：</span></p></body></html>"))
        self.labelPersonCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">5000</span></p></body></html>"))
        self.labelNormalPersonCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#0000ff;\">5000</span></p></body></html>"))
        self.labelLatencyPersonCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff0a;\">0</span></p></body></html>"))
        self.labelConfirmedPersonCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#fc0107;\">0</span></p></body></html>"))
        self.labelFreezePersonCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#20ffff;\">0</span></p></body></html>"))
        self.labelDeathPersonCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">0</span></p></body></html>"))
        self.labelFreeBedCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#21ff06;\">0</span></p></body></html>"))
        self.labelNeedBedCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#fc02ff;\">0</span></p></body></html>"))
        self.labelCurrentTime.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">0</span></p></body></html>"))
        self.labelBedCount.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#0000ff;\">100</span></p></body></html>"))
        self.labelAverageFlowIntention.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#fc02ff;\">1.99</span></p></body></html>"))
        self.labelBroadRate.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#fc0107;\">0.8</span></p></body></html>"))
        self.labelLatency.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff0a;\">14</span></p></body></html>"))
        self.labelReceiveTime.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#21ff06;\">10</span></p></body></html>"))
        self.labelSafeDistance.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">2</span></p></body></html>"))
        self.label_13.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; color:#000000;\">医院床位：</span></p></body></html>"))
        self.label_15.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; color:#000000;\">平均流动意向：</span></p></body></html>"))
        self.label_10.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; color:#000000;\">传播率：</span></p></body></html>"))
        self.label_11.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; color:#000000;\">潜伏期：</span></p></body></html>"))
        self.label_12.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#000000;\">医院收治响应时间：</span></p></body></html>"))
        self.label_14.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; color:#000000;\">安全距离：</span></p></body></html>"))

