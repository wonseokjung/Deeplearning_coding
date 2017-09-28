import os
import time


source=['/home/wonseok/Desktop/NeuralNetwork']
target_dir=['/home/wonseok/Desktop/python/back_up']

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command="zip -r {0} {1}".format(target, ' '.join(source))

print(zip_command)

print("running")

if os.system(zip_command)==0:
    print("success",target)
else:
    print("backup faile")
