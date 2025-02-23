
def analyze_user_behavior(user_data):
    user_data['hour'] = user_data['timestamp'].dt.hour
    return user_data['hour'].value_counts()
