import logging
import smtplib
from email.message import EmailMessage

logging.basicConfig(level=logging.DEBUG)


def main():
    my_email = 'username@gmail.com'
    password = 'supersecret'

    body = "What is Lorem Ipsum?<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


    msg = EmailMessage()
    msg['Subject'] = 'Test e-mail from python'
    msg['From'] = f"my test script <{my_email}>"
    msg['To'] = 'test@somewhere.com'
    msg.set_content(body)
    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
      <body>
        <h2 style="color:SlateGray;">{msg['Subject']}</h2><p>
        <pre>{body}</pre>
      </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(
            user=my_email,
            password=password
        )

        smtp.send_message(msg)


if __name__ == '__main__':
    main()

# logging.debug(stuff)
