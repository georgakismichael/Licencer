#importing wx files
import wx
 
#import the newly created GUI file
import lic_gen_gui

#import the lic_gen engine
import lic_gen
 
#inherit from the MainFrame created in wxFowmBuilder and create lic_gen_frame
class lic_gen_frame(lic_gen_gui.lic_gen_frm):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        lic_gen_gui.lic_gen_frm.__init__(self,parent)

    def generate_licence_func( self, event ):
        ret = lic_gen.generate_licence(self.Usage_txt.GetValue(), self.Expiry_txt.GetValue()) 
        if(ret == 1):
            self.m_statusBar.SetStatusText('OK', 0)
        elif(ret == 0):
            self.m_statusBar.SetStatusText('Error', 0)
        elif(ret == 2):
            self.m_statusBar.SetStatusText('Warning', 0)
        
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of lic_gen_frame
frame = lic_gen_frame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()