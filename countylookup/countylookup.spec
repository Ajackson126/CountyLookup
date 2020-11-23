# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['countylookup.py'],
             pathex=['C:\\Users\\Avery\\Desktop\\CountyLookup\\countylookup'],
             binaries=[('C:\\Users\\Avery\\Desktop\\CountyLookup\\countylookup\\webdriver', '.')],
             datas=[('C:\\Users\\Avery\\Desktop\\CountyLookup\\countylookup\\AddressFileDrop', 'AddressFileDrop'),
             ('C:\\Users\\Avery\\Desktop\\CountyLookup\\countylookup\\ResultFile','ResultFile')],
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
          debug=True,
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
