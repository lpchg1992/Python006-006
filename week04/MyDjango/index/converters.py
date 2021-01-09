class IntConverter:
    regex = '[0-9]+'

    # 从url转为python，由于url是字符串，因此需要将str转换类型，下同。
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
