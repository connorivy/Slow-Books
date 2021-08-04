from django.contrib import messages
from dashboard.models import product, vendor, invoice, inventory

def add_inventory(inventory, part, cost, quant):
    try:
        part_in_inventory = inventory.objects.get(part=part)
        part_in_inventory.value += cost * quant
        part_in_inventory.quant += quant
        part_in_inventory.save()

    except:
        part_in_inventory = inventory()
        part_in_inventory.part = part
        part_in_inventory.costper = cost
        part_in_inventory.value = cost * quant
        part_in_inventory.quant = quant
        part_in_inventory.save()

def sub_inventory(request):
    inv = invoice.objects.latest('date_added')
    prod = inv.prod
    vendor_ids = prod.part_ids
    quants_in_inventory = prod.part_quants.split('/')
    print('qininve', quants_in_inventory)

    disallowed_characters = "[]'"

    print('1', vendor_ids)
    for character in disallowed_characters:
        vendor_ids = vendor_ids.replace(character, "")
    # vendor_ids.split("'")
    vendor_ids = vendor_ids.split(",")

    print(vendor_ids)
    for index in range(len(vendor_ids)):
        vendor_ids[index] = vendor_ids[index].strip(' ')
        print(vendor_ids[index])
        vendor_entry = vendor.objects.get(pk=vendor_ids[index])
        part_in_inventory = inventory.objects.get(part=vendor_entry.part)

        part_in_inventory.value -= vendor_entry.cost * inv.quant * int(quants_in_inventory[index])
        part_in_inventory.quant -= inv.quant * int(quants_in_inventory[index])
        part_in_inventory.save()