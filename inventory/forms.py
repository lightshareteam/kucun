from django import forms
from .models import Product, StockMovement, Warehouse, IncomingStock, ProductionOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'fnsku', 'name', 'series', 'season', 'weight', 'length', 'width', 'height', 'low_stock_threshold']
        labels = {
            'sku': '店铺SKU',
            'name': '产品SKU',
            'series': '系列',
            'season': '季节',
            'weight': '重量(lb)',
            'length': '长度(inch)',
            'width': '宽度(inch)',
            'height': '高度(inch)',
            'low_stock_threshold': '库存阈值',
        }
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'fnsku': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'series': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'length': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'width': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'low_stock_threshold': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['warehouse', 'product', 'movement_type', 'quantity', 'date', 'notes']
        labels = {
            'product': '产品(店铺SKU)',
        }
        widgets = {
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'movement_type': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'code', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class IncomingStockForm(forms.ModelForm):
    class Meta:
        model = IncomingStock
        fields = ['product', 'warehouse', 'quantity', 'expected_arrival_date', 'status', 'notes']
        labels = {
            'product': '产品(店铺SKU)',
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'expected_arrival_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProductionOrderForm(forms.ModelForm):
    class Meta:
        model = ProductionOrder
        fields = ['product', 'order_number', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'order_number': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置产品选择器的查询集
        self.fields['product'].queryset = Product.objects.all().order_by('sku')
        # 添加帮助文本
        self.fields['order_number'].help_text = '请输入唯一的订单号'
        self.fields['quantity'].help_text = '请输入订单总数量' 