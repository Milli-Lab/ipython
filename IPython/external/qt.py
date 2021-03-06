""" A Qt API selector that can be used to switch between PyQt and PySide.
"""

import os

# Available APIs.
QT_API_PYQT = 'pyqt'
QT_API_PYSIDE = 'pyside'

# Use PyQt by default until PySide is stable.
QT_API = os.environ.get('QT_API', QT_API_PYQT)

if QT_API == QT_API_PYQT:
    # For PySide compatibility, use the new-style string API that automatically
    # converts QStrings to Unicode Python strings. Also, automatically unpack
    # QVariants to their underlying objects.
    import sip
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)

    from PyQt4 import QtCore, QtGui, QtSvg

    # Alias PyQt-specific functions for PySide compatibility.
    QtCore.Signal = QtCore.pyqtSignal
    QtCore.Slot = QtCore.pyqtSlot

elif QT_API == QT_API_PYSIDE:
    from PySide import QtCore, QtGui, QtSvg

else:
    raise RuntimeError('Invalid Qt API %r, valid values are: %r or %r' % 
                       (QT_API, QT_API_PYQT, QT_API_PYSIDE))
