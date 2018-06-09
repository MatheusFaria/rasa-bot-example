from rasa_core.actions.forms import FormAction, EntityFormField, BooleanFormField
from rasa_core.events import SlotSet

class ActionDriverLicenseForm(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("car_model", "car_model_slot"),
            BooleanFormField("has_driver_license_slot", "affirm", "deny")
        ]

    def name(self):
        return 'action_driver_license_form'

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('car_model: {} has_driver_license: {}'.format(
            tracker.get_slot("car_model_slot"),
            tracker.get_slot("has_driver_license_slot"))
        )
        print('=' * 80)
        return []
