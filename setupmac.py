from distutils.core import setup
import py2app
py2app_options = dict(
    iconfile='nenra.icns',
)
setup(
    app=['nenra.py'],
    data_files=[
      'fatura.png',
      'image.png',
    ],
    options=dict(
      py2app=py2app_options,
    )
)
 