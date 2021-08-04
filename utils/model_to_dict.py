
from django.db.models import ForeignKey

def query_to_list(query, fields_to_ignore=[]):
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

def get_withheld_amount(salary):
    fed = 0
    ss = 0
    medicare = 0

    ss = .062 * min(128000, salary)
    medicare = .0145 * salary

    if salary > 523601:
        fed = (salary - 523601) * .37 + 995 + 3668.88 + 10086.78 + 18851.76 + 14239.68 + 109960.90
    elif salary > 209425:
        fed = (salary - 209425) * .35 + 995 + 3668.88 + 10086.78 + 18851.76 + 14239.68
    elif salary > 164925:
        fed = (salary - 164925) * .32 + 995 + 3668.88 + 10086.78 + 18851.76
    elif salary > 86375:
        fed = (salary - 86375) * .24 + 995 + 3668.88 + 10086.78
    elif salary > 40525:
        fed = (salary - 40525) * .22 + 995 + 3668.88
    elif salary > 9950:
        fed = (salary - 9950) * .12 + 995
    else:
        fed = salary * .1

    return fed/12, ss/12, medicare/12