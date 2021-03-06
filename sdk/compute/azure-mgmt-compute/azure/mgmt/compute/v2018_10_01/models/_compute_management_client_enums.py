# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AvailabilitySetSkuTypes(str, Enum):
    """Specifies the sku of an Availability Set. Use 'Aligned' for virtual machines with managed disks
    and 'Classic' for virtual machines with unmanaged disks. Default value is 'Classic'.
    """

    classic = "Classic"
    aligned = "Aligned"

class CachingTypes(str, Enum):
    """Specifies the caching requirements. :code:`<br>`:code:`<br>` Possible values are:
    :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>` **ReadOnly**
    :code:`<br>`:code:`<br>` **ReadWrite** :code:`<br>`:code:`<br>` Default: **None for Standard
    storage. ReadOnly for Premium storage**
    """

    none = "None"
    read_only = "ReadOnly"
    read_write = "ReadWrite"

class DiskCreateOptionTypes(str, Enum):
    """Specifies how the virtual machine should be created.:code:`<br>`:code:`<br>` Possible values
    are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is used when you are using a
    specialized disk to create the virtual machine.:code:`<br>`:code:`<br>` **FromImage** \u2013
    This value is used when you are using an image to create the virtual machine. If you are using
    a platform image, you also use the imageReference element described above. If you are using a
    marketplace image, you  also use the plan element previously described.
    """

    from_image = "FromImage"
    empty = "Empty"
    attach = "Attach"

class IntervalInMins(str, Enum):
    """Interval value in minutes used to create LogAnalytics call rate logs.
    """

    three_mins = "ThreeMins"
    five_mins = "FiveMins"
    thirty_mins = "ThirtyMins"
    sixty_mins = "SixtyMins"

class IPVersion(str, Enum):
    """Available from Api-Version 2017-03-30 onwards, it represents whether the specific
    ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: 'IPv4' and
    'IPv6'.
    """

    i_pv4 = "IPv4"
    i_pv6 = "IPv6"

class MaintenanceOperationResultCodeTypes(str, Enum):
    """The Last Maintenance Operation Result Code.
    """

    none = "None"
    retry_later = "RetryLater"
    maintenance_aborted = "MaintenanceAborted"
    maintenance_completed = "MaintenanceCompleted"

class OperatingSystemStateTypes(str, Enum):
    """The OS State.
    """

    generalized = "Generalized"
    specialized = "Specialized"

class OperatingSystemTypes(str, Enum):
    """The operating system of the osDiskImage.
    """

    windows = "Windows"
    linux = "Linux"

class ProtocolTypes(str, Enum):
    """Specifies the protocol of listener. :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`\
    **http** :code:`<br>`:code:`<br>` **https**
    """

    http = "Http"
    https = "Https"

class ProximityPlacementGroupType(str, Enum):
    """Specifies the type of the proximity placement group. :code:`<br>`:code:`<br>` Possible values
    are: :code:`<br>`:code:`<br>` **Standard** : Co-locate resources within an Azure region or
    Availability Zone. :code:`<br>`:code:`<br>` **Ultra** : For future use.
    """

    standard = "Standard"
    ultra = "Ultra"

class ResourceIdentityType(str, Enum):
    """The type of identity used for the virtual machine. The type 'SystemAssigned, UserAssigned'
    includes both an implicitly created identity and a set of user assigned identities. The type
    'None' will remove any identities from the virtual machine.
    """

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"

class RollingUpgradeActionType(str, Enum):
    """The last action performed on the rolling upgrade.
    """

    start = "Start"
    cancel = "Cancel"

class RollingUpgradeStatusCode(str, Enum):
    """Code indicating the current status of the upgrade.
    """

    rolling_forward = "RollingForward"
    cancelled = "Cancelled"
    completed = "Completed"
    faulted = "Faulted"

class SettingNames(str, Enum):
    """Specifies the name of the setting to which the content applies. Possible values are:
    FirstLogonCommands and AutoLogon.
    """

    auto_logon = "AutoLogon"
    first_logon_commands = "FirstLogonCommands"

