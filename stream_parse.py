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
        dict1["CRC"]=str1[4:8]
        dict1["Subscriber ID"]=str1[8:17]
        dict1["CDSN"]=str1[17:27]
        dict1["STB Model"]=str1[27:31]
        dict1["LNB Model"]=str1[31:32]
        dict1["No. Of Tuners"]=str1[32:33]
        dict1["Tuner Status"]=str1[33:34]
        dict1["TP Name"]=str1[34:37]
        dict1["Signal Level"]=str1[37:39]
        dict1["Signal Quality"]=str1[39::]
    except:
        pass
    return dict1

# string1 = "01217c880075bcd1501a3c20a5931xxS1YK09a569"
# x=parse_string(string1)
# print(x)