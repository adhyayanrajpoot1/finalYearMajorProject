from flask import *
import numpy as np
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)
app=Flask(__name__)
@app.route('/')
def main():
    #return " hello"
    return render_template("index.html")
@app.route('/predict',methods=['POST' , 'GET'])
def predict1():
    itching = int(request.form['itching'])
    skin_rash = int(request.form['skin_rash'])
    nodal_skin_eruptions = int(request.form['nodal_skin_eruptions'])
    continuous_sneezing = int(request.form['continuous_sneezing'])
    shivering = int(request.form['shivering'])
    chills = int(request.form['chills'])
    joint_pain = int(request.form['joint_pain'])
    stomach_pain = int(request.form['stomach_pain'])
    acidity = int(request.form['acidity'])
    ulcers_on_tongue = int(request.form['ulcers_on_tongue'])
    muscle_wasting = int(request.form['muscle_wasting'])
    vomiting = int(request.form['vomiting'])
    burning_micturition = int(request.form['burning_micturition'])
    spotting_urination = int(request.form['spotting_urination'])
    fatigue = int(request.form['fatigue'])
    weight_gain = int(request.form['weight_gain'])
    anxiety = int(request.form['anxiety'])
    cold_hands_and_feets = int(request.form['cold_hands_and_feets'])
    mood_swings = int(request.form['mood_swings'])
    weight_loss = int(request.form['weight_loss'])
    restlessness = int(request.form['restlessness'])
    lethargy = int(request.form['lethargy'])
    patches_in_throat = int(request.form['patches_in_throat'])
    irregular_sugar_level = int(request.form['irregular_sugar_level'])
    cough = int(request.form['cough'])
    high_fever = int(request.form['high_fever'])
    sunken_eyes = int(request.form['sunken_eyes'])
    breathlessness = int(request.form['breathlessness'])
    sweating = int(request.form['sweating'])
    dehydration = int(request.form['dehydration'])
    indigestion = int(request.form['indigestion'])
    headache = int(request.form['headache'])
    yellowish_skin = int(request.form['yellowish_skin'])
    dark_urine = int(request.form['dark_urine'])
    nausea = int(request.form['nausea'])
    loss_of_appetite = int(request.form['loss_of_appetite'])
    pain_behind_the_eyes = int(request.form['pain_behind_the_eyes'])
    back_pain = int(request.form['back_pain'])
    constipation = int(request.form['constipation'])
    abdominal_pain = int(request.form['abdominal_pain'])
    diarrhoea = int(request.form['diarrhoea'])
    mild_fever = int(request.form['mild_fever'])
    yellow_urine = int(request.form['yellow_urine'])
    yellowing_of_eyes = int(request.form['yellowing_of_eyes'])
    acute_liver_failure = int(request.form['acute_liver_failure'])
    fluid_overload = int(request.form['fluid_overload'])
    swelling_of_stomach = int(request.form['swelling_of_stomach'])
    swelled_lymph_nodes = int(request.form['swelled_lymph_nodes'])
    malaise = int(request.form['malaise'])
    blurred_and_distorted_vision = int(request.form['blurred_and_distorted_vision'])
    phlegm = int(request.form['phlegm'])
    throat_irritation = int(request.form['throat_irritation'])
    redness_of_eyes = int(request.form['redness_of_eyes'])
    sinus_pressure = int(request.form['sinus_pressure'])
    runny_nose = int(request.form['runny_nose'])
    congestion = int(request.form['congestion'])
    chest_pain = int(request.form['chest_pain'])
    weakness_in_limbs = int(request.form['weakness_in_limbs'])
    fast_heart_rate = int(request.form['fast_heart_rate'])

    pain_during_bowel_movements = int(request.form['pain_during_bowel_movements'])
    pain_in_anal_region = int(request.form['pain_in_anal_region'])
    bloody_stool = int(request.form['bloody_stool'])
    irritation_in_anus = int(request.form['irritation_in_anus'])
    neck_pain = int(request.form['neck_pain'])
    dizziness = int(request.form['dizziness'])
    cramps = int(request.form['cramps'])
    bruising = int(request.form['bruising'])
    obesity = int(request.form['obesity'])
    swollen_legs = int(request.form['swollen_legs'])
    swollen_blood_vessels = int(request.form['swollen_blood_vessels'])
    puffy_face_and_eyes = int(request.form['puffy_face_and_eyes'])
    enlarged_thyroid = int(request.form['enlarged_thyroid'])
    brittle_nails = int(request.form['brittle_nails'])
    swollen_extremeties = int(request.form['swollen_extremeties'])
    excessive_hunger = int(request.form['excessive_hunger'])
    extra_marital_contacts = int(request.form['extra_marital_contacts'])
    drying_and_tingling_lips = int(request.form['drying_and_tingling_lips'])
    slurred_speech = int(request.form['slurred_speech'])
    knee_pain = int(request.form['knee_pain'])
    hip_joint_pain = int(request.form['hip_joint_pain'])
    muscle_weakness = int(request.form['muscle_weakness'])
    stiff_neck = int(request.form['stiff_neck'])
    swelling_joints = int(request.form['swelling_joints'])
    movement_stiffness = int(request.form['movement_stiffness'])
    spinning_movements = int(request.form['spinning_movements'])
    loss_of_balance = int(request.form['loss_of_balance'])
    unsteadiness = int(request.form['unsteadiness'])
    weakness_of_one_body_side = int(request.form['weakness_of_one_body_side'])
    loss_of_smell = int(request.form['loss_of_smell'])
    bladder_discomfort = int(request.form['bladder_discomfort'])
    foul_smell_of_urine = int(request.form['foul_smell_of_urine'])
    continuous_feel_of_urine = int(request.form['continuous_feel_of_urine'])
    passage_of_gases = int(request.form['passage_of_gases'])
    internal_itching = int(request.form['internal_itching'])
    toxic_look = int(request.form['toxic_look_(typhos)'])
    depression = int(request.form['depression'])
    irritability = int(request.form['irritability'])
    muscle_pain = int(request.form['muscle_pain'])
    altered_sensorium = int(request.form['altered_sensorium'])
    red_spots_over_body = int(request.form['red_spots_over_body'])
    belly_pain = int(request.form['belly_pain'])
    abnormal_menstruation = int(request.form['abnormal_menstruation'])
    dischromic = int(request.form['dischromic'])
    watering_from_eyes = int(request.form['watering_from_eyes'])
    increased_appetite = int(request.form['increased_appetite'])
    polyuria = int(request.form['polyuria'])
    family_history = int(request.form['family_history'])
    mucoid_sputum = int(request.form['mucoid_sputum'])
    rusty_sputum = int(request.form['rusty_sputum'])
    lack_of_concentration = int(request.form['lack_of_concentration'])
    visual_disturbances = int(request.form['visual_disturbances'])
    receiving_blood_transfusion = int(request.form['receiving_blood_transfusion'])
    receiving_unsterile_injections = int(request.form['receiving_unsterile_injections'])
    coma = int(request.form['coma'])
    stomach_bleeding = int(request.form['stomach_bleeding'])
    distention_of_abdomen = int(request.form['distention_of_abdomen'])
    history_of_alcohol_consumption = int(request.form['history_of_alcohol_consumption'])
    fluid_overload = int(request.form['fluid_overload.1'])
    blood_in_sputum = int(request.form['blood_in_sputum'])
    prominent_veins_on_calf = int(request.form['prominent_veins_on_calf'])
    palpitations = int(request.form['palpitations'])
    painful_walking = int(request.form['painful_walking'])
    pus_filled_pimples = int(request.form['pus_filled_pimples'])
    blackheads = int(request.form['blackheads'])
    scurring = int(request.form['scurring'])
    skin_peeling = int(request.form['skin_peeling'])
    silver_like_dusting = int(request.form['silver_like_dusting'])
    small_dents_in_nails = int(request.form['small_dents_in_nails'])
    inflammatory_nails = int(request.form['inflammatory_nails'])
    blister = int(request.form['blister'])
    red_sore_around_nose = int(request.form['red_sore_around_nose'])

    yellow_crust_ooze = int(request.form['yellow_crust_ooze'])
    

    lis =  [ itching, skin_rash, nodal_skin_eruptions, continuous_sneezing,
    shivering, chills, joint_pain, stomach_pain, acidity,
    ulcers_on_tongue,
     muscle_wasting, vomiting, burning_micturition,spotting_urination, fatigue, weight_gain, anxiety,
    cold_hands_and_feets, mood_swings, weight_loss, restlessness,
    lethargy, patches_in_throat, irregular_sugar_level, cough, high_fever,
    sunken_eyes, breathlessness, sweating, dehydration, indigestion,
    headache, yellowish_skin, dark_urine, nausea, loss_of_appetite,
    pain_behind_the_eyes, back_pain, constipation, abdominal_pain,
    diarrhoea, mild_fever, yellow_urine, yellowing_of_eyes,
    acute_liver_failure, fluid_overload, swelling_of_stomach,
    swelled_lymph_nodes, malaise, blurred_and_distorted_vision, phlegm,
    throat_irritation, redness_of_eyes, sinus_pressure, runny_nose,
    congestion, chest_pain, weakness_in_limbs, fast_heart_rate,
    pain_during_bowel_movements, pain_in_anal_region, bloody_stool,
    irritation_in_anus, neck_pain, dizziness, cramps, bruising, obesity,
    swollen_legs, swollen_blood_vessels, puffy_face_and_eyes,
    enlarged_thyroid, brittle_nails, swollen_extremeties, excessive_hunger,
    extra_marital_contacts, drying_and_tingling_lips, slurred_speech,
    knee_pain, hip_joint_pain, muscle_weakness, stiff_neck,
    swelling_joints, movement_stiffness, spinning_movements,
    loss_of_balance, unsteadiness, weakness_of_one_body_side, loss_of_smell,
    bladder_discomfort, foul_smell_of_urine, continuous_feel_of_urine,
    passage_of_gases, internal_itching, toxic_look, depression,
    irritability, muscle_pain, altered_sensorium, red_spots_over_body,
    belly_pain, abnormal_menstruation, dischromic,
    watering_from_eyes, increased_appetite, polyuria, family_history,
    mucoid_sputum, rusty_sputum, lack_of_concentration,visual_disturbances,
    receiving_blood_transfusion, receiving_unsterile_injections, coma,
    stomach_bleeding, distention_of_abdomen,history_of_alcohol_consumption,
    fluid_overload,blood_in_sputum, prominent_veins_on_calf, palpitations,
    painful_walking, pus_filled_pimples, blackheads, scurring,
    skin_peeling, silver_like_dusting, small_dents_in_nails,
    inflammatory_nails, blister, red_sore_around_nose, yellow_crust_ooze]

    npar = np.array(lis)
    res1 = model.predict(np.reshape(npar,(-1,132)))
    res1 = encoder.inverse_transform(res1)
    res = f"You are diagnosed with {res1}"
    return render_template('index.html',result = res)



app.run()