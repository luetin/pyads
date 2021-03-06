#!-*- coding: utf-8 -*-
# from .pyads import *
from .structs import AmsAddr, NotificationAttrib

from .ads import open_port, close_port, get_local_address, read_state, \
    write_control, read_device_info, write, read_write, read, \
    read_by_name, write_by_name, add_route, delete_route, \
    add_device_notification, del_device_notification, Connection

from .constants import PLCTYPE_BOOL, PLCTYPE_BYTE, PLCTYPE_DATE, \
    PLCTYPE_DINT, PLCTYPE_DT, PLCTYPE_DWORD, PLCTYPE_INT, PLCTYPE_LREAL, \
    PLCTYPE_REAL, PLCTYPE_SINT, PLCTYPE_STRING, PLCTYPE_TIME, PLCTYPE_TOD, \
    PLCTYPE_UDINT, PLCTYPE_UINT, PLCTYPE_USINT, PLCTYPE_WORD, \
    PLCTYPE_ARR_DINT, PLCTYPE_ARR_INT, PLCTYPE_ARR_LREAL, PLCTYPE_ARR_REAL, \
    PLCTYPE_ARR_SHORT

from .constants import PORT_EVENTLOGGER, PORT_IO, PORT_LOGGER, PORT_NC, \
    PORT_NOCKE, PORT_SCOPE, PORT_SPECIALTASK1, PORT_SPECIALTASK2, PORT_SPS1, \
    PORT_SPS2, PORT_SPS3, PORT_SPS4, PORT_SYSTEMSERVICE

from .constants import INDEXGROUP_MEMORYBYTE, INDEXGROUP_MEMORYBIT, \
    INDEXGROUP_MEMORYSIZE, INDEXGROUP_RETAIN, INDEXGROUP_RETAINSIZE, \
    INDEXGROUP_DATA, INDEXGROUP_DATASIZE

from .constants import ADSSTATE_INVALID, ADSSTATE_IDLE, ADSSTATE_RESET, \
    ADSSTATE_INIT, ADSSTATE_START, ADSSTATE_RUN, ADSSTATE_STOP, \
    ADSSTATE_SAVECFG, ADSSTATE_LOADCFG, ADSSTATE_POWERFAILURE, \
    ADSSTATE_POWERGOOD, ADSSTATE_ERROR, ADSSTATE_SHUTDOWN, ADSSTATE_SUSPEND, \
    ADSSTATE_RESUME, ADSSTATE_CONFIG, ADSSTATE_RECONFIG

from .constants import ADSTRANS_NOTRANS, ADSTRANS_CLIENTCYCLE, \
    ADSTRANS_CLIENT1REQ, ADSTRANS_SERVERCYCLE, ADSTRANS_SERVERONCHA

__version__ = '2.2.0'
