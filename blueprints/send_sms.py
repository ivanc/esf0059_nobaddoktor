from flask import Blueprint
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from twilio.rest import Client
import os
from flask import request

send_sms_bp = Blueprint("send", __name__,
                        template_folder='templates',
                        url_prefix="/send")

@send_sms_bp.route('/sms', methods=('GET', 'POST'))
def auth_sms():
        # set up Twilio account data (client) as anvironment variables
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        # set up Twilio account data (verify) as anvironment variables
        verify_sid = os.getenv("TWILIO_VERIFY_SID")
        ## TODO prenderlo dall'utente!!!!!! TODO
        verified_number = os.getenv("TWILIO_PHONE_NUMBER")
        # Twilio client
        client = Client(account_sid, auth_token)
        if request.method == 'GET':
        # 2 steps verification via SMS
                verification = client.verify.v2.services(verify_sid) \
                        .verifications \
                        .create(to=verified_number, channel="sms")
                        ## still have to edit 'to=user number', get it from db user
                return render_template('send/sms.html')
        else:
        
        # questa informazione dobbiamo ritornarla a chi ce l'ho chiede
        # da aggiungere ...        
        # OTP verification
                otp_code = request.form['otp_code'].strip()        
                verification_check = client.verify.v2.services(verify_sid) \
                        .verification_checks \
                        .create(to=verified_number, code=otp_code)
                return redirect(url_for("user.dashboard"))
