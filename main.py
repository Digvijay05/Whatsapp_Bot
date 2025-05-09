import alright

contacts = ["916351753750", "919427214492", "919824983757"]
whatsapp = alright.WhatsApp()

for i in contacts:
    whatsapp.find_user(i)
    whatsapp.send_message("TEST MESSAGE")
    whatsapp.send_message("TEST MESSAGE")
    whatsapp.send_message("TEST MESSAGE")

