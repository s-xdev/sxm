import colorama
import ctypes
import json
import os

# ! The following is important, and has the strucute for a sxm.config.json file.

# {
#     "StartupCommand" = "code {dir_location}" also only works for people with VSCODE and the VSCODE command installed
# }

class CommandClass:
    def __init__(self):
        self.CommandClassRunning = True
        
        ctypes.windll.kernel32.SetConsoleTitleW("sxm")
        
        colorama.init(autoreset=True)
        
        print(f"{colorama.Style.BRIGHT}{colorama.Fore.LIGHTCYAN_EX}Welcome to I guess sx's custom git proj manager thingy\n")
    
    def StartNewCommandSession(self):
        commandName = input(f'{os.getcwd()}$:> ')
        
        commandRan = False
        commandReturnMessage = ''
        
        if commandName.lower().startswith('open') == True:
            giveUP = False
            
            open_args = commandName.split(' ')
            
            ldata = open_args[1] # get the directory/project info
            
            folder_directory, project_directory = ldata.split(':')[0], ldata.split(':')[1]
            
            joined_directory = f"{os.getcwd()}\\{folder_directory}\\{project_directory}"
            
            if os.path.exists(joined_directory) == False and giveUP == False:
                commandReturnMessage = f'Directory Combination: {ldata} is not found.\n'
                giveUP = True
                
            if os.path.exists(joined_directory + '\\sxm.config.json') == False and giveUP == False:
                commandReturnMessage = f'An sxm.config.json file is not present.\n'
                giveUP = True
                
            if os.path.exists(joined_directory + '\\sxm.config.json'):
                sxmConfigPath = f"{joined_directory}\\sxm.config.json"
            
                sxmConfiguration = open(sxmConfigPath, 'r')
                sxmConfiguration = json.load(sxmConfiguration)
                
                print(sxmConfiguration)
                
                sxmStartupCommand: str = sxmConfiguration['StartupCommand']
                
                sxmStartupCommand = sxmStartupCommand.replace('{dir_location}', joined_directory)
                
                os.system(sxmStartupCommand)
                
                commandReturnMessage = f'Succesfully ran the startup command for: {ldata} '
            
            
            
            commandRan = True
            
            
        
        if commandName.lower() == 'clear':
            os.system('cls'); # just clear terminal
            commandRan = True
            commandReturnMessage = ''
            
        if commandName.lower() == 'exit':
            self.CommandClassRunning = False # make it so it wont run another new command session
        
        if self.CommandClassRunning == True:
            if commandRan == True:
                print(commandReturnMessage)
            else:
                print(f'"{commandName}" is not recognized as a command.\nTry again later.')
            
            self.StartNewCommandSession() # start new command session
        
MyCommandClass = CommandClass();
MyCommandClass.StartNewCommandSession();