#Example of Net-BIOS crafted packet with scapy.
sr1(IP(dst='10.0.0.1') /
       UDP(sport=RandShort()) /
       NBNSQueryRequest(NAME_TRN_ID=0x8228, QUESTION_NAME= '*', QUESTION_TYPE='NBSTAT'))
