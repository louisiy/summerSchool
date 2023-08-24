import wx
import random
nameList = ['李权','郭宝生','李志伟','高瑞奎','武昌基','杨煜程','李宇峰','刘一楠','蔡雨阳','李奕均','杨致亦','梁可','李悦然','张子琪','易炜力','姚锦昊','于海跃','赵立卓','王志恺','杨仲铉','王俊杰','王浠睿','常梓洋','李清敏','王文强','周瑞','王中天','周奕衡','董雨良','高凡','樊宇翔','马哲淏','许泽睿','田成涛','乐翼成','岳明德','张绪焜','王驰','刘明旭','陈奕衡','牛艺琳','郭瑞璇','王施俨','王子易','沈王瑾','张梓杰','林琮盛','刘汉清','刘宽','傅思维','史政超','赵卓凡','阎启铭','刘澄澄','殷桐','单明悦','江宇萱','刘雨轩','王一涵','王越淇','']

# 自定义窗口类
class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame,self).__init__(None,title ="点名器",size =(300,400))
        # 面板
        panel = wx.Panel(parent=self)
        # 文字控件
        self.staticText = wx.StaticText(parent = panel, label=nameList[60],pos=(120,70))
        # 按钮
        btn = wx.Button(parent = panel, label ="开奖",pos = (110,240))
        self.Bind(wx.EVT_BUTTON,self.on_click,btn)

    # 按钮事件
    def on_click(self, event):
        temp = random.randint(0,59)
        self.staticText.SetLabelText(nameList[temp])

#print(nameList[temp])
#主窗口
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()