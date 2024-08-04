def lengthOfLastWord(self, s: str) -> int:
        mylist1 = s.split(" ")
        mylist2= []
        for element in mylist1:
            if element != "":
                element = len(element)
                mylist2.append(element)
        
        return mylist2[-1]