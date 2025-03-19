from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum
from django.utils import timezone

class Warehouse(models.Model):
    name = models.CharField('仓库名称', max_length=100)
    code = models.CharField('仓库代码', max_length=50, unique=True)
    address = models.TextField('地址', blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name = '仓库'
        verbose_name_plural = '仓库'

class Product(models.Model):
    sku = models.CharField('SKU', max_length=100, unique=True)
    fnsku = models.CharField('FNSKU', max_length=100, blank=True)
    name = models.CharField('产品名称', max_length=200)
    weight = models.DecimalField('重量(lb)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    length = models.DecimalField('长度(inch)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    width = models.DecimalField('宽度(inch)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    height = models.DecimalField('高度(inch)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    low_stock_threshold = models.IntegerField('库存阈值', default=10, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    def get_stock_by_warehouse(self, warehouse):
        """获取指定仓库的库存数量"""
        total_in = StockMovement.objects.filter(
            product=self,
            warehouse=warehouse,
            movement_type='IN'
        ).aggregate(total=Sum('quantity'))['total'] or 0

        total_out = StockMovement.objects.filter(
            product=self,
            warehouse=warehouse,
            movement_type='OUT'
        ).aggregate(total=Sum('quantity'))['total'] or 0

        return total_in - total_out

    @property
    def total_stock(self):
        """获取所有仓库的总库存"""
        total_in = StockMovement.objects.filter(
            product=self,
            movement_type='IN'
        ).aggregate(total=Sum('quantity'))['total'] or 0

        total_out = StockMovement.objects.filter(
            product=self,
            movement_type='OUT'
        ).aggregate(total=Sum('quantity'))['total'] or 0

        return total_in - total_out

    def __str__(self):
        return f"{self.name} ({self.sku})"

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'

class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', '入库'),
        ('OUT', '出库'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='产品')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='仓库')
    movement_type = models.CharField('类型', max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField('数量', validators=[MinValueValidator(1)])
    date = models.DateField('日期')
    notes = models.TextField('备注', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return f"{self.get_movement_type_display()}: {self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = '库存变动'
        verbose_name_plural = '库存变动'
        ordering = ['-date', '-created_at']

class IncomingStock(models.Model):
    """入库途中产品模型"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='产品')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='仓库')
    quantity = models.IntegerField('数量', validators=[MinValueValidator(1)])
    expected_arrival_date = models.DateField('预计入仓时间')
    status = models.CharField('状态', max_length=20, default='待入库', 
                             choices=[('待入库', '待入库'), ('已入库', '已入库')])
    notes = models.TextField('备注', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    
    def __str__(self):
        return f"{self.product.sku} - {self.quantity} - {self.warehouse.code}"
    
    class Meta:
        verbose_name = '入库途中产品'
        verbose_name_plural = '入库途中产品'
        ordering = ['expected_arrival_date', '-created_at']

class ProductionOrder(models.Model):
    """生产订单模型"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='产品')
    order_number = models.CharField('订单号', max_length=100)
    quantity = models.IntegerField('数量', validators=[MinValueValidator(1)])
    remaining_quantity = models.IntegerField('剩余数量', validators=[MinValueValidator(0)])
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    
    def __str__(self):
        return f"订单 {self.order_number}: {self.product.sku} - {self.quantity}个"
    
    def save(self, *args, **kwargs):
        # 如果是新创建的订单，初始化剩余数量等于总数量
        if not self.pk:
            self.remaining_quantity = self.quantity
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = '生产订单'
        verbose_name_plural = '生产订单'
        ordering = ['-created_at']
