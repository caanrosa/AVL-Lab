from termcolor import colored
from TreeUtils import Node

def printTitle(title, centerNum=64):
    print (colored(f" {title} ".center(centerNum, "⸺"), "red"))
    
def printSubtitle(subtitle, centerNum=64):
    print (colored(f" {subtitle} ".center(centerNum), "light_grey"))
    
def printOption(number, option, colorNumber="red", colorOption="white"):
    op = colored(f" ({number})", colorNumber) + colored(f" {option} ", colorOption)
    
    print (f"{op}".center(80))
    
def printBottom():
    print (colored("".center(64, "⸺"), "red"))
    
def printMovieInfo(node: Node):
    printSubtitle("{title} ({y})".format(title = node.info["Title"], y = node.info["Year"]))
    printSubtitle("🌐 ${world} 📌 ${domestic} 📤 ${foreign}".format(world = node.info["Worldwide Earnings"], domestic = node.info["Domestic Earnings"], foreign = node.info["Foreign Earnings"]))
    printSubtitle("📌 {domestic}% 📤 {foreign}%".format(domestic = node.info["Domestic Percent Earnings"], foreign = node.info["Foreign Percent Earnings"]))
            
    
def getInput() -> str:
    got = ""
    while(len(got) == 0):
        got = input(colored("> ", "green"))
        
    return got

def getInputInt() -> int:
    recieved = ""
    p = False
    
    while(not p):
        recieved = getInput()
        try:
            int(recieved)
            p = True
        except ValueError:
            p = False
    
    return int(recieved)