# PistolMagazine 🎯
[![PyPI - Version](https://img.shields.io/pypi/v/PistolMagazine)](https://pypi.org/project/PistolMagazine/)


PistolMagazine is a data mocking tool designed to help you generate realistic data for testing and development purposes.

## Features ✨

- **Flexible Data Types** 📊: Supports various data types including integers, floats, strings, timestamps, and more.
- **Custom Providers** 🛠️: Easily create and integrate custom data providers.
- **Random Data Generation** 🎲: Generates realistic random data for testing.
- **Hook Functions** 🪝: Support for hook functions, allowing users to execute custom operations before or after generating mock data. These hooks can be utilized for:
  - **Logging**: Record relevant operations or data before or after data generation.
  - **Starting External Services**: Initiate external services or resources before generating data.
  - **Dynamic Data Modification**: Perform data validation or sanitization before generating mock data.
  - **Sending Data to Message Queues**: Transmit generated data to message queues for integration with other systems.
  - **Data Profiling**: Perform statistical analysis or monitoring post data generation.

## Installation 📦

Install PistolMagazine using pip:

```bash
pip install pistolmagazine
```

## Quick Start 🚀

Here’s a quick example to get you started:

```python
from pistol_magazine import *
from random import choice
from pistol_magazine.hooks.hooks import hook
from pprint import pprint

# Create a custom provider
@provider
class MyProvider:
    def user_status(self):
        return choice(["ACTIVE", "INACTIVE"])
    
@hook('before_generate', order=1)
def before_generate_first_hook(data):
    print("Start Mocking User Data")


@hook('before_generate', order=2)
def before_generate_second_hook(data):
    """
    Perform some preprocessing operations, such as starting external services.
    """


@hook('after_generate', order=1)
def after_generate_validation_hook(data):
    data['user_status'] = 'ACTIVE' if data['user_age'] >= 18 else 'INACTIVE'
    return data


@hook('after_generate', order=2)
def after_generate_validation_hook(data):
    """
    Suppose there is a function send_to_message_queue(data) to send data to the message queue
    send_to_message_queue(data)
    """

# Use the custom provider
class UserInfoMocker(DataMocker):
    create_time: Timestamp = Timestamp(Timestamp.D_TIMEE10, days=2)
    user_name: Str = Str(data_type="name")
    user_email: Str = Str(data_type="email")
    user_age: Int = Int(byte_nums=6, unsigned=True)
    user_status: ProviderField = ProviderField(MyProvider().user_status)
    user_marriage: Bool = Bool()
    user_dict: Dict = Dict(
        {
            "a": Float(left=2, right=4, unsigned=True),
            "b": Timestamp(Timestamp.D_TIMEE10, days=2)
        }
    )
    user_list: List = List(
        [
            Datetime(Datetime.D_FORMAT_YMD_T, weeks=2),
            StrInt(byte_nums=6, unsigned=True)
        ]
    )

data = UserInfoMocker().mock(num_entries=2, to_json=True)
"""
e.g.
('{"078b8418-5730-4c4b-a0e0-337be2510a67": {"create_time": 1718538271, '
 '"user_name": "Pamela Chapman", "user_email": "ambermurphy@example.net", '
 '"user_age": 13, "user_status": "INACTIVE", "user_marriage": true, "user_dict": '
 '{"a": -59.1054, "b": 1718443314}, "user_list": ["2024-06-30T18:23:50", '
 '"62"]}, "f2d257e7-a065-4f00-9180-34d11b81fec0": {"create_time": 1718712539, '
 '"user_name": "Amanda Green", "user_email": "christinebrown@example.org", '
 '"user_age": 27, "user_status": "ACTIVE", "user_marriage": false, '
 '"user_dict": {"a": 13.4132, "b": 1718661665}, "user_list": '
 '["2024-06-19T05:17:39", "29"]}}')
"""
pprint(data)

```

If you want more detailed instructions, you can refer to the examples and documentation in the [tests' directory](tests).


## Help PistolMagazine

If you find PistolMagazine useful, please ⭐️ Star it at GitHub

[Feature discussions](https://github.com/miyuki-shirogane/PistolMagazine/discussions) and [bug reports](https://github.com/miyuki-shirogane/PistolMagazine/issues) are also welcome!

**Happy Mocking!** 🎉🎉🎉