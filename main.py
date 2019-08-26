from  flask import Flask,render_template,request,redirect,url_for
from flask_mail import Mail,Message
app = Flask(__name__)

app.secret_key ="123"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'komaljamodkar28@gmail.com'
app.config['MAIL_PASSWORD'] = 'dfgfgjkuznijoifvh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


def  calculate(r1,r2,r3,r4,r5):
    total=0
    total = (r1+r2+r3+r4+r5)
    return total


def  calculate1(r1,r2,r3,r4,r5,r6):
    total=0
    total = (r1+r2+r3+r4+r5+r6)
    return total

def  score1(score):
    if score>20 and score<100:
        message =('Stress Detected is LOW... \nSuggesstions to reduce your stress: \n 1. Give time to think about yourself. \n 2. Be with family and friends and enjoy each moment.\n')

    elif score >=100 and score<250:
        message = ("Stress Detected is MODERATE... \nSuggesstions to reduce your stress:\n 1. Give time to think about yourself.\n 2. Be with family and friends and enjoy each moment.\n 3. Be calm under certain stressful situations.\n 4. Carry meditation regularly.\n")

    elif score >=250 and score <350:
        message = ("Stress Detected is HIGH... \nSuggesstions to reduce your stress:\n 1. Give time to think about yourself.\n 2. Be with family and friends and enjoy each moment.\n 3. Be calm under certain stressful situations.\n 4. Carry meditation regularly.\n 5. Do exercise regularly\n.")


    elif score >=350 and score<450:
        message = ("Stress Detected is VERY HIGH... \nSuggesstions to reduce your stress:\n 1. Give time to think about yourself.\n 2. Be with family and friends and enjoy each moment.\n 3. Be calm under certain stressful situations.\n 4. Carry meditation regularly.\n 5. Do exercise regularly.\n 6. Practise Gratitude.\n 7. Boost up your energy level.\n")

    else:
        message = ("Stress Detected is EXTREMELY HIGH (DANGER)... \nSuggesstions to reduce your stress:\n 1. Give time to think about yourself.\n 2. Be with family and friends and enjoy each moment.\n 3. Be calm under certain stressful situations.\n 4. Carry meditation regularly.\n 5. Do exercise regularly.\n 6. Practise Gratitude.\n 7. Boost up your energy level.\n 8. DO things that makes you feel comformtable.\n")

    return message

def  score2(score):
    if score>20 and score<100:
        message = ("Stress Detected is LOW... \nSuggesstions to reduce your stress:\n 1. Take proper required sleep of 7-8 hours per day.\n 2. Practise meditation.\n")

    elif score >=100 and score<250:
        message = ("Stress Detected is MODERATE... \nSuggesstions to reduce your stress:\n 1. Take proper required sleep of 7-8 hours per day.\n 2. Practise meditation.\n 3. Learn to forgive before going to sleep.\n 4. Organize yourself before sleeping.\n")

    elif score >=250 and score <350:
        message = ("Stress Detected is HIGH... \nSuggesstions to reduce your stress:\n 1. Take proper required sleep of 7-8 hours per day.\n 2. Practise meditation.\n 3. Learn to forgive before going to sleep.\n 4. Organize yourself before sleeping.\n 5. Have a sleep with silent mind.\n")

    elif score >=350 and score<450:
        message = ("Stress Detected is VERY HIGH... \nSuggesstions to reduce your stress:\n 1. Take proper required sleep of 7-8 hours per day.\n 2. Practise meditation. \n 3. Learn to forgive before going to sleep.\n 4. Organize yourself before sleeping.\n 5. Have a sleep with silent mind.\n 6. Avoid consuming sleep pills.")
    else:
        message = ("Stress Detected is EXTREMELY HIGH (DANGER)... \nSuggesstions to reduce your stress:\n 1. Take proper required sleep of 7-8 hours per day\n 2. Practise meditation.\n 3. Learn to forgive before going to sleep.\n 4. Organize yourself before sleeping.\n 5. Have a sleep with silent mind.\n 6. Avoid consuming sleep pills.\n 7. Not to overthink about any stressful conditions.\n")

    return message

