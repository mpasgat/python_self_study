from pydantic import BaseModel, Field
from task1 import User, valid_user

class OrderItem(BaseModel):
    product_id: int
    name: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)

class Order(BaseModel):
    id: int
    user: User
    items: list[OrderItem]
    
    @property
    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
    
item1 = OrderItem(
    product_id=1,
    name='banana',
    quantity=3,
    price=111
)

item2 = OrderItem(
    product_id=2,
    name='muslie',
    quantity=3,
    price=99
)

order = Order(
    id=1,
    user = valid_user,
    items=[item1, item2]
)

print(order.total)
print(order.model_dump_json())