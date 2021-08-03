def update_inventory(inventory, part, cost, quant):
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
