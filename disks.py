import subprocess
import logging

def format(
    device_name: str,
    mode: str,
    partion_start: list,
    partion_end: list,
    fs_type: list,
) -> "bool":
    status = True
    if mode == "GPT":
        command = f"/usr/bin/parted -s {device_name} mklabel gpt"
        status = subprocess.check_call(command)
		for start,end,fs in partion_start,partion_end,fs_type: 
			pass
    elif mode == "MBR":
        command = f"/usr/bin/parted -s {device_name} mklabel gpt"
        status = subprocess.check_call(command)
	else:
		logging.error("Unknown partition layout")
		return False
    return status
