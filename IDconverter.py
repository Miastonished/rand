from datetime import datetime
while 1:    
    try:
        a = (((int(input("Paste Snowflake ID: ").split()[0]) >> 22) + 1420070400000) / 1000)
        print(datetime.utcfromtimestamp(a).strftime("%Y-%m-%d %H:%M:%S")+"\n<t:"+((str(a)).split("."))[0]+":F>"+"\n"+(str(a * 1000)).split(".")[0])
    except:
        print("Error, use numbers or something idfk")
#made by will914 :sunglasses_emoji~102:
