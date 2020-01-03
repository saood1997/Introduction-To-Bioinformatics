import string
import re
from itertools import product

def return_seq(val):  #finding permutaion with repetation
    list = []
    str = "";
    for i in product(['A','C','G','T'], repeat = val):
        list.append(str.join(i))
    return list

def substring(No_DNA, DNA_Seq, Length_output_Substring):
    len_Substring = int(Length_output_Substring)
    Sequence = return_seq(len_Substring)
    list1 = DNA_Seq.split(" ")
    list2 = []
    for DNA in Sequence:       #take a one sequence from sequence's(permutaion's)
        count = 0
        for j in list1:       #take a one DNA sequence from given sequences       
            temp = 0
            for x in range(0,len_Substring): #run the loop to length of sequence of perputation
                new_string = list(DNA)
                new_string[x] = '.'
                string = "".join(new_string)
                match = re.search(string,j) #return None if no match using regular expresion ftn search
                if match != None:
                    temp = 1
                    break
            if(temp == 1):
                count+=1
        if(count == int(No_DNA)):
            list2.append(DNA)
    print(".........................")
    print("out put Substrings")
    for i in list2:
        string = ""
        string +=i
        print(string)

No_DNA = input("Enter length for every DNA Sequence between 0 and 9: ")
DNA_Seq = input("Enter DNA Sequences: ")
Length_output_Substring = input("Enter length of output Substring between 0 and 9: ")
substring(No_DNA,DNA_Seq,Length_output_Substring)
