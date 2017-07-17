#importing wx files
import wx
 
#import the newly created GUI file
import lic_check_gui

#import the lic_check engine
import lic_check
 
#inherit from the MainFrame created in wxFowmBuilder and create lic_check_frame
class lic_check_frame(lic_check_gui.lic_check_frm):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        lic_check_gui.lic_check_frm.__init__(self,parent)
        
    def file_convert_func( self, event ):
        if(lic_check.validate_licence()):
            print 'Converting file ' + self.m_filePicker1.GetPath()
        else:
            self.m_statusBar.SetStatusText('Invalid Licence', 0)

        
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of lic_gen_frame
frame = lic_check_frame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()