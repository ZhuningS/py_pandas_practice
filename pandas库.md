isin����
���õ��� DataFrame �� isin ���������Ĺٷ������������ģ�

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

������

DataFrame�е�ÿ��Ԫ���Ƿ������ֵ�С�



����

----------

ֵ:iterable��Series��DataFrame��dict

�����ֻ��һ��λ��Ϊ�棬�������

��ǩƥ�䡣���' values '��һ��Series���Ǿ������������

' values '��һ���ֵ䣬��������������

������ƥ�䡣���' values '��DataFrame��

��ô�������б�ǩ������ƥ�䡣



����

-------

DataFrame

����֡�Ĳ���ֵ����ʾ����֡�е�ÿ��Ԫ���Ƿ�

������ֵ�С�

������



_________________________________

���Կ�����Ҫ����һ������ values�������᷵��һ�� DataFrame��

���в��� values ���½������£�

values ��iterable, Series, DataFrame �� dict

������б�ǩ��ƥ�䣬��������ĳ��λ��Ϊ true��
��� values �� Series���Ǿ���������
��� values ��һ�� dict����������Ǳ���ƥ���������
���ֵ�� DataFrame����������ǩ���б�ǩ������ƥ�䡣
����ֵ��һ�������� DataFrame����ʾ DataFrame �е�ÿ��Ԫ���Ƿ������ֵ values �С�


���½���һ�£�

�� values ���б�ʱ���������б����Ƿ���� DataFrame �е�ÿ��ֵ

�� values �� dict ʱ������ͨ������ֵ�Էֱ���ÿһ��

�� values �� Series �� DataFrame ʱ���������б���ƥ��

"""���� DataFrame"""
df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]}, index=['falcon', 'dog'])
df
           num_legs  num_wings
falcon         2          2
dog            4          0

# values ���б�
df.isin([0, 2])
          num_legs  num_wings
falcon      True       True
dog        False       True

# values �� dict
df.isin({'num_wings': [0, 3]})
          num_legs  num_wings
falcon     False      False
dog        False       True

# values �� DataFrame
other = pd.DataFrame({'num_legs': [8, 2], 'num_wings': [0, 2]}, index=['spider','falcon'])
df.isin(other)
          num_legs  num_wings
falcon      True       True
dog        False      False
