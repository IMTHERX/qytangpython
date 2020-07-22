# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Python_Simple_SSH_Client.py'],
             pathex=['D:\\2.学习资料\\Python强化班V3\\999.基础跟练\\qytangpython\\1_python_basic_homework\\20200722_14'],
             binaries=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Python_Simple_SSH_Client',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