class StatusLevelTypes(str, Enum):
    """The level code.
    """

    info = "Info"
    warning = "Warning"
    error = "Error"

class StorageAccountTypes(str, Enum):
    """Specifies the storage account type for the managed disk. Managed OS disk storage account type
    can only be set when you create the scale set. NOTE: UltraSSD_LRS can only be used with data
    disks, it cannot be used with OS Disk.
    """

    standard_lrs = "Standard_LRS"
    premium_lrs = "Premium_LRS"
    standard_ssd_lrs = "StandardSSD_LRS"
    ultra_ssd_lrs = "UltraSSD_LRS"

class UpgradeMode(str, Enum):
    """Specifies the mode of an upgrade to virtual machines in the scale set.:code:`<br />`:code:`<br
    />` Possible values are::code:`<br />`:code:`<br />` **Manual** - You  control the application
    of updates to virtual machines in the scale set. You do this by using the manualUpgrade
    action.:code:`<br />`:code:`<br />` **Automatic** - All virtual machines in the scale set are
    automatically updated at the same time.
    """

    automatic = "Automatic"
    manual = "Manual"
    rolling = "Rolling"

class UpgradeOperationInvoker(str, Enum):
    """Invoker of the Upgrade Operation
    """

    unknown = "Unknown"
    user = "User"
    platform = "Platform"

class UpgradeState(str, Enum):
    """Code indicating the current status of the upgrade.
    """

    rolling_forward = "RollingForward"
    cancelled = "Cancelled"
    completed = "Completed"
    faulted = "Faulted"

class VirtualMachineEvictionPolicyTypes(str, Enum):
    """Specifies the eviction policy for virtual machines in a low priority scale set.
    :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
    """

    deallocate = "Deallocate"
    delete = "Delete"

class VirtualMachinePriorityTypes(str, Enum):
    """Specifies the priority for the virtual machines in the scale set.
    :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
    """

    regular = "Regular"
    low = "Low"

class VirtualMachineScaleSetSkuScaleType(str, Enum):
    """The scale type applicable to the sku.
    """

    automatic = "Automatic"
    none = "None"

