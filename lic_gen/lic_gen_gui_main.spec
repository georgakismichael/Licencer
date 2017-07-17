# -*- mode: python -*-

block_cipher = None


a = Analysis(['lic_gen_gui_main.py'],
             pathex=['C:\\Python27\\Lib\\site-packages\\netifaces-0.10.6.dist-info', 'D:\\My Documents\\Incoming\\py\\lic_gen'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='lic_gen_gui_main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
