class Pagination:

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        page = request.GET.get(page_param, '1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.pageQuerySet = queryset[self.start:self.end]

        totalCount = queryset.count()
        totalPageCount, div = divmod(totalCount, page_size)
        if div:
            totalPageCount += 1
        self.totalPageCount = totalPageCount
        self.plus = plus



