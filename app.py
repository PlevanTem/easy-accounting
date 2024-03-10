import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 简单的标题
st.title("支付宝和微信账单分析")

# 文件上传器，允许用户上传CSV文件
uploaded_file = st.file_uploader("选择账单CSV文件", type="csv")
if uploaded_file is not None:
    # 如果上传了文件，将其读取为DataFrame
    df = pd.read_csv(uploaded_file)
    
    # 数据清洗（示例，根据实际情况调整）
    
    # 绘制条形图和饼图的示例
    # 你可以在这里加入上文中创建的条形图和饼图代码
    
    # 展示DataFrame（可选）
    st.write(df)

    # 绘制图表的代码，例如：
    st.subheader("交易类型分布")
    fig, ax = plt.subplots()
    df['类型'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
    st.pyplot(fig)
