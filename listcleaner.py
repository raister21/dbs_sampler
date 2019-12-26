def cleaner(list_obj):
    clean_data = []
    for i in list_obj:
        clean_data.append(i.strip())
    
    return clean_data
