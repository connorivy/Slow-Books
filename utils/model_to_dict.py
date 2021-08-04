
from django.db.models import ForeignKey

def query_to_list(query, fields_to_ignore=None):
    data = []
    for obj in query:
        sub_data = []
        for field in obj._meta.get_fields():
            if field.name in fields_to_ignore:
                continue
            value = field.value_from_object(obj)
            print(field.name)
            if isinstance(field, ForeignKey):
                model = field.remote_field.model
                value = str(model.objects.get(pk=value))
            sub_data.append(value)
            print('value', value)
            print('sub_data', sub_data)
        data.append(sub_data)
    return data

def get_choices_list(model):

    query = model.objects.all()
    ids = [obj.pk for obj in query]
    name = [str(obj) for obj in query]
    list = [( '', 'Choose...')]

    for index in range(len(query)):
        list.append((ids[index],f'{name[index]}'))

    print(model, list)
    return list