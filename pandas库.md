isin函数
常用的是 DataFrame 的 isin 函数，它的官方定义是这样的：

def isin(self, values):
    """
    Whether each element in the DataFrame is contained in values.

 Parameters
    ----------
    values : iterable, Series, DataFrame or dict
    The result will only be true at a location if all the
    labels match. If `values` is a Series, that's the index. If
    `values` is a dict, the keys must be the column names,
    which must match. If `values` is a DataFrame,
    then both the index and column labels must match.

 Returns
    -------
    DataFrame
    DataFrame of booleans showing whether each element in the DataFrame
    is contained in values.
    """
______________

”“”

DataFrame中的每个元素是否包含在值中。



参数

----------

值:iterable、Series、DataFrame或dict

结果将只在一个位置为真，如果所有

标签匹配。如果' values '是一个Series，那就是索引。如果

' values '是一个字典，键必须是列名，

它必须匹配。如果' values '是DataFrame，

那么索引和列标签都必须匹配。



返回

-------

DataFrame

数据帧的布尔值，显示数据帧中的每个元素是否

包含在值中。

”“”



_________________________________

可以看到需要传入一个参数 values，函数会返回一个 DataFrame。

其中参数 values 大致解释如下：

values ：iterable, Series, DataFrame 或 dict

如果所有标签都匹配，则结果仅在某个位置为 true。
如果 values 是 Series，那就是索引。
如果 values 是一个 dict，则键必须是必须匹配的列名。
如果值是 DataFrame，则索引标签和列标签都必须匹配。
返回值是一个布尔的 DataFrame，显示 DataFrame 中的每个元素是否包含在值 values 中。


大致解释一下：

当 values 是列表时，将会检查列表中是否存在 DataFrame 中的每个值

当 values 是 dict 时，可以通过传递值以分别检查每一列

当 values 是 Series 或 DataFrame 时，索引和列必须匹配

"""创建 DataFrame"""
df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]}, index=['falcon', 'dog'])
df
           num_legs  num_wings
falcon         2          2
dog            4          0

# values 是列表
df.isin([0, 2])
          num_legs  num_wings
falcon      True       True
dog        False       True

# values 是 dict
df.isin({'num_wings': [0, 3]})
          num_legs  num_wings
falcon     False      False
dog        False       True

# values 是 DataFrame
other = pd.DataFrame({'num_legs': [8, 2], 'num_wings': [0, 2]}, index=['spider','falcon'])
df.isin(other)
          num_legs  num_wings
falcon      True       True
dog        False      False
