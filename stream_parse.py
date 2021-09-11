#################################################################
#################################################################
## string format in number of characters                       ##
## 2-2-4-9-10-4-1-1-1-3-2-2                                    ##
## eg:  0121E38200000000001A3C20C8231xxU1YK109E7E              ##
## eg:  01-21-E382-000000000-01A3C20C82-31xx-U-1-Y-K10-9E-7E   ##
#################################################################
#################################################################

def parse_string(str1):
    str1=str(str1)

    dict1={
        "Syntax Version":" ",
        "Length":"",
        "CRC":"",
        "Subscriber ID":"",
        "CDSN":"",
        "STB Model":"",
        "LNB Model":"",
        "No. Of Tuners":"",
        "Tuner Status":"",
        "TP Name":"",
        "Signal Level":"",
        "Signal Quality":""
    }
    try:

        dict1["Syntax Version"]=str1[0:2]  
        dict1["Length"]=str1[2:4]
        dict1["CRC"]=str1[4:8] + " - CRC is calculated using IBM3470 algorithm"
        subsID = str1[8:17]
        subsID=int(subsID,16)
        dict1["Subscriber ID"]=subsID
        cdsn = str1[17:27]
        cdsn=int(cdsn,16)
        dict1["CDSN"]=cdsn
        dict1["STB Model"]=str1[27:31]
        lnbM = str1[31:32]
        if lnbM == "U":
            dict1["LNB Model"]="Universal LNB"
        else:
            dict1["LNB Model"]="Super LNB"
        Tnum=str1[32:33]
        Tnum=int(Tnum,16)
        dict1["No. Of Tuners"]=Tnum
        dict1["Tuner Status"]=str1[33:34]
        dict1["TP Name"]=str1[34:37]
        sL = str1[37:39]
        sL = int(sL,16)
        dict1["Signal Level"]=sL
        sT = str1[39::]
        sT = int(sT,16)
        dict1["Signal Quality"]=sT
    except:
        pass
    return dict1

# string1 = "01217c880075bcd1501a3c20a5931xxS1YK09a569"
# x=parse_string(string1)
# print(x)