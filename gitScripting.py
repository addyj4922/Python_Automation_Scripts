import os
from datetime import datetime as dt
counter = 0
flag = 0
pull_counter=0
date_Time = dt.now()
#print(date_Time)
#print("Previous working Directory : {0}".format(os.getcwd()))
#os.chdir('d:')
f = open("gitlogs.txt","w+")
log_File_Path = "gitlogs.txt"
print("GitLogs file is created in: {0}".format(os.getcwd()))
#os.chdir('UIProject_OH')
print("Present working directory : {0}".format(os.getcwd()))
###check for status###
status = os.popen("git status")

f.write("----------------------------------------------------------\n")
f.write("GIT STATUS:\n")
f.write(date_Time.strftime("%m/%d/%Y, %H:%M:%S:%f")+"\n\n")
status = os.popen('git status')
f.write(status.read())
f.write("\n----------------------------------------------------------\n")
f.close()
Text = "Changes not staged for commit:"
fileR = open(log_File_Path,"r")
status_data = fileR.read()
if Text in status_data:
    print("\nThere are pending changes, Now going to stash the changes\n")
    flag = 1
else:
    print("There are no pending changes, Ready to Pull...")
    flag = 0
fileR.close()
if flag == 1:
    ###Stash the changes###
    stash = os.popen("git stash")
    stash_data = stash.read()
    stashed_Text = "Saved working directory"
    if stashed_Text in stash_data:
        print("Stashed\n")
        file_Stash = open(log_File_Path,"a+")
        file_Stash.write("\nGIT STASH:\n")
        #print("\nSTASH: \n {0}".format(file_Stash.read()))
        file_Stash.write(stash.read())
        file_Stash.write("\n----------------------------------------------------------\n")
        file_Stash.close()
        ###check for status again###
        status1 = os.popen('git status')
        status1_data = status1.read()
        #print (status1.read())
        status1_Text = "working tree clean"
        if status1_Text in status1_data:
            print("Working tree is clean, \nReady to Pull...\n")
            GitPull()
        else :
            print("Error, Please proceed manually\n")
    else :
        print("Not Stashed, Please proceed masnually\n")
else :
    print("Ready to Pull...\n")
    GitPull()


def GitPull():
    file_pull = open(log_File_Path,"a+")
    pull = os.popen('git pull')
    file_pull.write("\n----------------------------------------------------------\n")
    file_pull.write("GIT PULL:\n")
    file_pull.write(pull.read())
    print("Pull Successfull\n")
    print("Restoring Stashed Data\n")
    os.popen('git stash pop')
    print("Stashed data restored, You can now proceed...!\n")
    exit()

exit()

#os.system('cmd /k "git status"')
