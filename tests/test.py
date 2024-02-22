import unittest

import clickhouse_query as ch


class TestClickhouseQuery(unittest.TestCase):

    def test_array(self):
        q = ch.QuerySet().select(a="b").prewhere(b__in=[1, 2, 3])
        print(ch.get_sql(q))

        q = ch.QuerySet().select(a="b").prewhere(b__in=[(1, "a"), (2, "b"), (3, "c")])
        print(ch.get_sql(q))

    def test_field(self):
        q = ch.QuerySet().select(a="b").prewhere(ch.Equals("b", ch.Value("salam")))
        print(ch.get_sql(q))

    def test_multi_filter_on_field(self):
        q = ch.QuerySet().select(a="b").prewhere(b__lt=4).prewhere(b__lt=5)
        print(ch.get_sql(q))

    def test_int(self):
        q = ch.QuerySet().select(a="b").prewhere(ch.Equals("b", 2))
        print("#1", ch.get_sql(q))

    def test_isnull(self):
        q = ch.QuerySet().select(a="b").prewhere(b__isnull=False)
        print(ch.get_sql(q))

    def test_clear_where(self):
        q = ch.QuerySet().select(a="b").where(b=2)
        q.where(None)
        print("#3", ch.get_sql(q))

    def test_clear_select(self):
        q = ch.QuerySet().select(a="b").where(b=2)
        q.select(None)
        print("#4", ch.get_sql(q))

    def test_same_filter(self):
        q = ch.QuerySet().select(a="b").prewhere(b__lt=4).prewhere(b__lt=5)
        print("#5", ch.get_sql(q))
