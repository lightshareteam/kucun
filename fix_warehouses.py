import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings')
django.setup()

from inventory.models import Warehouse, StockMovement

def fix_warehouses():
    # 打印当前仓库
    print("当前仓库:")
    for w in Warehouse.objects.all():
        print(f"{w.name} ({w.code})")
    
    # 确保GA仓库名称为"亚特兰大仓库"
    try:
        ga_warehouse = Warehouse.objects.get(code='GA')
        ga_warehouse.name = '亚特兰大仓库'
        ga_warehouse.save()
        print(f"已更新GA仓库名称: {ga_warehouse.name}")
    except Warehouse.DoesNotExist:
        print("GA仓库不存在")
    
    # 确保CA仓库名称为"加州仓库"
    try:
        ca_warehouse = Warehouse.objects.get(code='CA')
        ca_warehouse.name = '加州仓库'
        ca_warehouse.save()
        print(f"已更新CA仓库名称: {ca_warehouse.name}")
    except Warehouse.DoesNotExist:
        print("CA仓库不存在")
    
    # 处理ATL仓库
    try:
        atl_warehouse = Warehouse.objects.get(code='ATL')
        # 将ATL仓库的库存记录转移到GA仓库
        movements = StockMovement.objects.filter(warehouse=atl_warehouse)
        movement_count = movements.count()
        print(f"需要转移的库存记录数: {movement_count}")
        
        if movement_count > 0:
            movements.update(warehouse=ga_warehouse)
            print("库存记录已转移")
        
        # 删除ATL仓库
        atl_warehouse.delete()
        print("ATL仓库已删除")
    except Warehouse.DoesNotExist:
        print("ATL仓库不存在")
    
    # 打印更新后的仓库
    print("\n更新后的仓库:")
    for w in Warehouse.objects.all():
        print(f"{w.name} ({w.code})")

if __name__ == "__main__":
    fix_warehouses() 