class Filtration:
    def __init__(self, fields_to_filter):
        self.fields_to_filter = fields_to_filter

    def get_filter_types(self, items):
        filter_types = {}
        for field, name in self.fields_to_filter.items():
            filter_types[field] = {
                'name': name,
                'options': sorted(list(set([getattr(item, field) for item in items if getattr(item, field)])))
            }
        return filter_types

    @staticmethod
    def filters_from_request(request, filter_types):
        filters = {}
        for index, (field, filter_type) in enumerate(filter_types.items()):
            str_options = [filter_type['options'][int(option)]
                           for option in request.GET.getlist(str(index), '')]
            filters[field] = str_options
        return filters

    @staticmethod
    def filter_items(items, filters):
        filtered_items = []
        for item in items:
            used_filters = 0
            for filter_values in filters.values():
                if filter_values:
                    used_filters += 1

            passed_fields = 0
            for filter_attr, filter_values in filters.items():
                for filter_value in filter_values:
                    if filter_value == getattr(item, filter_attr):
                        passed_fields += 1
                        break

            if passed_fields == used_filters:
                filtered_items.append(item)
        return filtered_items