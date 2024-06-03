import time
import auto
import sys
import multiprocessing 
from PyQt5.QtWidgets import QApplication, QCheckBox,QHBoxLayout, QWidget,QListWidgetItem,QListWidget, QPushButton
checked_monster = []
def start(args):
    time.sleep(5)
    # time.sleep(3)
    auto.change_map()
    while True:
        for item in args:
            auto.go(item)

monster_list1 = ['鸣钟之龟', '辉萤军势', '燎照之骑', '哀声鸷', '无冠者','无常凶鹭', '飞廉之猩', '聚械机偶', '朔雷之鳞', '云闪之鳞']
class Winform(QWidget):
    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("mc-script") 
        self.resize(330, 150)  
        # 垂直布局按照从上到下的顺序进行添加按钮部件。
        hlayout = QHBoxLayout()
        list_widget = QListWidget()
        for item in monster_list1:
            checkBox = QCheckBox(str(item))
            checkBox.stateChanged.connect(lambda checked, cb=checkBox: btnState(checked,cb))
            list_item = QListWidgetItem()
            list_widget.addItem(list_item)
            list_widget.setItemWidget(list_item, checkBox)
        hlayout.addWidget(list_widget)
        button1 = QPushButton('开始', self)
        button1.clicked.connect(clickButton)
        hlayout.addWidget(button1)
        self.setLayout(hlayout)

    def closeEvent(self,event):
        p.terminate()
        p.join()
        sys.exit(app.exec_())

def btnState(checked, cb):
    if (cb.isChecked()):
        if(len(checked_monster) >= 3):
            cb.setChecked(False)
            return
        else:
            checked_monster.append(cb.text())
    else:
        if cb.text() in checked_monster:
            checked_monster.remove(cb.text())

p = multiprocessing.Process(target=start, args=[checked_monster])
def clickButton():
    p.start()

def close():
    p.terminate()
    p.join()
    

if __name__ == '__main__':
    # ------window------
    multiprocessing.freeze_support()
    app = QApplication(sys.argv) 
    form = Winform()
    form.show()
    sys.exit(app.exec_())
    # start()