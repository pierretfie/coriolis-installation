from subprocess import run, check_output
from os import chdir
print('**********maina_2024***********')
print('please wait......\n \n \n')
#moving coriolis executables
def move():    
    try:
        # using graal to locate the install folder
        username = check_output(['whoami']).decode('utf-8').strip()
        dir = f'/home/{username}/coriolis-2.x/Linux.SL7_64/Release.Shared/install/bin'
        exdir = check_output(['find',dir,'-name','graal'])
    except Exception as a:
        print(f'an error occurred\n {a}')
        exit()
    else:
       
        #finding the installation dir
        exdir = exdir.decode('utf-8').strip('\n')
        if exdir == '':
            print('graal was not found')
            exit()
        exdir = exdir.split('graal')[0]
        # check files and executables for coriolis
        file_move = check_output(['ls',exdir])
        file_move = file_move.decode('utf-8').splitlines()
        # move into the coriolis bin directory
        chdir(exdir)
        for file in file_move:
            # move files into the /usr/local/bin
            run(['sudo','cp',file,'/usr/local/bin'])
            # move into /usr/local/bin dir
        chdir('/usr/local/bin')
        for file in file_move:
            # make the coriolis execute-files executables
            run(['sudo','chmod','+x',file])
        # print(file_move)
    print('process completed\n try running graal command from any terminal')
move()