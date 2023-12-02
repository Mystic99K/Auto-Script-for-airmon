# import os
# output = os.popen('sudo intel_gpu_top').read()
# print(output)



# import subprocess
# process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
# out, err = process.communicate()
# print(out)


# import subprocess
# command = ['sudo', 'intel_gpu_top']
# process = subprocess.Popen(command, stdout=subprocess.PIPE)
# output, error = process.communicate()
# print(output)
   
# import subprocess
# subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'sudo intel_gpu_top; exec bash'])





# import subprocess
# import time

# # Open a new terminal and execute command
# p = subprocess.Popen(['sudo', 'bash', '-c', 'iwconfig'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p.communicate(b'3542\n')

# # Wait for 5 seconds
# time.sleep(2)

# p.communicate(b'q')

# # Get the output
# output, error = p.communicate()

# # Decode the output and error
# output = output.decode('utf-8')
# error = error.decode('utf-8')

# # Print the output
# print("Output:", output)
# print("Error:", error)




# import subprocess
# import time


# p = subprocess.Popen(['speedtest'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p.communicate(b'3542\n')
# output, errors = p.communicate()
# out = output.decode('utf-8')


# print(out)








from subprocess import Popen, PIPE
import time

# Start the process
p = Popen(['neofetch'], stdin=PIPE)
# Wait for a while for the process to do its work
time.sleep(5)

# Send 'q' to the stdin of the process
p.communicate(input='q')
