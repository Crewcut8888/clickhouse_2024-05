from infi.clickhouse_orm import Model, Float32Field, MergeTree, BufferModel, Buffer, Int16Field, Int8Field, StringField

class mouse_movements(Model):
    x = Int16Field()
    y = Int16Field()
    deltaX = Int16Field()
    deltaY = Int16Field()
    clientTimeStamp = Float32Field()
    button = Int8Field()
    target = StringField()

    engine = MergeTree(order_by=[clientTimeStamp], date_col='timestamp')

class mouse_movementsBuffer(BufferModel, mouse_movements):
    engine = Buffer(mouse_movements)