from helper import models, db, uid, password

# ids = models.execute_kw(db, uid, password,
#                         'res.partner', 'search', [[['is_company', '=', True]]])
# print(ids)

# ids = models.execute_kw(db, uid, password,
#                         'res.partner', 'search',
#                         [[['is_company', '=', True]]],
#                         {'offset': 10, 'limit': 5})
# print(ids)

# ids_count = models.execute_kw(db, uid, password,
#                               'res.partner', 'search_count',
#                               [[['is_company', '=', True]]])
# print(ids_count)

# ids = models.execute_kw(db, uid, password,
#                         'res.partner', 'search',
#                         [[['is_company', '=', True]]],
#                         {'limit': 1})
# print(ids)
# [record] = models.execute_kw(db, uid, password,
#                               'res.partner', 'read', [ids])
# count the number of fields fetched by default
# print(len(record))
# print(record)


# records = models.execute_kw(db, uid, password,
#                             'res.partner', 'read',
#                             [ids], {'fields': ['name', 'country_id', 'comment']})
# print(records)

records = models.execute_kw(db, uid, password,
                            'res.partner', 'search_read',
                            [[['is_company', '=', True]]],
                            {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print(records)

# sale.order