def  score3(score):
    if score>20 and score<100:
        message = ("Stress Detected is LOW... \nSuggesstions to reduce your stress:\n 1. Try to behave properly with everyone.\n 2. Meditate regularly.\n")

    elif score >=100 and score<250:
        message = ("Stress Detected is MODERATE...\nSuggesstions to reduce your stress:\n 1. Try to behave properly with everyone.\n 2. Meditate regularly.\n 3. Make yourself busy.")

    elif score >=250 and score <350:
        message = ("Stress Detected is HIGH...\nSuggesstions to reduce your stress:\n 1. Try to behave properly with everyone.\n 2. Meditate regularly.\n 3. Make yourself busy.\n 4. Do not overthink.\n 5. Trust others.")

    elif score >=350 and score<450:
        message = ("Stress Detected is VERY HIGH...\nSuggesstions to reduce your stress:\n 1. Try to behave properly with everyone.\n 2. Meditate regularly.\n 3. Make yourself busy.\n 4. Do not overthink.\n 5. Trust others.\n 6. Learn to forgive.\n 7. Organize yourself.\n")

    else:
        message = ("Stress Detected is EXTREMELY HIGH(DANGER)...\nSuggesstions to reduce your stress:\n 1. Try to behave properly with everyone.\n 2. Meditate regularly.\n 3. Make yourself busy.\n 4. Do not overthink\n 5. Trust others.\n 6. Learn to forgive.\n 7. Keep the sense of humor.\n 8. Avoid consumption of alcohol and drugs.\n 9. Organize yourself.")

    return message

def  score4(score):
    if score>20 and score<100:
        message = ("Stress Detected is LOW...\n Suggesstions to reduce your stress:\n 1. Try to speak politely.\n 2. Try not to be rude.\n 3. Meditate regularly.")

    elif score >=100 and score<250:
        message = ("Stress Detected is MODERATE...\nSuggesstions to reduce your stress:\n 1. Try to speak politely\n 2. Try not to be rude.\n 3. Meditate regularly.\n 4. Share your feelings.\n 5. Give time to other activities along with regular work.\n")

    elif score >=250 and score <350:
        message = ("Stress Detected is HIGH...\nSuggesstions to reduce your stress:\n 1. Try to speak politely\n 2. Try not to be rude\n 3. Meditate regularly.\n 4. Share your feelings.\n 5. Give time to other activities along with regular work.\n 6. Maintain a proper schedule.\n 7. Give time to people who value you.")

    elif score >=350 and score<450:
        message = ("Stress Detected is VERY HIGH...\nSuggesstions to reduce your stress:\n 1. Try to speak politely.\n 2. Try not to be rude.\n 3. Meditate regularly.\n 4. Share your feelings.\n 5. Give time to other activities along with regular work.\n 6. Maintain a proper schedule.\n 7. Give time to people who value you.\n 8. Have a balanced diet.")

    else:
        message = ("Stress Detected is EXTREMELY HIGH(DANGER)...\nSuggesstions to reduce your stress:\n 1. Try to speak politely.\n 2. Try not to be rude.\n 3. Meditate regularly.\n 4. Share your feelings\n 5. Give time to other activities along with regular work.\n 6. Maintain a proper schedule.\n 7. Give time to people who value you.\n 8. Have a balanced diet.\n 9. Avoid consmption of alcohol, cigarattes and drugs.\n 10. Keep youself entertaining.")

    return message

