# allocation_language
Language intented to construct the financial behaviour of (re)insurance contracts. 
Complete documentation of all methods is still pending because this is still in development.

## Installation

> $ pip install allocation_language

## Examples

``` python
import random
from allocation_language import make_contract
from allocation_language.alloc_lang_data_containers import converters

contract = make_contract.make_contract_from_text("alloc @'claim' $name_1 @'liable';")
contract.update('name_1', 50)
def loss_data():
    for i in range(10):
        yield {
            'id': i,
            'claim': random.randint(1, 1e3),
            'liable': 0,
        }

losses = converters.dict_iter_to_event_iter(loss_data())
results = contract.evaluate_stream(losses)

for x in results:
    print(x)
```
The above code is an example to feed a generator of loss data into a contract. 
The "alloc @'claim' $name_1 @'liable';" command translates in english to 'move as much as possible, limited to name_1's value, from the claim field into the liable field'.
This means it applies an occurence equal to name_1.
The contract.update method allows modification of any named variables in a contract. There can be multiple. 
