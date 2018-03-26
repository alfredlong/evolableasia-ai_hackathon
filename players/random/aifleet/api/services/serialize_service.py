class SerializeServices(object):
    @staticmethod
    def deserialize_from_dict(data, serializer):
        op = serializer(data=data)
        if op.is_valid():
            obj = op.save()
            return obj, op

        print("invalid")
        return None, op

    @staticmethod
    def serialize_to_dict(obj, serializer):
        op = serializer(obj)
        return op.data
