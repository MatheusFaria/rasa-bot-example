from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction, EntityFormField, BooleanFormField, FreeTextFormField
from rasa_core.events import SlotSet

class ActionListSlots(Action):
    def name(self):
        return 'action_list_slots'

    def run(self, dispatcher, tracker, domain):
        for key in tracker.slots:
            dispatcher.utter_message(
                "{}: {}".format(key, tracker.slots[key].value)
            )
        return []

class ActionDriverLicenseForm(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("car_model", "car_model_slot"),
            FreeTextFormField("zipcode_slot"),
            BooleanFormField("has_driver_license_slot", "affirm", "deny"),
        ]

    def name(self):
        return 'action_driver_license_form'

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Submitting Form...')
        dispatcher.utter_message(
            'car_model: {} has_driver_license: {} zipcode: {}'.format(
                tracker.get_slot("car_model_slot"),
                tracker.get_slot("has_driver_license_slot"),
                tracker.get_slot("zipcode_slot"),
            )
        )

        return []

