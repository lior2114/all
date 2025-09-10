# -*- mode: python ; coding: utf-8 -*-
# Image Processor Application Spec File
# Created for legitimate image processing software

app_analysis = Analysis(
    ['image_processor_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL._tkinter_finder',
        'PIL.ImageTk',
        'PIL.Image',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.ttk'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter.test', '_tkinter_test'],
    noarchive=False,
    optimize=1,
)

app_pyz = PYZ(app_analysis.pure, app_analysis.zipped_data)

app_exe = EXE(
    app_pyz,
    app_analysis.scripts,
    app_analysis.binaries,
    app_analysis.datas,
    [],
    name='ImageProcessor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    version_info=None
)
