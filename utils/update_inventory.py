from django.contrib import messages

def add_inventory(inventory, part, cost, quant):
    try:
        part_in_inventory = inventory.objects.get(part=part)

        part_in_inventory.cost += cost * quant
        part_in_inventory.quant += quant
        part_in_inventory.save()

    except:
        part_in_inventory = inventory()
        part_in_inventory.part = part
        part_in_inventory.cost = cost * quant
        part_in_inventory.quant = quant
        part_in_inventory.save()

def sub_inventory(inventory, part, cost, quant, request):
    try:
        part_in_inventory = inventory.objects.get(part=part)
        
    except:
        messages.error(request, f'No {part} in inventory')
        return False

    # part_in_inventory.cost += cost * quant
    # part_in_inventory.quant += quant
    # part_in_inventory.save()

    # except:
    #     part_in_inventory = inventory()
    #     part_in_inventory.part = part
    #     part_in_inventory.cost = cost * quant
    #     part_in_inventory.quant = quant
    #     part_in_inventory.save()
