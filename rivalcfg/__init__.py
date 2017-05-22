import collections

from . import usbhid
from .version import VERSION
from .profiles import mice_profiles


MouseInfo = collections.namedtuple(
        "MouseInfo", ("name", "vendor_id", "product_id"))


def list_supported_mice():
    """Returns the list of all mice supported by this software."""
    return (MouseInfo(
            name=profile["name"],
            vendor_id=profile["vendor_id"],
            product_id=profile["product_id"],
        ) for profile in mice_profiles)


def list_available_mice():
    """Return the list of supported mice currently availale (plugged to the
    computer)."""
    for mouse in list_supported_mice():
        if usbhid.is_device_plugged(mouse.vendor_id, mouse.product_id):
            yield mouse


def get_mouse_profile(vendor_id, product_id):
    """Returns the profile (informations and list of available commands) of the
    given mouse.

    Arguments:
    vendor_id -- The vendor id (currenlty this should be set to 0x1038)
    product_id -- The product id of the mouse (e.g. 0x1710 for the Rival 300)
    """
    for profile in mice_profiles:
        if profile["vendor_id"] == vendor_id and profile["product_id"] == product_id:
            return profile
    return None


def get_mouse(vendor_id, product_id):
    """Returns a class that allows you to manipulaite the given mouse if it is
    available, else returns None.

    Arguments:
    vendor_id -- The vendor id (currenlty this should be set to 0x1038)
    product_id -- The product id of the mouse (e.g. 0x1710 for the Rival 300)
    """
    raise NotImplementedError()