class VirtualMachineSizeTypes(str, Enum):
    """Specifies the size of the virtual machine. For more information about virtual machine sizes,
    see `Sizes for virtual machines <https://docs.microsoft.com/azure/virtual-machines/virtual-
    machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
    :code:`<br>`:code:`<br>` The available VM sizes depend on region and availability set. For a
    list of available sizes use these APIs:  :code:`<br>`:code:`<br>` `List all available virtual
    machine sizes in an availability set
    <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes in a region
    <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes for resizing
    <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
    """

    basic_a0 = "Basic_A0"
    basic_a1 = "Basic_A1"
    basic_a2 = "Basic_A2"
    basic_a3 = "Basic_A3"
    basic_a4 = "Basic_A4"
    standard_a0 = "Standard_A0"
    standard_a1 = "Standard_A1"
    standard_a2 = "Standard_A2"
    standard_a3 = "Standard_A3"
    standard_a4 = "Standard_A4"
    standard_a5 = "Standard_A5"
    standard_a6 = "Standard_A6"
    standard_a7 = "Standard_A7"
    standard_a8 = "Standard_A8"
    standard_a9 = "Standard_A9"
    standard_a10 = "Standard_A10"
    standard_a11 = "Standard_A11"
    standard_a1_v2 = "Standard_A1_v2"
    standard_a2_v2 = "Standard_A2_v2"
    standard_a4_v2 = "Standard_A4_v2"
    standard_a8_v2 = "Standard_A8_v2"
    standard_a2_m_v2 = "Standard_A2m_v2"
    standard_a4_m_v2 = "Standard_A4m_v2"
    standard_a8_m_v2 = "Standard_A8m_v2"
    standard_b1_s = "Standard_B1s"
    standard_b1_ms = "Standard_B1ms"
    standard_b2_s = "Standard_B2s"
    standard_b2_ms = "Standard_B2ms"
    standard_b4_ms = "Standard_B4ms"
    standard_b8_ms = "Standard_B8ms"
    standard_d1 = "Standard_D1"
    standard_d2 = "Standard_D2"
    standard_d3 = "Standard_D3"
    standard_d4 = "Standard_D4"
    standard_d11 = "Standard_D11"
    standard_d12 = "Standard_D12"
    standard_d13 = "Standard_D13"
    standard_d14 = "Standard_D14"
    standard_d1_v2 = "Standard_D1_v2"
    standard_d2_v2 = "Standard_D2_v2"
    standard_d3_v2 = "Standard_D3_v2"
    standard_d4_v2 = "Standard_D4_v2"
    standard_d5_v2 = "Standard_D5_v2"
    standard_d2_v3 = "Standard_D2_v3"
    standard_d4_v3 = "Standard_D4_v3"
    standard_d8_v3 = "Standard_D8_v3"
    standard_d16_v3 = "Standard_D16_v3"
    standard_d32_v3 = "Standard_D32_v3"
    standard_d64_v3 = "Standard_D64_v3"
    standard_d2_s_v3 = "Standard_D2s_v3"
    standard_d4_s_v3 = "Standard_D4s_v3"
    standard_d8_s_v3 = "Standard_D8s_v3"
    standard_d16_s_v3 = "Standard_D16s_v3"
    standard_d32_s_v3 = "Standard_D32s_v3"
    standard_d64_s_v3 = "Standard_D64s_v3"
    standard_d11_v2 = "Standard_D11_v2"
    standard_d12_v2 = "Standard_D12_v2"
    standard_d13_v2 = "Standard_D13_v2"
    standard_d14_v2 = "Standard_D14_v2"
    standard_d15_v2 = "Standard_D15_v2"
    standard_ds1 = "Standard_DS1"
    standard_ds2 = "Standard_DS2"
    standard_ds3 = "Standard_DS3"
    standard_ds4 = "Standard_DS4"
    standard_ds11 = "Standard_DS11"
    standard_ds12 = "Standard_DS12"
    standard_ds13 = "Standard_DS13"
    standard_ds14 = "Standard_DS14"
    standard_ds1_v2 = "Standard_DS1_v2"
    standard_ds2_v2 = "Standard_DS2_v2"
    standard_ds3_v2 = "Standard_DS3_v2"
    standard_ds4_v2 = "Standard_DS4_v2"
    standard_ds5_v2 = "Standard_DS5_v2"
    standard_ds11_v2 = "Standard_DS11_v2"
    standard_ds12_v2 = "Standard_DS12_v2"
    standard_ds13_v2 = "Standard_DS13_v2"
    standard_ds14_v2 = "Standard_DS14_v2"
    standard_ds15_v2 = "Standard_DS15_v2"
    standard_ds13_4_v2 = "Standard_DS13-4_v2"
    standard_ds13_2_v2 = "Standard_DS13-2_v2"
    standard_ds14_8_v2 = "Standard_DS14-8_v2"
    standard_ds14_4_v2 = "Standard_DS14-4_v2"
    standard_e2_v3 = "Standard_E2_v3"
    standard_e4_v3 = "Standard_E4_v3"
    standard_e8_v3 = "Standard_E8_v3"
    standard_e16_v3 = "Standard_E16_v3"
    standard_e32_v3 = "Standard_E32_v3"
    standard_e64_v3 = "Standard_E64_v3"
    standard_e2_s_v3 = "Standard_E2s_v3"
    standard_e4_s_v3 = "Standard_E4s_v3"
    standard_e8_s_v3 = "Standard_E8s_v3"
    standard_e16_s_v3 = "Standard_E16s_v3"
    standard_e32_s_v3 = "Standard_E32s_v3"
    standard_e64_s_v3 = "Standard_E64s_v3"
    standard_e32_16_v3 = "Standard_E32-16_v3"
    standard_e32_8_s_v3 = "Standard_E32-8s_v3"
    standard_e64_32_s_v3 = "Standard_E64-32s_v3"
    standard_e64_16_s_v3 = "Standard_E64-16s_v3"
    standard_f1 = "Standard_F1"
    standard_f2 = "Standard_F2"
    standard_f4 = "Standard_F4"
    standard_f8 = "Standard_F8"
    standard_f16 = "Standard_F16"
    standard_f1_s = "Standard_F1s"
    standard_f2_s = "Standard_F2s"
    standard_f4_s = "Standard_F4s"
    standard_f8_s = "Standard_F8s"
    standard_f16_s = "Standard_F16s"
    standard_f2_s_v2 = "Standard_F2s_v2"
    standard_f4_s_v2 = "Standard_F4s_v2"
    standard_f8_s_v2 = "Standard_F8s_v2"
    standard_f16_s_v2 = "Standard_F16s_v2"
    standard_f32_s_v2 = "Standard_F32s_v2"
    standard_f64_s_v2 = "Standard_F64s_v2"
    standard_f72_s_v2 = "Standard_F72s_v2"
    standard_g1 = "Standard_G1"
    standard_g2 = "Standard_G2"
    standard_g3 = "Standard_G3"
    standard_g4 = "Standard_G4"
    standard_g5 = "Standard_G5"
    standard_gs1 = "Standard_GS1"
    standard_gs2 = "Standard_GS2"
    standard_gs3 = "Standard_GS3"
    standard_gs4 = "Standard_GS4"
    standard_gs5 = "Standard_GS5"
    standard_gs4_8 = "Standard_GS4-8"
    standard_gs4_4 = "Standard_GS4-4"
    standard_gs5_16 = "Standard_GS5-16"
    standard_gs5_8 = "Standard_GS5-8"
    standard_h8 = "Standard_H8"
    standard_h16 = "Standard_H16"
    standard_h8_m = "Standard_H8m"
    standard_h16_m = "Standard_H16m"
    standard_h16_r = "Standard_H16r"
    standard_h16_mr = "Standard_H16mr"
    standard_l4_s = "Standard_L4s"
    standard_l8_s = "Standard_L8s"
    standard_l16_s = "Standard_L16s"
    standard_l32_s = "Standard_L32s"
    standard_m64_s = "Standard_M64s"
    standard_m64_ms = "Standard_M64ms"
    standard_m128_s = "Standard_M128s"
    standard_m128_ms = "Standard_M128ms"
    standard_m64_32_ms = "Standard_M64-32ms"
    standard_m64_16_ms = "Standard_M64-16ms"
    standard_m128_64_ms = "Standard_M128-64ms"
    standard_m128_32_ms = "Standard_M128-32ms"
    standard_nc6 = "Standard_NC6"
    standard_nc12 = "Standard_NC12"
    standard_nc24 = "Standard_NC24"
    standard_nc24_r = "Standard_NC24r"
    standard_nc6_s_v2 = "Standard_NC6s_v2"
    standard_nc12_s_v2 = "Standard_NC12s_v2"
    standard_nc24_s_v2 = "Standard_NC24s_v2"
    standard_nc24_rs_v2 = "Standard_NC24rs_v2"
    standard_nc6_s_v3 = "Standard_NC6s_v3"
    standard_nc12_s_v3 = "Standard_NC12s_v3"
    standard_nc24_s_v3 = "Standard_NC24s_v3"
    standard_nc24_rs_v3 = "Standard_NC24rs_v3"
    standard_nd6_s = "Standard_ND6s"
    standard_nd12_s = "Standard_ND12s"
    standard_nd24_s = "Standard_ND24s"
    standard_nd24_rs = "Standard_ND24rs"
    standard_nv6 = "Standard_NV6"
    standard_nv12 = "Standard_NV12"
    standard_nv24 = "Standard_NV24"
