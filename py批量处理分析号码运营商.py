# ��ȡ�ƶ���Ӫ�̵ĺŶ�
mobile_list = df_data.loc[df_data['��Ӫ��'] == '�ƶ�', '�Ŷ�'].drop_duplicates().tolist()
# �����ƶ��Ŷ�ƥ�������ƶ��û�
df_data_mobile = df_data.loc[df_data['�Ŷ�'].str.slice(0, 3).isin(mobile_list), :]

# ��ȡ��ͨ��Ӫ�̵ĺŶ�
unicom_list = df_data.loc[df_data['��Ӫ��'] == '��ͨ', '�Ŷ�'].drop_duplicates().tolist()
# ������ͨ�Ŷ�ƥ��������ͨ�û�
df_data_unicom = df_data.loc[df_data['�Ŷ�'].str.slice(0, 3).isin(unicom_list), :]

# ƥ������û�
df_data_net = df_data.loc[~df_data['�Ŷ�'].str.slice(0, 3).isin(mobile_list) &
                          ~df_data['�Ŷ�'].str.slice(0, 3).isin(unicom_list)
                          , :]
