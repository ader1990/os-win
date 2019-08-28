# Copyright 2017 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from os_win.utils.winapi import wintypes

# Windows.h
# ----------
# winerror.h
ERROR_INVALID_HANDLE = 6
ERROR_NOT_READY = 21
ERROR_SHARING_PAUSED = 70
ERROR_INSUFFICIENT_BUFFER = 122
ERROR_DIR_IS_NOT_EMPTY = 145
ERROR_PIPE_BUSY = 231
ERROR_PIPE_NOT_CONNECTED = 233
ERROR_MORE_DATA = 234
ERROR_WAIT_TIMEOUT = 258
ERROR_IO_PENDING = 997
ERROR_NOT_FOUND = 1168
EPT_S_NOT_REGISTERED = 1753

# Cluster errors
ERROR_DEPENDENCY_NOT_FOUND = 5002
ERROR_RESOURCE_NOT_FOUND = 5007
ERROR_GROUP_NOT_FOUND = 5013
ERROR_CLUSTERLOG_CHKPOINT_NOT_FOUND = 5032
ERROR_CLUSTER_NODE_NOT_FOUND = 5042
ERROR_CLUSTER_LOCAL_NODE_NOT_FOUND = 5043
ERROR_CLUSTER_NETWORK_NOT_FOUND = 5045
ERROR_CLUSTER_NETINTERFACE_NOT_FOUND = 5047
ERROR_CLUSTER_RESOURCE_TYPE_NOT_FOUND = 5078
ERROR_CLUSTER_RESNAME_NOT_FOUND = 5080
ERROR_QUORUM_DISK_NOT_FOUND = 5086
ERROR_CLUSTER_QUORUMLOG_NOT_FOUND = 5891
ERROR_CLUSTER_NETWORK_NOT_FOUND_FOR_IP = 5894

CLUSTER_NOT_FOUND_ERROR_CODES = [
    ERROR_DEPENDENCY_NOT_FOUND, ERROR_RESOURCE_NOT_FOUND,
    ERROR_GROUP_NOT_FOUND, ERROR_CLUSTERLOG_CHKPOINT_NOT_FOUND,
    ERROR_CLUSTER_NODE_NOT_FOUND, ERROR_CLUSTER_LOCAL_NODE_NOT_FOUND,
    ERROR_CLUSTER_NETWORK_NOT_FOUND, ERROR_CLUSTER_NETINTERFACE_NOT_FOUND,
    ERROR_CLUSTER_RESOURCE_TYPE_NOT_FOUND, ERROR_CLUSTER_RESNAME_NOT_FOUND,
    ERROR_QUORUM_DISK_NOT_FOUND, ERROR_CLUSTER_QUORUMLOG_NOT_FOUND,
    ERROR_CLUSTER_NETWORK_NOT_FOUND_FOR_IP,
]

ERROR_INVALID_STATE = 5023
ERROR_VHD_INVALID_TYPE = 0xC03A001B

# winbase.h
WAIT_FAILED = 0xFFFFFFFF

FILE_FLAG_OVERLAPPED = 0x40000000

FORMAT_MESSAGE_FROM_SYSTEM = 0x00001000
FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x00000100
FORMAT_MESSAGE_IGNORE_INSERTS = 0x00000200

JobObjectBasicLimitInformation = 2
JobObjectExtendedLimitInformation = 9

INFINITE = 0xFFFFFFFF  # Infinite timeout

# FileAPI.h
OPEN_EXISTING = 3

INVALID_FILE_ATTRIBUTES = 4294967295

# minwinbase.h
# FILE_INFO_BY_HANDLE_CLASS enum
FileIdInfo = 18

# winnt.h
FILE_ATTRIBUTE_REPARSE_POINT = 0x0400

FILE_SHARE_READ = 1
FILE_SHARE_WRITE = 2
FILE_SHARE_DELETE = 4
GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000

OWNER_SECURITY_INFORMATION = 0x00000001
GROUP_SECURITY_INFORMATION = 0x00000002
DACL_SECURITY_INFORMATION = 0x00000004
SACL_SECURITY_INFORMATION = 0x00000008

# If the following flag is set, all processes associated with
# the job are terminated when the last job handle is closed.
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000

# The following flags specify access rights that may be
# requested when opening proccesses.
#
# Allows setting process limits.
PROCESS_SET_QUOTA = 0x0100
# Allows terminating a process.
PROCESS_TERMINATE = 0x0001
# Allows waiting for a process.
SYNCHRONIZE = 0x00100000

# winioctl.h
FILE_DEVICE_DISK = 7

# handleapi.h
INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value

# minwindef.h
MAX_PATH = 260

# AccCtrl.h
TRUSTEE_IS_NAME = 1
# Indicates a file or directory object.
SE_FILE_OBJECT = 1
# ---------

