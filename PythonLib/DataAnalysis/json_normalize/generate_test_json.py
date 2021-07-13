import json

data_dic = {
    'customer': [{'customer_id': 1, 'customer_name': 'xiaohong',
                  'Address': [{'address_id': '1', 'address_name': 'address_AAA'},
                              {'address_id': '2', 'address_name': 'address_BBB'}]},
                 {'customer_id': 2, 'customer_name': 'xiaoming',
                  'Address': [{'address_id': '3', 'address_name': 'address_CCC'},
                              {'address_id': '4', 'address_name': 'address_DDD',
                               'block': [{'block_id': 1, 'block_name': 'block_aaa'},
                                         {'block_id': 1, 'block_name': 'block_bbb'}]}]}]
}
json_data = json.dumps(data_dic)
with open('customer.json', 'w+') as f:
    f.write(json_data)
