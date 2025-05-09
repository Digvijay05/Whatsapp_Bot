import os
import time
import sqlite3
import pywhatkit
from pywhatkit.core.core import check_number
from pywhatkit.core.log import format_message


def log_message(_time: time.struct_time, receiver: str, message: str) -> None:
    """Logs the Message Information after it is Sent"""

    if not os.path.exists("PyWhatKit_DB.db"):
        file = open("PyWhatKit_DB.db", "w+")
        file.close()

    message = format_message(message)

    conn = sqlite3.connect("PyWhatKit_DB.db")
    cursor = conn.cursor()

    sql_command = """CREATE TABLE IF NOT EXISTS WHATSAPP_MSGS(
                        Time TIMESTAMP,
                        Phone_Number VARCHAR(20),
                        Message
                        )
                    """
    message_log = """INSERT INTO WHATSAPP_MSGS VALUES (?,?,?)"""
    values = (f"{_time.tm_mday}/{_time.tm_mon}/{_time.tm_year} {_time.tm_hour}:{_time.tm_min}"
                  ,f"{receiver}",f"{message}")
    cursor.execute(sql_command)
    cursor.execute(message_log, values)
    conn.commit()
    cursor.close()
    conn.close()



    with open("PyWhatKit_DB.txt", "a", encoding="utf-8") as file:
        if check_number(receiver):
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Phone Number: {receiver}\nMessage: {message}"
            )
        else:
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}\nMessage: {message}"
            )
        file.write("\n--------------------\n")
        file.close()


pywhatkit.whats.sendwhatmsg_instantly("+916351753750","TEST MESSAGE")