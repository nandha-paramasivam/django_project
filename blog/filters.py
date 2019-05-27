import django_filters

class Article_Filter(django_filters.FilterSet):

    @property
    def qs(self):
        queryset = super(Article_Filter, self).qs
        result = queryset.filter()
        print("Result :", result)
        return result
        # return queryset