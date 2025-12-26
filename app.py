import streamlit as st
import google.generativeai as genai

st.title("🛠️ AI 诊断与修复助手")

# 1. 获取 API Key
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"API Key 配置出错: {e}")
    st.stop()

# 2. 【核心修复】列出所有当前可用的模型名字
st.subheader("1. 正在查询可用模型...")
try:
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
    
    if available_models:
        st.success(f"成功找到 {len(available_models)} 个可用模型！")
        # 让用户选择一个模型（这样绝对不会错）
        selected_model_name = st.selectbox("请选择一个模型：", available_models, index=0)
    else:
        st.error("未找到任何可用模型，请检查 API Key 权限。")
        st.stop()
except Exception as e:
    st.error(f"查询模型列表失败: {e}")
    st.stop()

# 3. 使用选中的模型
model = genai.GenerativeModel(selected_model_name)

# 4. 输入框
user_input = st.text_input("输入你的设计需求：", "设计一个现代风格的博物馆")

if st.button("测试生成"):
    if user_input:
        with st.spinner('正在生成中...'):
            try:
                response = model.generate_content(user_input)
                st.write("### ✅ 生成结果：")
                st.write(response.text)
            except Exception as e:
                st.error(f"生成出错: {e}")
