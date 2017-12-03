#import library for the use of images
import Image
 
#Method that creates dictionary from Life facts
def LifeDictionary(path_name):
        try:
            myFile = open(path_name, 'r')
        except:
            print "File open error!"
             
        lifeDict = {}
        for line in myFile:
            x = line.split(",")
            a = x[0]
            b = x[1]
            c = len(b)-1
            b = b[0:c]
            lifeDict[a] = b
         
        return lifeDict
 
#Method that creates dictionary from Historic facts     
def HistoryDictionary(path_name):
        try:
            myFile = open(path_name, 'r')
        except:
            print "File open error!"
             
        historyDict = {}
        for line in myFile:
            x = line.split(",")
            a = x[0]
            b = x[1]
            c = len(b)-1
            b = b[0:c]
            historyDict[a] = b
         
        return historyDict
         
def main():
    #Data members to open text files
    filename1 = "Life_Mindblow.txt"
    filename2 = "History_Mindblow.txt"
     
    #Data member to create text file
    reward_file = open('Book of Awe.txt', 'w')
     
    #Data members to store dictionaries 
    L = LifeDictionary(filename1)
    H = HistoryDictionary(filename2)
     
    x = ""
    print "                            BLOW YOUR MIND OUT WITH AWE!\n                        Grab your book of awe when you finish \n"
    while x != "e": 
        x = raw_input("What are you interested in? Type 'Life' or 'History' or 'e' to finish: ")
        if x == "Life":
            x = raw_input("Type a number from 1-10: ")
            fact = Mindblow_Life(x, L)
            print (fact.SearchFact() + "\n")
            fact.SetImage()
             
            lst = fact.BookFile()
            z = str(lst)
            reward_file.write(z + "\n")
                 
        elif x == "History":
            x = raw_input("Type a number from 1-10: ")
            fact = Mindblow_History(x, H)
            print (fact.SearchFact() + "\n")
            fact.SetImage()
             
            lst = fact.BookFile()
            z = str(lst)
            reward_file.write(z + "\n")
     
    reward_file.close()
    print "Your facts have been saved in a book! Congratulations! "
     
#class for mindblowing facts for life
class Mindblow_Life:
    #initializer for the user choice and the specific dictionary 
    def __init__(self, choice, LDict):
        self.choice = choice
        self.LDict = LDict
         
    #method to search for a fact in the specific dictionary
    def SearchFact(self):
        for i in self.choice:
            if self.LDict.has_key(i):
                i = self.LDict[self.choice]
                return i
     
    #method to assign image based on the specific fact
    def SetImage(self):
        for i in self.choice:
            if self.LDict.has_key(i):
                x = self.choice
                image = Image.open('Life'+ x +'.jpg')
                image.show()
     
    #method to store fact in the reward file        
    def BookFile(self):
        Book = []
        Book.append(self.LDict[self.choice])
        return Book
 
#class for mindblowing facts for history
class Mindblow_History:
    #initializer for the user choice and the specific dictionary 
    def __init__(self, choice, HDict):
        self.choice = choice
        self.HDict = HDict
     
    #method to search for a fact in the specific dictionary
    def SearchFact(self):
        for i in self.choice:
            if self.HDict.has_key(i):
                i = self.HDict[self.choice]
                return i
     
    #method to assign image based on the specific fact  
    def SetImage(self):
        for i in self.choice:
            if self.HDict.has_key(i):
                x = self.choice
                image = Image.open('History'+ x +'.jpg')
                image.show()
     
    #method to store fact in the reward file
    def BookFile(self):
        Book = []
        Book.append(self.HDict[self.choice])
        return Book
 
if __name__ == '__main__':
    main() 
