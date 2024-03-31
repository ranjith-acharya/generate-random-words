def user_data(cursor, **kwargs):
    query = 'SELECT * FROM users WHERE 1=1'
    to_filter = []

    for key, value in kwargs.items():
        if value is not None:
            query += f' AND {key}=%s'
            to_filter.append(value)

    cursor.execute(query, to_filter)
    users = cursor.fetchall()
    data = []
    for user in users:
        user_dict = {
            'id' : user[0],
            'name' : user[1],
            'email' : user[2]
        }
        data.append(user_dict)

    return data