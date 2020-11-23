# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['countylookup\\countylookup.py'],
             pathex=['C:\\Users\\Avery\\Desktop\\CountyLookup'],
             binaries=[( '.\\countylookup\\webdriver\\chromedriver.exe', '.\\countylookup\\webdriver\\chromedriver.exe' )],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='countylookup',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='countylookup')
