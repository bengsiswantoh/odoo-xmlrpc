from helper import models, db, uid, password

[sales_order] = models.execute_kw(db, uid, password,
                            'sale.order', 'search_read',
                            [[['id', '=', 18]]])
print(sales_order)

sales_order_line_ids = sales_order['order_line']

[sales_order_line] = models.execute_kw(db, uid, password,
                            'sale.order.line', 'search_read',
                            [[['id', 'in', sales_order_line_ids]]])
print(sales_order_line)

# records = models.execute_kw(db, uid, password,
#                             'sale.order', 'search_read',
#                             [[]],
#                             {'fields': ['name', 'invoice_status', 'state']})
# print(records)