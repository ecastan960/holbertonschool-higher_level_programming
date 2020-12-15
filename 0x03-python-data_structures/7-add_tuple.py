#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple1 = ()
    new_tuple2 = ()
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        return tuple(p+q for p, q in zip(tuple_a, tuple_b))
    else:
        if len(tuple_a) == 1 and len(tuple_b) >= 2:
            new_tuple1 = (tuple_a[0], 0)
            new_tuple2 = (tuple_b[0], tuple_b[1])
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
        elif len(tuple_a) >= 2 and len(tuple_b) == 1:
            new_tuple1 = (tuple_a[0], tuple_a[1])
            new_tuple2 = (tuple_b[0], 0)
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
        elif len(tuple_a) > 2 and len(tuple_b) > 2:
            new_tuple1 = (tuple_a[0], tuple_a[1])
            new_tuple2 = (tuple_b[0], tuple_b[1])
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
        elif len(tuple_a) == 1 and len(tuple_b) == 1:
            new_tuple1 = (tuple_a[0], 0)
            new_tuple2 = (tuple_b[0], 0)
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
        elif len(tuple_a) == 0 and len(tuple_b) == 0:
            new_tuple1 = (0, 0)
            new_tuple2 = (0, 0)
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
        elif len(tuple_a) == 0 and len(tuple_b) >= 2:
            new_tuple1 = (0, 0)
            new_tuple2 = (tuple_b[0], tuple_b[1])
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
        elif len(tuple_a) >= 2 and len(tuple_b) == 0:
            new_tuple1 = (tuple_a[0], tuple_a[1])
            new_tuple2 = (0, 0)
            return tuple(p+q for p, q in zip(new_tuple1, new_tuple2))
