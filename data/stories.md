## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## survey happy path
* greet
    - utter_greet
* affirm
    - complaint_form
    - form{"name": "complaint_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_no_worries
    - utter_goodbye

## survey stop
* greet
    - utter_greet
* affirm
    - complaint_form
    - form{"name": "complaint_form"}
* out_of_scope
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye

## survey continue
* greet
    - utter_greet
* affirm
    - complaint_form
    - form{"name": "complaint_form"}
* out_of_scope
    - utter_ask_continue
* affirm
    - complaint_form
    - form{"name": null}
    - utter_slots_values

## no survey
* greet
    - utter_greet
* deny
    - utter_goodbye