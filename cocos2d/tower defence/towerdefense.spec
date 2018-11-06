# -*- mode: python -*-

block_cipher = None


a = Analysis(['towerdefense.py'],
             pathex=['C:\\Users\\Nurlybek\\Desktop\\python-projects\\cocos2d\\tower defence'],
             binaries=[],
             datas=[
                 ('assets/*.png', 'assets'),
                 ('assets/*.ttf', 'assets'),
                 ('assets/*.tmx', 'assets'),
             ],
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
          name='towerdefense',
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
               name='towerdefense')
