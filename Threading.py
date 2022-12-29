# single thread
'''
import os #To interact with the under lying Operating System.
import time#Here to calculate the time taken by the process.
import win32api#To Get the all the drives in our system.
start=time.perf_counter()#To start the timer.
def find_files(filename, search_path):
    result = []
    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        #for loop is used to search the files by walking through all the folders of drive
        if filename in files:#here iam sending all the files to filename
            result.append(os.path.join(root, filename))#filename and root will be appended to result list
    return result#returning result
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:#to get all the drives available in our system
    print(find_files("sample.txt", drive))#here iam calling the method called find_files it walks through the all drive and displays that file particular path
finish=time.perf_counter()
print(f"time {finish-start} seconds")'''




# multi threading


'''import os
import concurrent.futures
import time
import win32api
start=time.perf_counter()

availableDrive=win32api.GetLogicalDriveStrings()
#print(availableDrive)
Drives=[drivestr for drivestr in availableDrive.split('\000') if drivestr]

#drives=drives.split('\000')[:-1]
#to find the files in the system
def find_files(filename, search_path):
    result = []
    # Walking top-down through all the folders in drives
    for root, dir, files in os.walk(search_path):
        #checking whether the file matches or not with existing files in the system
        if filename in files:
            result.append(os.path.join(root, filename))     #to append filename and path to a list
    return result

input_file='sample.txt'
#To acheieve multi threading,use concurrency,means parallel execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(find_files,input_file,drive) for drive in Drives]
    print(results)
    for r in concurrent.futures.as_completed(results):
        print(r.result())


finish=time.perf_counter()
print(f"time {finish-start} seconds")


finish = time.perf_counter()

print(f'Finised in {finish - start} seconds')
'''