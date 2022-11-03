import subprocess
import inquirer
import qrcode

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
ssid = inquirer.prompt([inquirer.List('ssid', message="Choose an SSID", choices=profiles)])['ssid']
results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode('utf-8').split('\n')
results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
password = results[0] if results else ''

qr = qrcode.QRCode()
qr.add_data(f'WIFI:S:{ssid};T:WPA;P:{password};;')
qr.print_ascii()

print(f'    {ssid}\n    {password}\n\n')

input()