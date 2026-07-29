import os
import datetime
import psutil
import sys
import smtplib
from email.message import EmailMessage

def send_mail(sender, app_password, receiver, subject, body,attachment_path):
    try:
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.set_content(body)

# Attach file only if a valid path is provided
        if attachment_path:
            if os.path.isfile(attachment_path):

                with open(attachment_path, "rb") as file:
                    file_data = file.read()
                    file_name = os.path.basename(attachment_path)

                msg.add_attachment(file_data,
                                   maintype="application",
                                   subtype="octet-stream",
                                   filename=file_name)

                print("Attachment Added :", file_name)

            else:

                print("\nAttachment file not found.")
                print("Sending email without attachment.")

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(sender, app_password)
        smtp.send_message(msg)
        smtp.quit()

    except Exception as e:
        print("Error : ",e)

def CreateLog(directory):

    filename = "Assignment_34_4_ProcessLog.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        file.write("=" * 70 + "\n")
        file.write("Running Process Information\n")
        file.write("=" * 70 + "\n")

    return filepath


def WriteLog(filepath, message):
    with open(filepath, "a") as file:
        file.write(message + "\n")

def ProcessInformation(logfile):
    count = 0
    header = "{:<10}{:<35}{}".format("PID",
                                     "Process Name",
                                     "Username")

    WriteLog(logfile, header)
    WriteLog(logfile, "-" * 70)

    for process in psutil.process_iter(['pid',
                                        'name',
                                        'username']):

        try:
            pid = process.info['pid']
            name = process.info['name']
            username = process.info['username']
            data = "{:<10}{:<35}{}".format(pid,
                                           str(name),
                                           str(username))

            WriteLog(logfile, data)
            count += 1

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):

            continue

    WriteLog(logfile, "-" * 70)
    WriteLog(logfile, "Total Running Processes : {}".format(count))


def Help():

    print("""
-----------------------------------------------------------------

Execute the script in below shown format.

python Assignment34_4.py DirectoryNamewithPath RecieverEmailID

-----------------------------------------------------------------
""")


def main():

    if len(sys.argv) != 3:
        Help()
        return

    if sys.argv[1] in ("-h", "--help"):
        Help()
        return

    directory = sys.argv[1]

    if not os.path.exists(directory):
        print("Directory does not exist")
        os.mkdir(directory)
        print(f"\nNew Directory {directory} created.")
    else:
        print(f"\nDirectory {directory} already exists.")

    try:
        logfile = CreateLog(directory)
        ProcessInformation(logfile)
        print("\nLog File Created Successfully")

        print("\nLog file path is : ",logfile)

        sender_email = "Marvellous.MithileshSutrave@gmail.com"
        app_password = "oaqa vrin rqly mbfw"
        receiver_email = sys.argv[2]
        subject = "Mail from Python Script"

        body = """
                    Jay Ganesh,
                    
                    Attached is the log file generated for all the current running procesess.
                    
                    Regards,
                    Mithilesh Marvellous
                
                """
        attachment = logfile

        if attachment == "":
            attachment = None

        send_mail(sender_email, app_password, receiver_email, subject, body,attachment)

        if attachment:
            print("\nMail Sent Successfully.")
        else:
            print("\nMail sent Successfully without any attachment.")

    except Exception as eobj:
        print("Error: ",eobj)


if __name__ == "__main__":

    main()