import streamlit as st
import google.generativeai as genai

# 页面标题
st.title("我的 AI 建筑助手")

# 1. 获取 API Key (从云端安全读取，而不是写死在这里)
# 如果是本地运行，它会读取 .streamlit/secrets.toml
# 如果是云端运行，它会读取 Streamlit Cloud 的 Secrets 设置
api_key = st.secrets["GOOGLE_API_KEY"]

# 2. 配置 Google AI
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro') # 或者你选择的其他模型

# 3. 创建输入框
user_input = st.text_input("请输入你的设计需求：", "例如：设计一个位于山顶的现代风格别墅...")

# 4. 创建按钮和逻辑
if st.button("开始生成"):
    if user_input:
        with st.spinner('AI 正在思考中...'):
            try:
                response = model.generate_content(user_input)
                st.write("### AI 回复：")
                st.write(response.text)
            except Exception as e:
                st.error(f"发生错误: {e}")
    else:

        st.warning("请先输入内容！")

