from django.contrib import messages
from dashboard.models import product, vendor

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

def sub_inventory(inventory, prod, cost, quant, request):
    prod_sold = product.objects.get(id=prod)
    vendor_ids = prod_sold.part_ids
    quants_in_inventory = prod_sold.part_quants.split('/')
    print('qininve', quants_in_inventory)

    disallowed_characters = "[]'"

    print('1', vendor_ids)
    for character in disallowed_characters:
        vendor_ids = vendor_ids.replace(character, "")
    # vendor_ids.split("'")
    vendor_ids = vendor_ids.split(",")

    for index in range(len(vendor_ids)):
        vendor_entry = vendor.objects.get(id=vendor_ids[index])
        part_in_inventory = inventory.objects.get(part=vendor_entry.part)

        part_in_inventory.value -= cost * quant * int(quants_in_inventory[index])
        part_in_inventory.quant -= quant * int(quants_in_inventory[index])
        part_in_inventory.save()