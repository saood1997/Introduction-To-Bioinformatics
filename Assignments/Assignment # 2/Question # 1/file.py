def read_Gen_File():
        Gen = []
        with open("File.txt", 'r') as file:
            seq = file.readline()
            Gen = seq.upper()
        return Gen

def Remove_Introns(seq,splicing_list):
    list_seq = []
    Seq = ""
    removedLen = 0
    for i in range(len(seq)):
        if(i>=int(splicing_list[0]) and i<=int(splicing_list[1])):
            continue
        Seq += seq[i]
    list_seq = Seq;
    return list_seq

def Transcription(Gen_Seq):
    
        RNA = ""
        for i in Gen_Seq:
            if i == "A":
                RNA += "U"
            elif i == "C":
                RNA += "G"
            elif i == "G":
                RNA += "C"
            elif i == "T":
                RNA += "A"
        
        return RNA

def Translation(RNA):
        flag = False
        proteins = []
        temp = ""
        Len_RNA = len(RNA)
        Table = {
                    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", 
                    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                    "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
                    "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
                    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", 
        }
            
        for i in range(0,len(RNA), 3):
            codon = RNA[i:i+3]

            if len(codon) < 3:
                continue

            if codon == "AUG":
                flag = True

            if flag == True:
                aminoAcid = Table[codon]
                temp += aminoAcid

                if aminoAcid == "STOP":
                    flag = False
                    proteins.append(temp)
                    temp = ""
        
        return proteins
    
splicing_list = []
Gen_Seq = read_Gen_File()
print(len(Gen_Seq))
ini_val = input("Enter initial position of intron:")
splicing_list.append(ini_val)
final_val = input("Enter final position of intron")
splicing_list.append(final_val)
print(splicing_list)
Remove_Introns(Gen_Seq,splicing_list)
RNA = Transcription(Gen_Seq)
protein = Translation(RNA)
print(protein)

