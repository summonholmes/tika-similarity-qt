'''
         _,met$$$$$gg.           summonholmes@10x-Orange-G
      ,g$$$$$$$$$$$$$$$P.        OS: Debian 9.3 stretch
    ,g$$P""       """Y$$.".      Kernel: x86_64 Linux 4.9.0-4-amd64
   ,$$P'              `$$$.      Uptime: 40m
  ',$$P       ,ggs.     `$$b:    Packages: 1707
  `d$$'     ,$P"'   .    $$$     Shell: zsh 5.3.1
   $$P      d$'     ,    $$P     Resolution: 1280x800
   $$:      $$.   -    ,d$$'     DE: XFCE
   $$\;      Y$b._   _,d$P'      WM: Xfwm4
   Y$$.    `.`"Y$$$$P"'          WM Theme: Adapta-Nokto
   `$$b      "-.__               GTK Theme: Adapta-Nokto-Eta [GTK2]
    `Y$$                         Icon Theme: Papirus-Adapta-Nokto
     `Y$$.                       Font: Roboto Medium 10
       `$$b.                     CPU: Intel Core i7 CPU L 640 @ 2.134GHz
         `Y$$b.                  GPU: Mesa DRI Intel(R) Ironlake Mobile 
            `"Y$b._              RAM: 1358MiB / 7783MiB
                `""""           

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from sys import argv, exit
from os import path, system
from urllib2 import urlopen, URLError
from csv import reader
import metalevenshtein
import features

# 1. QtDesigner UI is converted to the Python code below:

class Ui_win_Title(object):
    def setupUi(self, win_Title):
        win_Title.setObjectName("win_Title")
        win_Title.resize(420, 433)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(win_Title)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.total_Layout = QtWidgets.QVBoxLayout()
        self.total_Layout.setObjectName("total_Layout")
        self.in_out_Layout = QtWidgets.QHBoxLayout()
        self.in_out_Layout.setObjectName("in_out_Layout")
        self.in_out_line_Layout = QtWidgets.QVBoxLayout()
        self.in_out_line_Layout.setObjectName("in_out_line_Layout")
        self.input_lineEdit = QtWidgets.QLineEdit(win_Title)
        self.input_lineEdit.setObjectName("input_lineEdit")
        self.in_out_line_Layout.addWidget(self.input_lineEdit)
        self.output_lineEdit = QtWidgets.QLineEdit(win_Title)
        self.output_lineEdit.setObjectName("output_lineEdit")
        self.in_out_line_Layout.addWidget(self.output_lineEdit)
        self.in_out_Layout.addLayout(self.in_out_line_Layout)
        self.in_out_button_Layout = QtWidgets.QVBoxLayout()
        self.in_out_button_Layout.setObjectName("in_out_button_Layout")
        self.input_Button = QtWidgets.QPushButton(win_Title)
        self.input_Button.setObjectName("input_Button")
        self.in_out_button_Layout.addWidget(self.input_Button)
        self.output_Button = QtWidgets.QPushButton(win_Title)
        self.output_Button.setObjectName("output_Button")
        self.in_out_button_Layout.addWidget(self.output_Button)
        self.in_out_Layout.addLayout(self.in_out_button_Layout)
        self.total_Layout.addLayout(self.in_out_Layout)
        self.comp_Layout = QtWidgets.QVBoxLayout()
        self.comp_Layout.setObjectName("comp_Layout")
        self.sim_comp_label = QtWidgets.QLabel(win_Title)
        self.sim_comp_label.setObjectName("sim_comp_label")
        self.comp_Layout.addWidget(self.sim_comp_label)
        self.comp_key_val_Layout = QtWidgets.QHBoxLayout()
        self.comp_key_val_Layout.setObjectName("comp_key_val_Layout")
        self.comp_key_Button = QtWidgets.QPushButton(win_Title)
        self.comp_key_Button.setObjectName("comp_key_Button")
        self.comp_key_val_Layout.addWidget(self.comp_key_Button)
        self.comp_val_Button = QtWidgets.QPushButton(win_Title)
        self.comp_val_Button.setObjectName("comp_val_Button")
        self.comp_key_val_Layout.addWidget(self.comp_val_Button)
        self.comp_Layout.addLayout(self.comp_key_val_Layout)
        self.comp_cos_ed_Layout = QtWidgets.QHBoxLayout()
        self.comp_cos_ed_Layout.setObjectName("comp_cos_ed_Layout")
        self.comp_cos_Button = QtWidgets.QPushButton(win_Title)
        self.comp_cos_Button.setObjectName("comp_cos_Button")
        self.comp_cos_ed_Layout.addWidget(self.comp_cos_Button)
        self.sim_sty_Button = QtWidgets.QPushButton(win_Title)
        self.sim_sty_Button.setObjectName("sim_sty_Button")
        self.comp_cos_ed_Layout.addWidget(self.sim_sty_Button)
        self.comp_edit_Button = QtWidgets.QPushButton(win_Title)
        self.comp_edit_Button.setObjectName("comp_edit_Button")
        self.comp_cos_ed_Layout.addWidget(self.comp_edit_Button)
        self.comp_Layout.addLayout(self.comp_cos_ed_Layout)
        self.total_Layout.addLayout(self.comp_Layout)
        self.sim_Layout = QtWidgets.QVBoxLayout()
        self.sim_Layout.setObjectName("sim_Layout")
        self.sim_vis_label = QtWidgets.QLabel(win_Title)
        self.sim_vis_label.setObjectName("sim_vis_label")
        self.sim_Layout.addWidget(self.sim_vis_label)
        self.sim_button_Layout = QtWidgets.QHBoxLayout()
        self.sim_button_Layout.setObjectName("sim_button_Layout")
        self.sim_cos_Button = QtWidgets.QPushButton(win_Title)
        self.sim_cos_Button.setObjectName("sim_cos_Button")
        self.sim_button_Layout.addWidget(self.sim_cos_Button)
        self.sim_jac_Button = QtWidgets.QPushButton(win_Title)
        self.sim_jac_Button.setObjectName("sim_jac_Button")
        self.sim_button_Layout.addWidget(self.sim_jac_Button)
        self.sim_Layout.addLayout(self.sim_button_Layout)
        self.total_Layout.addLayout(self.sim_Layout)
        self.oth_Layout = QtWidgets.QVBoxLayout()
        self.oth_Layout.setObjectName("oth_Layout")
        self.oth_Label = QtWidgets.QLabel(win_Title)
        self.oth_Label.setObjectName("oth_Label")
        self.oth_Layout.addWidget(self.oth_Label)
        self.oth_button_Layout = QtWidgets.QHBoxLayout()
        self.oth_button_Layout.setObjectName("oth_button_Layout")
        self.oth_bell_Button = QtWidgets.QPushButton(win_Title)
        self.oth_bell_Button.setObjectName("oth_bell_Button")
        self.oth_button_Layout.addWidget(self.oth_bell_Button)
        self.oth_meta_Button = QtWidgets.QPushButton(win_Title)
        self.oth_meta_Button.setObjectName("oth_meta_Button")
        self.oth_button_Layout.addWidget(self.oth_meta_Button)
        self.oth_Layout.addLayout(self.oth_button_Layout)
        self.total_Layout.addLayout(self.oth_Layout)
        self.exit_Button = QtWidgets.QPushButton(win_Title)
        self.exit_Button.setObjectName("exit_Button")
        self.total_Layout.addWidget(self.exit_Button)
        self.verticalLayout_4.addLayout(self.total_Layout)

        self.retranslateUi(win_Title)
        QtCore.QMetaObject.connectSlotsByName(win_Title)

    def retranslateUi(self, win_Title):
        _translate = QtCore.QCoreApplication.translate
        win_Title.setWindowTitle(_translate("win_Title", "Tika Similarity Qt5"))
        self.input_Button.setText(_translate("win_Title", "Input"))
        self.output_Button.setText(_translate("win_Title", "Output"))
        self.sim_comp_label.setText(_translate("win_Title", "1. Similarity & Comparison"))
        self.comp_key_Button.setText(_translate("win_Title", "Key"))
        self.comp_val_Button.setText(_translate("win_Title", "Value"))
        self.comp_cos_Button.setText(_translate("win_Title", "Cosine-Distance"))
        self.sim_sty_Button.setText(_translate("win_Title", "Stylistic"))
        self.comp_edit_Button.setText(_translate("win_Title", "Edit-Distance"))
        self.sim_vis_label.setText(_translate("win_Title", "2. Visualization"))
        self.sim_cos_Button.setText(_translate("win_Title", "Cosine"))
        self.sim_jac_Button.setText(_translate("win_Title", "Jaccard"))
        self.oth_Label.setText(_translate("win_Title", "3. Other"))
        self.oth_bell_Button.setText(_translate("win_Title", "Bell Curve"))
        self.oth_meta_Button.setText(_translate("win_Title", "Metalevenshtein"))
        self.exit_Button.setText(_translate("win_Title", "Exit"))

# 2. Code providing basic GUI functionality (mostly boolean based):

    # Any popup window such as warnings and status
    def pop_msg_win(self, win_title, msg_text):
        pop_msg = QtWidgets.QMessageBox()
        pop_msg.setWindowTitle(win_title)
        pop_msg.setText(msg_text)
        pop_msg.exec_()
    
    # The program requires internet
    def check_connect(self):
        try:
            urlopen('http://216.58.192.142', timeout=1)
        except URLError:
            self.pop_msg_win('Error', 'No Internet connection detected.  '
                                      'The program will now terminate.')
            exit(0)
    
    def input_folder(self):
        self.input_lineEdit.setText(str(QtWidgets.QFileDialog.getExistingDirectory()))

    def input_file(self):
        self.input_lineEdit.setText(str(QtWidgets.QFileDialog.getOpenFileName()[0]))
    
    def output_folder(self):
        self.output_lineEdit.setText(str(QtWidgets.QFileDialog.getExistingDirectory()))
    
    def input_check(self):
        if path.isdir(self.input_lineEdit.text()) is True and \
                        path.expanduser("%USERPROFILE%") in str(self.input_lineEdit.text()):
            return True
        elif self.input_lineEdit.text() == "":
            self.pop_msg_win('Error', 'Please provide or browse for an input folder.')
            return False
        elif path.isdir(self.input_lineEdit.text()) and \
                        path.expanduser("%USERPROFILE%") not in str(self.input_lineEdit.text()):
            self.pop_msg_win('Error', 'You do not have permission to write to this directory.')
            return False
        else:
            self.pop_msg_win('Error', 'Not a Directory.')
            return False
    
    def output_check(self):
        if path.isdir(self.output_lineEdit.text()) is True and \
                        path.expanduser("%USERPROFILE%") in str(self.output_lineEdit.text()):
            return True
        elif self.output_lineEdit.text() == "":
            user_response = self.output_empty()
            if user_response is True:
                return True
            else:
                return False
        elif path.isdir(self.output_lineEdit.text()) and \
                        path.expanduser("%USERPROFILE%") not in str(self.output_lineEdit.text()):
            self.pop_msg_win('Error', 'You do not have permission to write to this directory.')
            return False
        else:
            self.pop_msg_win('Error', 'Not a Directory.')
            return False

    # The program will offer to set the output to input if input exists, and output does not
    def output_empty(self):
        false_msg = QtWidgets.QMessageBox()
        buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        set_out = QtWidgets.QMessageBox.question(false_msg, 'Warning',
                                   'No output specified.  '
                                   'Use the input directory for output?', buttons)
        if set_out == QtWidgets.QMessageBox.Yes:
            self.output_lineEdit.setText(str(self.input_lineEdit.text()))
            return True
        else:
            return False
        
    def set_threshold(self):
        thres_msg = QtWidgets.QInputDialog.getDouble(self.__init__(), 'Set Threshold',
                                                 'Please specify the threshold (Default = 0.01)',
                                                 decimals = 2)
        if isinstance(thres_msg[0], float) is True and thres_msg[1] is True:
            return thres_msg[0]
        else:
            return False
    
    def set_cluster(self):
        items = ("X-Coordinate", "Y-Coordinate", "Similarity Score")
        clust_msg = QtWidgets.QInputDialog.getItem(self.__init__(),
                                               'Set Cluster Mode',
                                               'Please specify the cluster mode',
                                               items)
        if clust_msg[0] == 'X-Coordinate' and clust_msg[1] is True:
            return 0
        elif clust_msg[0] == 'Y-Coordinate' and clust_msg[1] is True:
            return 1
        elif clust_msg[0] == 'Similarity Score' and clust_msg[1] is True:
            return 2
        elif clust_msg[1] is False:
            return False
        else:
            self.pop_msg_win('Error', 'Not a valid option.')
            return False
    
    def set_meta(self, string_order):
        met_msg = QtWidgets.QInputDialog.getText(self.__init__(),
                                                 'Metalevenshtein',
                                                 'Please enter the %s string' % string_order)
        if met_msg[1] is False:
            return False
        elif met_msg[0] == '' or str(met_msg[0]).isspace() is True:
            self.pop_msg_win('Error', 'You must provide input.')
            return False
        elif isinstance(str(met_msg[0]), str):
            return met_msg[0]
        else:
            self.pop_msg_win('Error', 'An unknown error occurred.')
            return False
    
    def set_bell(self, string_order):
        bell_in = QtWidgets.QInputDialog.getText(self.__init__(),
                                                 'Bell Curve Overlap',
                                                 'Please enter the %s set '
                                                 '(Integers only using spaces)'
                                                 '  ex: 1 2 3 4 5 6' % string_order)
        bell_list = self.bell_conv(bell_in[0])
        if bell_in[1] is False:
            return False
        elif bell_in[0] == '' or str(bell_in[0]).isspace() is True:
            self.pop_msg_win('Error', 'You must provide input.')
            return False
        elif isinstance(str(bell_in[0]), str):
            return bell_list
        else:
            self.pop_msg_win('Error', 'An unknown error occurred.')
            return False
    
    def bell_conv(self, bell_in):
        bell_msg = str(bell_in)
        bell_list = bell_msg.split()
        if self.bell_conv_check(bell_list) is True:
            bell_int_list = []
            for x in range(len(bell_list)):
                bell_int_list.append(int(bell_list[x]))
            return bell_int_list
        else:
            return False
    
    def bell_conv_check(self, bell_list):
        for x in range(len(bell_list)):
            if bell_list[x].isdigit() is False:
                self.pop_msg_win('Error', 'You did not provide an integer')
                return False
        return True

    def csv_check(self):
        rdr = reader(open(self.input_lineEdit.text()))
        line_1 = rdr.next()
        if line_1 == ['x-coordinate', 'y-coordinate', 'Similarity_score']:
            self.cosine_sim_run()
        else:
            self.pop_msg_win('Error', 'The file is corrupted')
            return False

    # 3. The buttons are linked to the existing Python files here:

    def key_comp(self):
        check_input = self.input_check()
        if check_input is True:
            self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
            system("C:\Python27\python.exe similarity.py similarity.py -f %s" % self.input_lineEdit.text())
            results = 'similarity-scores.txt'
            self.pop_msg_win('Complete', 'Results saved to %s' % results)
        else:
            return None
    
    def value_comp(self):
        check_input = self.input_check()
        if check_input is True:
            self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
            system("C:\Python27\python.exe similarity.py value-similarity.py -f %s" % self.input_lineEdit.text())
            results = 'value-similarity-scores.txt'
            self.pop_msg_win('Complete', 'Results saved to %s' % results)
        else:
            return None
    
    def cosine_comp(self):
        check_input = self.input_check()
        if check_input is True:
            check_output = self.output_check()
            if check_output is True:
                self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
                system("C:\Python27\python.exe cosine_similarity.py --inputDir %s "
                       "--outCSV %s/cosine_similarity.csv"
                       % (self.input_lineEdit.text(), self.output_lineEdit.text()))
                results = '%s/cosine_similarity.csv' % self.output_lineEdit.text()
                self.pop_msg_win('Complete', 'Results saved to %s' % results)
            else:
                return None
        else:
            return None
    
    def edit_comp(self):
        check_input = self.input_check()
        if check_input is True:
            check_output = self.output_check()
            if check_output is True:
                self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
                system("C:\Python27\python.exe edit-value-similarity.py --inputDir %s "
                       "--outCSV %s/edit-value-similarity.csv"
                       % (self.input_lineEdit.text(), self.output_lineEdit.text()))
                results = '%s/edit-value-similarity.csv' % self.output_lineEdit.text()
                self.pop_msg_win('Complete', 'Results saved to %s' % results)
            else:
                return None
        else:
            return None

    def stylistic_sim(self):
        check_input = self.input_check()
        if check_input is True:
            check_output = self.output_check()
            if check_output is True:
                self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
                system("C:\Python27\python.exe psykey.py --inputDir %s "
                       "--outCSV %s/psykey.csv "
                       "--wordlists wordlists"
                       % (self.input_lineEdit.text(), self.output_lineEdit.text()))
                results = '%s/psykey.csv' % self.output_lineEdit.text()
                self.pop_msg_win('Complete', 'Results saved to %s' % results)
            else:
                return None
        else:
            return None
    
    def jaccard_sim(self):
        if path.isfile('similarity-scores.txt') is True:
            with open('similarity-scores.txt', 'r') as f:
                line_1 = f.readline().strip()
                if line_1 == 'Resemblance :':
                    self.jaccard_sim_run()
                else:
                    self.pop_msg_win('Error', 'The file is corrupted')
                    return None
        else:
            self.pop_msg_win('Error', 'Please run Key Comparison first')
            return None
    
    def jaccard_sim_run(self):
        thres_val = self.set_threshold()
        if thres_val is False:
            return None
        else:
            self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
            system("C:\Python27\python.exe cluster-scores.py -t %s" % thres_val)
            system("C:\Python27\python.exe circle-packing.py")
            results = 'cluster-d3.html dynamic-cluster.html, and circlepacking.html'
            self.pop_msg_win('Complete', 'Results saved to %s' % results)

    def cosine_sim(self):
        self.pop_msg_win('Update File', 'Browse to either edit-value-similarity.csv or '
                                        'cosine_similarity.csv')
        self.input_file()
        if 'edit-value-similarity.csv' in self.input_lineEdit.text():
            if self.csv_check() is False:
                return False
        elif 'cosine_similarity.csv' in self.input_lineEdit.text():
            if self.csv_check() is False:
                return False
        elif self.input_lineEdit.text() == '':
            return False
        else:
            self.pop_msg_win('Error', 'You did not browse for edit-value-similarity.csv '
                                      'or cosine_similarity.csv')
            return False
    
    def cosine_sim_run(self):
        cluster_mode = self.set_cluster()
        if cluster_mode is False:
            return None
        else:
            self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
            system("C:\Python27\python.exe edit-cosine-cluster.py --inputCSV %s --cluster %d" %
                    (self.input_lineEdit.text(), cluster_mode))
            system("C:\Python27\python.exe edit-cosine-circle-packing.py --inputCSV %s --cluster %d" %
                (self.input_lineEdit.text(), cluster_mode))
            results = 'cluster-d3.html dynamic-cluster.html, and circlepacking.html'
            self.pop_msg_win('Complete', 'Results saved to %s' % results)
        
    def metalev(self):
        string_1 = str(self.set_meta('first'))
        if string_1 is False:
            return None
        else:
            string_2 = str(self.set_meta('second'))
            if string_2 is False:
                return None
            else:
                self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
                results = metalevenshtein.meta_levenshtein(string_1, string_2)
                self.pop_msg_win('Complete', 'Result: %s' % results)
    
    def bell_curve(self):
        list_1 = self.set_bell('first')
        if list_1 is False:
            return None
        else:
            list_2 = self.set_bell('second')
            if list_2 is False:
                return None
            else:
                self.pop_msg_win('In Progress', 'Please wait for the operation to complete')
                results = features.gaussian_overlap(list_1, list_2)
                self.pop_msg_win('Complete', 'Result: %s' % results)

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    win_Title = QtWidgets.QDialog()
    ui = Ui_win_Title()
    ui.setupUi(win_Title)

    ui.check_connect()

    ui.input_Button.clicked.connect(ui.input_folder)
    ui.output_Button.clicked.connect(ui.output_folder)
    ui.comp_key_Button.clicked.connect(ui.key_comp)
    ui.comp_val_Button.clicked.connect(ui.value_comp)
    ui.comp_cos_Button.clicked.connect(ui.cosine_comp)
    ui.comp_edit_Button.clicked.connect(ui.edit_comp)
    ui.sim_sty_Button.clicked.connect(ui.stylistic_sim)
    ui.sim_jac_Button.clicked.connect(ui.jaccard_sim)
    ui.sim_cos_Button.clicked.connect(ui.cosine_sim)
    ui.oth_meta_Button.clicked.connect(ui.metalev)
    ui.oth_bell_Button.clicked.connect(ui.bell_curve)

    ui.exit_Button.clicked.connect(QtCore.QCoreApplication.instance().quit)

    win_Title.show()
    exit(app.exec_())
