import os
import webbrowser

from hydrus.core import HydrusConstants as HC
from hydrus.core import HydrusData
from hydrus.core import HydrusGlobals as HG
from hydrus.core import HydrusPaths

def DeletePath( path, always_delete_fully = False ):
    
    if HC.options[ 'delete_to_recycle_bin' ] == True and not always_delete_fully:
        
        HydrusPaths.RecyclePath( path )
        
    else:
        
        HydrusPaths.DeletePath( path )
        
    
def LaunchPathInWebBrowser( path ):
    
    LaunchURLInWebBrowser( 'file:///' + path )
    
def LaunchURLInWebBrowser( url ):
    
    web_browser_path = HG.client_controller.new_options.GetNoneableString( 'web_browser_path' )
    
    if web_browser_path is None:
        
        webbrowser.open( url )
        
    else:
        
        HydrusPaths.LaunchFile( url, launch_path = web_browser_path )
        
    
