# 获取移动运营商的号段
mobile_list = df_data.loc[df_data['运营商'] == '移动', '号段'].drop_duplicates().tolist()
# 根据移动号段匹配所有移动用户
df_data_mobile = df_data.loc[df_data['号段'].str.slice(0, 3).isin(mobile_list), :]

# 获取联通运营商的号段
unicom_list = df_data.loc[df_data['运营商'] == '联通', '号段'].drop_duplicates().tolist()
# 根据联通号段匹配所有联通用户
df_data_unicom = df_data.loc[df_data['号段'].str.slice(0, 3).isin(unicom_list), :]

# 匹配电信用户
df_data_net = df_data.loc[~df_data['号段'].str.slice(0, 3).isin(mobile_list) &
                          ~df_data['号段'].str.slice(0, 3).isin(unicom_list)
                          , :]