def  score5(score):
    if score>20 and score<100:
        message = ("Stress Detected is LOW...\nSuggesstions to reduce your stress:\n 1. Prepare a work schedule\n 2. Work according to the schedule.")

    elif score >=100 and score<250:
        message = ("Stress Detected is MODERATE...\nSuggesstions to reduce your stress:\n 1. Prepare a work schedule\n 2. Give proper timing to each task.\n 3. Enjoy accompaning your hobbies.\n 4. Love yourself.\n")

    elif score >=250 and score <350:
        message = ("Stress Detected is HIGH...\nSuggesstions to reduce your stress:n\ 1. Prepare a work schedule.\n 2. Give proper timing to each task.\n 3. Enjoy accompaning your hobbies.\n 4. Love youself.\n5. Avoid much involvement in social media.\n 6. Keep yourself away from people who may produce stress to you.")

    elif score >=350 and score<450:
        message = ("Stress Detected is VERY HIGH...\nSuggesstions to reduce your stress:\n 1. Prepare a work schedule.\n 2. Give proper timing to each task\n 3. Enjoy accompaning your hobbies.\n 4. Love yourself.\n 5. Avoid much involvement in social media.\n 6. Avoid addictive things.\n 7. Have a well and healty diet.\n 8. Keep yourself away from people who may produce stress to you.\n")

    else:
        message = ("Stress Detected is EXTREMELY HIGH(DANGER)...\nSuggesstions to reduce your stress:\n 1. Prepare a work schedule\n 2. Give proper timing to each task.\n 3. Enjoy accompaning your hobbies.\n 4. Love yourself.\n 5. Avoid much involvement in social media.\n 6. Avoid addictive things\n 7. Have a well and healty diet.\n 8. Enjoy special moments with friends and family.\n 9. Keep yourself away from people who may produce stress to you.")

    return message


@app.route('/check', methods=['GET','POST'])
def registeruser():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        reason1= request.form["options"]
        reason2 = request.form["options1"]
        reason3 = request.form["options2"]
        reason4 = request.form["options3"]
        reason5 = request.form["options4"]

        reason11 = request.form["options11"]
        reason12 = request.form["options12"]
        reason13 = request.form["options13"]
        reason14 = request.form["options14"]
        reason15 = request.form["options15"]

        reason16 = request.form["options16"]
        reason17 = request.form["options17"]
        reason18 = request.form["options18"]
        reason19 = request.form["options19"]
        reason20 = request.form["options20"]
        reason21 = request.form["options21"]

        reason22 = request.form["options22"]
        reason23 = request.form["options23"]
        reason24 = request.form["options24"]
        reason25 = request.form["options25"]
        reason26 = request.form["options26"]
        reason27 = request.form["options27"]

        reason29 = request.form["options29"]
        reason30 = request.form["options30"]
        reason31 = request.form["options31"]
        reason32 = request.form["options32"]
        reason33 = request.form["options33"]

        p_score=calculate(int(reason1),int(reason2),int(reason3),int(reason4),int(reason5))
        s_score = calculate(int(reason11), int(reason12), int(reason13), int(reason14), int(reason15))
        e_score = calculate1(int(reason16), int(reason17), int(reason18), int(reason19), int(reason20),int(reason21))
        b_score = calculate1(int(reason22), int(reason23), int(reason24), int(reason25), int(reason26),int(reason27))
        h_score = calculate(int(reason29), int(reason30), int(reason31), int(reason32), int(reason33))

        result1 = score1(p_score)
        result2 = score2(s_score)
        result3 = score3(e_score)
        result4 = score4(b_score)
        result5 = score5(h_score)

        msg = Message("Stress Indicator..!", sender='komaljamodkar28@gmail.com', recipients=[email])

        aa = ("Physical Indicator :%s \nSleep Indicator :%s \nEmotional Indicator :%s \nBehavioral Indicator :%s \nPersonal Habit :%s\n") % (p_score,s_score,e_score,b_score,h_score)
        res=("Suggestion to reduce Stress :\n physical stress : %s \n Sleep stress :%s \nEmotional stress :%s \nBehavioral stress:%s \n Personal stress :%s\n") % (result1,result2,result3,result4,result5)

        msg.body =("Hey %s.. \nYour Score..!!\n %s \n\n %s \n") % (name,aa,res)
        mail.send(msg)

        mess="Thank You..!! For your responce ,please check your email..."
        return render_template("message.html",n=mess,m=name)

    else:
        return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)
