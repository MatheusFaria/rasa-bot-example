## path1
* greet
  - utter_greet
  - action_driver_license_form
  - slot{"requested_slot": "car_model_slot"}
* inform_car_model
  - action_driver_license_form
  - slot{"car_model_slot": "civic"}
  - slot{"requested_slot": "has_driver_license_slot"}
* affirm
  - slot{"has_driver_license_slot": true}
  - utter_list_slots
* bye
  - utter_bye

## path2
* greet
  - utter_greet
  - action_driver_license_form
  - slot{"requested_slot": "car_model_slot"}
* inform_car_model
  - action_driver_license_form
  - slot{"car_model_slot": "civic"}
  - slot{"requested_slot": "has_driver_license_slot"}
* deny
  - slot{"has_driver_license_slot": false}
  - utter_list_slots
* bye
  - utter_bye
