import subprocess as sp
#sp.call(['dir', '/B'], shell = True)
# fire and forget
#sp.call('dir', shell = True)
# check the exit status
#sp.check_call('move a.txt b.txt', shell = True)
#sp.call(r'find "output" *', shell = True)
#result = sp.check_output('find "output" *.py', shell = True)
#print result

#tasks = sp.check_output('tasklist', shell=True)
#print tasks
#tasks_list = tasks.split("\r\n")[3:]
#print tasks_list
#chrome = filter(lambda x : 'chrome' in x, tasks_list)
#chrome = [x for x in tasks_list if 'chrome' in x]
#print chrome
#chrome_pids = map(lambda x : x.split()[1], chrome)
#print chrome_pids
# taskkill /PID 11220 /F
#for pid in chrome_pids:
#    sp.call('taskkill /PID '+ pid +' /F')

with open('numbers.txt') as fh:
    for line in fh:
        p = sp.Popen('python acceptinput.py', stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
        stdout, stderr = p.communicate(line)
        print "STDIN: ", line
        print "STDOUT: ", stdout
        print "STDERR: ", stderr
