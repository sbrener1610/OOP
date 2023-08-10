class CheckParity:

    def __init__(self, *args):
        #print(args[0])
        if isinstance(args[0],int):
            self.number = args[0]
            if len(args)>1:
                self.parity = args[1]
            else:
                self.parity = None
        else:
            self.number = None

    def isOdd(self):
        if self.number != None:
            if self.number%2==0:
                return False
            elif self.number%2==1:
                return True
        else:
           return "Error"
        
    def isEven(self):
        if self.number != None:
            if self.number%2!=0:
                return False
            elif self.number%2==0:
                return True
        else:
            return "Error"

    def getParity(self):
        if self.number != None:
            if self.parity=="odd":
                if self.number%2==1:
                    return True
                elif self.number%2==0:
                    return False
            elif self.parity=="even":
                if self.number%2==0:
                    return True
                elif self.number%2==1:
                    return False
            else:
                return "Parity indicated is unknown or abscent"
        else:
            return "Not an integer" 
        
a=CheckParity(3)
b=CheckParity(4,"odd")
c=CheckParity(3.45)

print(a.isOdd())
print(b.isOdd())
print(b.getParity())
print(c.isOdd())