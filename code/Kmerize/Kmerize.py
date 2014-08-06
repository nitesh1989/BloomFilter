__author__ = 'niteshturaga'

import os
os.chdir("/Users/niteshturaga/Documents/BenLangmeadResearch/BloomFilter/data")



def kmerize(filename):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        f = open(filename, 'rb')
        fa = f.readlines()[1:]
        clean = []
        for i in range(len(fa)):
            clean.append(fa[i].strip('\n'))
        clean = "".join(clean)
        f.close()

        #Kmerize
        kmers = ""
        for i, c in enumerate(clean):
            try:
                kmers += clean[i:i+20]
                kmers += "\n"
            except:  # Figure out the excpet statement
                kmers += clean[i:len(clean)]
                break
        fn = filename.replace(".fa","") + "_kmerized.fa"
        with open(fn, 'wb') as out:
            out.write(kmers)
        return

    if filename.endswith(".fastq") or filename.endswith(".fq"):
        return

    return


def main():
    kmerize("chrI_1.fa")
    return

if __name__=="__main__":
    main()