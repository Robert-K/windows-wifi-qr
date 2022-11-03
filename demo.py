import inquirer
import qrcode

ssids = ['Martin Router King', 'Tell my WiFi love her', 'WLAN-1234567890', 'WLAN-0987654321', 'Epstein\'s Guest WiFi', 'FrankBox-P33']
ssid = inquirer.prompt([inquirer.List('ssid', message="Choose an SSID", choices=ssids)])['ssid']
password = '1234567890'

qr = qrcode.QRCode()
qr.add_data(f'WIFI:S:{ssid};T:WPA;P:{password};;')
qr.print_ascii()

print(f'    {ssid}\n    {password}\n\n')

input()