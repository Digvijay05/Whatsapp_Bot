import alright

contacts = ["+916351753750"]
whatsapp = alright.WhatsApp()

def greeting():
    msg = """*નમસ્કાર જાદવ કમ્પ્યુટર સેંટર નો સહાયક બોટ આપનું સ્વાગત કરે છે.*\nતમે નીચે મુજબ લીસ્ટ ના દ્વારા chat કરી શકશો."""
    reply_list = ["લેપટોપ","૧૦ પાસ જાહેરાત","૧૨ પાસ જાહેરાત","કેન્દ્ર જાહેરાત","રાજ્ય સરકાર જાહેરાત","ગ્રેજયુએટ જાહેરાત","બઁક જાહેરાત","GEB લગતા કામ"]
    count = 1
    for i in reply_list:
        msg += "\n" + str(count) + ") " + i
        count+=1

    msg += "\n\n ઉપર મુજબ નંબર સેન્ડ કરો."
    return msg
whatsapp.find_user(contacts[0])
whatsapp.send_message(greeting())
whatsapp.wait_until_message_successfully_sent()

# to do
# 1) wait until user replies functionality


laptop_list = ["5000 - 10000","10000 - 15000","15000 - 20000","20000 - 25000","25000+"]
geb_list = ["ઘર માટે", "ખેતી માટે", "વ્યવસાય માટે"]
geb_work_list = ["નામ ફેરફાર", "લોડ વધારો/ઘટાડો", "નવું કનેક્શન"]


