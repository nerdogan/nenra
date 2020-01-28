# -*- mode: python -*-

block_cipher = None


a = Analysis(['nenra.py'],
             pathex=['C:\\Users\\NAMIK\\PycharmProjects\\nenra'],
             binaries=None,
             datas=None,
             hiddenimports=[
                '',
                '',
                '',
                '',
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=True,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='nenra',
          debug=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               Tree('C:\\Users\\NAMIK\\PycharmProjects\\nenra\\images', prefix='images\\'),
               a.zipfiles,
               a.datas ,
               strip=False,
               upx=True,
               name='nenra')