## path1
* greet
  - action_list_slots
  - utter_greet
  - action_driver_license_form
  - slot{"requested_slot": "car_model_slot"}
* inform_car_model
  - action_driver_license_form
  - slot{"car_model_slot": "civic"}
  - slot{"requested_slot": "has_driver_license_slot"}
* affirm
  - slot{"has_driver_license_slot": true}
  - utter_inform_id
* inform_identification
  - slot{"identification": "xc123"}
* bye
  - action_list_slots
  - utter_bye

## path2
* greet
  - action_list_slots
  - utter_greet
  - action_driver_license_form
  - slot{"requested_slot": "car_model_slot"}
* inform_car_model
  - action_driver_license_form
  - slot{"car_model_slot": "civic"}
  - slot{"requested_slot": "has_driver_license_slot"}
* deny
  - slot{"has_driver_license_slot": true}
  - utter_inform_id
* inform_identification
  - slot{"identification": "xc123"}
* bye
  - action_list_slots
  - utter_bye