# ClusApi.h
# ---------
CLUSPROP_SYNTAX_NAME = 262147
CLUSPROP_SYNTAX_ENDMARK = 0
CLUSPROP_SYNTAX_LIST_VALUE_DWORD = 65538
CLUSPROP_SYNTAX_LIST_VALUE_ULARGE_INTEGER = 65542

CLUSAPI_GROUP_MOVE_RETURN_TO_SOURCE_NODE_ON_ERROR = 2
CLUSAPI_GROUP_MOVE_QUEUE_ENABLED = 4
CLUSAPI_GROUP_MOVE_HIGH_PRIORITY_START = 8

CLUSTER_OBJECT_TYPE_GROUP = 2

CLUSTER_CHANGE_GROUP_COMMON_PROPERTY_V2 = 2
CLUSTER_CHANGE_GROUP_STATE_V2 = 8
CLUSTER_CHANGE_GROUP_OWNER_NODE_V2 = 0x00000010

CLUSGRP_STATUS_WAITING_IN_QUEUE_FOR_MOVE = 4

CLUS_RESTYPE_NAME_VM = "Virtual Machine"
CLUS_RESTYPE_NAME_VM_CONFIG = "Virtual Machine Configuration"

CLUSREG_NAME_GRP_TYPE = "GroupType"
CLUSREG_NAME_GRP_STATUS_INFORMATION = 'StatusInformation'

CLUSCTL_GROUP_GET_RO_COMMON_PROPERTIES = 0x3000055

ClusGroupTypeVirtualMachine = 111

CLUSTER_ENUM_NODE = 0x00000001
CLUSTER_ENUM_RESTYPE = 0x00000002
CLUSTER_ENUM_RESOURCE = 0x00000004
CLUSTER_ENUM_GROUP = 0x00000008
CLUSTER_ENUM_NETWORK = 0x00000010
CLUSTER_ENUM_NETINTERFACE = 0x00000020
CLUSTER_ENUM_SHARED_VOLUME_GROUP = 0x20000000
CLUSTER_ENUM_SHARED_VOLUME_RESOURCE = 0x40000000
CLUSTER_ENUM_INTERNAL_NETWORK = 0x80000000

# iscsidsc.h
# ----------
ISCSI_ANY_INITIATOR_PORT = wintypes.ULONG(-1).value
ISCSI_ALL_INITIATOR_PORTS = wintypes.ULONG(-1).value
MAX_ISCSI_PORTAL_NAME_LEN = 256
MAX_ISCSI_PORTAL_ADDRESS_LEN = 256
MAX_ISCSI_NAME_LEN = 223
MAX_ISCSI_HBANAME_LEN = 256

ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED = 2
ISCSI_LOGIN_OPTIONS_USERNAME = 0x00000020
ISCSI_LOGIN_OPTIONS_PASSWORD = 0x00000040
ISCSI_LOGIN_OPTIONS_AUTH_TYPE = 0x00000080

