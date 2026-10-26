import streamlit as st
from engine import troubleshoot
from ai_helper import ask_ai

st.set_page_config(page_title='AI Help Desk | Prototype', page_icon='🛠️', layout='centered')
st.title('🛠️ IT Help Desk Assistant')
st.caption('Phase 2 prototype | Offline, rules-based troubleshooting | No AI model connected yet')
st.info('For learning and low-risk diagnostics only. Do not enter passwords, personal data, or confidential information.')

import os

PUBLIC_DEMO = os.getenv("PUBLIC_DEMO", "false").lower() == "true"

with st.sidebar:
    if PUBLIC_DEMO:
        st.info("AI explanations are unavailable in this public demo.")
        use_ai = False
    else:
        use_ai = st.checkbox("Enable AI explanations", value=False)

if 'messages' not in st.session_state:
    st.session_state.messages = []

for item in st.session_state.messages:
    with st.chat_message(item['role']):
        st.markdown(item['content'])

if prompt := st.chat_input('Describe your Windows or networking problem...'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    with st.chat_message('user'):
        st.markdown(prompt)
    result = troubleshoot(prompt)
    
    lines = [f"### {result['title']}", '', *[f'{i}. {step}' for i, step in enumerate(result['steps'], 1)]]
    
    if result['caution']:
        lines += ['', f"⚠️ {result['caution']}"]
    
    lines += ['', f"*Source: {result['source']}*", '', 'Did this help? If not, tell me what happened at the next step.']
    
    answer = '\n'.join(lines)

    if use_ai and result['title'] != 'Human IT support recommended':
        try:
            explanation = ask_ai(prompt, result['steps'])
            answer += (
                "\n\n### 🤖 AI-Generated Explanation\n"
                + explanation
                + "\n\n*AI explanations may contain mistakes. "
                "Follow the approved troubleshooting steps above.*"
            )
        except Exception:
            answer += (
                "\n\n⚠️ AI explanation unavailable. "
                "The approved troubleshooting guide is still available above."
            )
    
    st.session_state.messages.append({'role': 'assistant', 'content': answer})
    
    with st.chat_message('assistant'):
        st.markdown(answer)

with st.sidebar:
    
    st.subheader('Try an example')
    st.write('• My Wi-Fi is connected but internet does not work')
    st.write('• DNS lookup is failing')
    st.write('• My Windows laptop is very slow')
    st.write('• My printer is not printing')
    st.divider()
    st.write('Version 0.1: local guide matching. No document retrieval, model, automatic commands, or cloud storage.')
    if st.button('Clear chat'):
        st.session_state.messages = []
        st.rerun()
