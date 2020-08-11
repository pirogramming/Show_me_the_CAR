from django import forms


class RateShopWidget(forms.NumberInput):
    # input_type = 'rating'
    template_name = 'widgets/rate_shop_number.html'

    # class Media:
    #     css = {
    #         'all': [
    #             'widgets/rateit/scripts/rateit.css',
    #         ],
    #     }
    #     js = [
    #         "//code.jquery.com/jquery-3.4.1.min.js",
    #         'widgets/rateit/scripts/jquery.rateit.min.js',
    #     ]
    #
    # def build_attrs(self, *args, **kwargs):
    #     attrs = super().build_attrs(*args, **kwargs)
    #     attrs.update({
    #         'min': 0,
    #         'max': 5,
    #         'step': 1,
    #     })
    #     return attrs
