import subprocess
import time


p = subprocess.Popen(['sudo', 'bash', '-c', 'iwconfig | grep IEEE'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate(b'3542\n')
output, errors = p.communicate()
out = output.decode('utf-8')


net_con_name = out.split('\n')[0].split('      ')[0]


print(net_con_name)



# p = subprocess.Popen(['sudo', 'bash', '-c', 'airmon-ng check kill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# output, errors = p.communicate()
# out = output.decode('utf-8')
# print(out)

# print('done')


# p = subprocess.Popen(['sudo', 'bash', '-c', f'airmon start {net_con_name}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# output, errors = p.communicate()
# out = output.decode('utf-8')
# print(out)

# print('done')

time.sleep(2)

p = subprocess.Popen(['sudo', 'bash', '-c', f'sudo airodump-ng -w /var/log/myOutput --output-format csv wlo1mon'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
time.sleep(5)

p.communicate(b'q\n')
time.sleep(0.5)
p.communicate(b'q\n')
time.sleep(0.5)
p.communicate(b'q\n')
time.sleep(0.5)
p.communicate(b'q\n')
time.sleep(0.5)
p.communicate(b'q\n')
time.sleep(0.5)


output, errors = p.communicate()
out = output.decode('utf-8')
print(out)

print('done')



print(errors.decode('utf-8'))
