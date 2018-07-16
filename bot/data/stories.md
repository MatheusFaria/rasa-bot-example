## path1
* greet
  - utter_greet
  - action_driver_license_form
  - slot{"requested_slot": "car_model_slot"}
* inform_car_model
  - action_driver_license_form
  - slot{"car_model_slot": "civic"}
  - slot{"requested_slot": "zipcode_slot"}
* inform_zipcode
  - action_driver_license_form
  - slot{"zipcode_slot": "my zipcode is 12345"}
  - slot{"requested_slot": "has_driver_license_slot"}
* affirm
  - slot{"has_driver_license_slot": true}
  - utter_thanks
* bye
  - action_list_slots
  - utter_bye

## path2
* greet
  - utter_greet
  - action_driver_license_form
  - slot{"requested_slot": "car_model_slot"}
* inform_car_model
  - action_driver_license_form
  - slot{"car_model_slot": "civic"}
  - slot{"requested_slot": "zipcode_slot"}
* inform_zipcode
  - action_driver_license_form
  - slot{"zipcode_slot": "my zipcode is 12345"}
  - slot{"requested_slot": "has_driver_license_slot"}
* deny
  - slot{"has_driver_license_slot": false}
  - utter_thanks
* bye
  - action_list_slots
  - utter_bye
