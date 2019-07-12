import os

print("-" * 32)
print("=" * 10 + " Ping Tool " + "=" * 10)
print("-" * 32)


targets = []  # Array of IP addresses

ip = ''
while True:  # Loop to ask user for IP addresses
    ip = input('Enter an IP (0 to exit): ')
    if ip == '0':
        break
    else:
        targets.append(ip)

for target_ip in targets:  # Loop to ping all IP's in targets[]
    print()
    print("Pinging . . .")
    msg = os.system('ping -c 1 ' + target_ip)
    if msg == 0:
        print(target_ip + ' is UP')
    else:
        print(target_ip + ' is DOWN')
