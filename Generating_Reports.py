
#!/usr/bin/env python3

import os, sys
from PIL import Image

user = os.getenv('USER') # To get the username from environment variable
image_directory = '/home/supplier-data/iamges/'.format(user)
for image_name in os.listdir(image_directory):
   if not image_name.startswith('.') and 'tiff' in image_name:
       image_path = image_directory + image_name
       path = os.path.splitext(image_path)[0]
       im = image.open(image_path)
       new_path = '{}.jepg'.format(path)
       im.convert('RGB').resize((600, 400).save(new_path, "JPEG")



#Below is working script for "Working with supplier images
#In this section, you will write a Python script named changeImage.py to process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

#Size: Change image resolution from 3000x2000 to 600x400 pixel
#Format: Change image format from .TIFF to .JPEG


#!/usr/bin/env python3
from os import listdir, path
from PIL import Image

# set image dir:
img_dir = "supplier-data/images/"

# set reprocess vars:
rx_size = (600, 400)
rx_frmt = "JPEG"

# gather list of image files:
img_files = [f for f in listdir(img_dir) if f.endswith(".tiff")]

# reprocess images:
for file in img_files:
    src_img = Image.open(img_dir + file)
    new_img = src_img.resize(rx_size)
    # NOTE: we need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")
    file, ext = path.splitext(file)
    file += ".jpeg"
    new_img.save(img_dir + file, rx_frmt)
    
    
#Uploading images to web server
#You have modified the fruit images through changeImage.py script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the [linux-instance-IP-Address]/upload URL.

#Copy the external IP address of your instance from the Connection Details Panel on the left side and enter the IP address in a new web browser tab. This opens a web page displaying the text "Fruit Catalog".
#In the home directory, you'll have a script named example_upload.py to upload images to the running fruit catalog web server. To view the example_upload.py script use the cat command.

#Example script is below:

#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})



#Script for uploading images to webserver


#!/usr/bin/env python3
import requests
from os import listdir

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"


def upload(file, url):
    with open(file, "rb") as opened:
        requests.post(url, files={"file": opened})


# set image dir:
img_dir = "supplier-data/images/"

# gather list of image files:
img_files = [img_dir + f for f in listdir(img_dir) if f.endswith(".jpeg")]
for file in img_files:
    upload(file, url)
    
    
    
#Uploading the descriptions
#The Django server is already set up to show the fruit catalog for your company. 
#You can visit the main website by entering linux-instance-IP-Address in the URL bar or by removing /media/images from the existing URL opened earlier. The interface looks like this:

#!/usr/bin/env python3
from os import listdir, path
from unicodedata import normalize
import requests
import json

# set text dir:
txt_dir = "supplier-data/descriptions/"

# gather list of text files:
text_files = [txt_dir + f for f in listdir(txt_dir) if f.endswith(".txt")]

# read text entry:
def getEntry(file):
    # get entry id & set image file name:
    entry_id = path.splitext(path.basename(file))[0]
    img_name = entry_id + ".jpeg"

    # read lines in file, assign to vars:
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name, weight, description = lines

    # reformat weight to integer:
    weight = int(weight.replace(" lbs", ""))

    # set & return entry object:
    keys = ["name", "weight", "description", "image_name"]
    vals = [name, weight, description, img_name]
    entry = dict(zip(keys, vals))
    return entry


url = "http://localhost/fruits/"
for file in text_files:
    data = getEntry(file)
    response = requests.post(url, data=data)
    if response.ok:
        print("uploaded data")
    else:
        print(f"error: {response.status_code}")
        
        
#Generate a PDF report and send it through email
#Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. 
#To generate PDF reports, you can use the ReportLab library. The content of the report should look like this

#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info])
    
    
#Report_email.py

#!/usr/bin/env python3
import os
import datetime
import reports
import emails


# read text entry:
def getDesc(file):
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)


def main():
    # set text dir & gather files:
    txt_dir = "supplier-data/descriptions/"
    txt_files = [txt_dir + f for f in os.listdir(txt_dir) if f.endswith(".txt")]

    # set report file:
    report_file = "/tmp/processed.pdf"

    # generate report body:
    report_body = ""
    for file in txt_files:
        report_body += getDesc(file)

    # set report title:
    today = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(
        today.strftime("%B"), today.day, today.year
    )

    # generate report file:
    reports.generate_report(report_file, report_title, report_body)

    # generate & send email report:
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": report_file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)


if __name__ == "__main__":
    main()
    
    
#Health check py.script


#Health check
#This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

#Report an error if CPU usage is over 80%
#Report an error if available disk space is lower than 20%
#Report an error if available memory is less than 500MB
#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"



#!/usr/bin/env python3
import psutil
import socket
import emails

# set system thresholds:
max_cpu_usage_perc = 80
max_disk_avail_perc = 20
max_mem_avail_mb = 500
chk_local_host_ip = "127.0.0.1"


def chkCPU():
    """check if CPU usage % exceeds max threshold"""
    cpu_usage_perc = psutil.cpu_percent(interval=3)
    return cpu_usage_perc > max_cpu_usage_perc


def chkDisk():
    """check if Disk usage exceeds max threshold"""
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    return dsk_usage_perc > max_disk_usage_perc


def chkMem():
    """check if Memory usage % exceeds max threshold"""
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_mem_avail_mb
    mem_avail = psutil.virtual_memory().available
    return mem_avail < max_mem_avail


def chkNet():
    """check if local host name resolves to local IP"""
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != chk_local_host_ip


def sendAlert(alert):
    """output alert error and send email"""
    content = {
        "sender": "automation@example.com",
        "receiver": "student@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    try:
        message = emails.generate_email(**content)
        emails.send_email(message)
    except:
        print("unable to send alert email notification!")
    finally:
        print(alert)
        exit(1)


def main():
    # check system resources:
    print("checking system resources")
    alert = None
    if chkCPU():
        alert = f"Error - CPU usage is over {max_cpu_usage_perc}%"
    elif chkDisk():
        alert = f"Error - Available disk space is less than {max_disk_avail_perc}%"
    elif chkMem():
        alert = f"Error - Available memory is less than {max_mem_avail_mb}MB"
    elif chkNet():
        alert = f"Error - localhost cannot be resolved to {chk_local_host_ip}"

    # alert if error raised:
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()
    
    
