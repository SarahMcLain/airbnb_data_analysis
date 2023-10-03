def bed_bath_rating(df):
    split_info = df['name'].str.split(' ·')
    rating = []
    bedrooms = []
    beds = []
    bath = []

    for item in split_info:
        num_rating = 0
        num_bedrooms = 0
        num_beds = 0
        num_bath = 0

        for info in item:
            stripped_info = info.strip()
            if "★" in stripped_info:
                num_rating = stripped_info.replace("★", "")
            elif "bedroom" in stripped_info:
                num_bedrooms = stripped_info.split()[0] 
            elif "bed" in stripped_info:
                num_beds = stripped_info.split()[0]
            elif "bath" in stripped_info:
                num_bath = stripped_info.split()[0]
        
        rating.append(num_rating)
        bedrooms.append(num_bedrooms)
        beds.append(num_beds)
        bath.append(num_bath)
    
    df["rating"] = rating
    df["bedrooms"] = bedrooms
    df["beds"] = beds
    df["bath"] = bath

    return df



def cols_to_drop(df):
    df.drop(columns=['name', 'license', 'last_review'], inplace=True)

    return df


def missing_room_count(df):
    missing_room_by_type = df[["room_type", "bedrooms", "beds", "bath"]].groupby("room_type").apply(lambda group: group.isnull().sum())

    return missing_room_by_type