# iscsierr.h
# ----------
ISDSC_NON_SPECIFIC_ERROR = 0xEFFF0001
ISDSC_LOGIN_FAILED = 0xEFFF0002
ISDSC_CONNECTION_FAILED = 0xEFFF0003
ISDSC_INITIATOR_NODE_ALREADY_EXISTS = 0xEFFF0004
ISDSC_INITIATOR_NODE_NOT_FOUND = 0xEFFF0005
ISDSC_TARGET_MOVED_TEMPORARILY = 0xEFFF0006
ISDSC_TARGET_MOVED_PERMANENTLY = 0xEFFF0007
ISDSC_INITIATOR_ERROR = 0xEFFF0008
ISDSC_AUTHENTICATION_FAILURE = 0xEFFF0009
ISDSC_AUTHORIZATION_FAILURE = 0xEFFF000A
ISDSC_NOT_FOUND = 0xEFFF000B
ISDSC_TARGET_REMOVED = 0xEFFF000C
ISDSC_UNSUPPORTED_VERSION = 0xEFFF000D
ISDSC_TOO_MANY_CONNECTIONS = 0xEFFF000E
ISDSC_MISSING_PARAMETER = 0xEFFF000F
ISDSC_CANT_INCLUDE_IN_SESSION = 0xEFFF0010
ISDSC_SESSION_TYPE_NOT_SUPPORTED = 0xEFFF0011
ISDSC_TARGET_ERROR = 0xEFFF0012
ISDSC_SERVICE_UNAVAILABLE = 0xEFFF0013
ISDSC_OUT_OF_RESOURCES = 0xEFFF0014
ISDSC_CONNECTION_ALREADY_EXISTS = 0xEFFF0015
ISDSC_SESSION_ALREADY_EXISTS = 0xEFFF0016
ISDSC_INITIATOR_INSTANCE_NOT_FOUND = 0xEFFF0017
ISDSC_TARGET_ALREADY_EXISTS = 0xEFFF0018
ISDSC_DRIVER_BUG = 0xEFFF0019
ISDSC_INVALID_TEXT_KEY = 0xEFFF001A
ISDSC_INVALID_SENDTARGETS_TEXT = 0xEFFF001B
ISDSC_INVALID_SESSION_ID = 0xEFFF001C
ISDSC_SCSI_REQUEST_FAILED = 0xEFFF001D
ISDSC_TOO_MANY_SESSIONS = 0xEFFF001E
ISDSC_SESSION_BUSY = 0xEFFF001F
ISDSC_TARGET_MAPPING_UNAVAILABLE = 0xEFFF0020
ISDSC_ADDRESS_TYPE_NOT_SUPPORTED = 0xEFFF0021
ISDSC_LOGON_FAILED = 0xEFFF0022
ISDSC_SEND_FAILED = 0xEFFF0023
ISDSC_TRANSPORT_ERROR = 0xEFFF0024
ISDSC_VERSION_MISMATCH = 0xEFFF0025
ISDSC_TARGET_MAPPING_OUT_OF_RANGE = 0xEFFF0026
ISDSC_TARGET_PRESHAREDKEY_UNAVAILABLE = 0xEFFF0027
ISDSC_TARGET_AUTHINFO_UNAVAILABLE = 0xEFFF0028
ISDSC_TARGET_NOT_FOUND = 0xEFFF0029
ISDSC_LOGIN_USER_INFO_BAD = 0xEFFF002A
ISDSC_TARGET_MAPPING_EXISTS = 0xEFFF002B
ISDSC_HBA_SECURITY_CACHE_FULL = 0xEFFF002C
ISDSC_INVALID_PORT_NUMBER = 0xEFFF002D
ISDSC_OPERATION_NOT_ALL_SUCCESS = 0xAFFF002E
ISDSC_HBA_SECURITY_CACHE_NOT_SUPPORTED = 0xEFFF002F
ISDSC_IKE_ID_PAYLOAD_TYPE_NOT_SUPPORTED = 0xEFFF0030
ISDSC_IKE_ID_PAYLOAD_INCORRECT_SIZE = 0xEFFF0031
ISDSC_TARGET_PORTAL_ALREADY_EXISTS = 0xEFFF0032
ISDSC_TARGET_ADDRESS_ALREADY_EXISTS = 0xEFFF0033
ISDSC_NO_AUTH_INFO_AVAILABLE = 0xEFFF0034
ISDSC_NO_TUNNEL_OUTER_MODE_ADDRESS = 0xEFFF0035
ISDSC_CACHE_CORRUPTED = 0xEFFF0036
ISDSC_REQUEST_NOT_SUPPORTED = 0xEFFF0037
ISDSC_TARGET_OUT_OF_RESORCES = 0xEFFF0038
ISDSC_SERVICE_DID_NOT_RESPOND = 0xEFFF0039
ISDSC_ISNS_SERVER_NOT_FOUND = 0xEFFF003A
ISDSC_OPERATION_REQUIRES_REBOOT = 0xAFFF003B
ISDSC_NO_PORTAL_SPECIFIED = 0xEFFF003C
ISDSC_CANT_REMOVE_LAST_CONNECTION = 0xEFFF003D
ISDSC_SERVICE_NOT_RUNNING = 0xEFFF003E
ISDSC_TARGET_ALREADY_LOGGED_IN = 0xEFFF003F
ISDSC_DEVICE_BUSY_ON_SESSION = 0xEFFF0040
ISDSC_COULD_NOT_SAVE_PERSISTENT_LOGIN_DATA = 0xEFFF0041
ISDSC_COULD_NOT_REMOVE_PERSISTENT_LOGIN_DATA = 0xEFFF0042
ISDSC_PORTAL_NOT_FOUND = 0xEFFF0043
ISDSC_INITIATOR_NOT_FOUND = 0xEFFF0044
ISDSC_DISCOVERY_MECHANISM_NOT_FOUND = 0xEFFF0045
ISDSC_IPSEC_NOT_SUPPORTED_ON_OS = 0xEFFF0046
ISDSC_PERSISTENT_LOGIN_TIMEOUT = 0xEFFF0047
ISDSC_SHORT_CHAP_SECRET = 0xAFFF0048
ISDSC_EVALUATION_PEROID_EXPIRED = 0xEFFF0049
ISDSC_INVALID_CHAP_SECRET = 0xEFFF004A
ISDSC_INVALID_TARGET_CHAP_SECRET = 0xEFFF004B
ISDSC_INVALID_INITIATOR_CHAP_SECRET = 0xEFFF004C
ISDSC_INVALID_CHAP_USER_NAME = 0xEFFF004D
ISDSC_INVALID_LOGON_AUTH_TYPE = 0xEFFF004E
ISDSC_INVALID_TARGET_MAPPING = 0xEFFF004F
ISDSC_INVALID_TARGET_ID = 0xEFFF0050
ISDSC_INVALID_ISCSI_NAME = 0xEFFF0051
ISDSC_INCOMPATIBLE_ISNS_VERSION = 0xEFFF0052
ISDSC_FAILED_TO_CONFIGURE_IPSEC = 0xEFFF0053
ISDSC_BUFFER_TOO_SMALL = 0xEFFF0054
ISDSC_INVALID_LOAD_BALANCE_POLICY = 0xEFFF0055
ISDSC_INVALID_PARAMETER = 0xEFFF0056
ISDSC_DUPLICATE_PATH_SPECIFIED = 0xEFFF0057
ISDSC_PATH_COUNT_MISMATCH = 0xEFFF0058
ISDSC_INVALID_PATH_ID = 0xEFFF0059
ISDSC_MULTIPLE_PRIMARY_PATHS_SPECIFIED = 0xEFFF005A
ISDSC_NO_PRIMARY_PATH_SPECIFIED = 0xEFFF005B
ISDSC_DEVICE_ALREADY_PERSISTENTLY_BOUND = 0xEFFF005C
ISDSC_DEVICE_NOT_FOUND = 0xEFFF005D
ISDSC_DEVICE_NOT_ISCSI_OR_PERSISTENT = 0xEFFF005E
ISDSC_DNS_NAME_UNRESOLVED = 0xEFFF005F
ISDSC_NO_CONNECTION_AVAILABLE = 0xEFFF0060
ISDSC_LB_POLICY_NOT_SUPPORTED = 0xEFFF0061
ISDSC_REMOVE_CONNECTION_IN_PROGRESS = 0xEFFF0062
ISDSC_INVALID_CONNECTION_ID = 0xEFFF0063
ISDSC_CANNOT_REMOVE_LEADING_CONNECTION = 0xEFFF0064
ISDSC_RESTRICTED_BY_GROUP_POLICY = 0xEFFF0065
ISDSC_ISNS_FIREWALL_BLOCKED = 0xEFFF0066
ISDSC_FAILURE_TO_PERSIST_LB_POLICY = 0xEFFF0067
ISDSC_INVALID_HOST = 0xEFFF0068


