from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction, EntityFormField, BooleanFormField
from rasa_core.events import SlotSet

class ActionListSlots(Action):
    def name(self):
        return 'action_list_slots'

    def run(self, dispatcher, tracker, domain):
        print(dir(dispatcher))
        print(dir(tracker))
        print(dir(domain))
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

# Dispatcher
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_fill_template_text', '_template_variables', 'domain', 'latest_bot_messages', 'output_channel', 'retrieve_template', 'send_messages', 'sender_id', 'utter_attachment', 'utter_button_message', 'utter_button_template', 'utter_custom_message', 'utter_message', 'utter_response', 'utter_template']
# Tracker
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_create_events', '_max_event_history', '_merge_slots', '_paused', '_reset', '_reset_slots', '_set_slot', 'applied_events', 'as_dialogue', 'clear_follow_up_action', 'copy', 'current_slot_values', 'current_state', 'events', 'events_after_latest_restart', 'export_stories', 'export_stories_to_file', 'follow_up_action', 'from_dict', 'generate_all_prior_trackers', 'get_latest_entity_values', 'get_slot', 'idx_after_latest_restart', 'init_copy', 'is_paused', 'latest_action_name', 'latest_bot_utterance', 'latest_message', 'recreate_from_dialogue', 'replay_events', 'sender_id', 'slots', 'travel_back_in_time', 'trigger_follow_up_action', 'update']
# Domain
# ['DEFAULT_ACTIONS', '__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_action_classes', '_action_names', '_actions', '_entities', '_factory_name', '_intents', '_lazy_actions', '_lazy_entities', '_lazy_entity_states', '_lazy_input_state_map', '_lazy_input_states', '_lazy_intent_states', '_lazy_intents', '_lazy_num_actions', '_lazy_prev_action_states', '_lazy_slot_states', '_lazy_slots', '_raise_action_not_found_exception', '_slot_definitions', '_slots', '_templates', 'action_for_index', 'action_for_name', 'action_map', 'action_names', 'actions', 'collect_slots', 'collect_templates', 'compare_with_specification', 'entities', 'entity_states', 'get_active_states', 'get_parsing_states', 'get_prev_action_states', 'index_for_action', 'index_of_state', 'input_state_map', 'input_states', 'instantiate_actions', 'intent_states', 'intents', 'load', 'load_specification', 'num_actions', 'num_states', 'persist', 'persist_specification', 'prev_action_states', 'random_template_for', 'restart_intent', 'slot_states', 'slots', 'slots_for_entities', 'states_for_tracker_history', 'store_entities_as_slots', 'templates', 'validate_domain_yaml']
