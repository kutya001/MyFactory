from soksfactory.admin_app_reorder import CounterpartyGroup, PersonsGroup, SpecialKeysGroup, FefGroup

def create_admin_reorder(*groups):
    ADMIN_REORDER = []
    for group in groups:
        models_tuple = tuple(f'{group.app_name}.{model}' for model in group.models_list)
        group_data = {
            'app': group.app_name,
            'label': group.group_name,
            'models': models_tuple,
        }
        ADMIN_REORDER.append(group_data)
    return tuple(ADMIN_REORDER)


GROUPS_LIST = create_admin_reorder(CounterpartyGroup, PersonsGroup, SpecialKeysGroup, FefGroup)