# virtdisk.h
# ----------
VIRTUAL_STORAGE_TYPE_VENDOR_MICROSOFT = wintypes.GUID(
    Data1=0xec984aec,
    Data2=0xa0f9,
    Data3=0x47e9,
    Data4=(wintypes.BYTE * 8)(0x90, 0x1f, 0x71, 0x41,
                              0x5a, 0x66, 0x34, 0x5b))

VIRTUAL_STORAGE_TYPE_DEVICE_ISO = 1
VIRTUAL_STORAGE_TYPE_DEVICE_VHD = 2
VIRTUAL_STORAGE_TYPE_DEVICE_VHDX = 3

VIRTUAL_DISK_ACCESS_NONE = 0
VIRTUAL_DISK_ACCESS_ALL = 0x003f0000
VIRTUAL_DISK_ACCESS_CREATE = 0x00100000
VIRTUAL_DISK_ACCESS_GET_INFO = 0x80000
VIRTUAL_DISK_ACCESS_DETACH = 0x00040000
VIRTUAL_DISK_ACCESS_ATTACH_RO = 0x00010000
VIRTUAL_DISK_ACCESS_ATTACH_RW = 0x00020000

ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY = 0x00000001
ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME = 0x00000004

OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS = 1
OPEN_VIRTUAL_DISK_VERSION_1 = 1
OPEN_VIRTUAL_DISK_VERSION_2 = 2

RESIZE_VIRTUAL_DISK_VERSION_1 = 1

CREATE_VIRTUAL_DISK_VERSION_2 = 2
CREATE_VHD_PARAMS_DEFAULT_BLOCK_SIZE = 0
CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION = 1

MERGE_VIRTUAL_DISK_VERSION_1 = 1

GET_VIRTUAL_DISK_INFO_SIZE = 1
GET_VIRTUAL_DISK_INFO_PARENT_LOCATION = 3
GET_VIRTUAL_DISK_INFO_VIRTUAL_STORAGE_TYPE = 6
GET_VIRTUAL_DISK_INFO_PROVIDER_SUBTYPE = 7
GET_VIRTUAL_DISK_INFO_IS_LOADED = 13

SET_VIRTUAL_DISK_INFO_PARENT_PATH = 1
