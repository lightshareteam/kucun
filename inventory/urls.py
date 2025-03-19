from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('products/batch-delete/', views.product_batch_delete, name='product_batch_delete'),
    path('products/import/', views.import_products, name='import_products'),
    path('products/export/', views.export_products, name='export_products'),
    path('products/template/download/', views.download_product_template, name='download_product_template'),
    path('products/search/', views.search_products, name='search_products'),
    
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/create/', views.warehouse_create, name='warehouse_create'),
    path('warehouses/<int:pk>/edit/', views.warehouse_edit, name='warehouse_edit'),
    path('warehouses/<int:pk>/delete/', views.warehouse_delete, name='warehouse_delete'),
    path('warehouses/batch-delete/', views.warehouse_batch_delete, name='warehouse_batch_delete'),
    
    path('movements/', views.stock_movement_list, name='stock_movement_list'),
    path('movements/create/', views.stock_movement_create, name='stock_movement_create'),
    path('movements/<int:pk>/delete/', views.stock_movement_delete, name='stock_movement_delete'),
    path('movements/batch-delete/', views.stock_movement_batch_delete, name='stock_movement_batch_delete'),
    path('movements/import/', views.import_stock_movements, name='stock_movement_import'),
    path('movements/template/download/', views.download_stock_movement_template, name='download_stock_movement_template'),
    path('movements/export/', views.export_stock_movements, name='export_stock_movements'),
    
    path('stock-movements/', views.stock_movement_list, name='stock_movement_list'),
    path('stock-movements/create/', views.stock_movement_create, name='stock_movement_create'),
    path('stock-movements/<int:pk>/delete/', views.stock_movement_delete, name='stock_movement_delete'),
    
    path('historical-stock/', views.historical_stock, name='historical_stock'),
    path('historical-stock/export/', views.export_historical_stock, name='export_historical_stock'),
    
    # 入库途中产品相关URL
    path('incoming-stock/', views.incoming_stock_list, name='incoming_stock_list'),
    path('incoming-stock/create/', views.incoming_stock_create, name='incoming_stock_create'),
    path('incoming-stock/<int:pk>/edit/', views.incoming_stock_edit, name='incoming_stock_edit'),
    path('incoming-stock/<int:pk>/delete/', views.incoming_stock_delete, name='incoming_stock_delete'),
    path('incoming-stock/batch-delete/', views.incoming_stock_batch_delete, name='incoming_stock_batch_delete'),
    path('incoming-stock/<int:pk>/approve/', views.incoming_stock_approve, name='incoming_stock_approve'),
    path('incoming-stock/batch-approve/', views.incoming_stock_batch_approve, name='incoming_stock_batch_approve'),
    path('incoming-stock/import/', views.import_incoming_stock, name='import_incoming_stock'),
    path('incoming-stock/export/', views.export_incoming_stock, name='export_incoming_stock'),
    path('incoming-stock/template/', views.download_incoming_stock_template, name='download_incoming_stock_template'),
    path('incoming-stock/batch-action/', views.incoming_stock_batch_action, name='incoming_stock_batch_action'),
    
    # 生产订单相关URL
    path('production-orders/', views.production_order_list, name='production_order_list'),
    path('production-orders/create/', views.production_order_create, name='production_order_create'),
    path('production-orders/<int:pk>/edit/', views.production_order_edit, name='production_order_edit'),
    path('production-orders/<int:pk>/delete/', views.production_order_delete, name='production_order_delete'),
    path('production-orders/batch-delete/', views.production_order_batch_delete, name='production_order_batch_delete'),
    path('production-orders/import/', views.import_production_orders, name='import_production_orders'),
    path('production-orders/export/', views.export_production_orders, name='export_production_orders'),
    path('production-orders/template/', views.download_production_order_template, name='download_production_order_template'),
] 