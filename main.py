import subprocess

p = subprocess.Popen(['sudo', 'bash', '-c', 'iwconfig | grep IEEE'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate(b'3542\n')
output, errors = p.communicate()
out = output.decode('utf-8')


net_con_name = out.split('\n')[0].split('      ')[0]


print(net_con_name)













# print('Errors:', errors.decode('utf-8'))
