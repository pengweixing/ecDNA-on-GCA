#################################################
#  File Name:vcf2ShatterSeek.py
#  Author: xingpengwei
#  Mail: xingwei421@qq.com
#  Created Time: Fri 05 Jun 2020 03:38:20 PM UTC
#################################################

import sys

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w')
header=["chrom1","start1","end1","chrom2","start2","end2","sv_id","pe_support","strand1","strand2","svclass","svmethod"]
print(*header,sep="\t",file=f2)
for line in f1:
    line = line.strip()
    if not line.startswith("#"):
        line1 = line.split("\t")
        if 'BND' in line1[2]:
            mychr_1 = line1[0]
            start_1 = int(line1[1])
            info = line1[7]
            end_1 = int(info.split(';')[3].split('=')[1])
            mychr_2 = line1[7].split(';')[4].split('=')[1]
            start_2 = int(line1[7].split(";")[5].split('=')[1])
            end_2 = start_2+1
            pe = line1[7].split(';')[7].split('=')[1]
            strand = line1[7].split(';')[8].split('=')[1]
            sv_name = line1[2]
            if strand=="3to3":
                strand1 = '-'
                strand2 = '-'
            if strand=="5to5":
                strand1 = '+'
                strand2 = '+'
            if strand=="5to3":
                strand1 ='+'
                strand2 = '-'
            if strand=="3to5":
                strand1 = '-'
                strand2 = '+'
            print(mychr_1,start_1,end_1,mychr_2,start_2,end_2,sv_name,pe,strand1,strand2,"TRA","DELLY",sep="\t",file=f2)
        elif 'INV' in line1[2]:
            mychr_1 = line1[0]
            start_1 = int(line1[1])
            info = line1[7]
            end_1 = int(info.split(';')[3].split('=')[1])
            pe = line1[7].split(';')[4].split('=')[1]
            strand = line1[7].split(';')[6].split('=')[1]
            sv_name = line1[2]
            mychr_2 = mychr_1
            start_2 = end_1
            end_1  = start_1 + 1
            end_2 = start_2 + 1
            if strand=="3to3":
                strand1 = '-'
                strand2 = '-'
                print(mychr_1,start_1,end_1,mychr_2,start_2,end_2,sv_name,pe,strand1,strand2,"t2tINV","DELLY",sep="\t",file=f2)
            if strand=="5to5":
                strand1 = '+'
                strand2 = '+'
                print(mychr_1,start_1,end_1,mychr_2,start_2,end_2,sv_name,pe,strand1,strand2,"h2hINV","DELLY",sep="\t",file=f2)
        elif 'DUP' in line1[2]:
            mychr_1 = line1[0]
            start_1 = int(line1[1])
            info = line1[7]
            end_1 = int(info.split(';')[3].split('=')[1])
            pe = line1[7].split(';')[4].split('=')[1]
            sv_name = line1[2]
            mychr_2 = mychr_1
            start_2 = end_1
            end_1  = start_1 + 1
            end_2 = start_2 + 1
            strand1 = '-'
            strand2 = '+'
            print(mychr_1,start_1,end_1,mychr_2,start_2,end_2,sv_name,pe,strand1,strand2,"DUP","DELLY",sep="\t",file=f2)
        else:
            mychr_1 = line1[0]
            start_1 = int(line1[1])
            info = line1[7]
            end_1 = int(info.split(';')[3].split('=')[1])
            pe = line1[7].split(';')[4].split('=')[1]
            sv_name = line1[2]
            mychr_2 = mychr_1
            start_2 = end_1
            end_1  = start_1 + 1
            end_2 = start_2 + 1
            strand1 = '-'
            strand2 = '+'
            print(mychr_1,start_1,end_1,mychr_2,start_2,end_2,sv_name,pe,strand1,strand2,"DEL","DELLY",sep="\t",file=f2)
