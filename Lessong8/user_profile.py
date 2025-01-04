def build_profile(first, last, **user_info):
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_info = build_profile('albert', 'einstein',
                          location='princeton',
                          field='physics',
                          occupation='scientist',
                          status='alive',)
print(user_info)

user_info = build_profile('marie', 'curie',
                          location='paris',
                          field='chemistry',
                          occupation='scientist',
                          status='alive',
                          age=35,)
print(user_info)