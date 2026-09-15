"""List nearby Pybricks hubs advertising over Bluetooth LE.

Uses bleak, which is already installed as a pybricksdev dependency,
so no extra install is needed inside your project's virtual environment.

Usage:
    python scan_hubs.py
"""

import asyncio

from bleak import BleakScanner

# The BLE service UUID every Pybricks hub advertises.
PYBRICKS_SERVICE_UUID = "c5f50001-8280-46da-89f4-6d8051e4aeef"


async def main():
    print("Scanning for 5 seconds... (make sure each hub is powered on)")
    devices = await BleakScanner.discover(timeout=5.0, return_adv=True)

    found = False
    for device, adv in devices.values():
        if PYBRICKS_SERVICE_UUID in adv.service_uuids:
            found = True
            print(f"  {device.name or '(unnamed hub)':<20}  {device.address}")

    if not found:
        print("No Pybricks hubs found. Check that a hub is on and in range.")


if __name__ == "__main__":
    asyncio.run(main())
