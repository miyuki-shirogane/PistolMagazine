from pprint import pprint
from pistol_magazine import *


class Asset(DataMocker):
    assetName: Str = Str()
    assetId: Str = Str(data_type="md5")
    heat: StrInt = StrInt(byte_nums=16, unsigned=True)
    impact: StrInt = StrInt(byte_nums=16, unsigned=True)
    profitability: StrInt = StrInt(byte_nums=16, unsigned=True)
    noOfContents: StrInt = StrInt(byte_nums=16, unsigned=True)
    totalViews: StrInt = StrInt(byte_nums=16, unsigned=True)
    totalDuration: ProviderField = ProviderField(RegexProvider(pattern=r"^\d{1,3}:[0-5]\d:[0-5]\d$").gen)
    totalEarning: StrFloat = StrFloat(left=6, right=2, unsigned=True)
    lastOneMonthEarning: StrFloat = StrFloat(left=4, right=2, unsigned=True)

    # 这里加入 -> hook set，可以在数据mock结束后，做一些其他的事情
    def gen_data(self):
        return self.mock(single_item=True)


class Items(DataMocker):
    id: Str = Str(data_type="md5")
    name: Str = Str()
    heat: StrInt = StrInt(byte_nums=16, unsigned=True)
    impact: StrInt = StrInt(byte_nums=16, unsigned=True)
    profitability: StrInt = StrInt(byte_nums=16, unsigned=True)
    earning: StrFloat = StrFloat(left=6, right=2, unsigned=True)
    rankListDateType: ProviderField = ProviderField(RandomChoiceFromListProvider(
        value_list=[0, 1, 2, 3, 4, 5]
    ).gen)
    toMaxLink: ProviderField = ProviderField(RegexProvider(
        pattern=r"^https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]{11}$"
    ).gen)

    def gen_data(self):
        return self.mock(as_list=True, num_entries=3)


def test_fake_max_push_data():
    data = Asset().gen_data()
    data["assetItems"] = Items().gen_data()
    pprint(data)




