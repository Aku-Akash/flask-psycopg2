def serialize(tup):
        return {
            'id': tup[0][0], 
            'name': tup[0][1],
            'score': tup[0][2],
        }
